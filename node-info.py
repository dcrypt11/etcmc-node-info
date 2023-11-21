#!/usr/bin/python
import web
import screen_ocr
import re
import json


def get_data():
    ocr_reader = screen_ocr.Reader.create_quality_reader()
    # To read a cropped region, add bounding_box=(left, top, right, bottom).
    result = ocr_reader.read_screen(bounding_box=(1300, 0, 1900, 400))
    string_result = result.as_string()
    lines = string_result.splitlines()

    transactions = None
    balance = None
    cpu = None
    ram = None

    balance_index = None

    line_index = 0
    for line in lines:
        if '•' in line:
            try:
                transactions = int(re.search(r'\d+', line).group())
            except:
                transactions = None
        if 'Balance' in line:
            try:
                balance = float(line.replace('ETCPOW Balance: ', '').replace(',', '.').strip().replace(' ', '.'))
            except:
                balance = None
                balance_index = line_index
        if 'CPU' in line:
            try:
                cpu = float(line.replace('CPU: ', '').replace('%', '').replace('/0', '').replace(' ', '.'))
            except:
                cpu = None
        if 'RAM' in line:
            try:
                ram = float(line.replace('RAM: ', '').replace('%', '').replace('/0', '').replace(' ', '.'))
            except:
                ram = None
        line_index += 1

    if balance is None and balance_index is not None:
        try:
            balance = float(lines[balance_index + 1])
        except:
            balance = None

    data = {
        "transactions": transactions,
        "balance": balance,
        "cpu": cpu,
        "ram": ram
    }

    print(data)

    return data


urls = (
    '/', 'index'
)


class index:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps(get_data())


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()