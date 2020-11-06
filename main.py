import datetime
import collections

import argparse
import pandas
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

parser = argparse.ArgumentParser(
    description='Программа модуля "Верстка для питониста" урок 1'
)
parser.add_argument('--datafile', default='wine.xlsx', help='Файл с данными по продукции')
parser.add_argument('--sheet', default='Лист1', help='Название листа с данными')
args = parser.parse_args()

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
start_year = 1920
products_data = pandas.read_excel(
    args.datafile,
    sheet_name=args.sheet,
    keep_default_na=''
)

products = collections.defaultdict(list)
for record in products_data.to_dict(orient='records'):
    products[record['Категория']].append(record)

rendered_page = template.render(
    years_old=str(int(datetime.date.today().year) - start_year),
    products=products,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
