import requests
import configuration
import data

# Создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         headers=data.headers,
                         json=data.order_body)

# Получение заказа по трекеру
def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER + '?t=' + str(track),
                        headers=data.headers)
