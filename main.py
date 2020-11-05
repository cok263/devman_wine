import datetime
import collections

import pandas
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
start_year = 1920
products_data = pandas.read_excel(
    'wine3.xlsx',
    sheet_name='Лист1',
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
