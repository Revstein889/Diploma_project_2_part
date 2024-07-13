# Алексей Кучеренко, 18-я когорта — Финальный проект. Инженер по тестированию плюс
import data
from sender_test_request import post_new_order, get_order_track


def get_order_status_code_200():
    response_code = post_new_order(data.order_body)
    # сохранение track номера заказа
    track = response_code.json()["track"]
    return get_order_track(track).status_code

# Тест, что код ответа равен 200.
def test_get_order_track_code_200():
    assert get_order_status_code_200() == 200
