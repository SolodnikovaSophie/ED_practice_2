#Задание 4
import json
import pickle

with open('products_95.pkl', 'rb') as pkl_f:
    products = pickle.load(pkl_f)
    #print(pkl_data)

with open('price_info_95.json', 'r') as json_f:
    price_info = json.load(json_f)


def update_price(product, price_info):
    method = price_info['method']
    if method == 'add':
        product['price'] += price_info['param']
    elif method == 'sub':
        product['price'] -= price_info['param']
    elif method == 'percent+':
        product['price'] *= (1 + price_info['param'])
    elif method == 'percent-':
        product['price'] *= (1 - price_info['param'])
    # Округлим цены до двух знаков
    product['price'] = round(product['price'], 2)

# Создадим словарь для текущего файла с необновленными ценами
price_info_dict = dict()

for item in price_info:
    price_info_dict[item['name']] = item


for product in products:
    current_price_info = price_info_dict[product['name']]
    update_price(product, current_price_info)

with open('products_updated_95_4.pkl', 'wb') as f:
    f.write(pickle.dumps(products))