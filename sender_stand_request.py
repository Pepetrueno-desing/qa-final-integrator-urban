# sender_stand_request.py
import requests
import configuration

def post_create_courier(body):
    return requests.post(
        configuration.BASE_URL + configuration.CREATE_COURIER,
        json=body
    )

def post_login_courier(body):
    return requests.post(
        configuration.BASE_URL + configuration.LOGIN_COURIER,
        json=body
    )