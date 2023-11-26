#!/usr/bin/python
import web
import screen_ocr
import re
import json

current_balance = 0


def get_data(old_balance):
    global current_balance

    ocr_reader = screen_ocr.Reader.create_quality_reader()
    # To read a cropped region, add bounding_box=(left, top, right, bottom).
    result = ocr_reader.read_screen(bounding_box=(1300, 0, 1900, 400))
    string_result = result.as_string()
    lines = string_result.splitlines()

    transactions = None
    balance = None
    cpu = None
    ram = None
    disk = None

    balance_index = None
    balance_string = None

    line_index = 0
    for line in lines:
        if '•' in line:
            try:
                transactions = int(re.search(r'\d+', line).group())
            except:
                transactions = None
        if 'Balance' in line:
            try:
                balance_string = line.replace('ETCPOW Balance: ', '')
            except:
                balance_string = None
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
        if 'DISK' in line:
            try:
                disk = float(line.replace('DISK: ', '').replace('%', '').replace('/0', '').replace(' ', '.'))
            except:
                disk = None

        line_index += 1

    if balance_string is None and balance_index is not None:
        try:
            balance_string = lines[balance_index + 1]
        except:
            balance_string = None

    try:
        balance = float(balance_string.replace(',', '.').strip().replace(' ', '.'))
    except:
        balance = None

    if old_balance > 1 and balance > (old_balance * 50):
        balance = None

    if 0 < old_balance <= 1 and balance > (old_balance + 50):
        balance = None

    data = {
        "transactions": transactions,
        "balance": balance,
        "cpu": cpu,
        "ram": ram,
        "disk": disk
    }

    if balance is not None:
        current_balance = balance

    return data


urls = (
    '/', 'index'
)


class index:
    def GET(self):
        global current_balance
        web.header('Content-Type', 'application/json')
        return json.dumps(get_data(current_balance))


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()