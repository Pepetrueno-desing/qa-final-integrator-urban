# tests/test_login_courier.py
import pytest
import sender_stand_request
import data


class TestLoginCourier:

    def test_login_success(self):
        """200: Login con credenciales válidas"""
        # Primero crear el repartidor
        sender_stand_request.post_create_courier(data.valid_courier)
        # Luego hacer login
        body = {"login": "juancho", "password": "1234"}
        response = sender_stand_request.post_login_courier(body)
        assert response.status_code == 200
        assert "id" in response.json()

    def test_login_wrong_password(self):
        """404: Login con contraseña incorrecta"""
        body = {"login": "juancho", "password": "0000"}
        response = sender_stand_request.post_login_courier(body)
        assert response.status_code == 404

    def test_login_non_existent_user(self):
        """404: Login con usuario que no existe"""
        body = {"login": "noexiste", "password": "1234"}
        response = sender_stand_request.post_login_courier(body)
        assert response.status_code == 404