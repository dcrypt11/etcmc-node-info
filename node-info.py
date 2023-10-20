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

    for line in lines:
        if '' in line:
            try:
                transactions = int(re.search(r'\d+', line).group())
            except:
                transactions = None
        if 'Balance' in line:
            try:
                balance = line.replace('ETCPOW Balance: ', '')
            except:
                balance = None
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

    data = {
        "transactions": transactions,
        "balance": balance,
        "cpu": cpu,
        "ram": ram
    }

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