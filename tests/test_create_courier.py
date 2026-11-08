import pytest
import sender_stand_request
import data


class TestCreateCourier:

    def test_create_courier_success(self):
        """201: Crear repartidor con datos válidos"""
        response = sender_stand_request.post_create_courier(data.valid_courier)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    # --- Login inválido por longitud ---
    def test_create_courier_login_corto(self):
        """400: Login con 1 carácter (límite inferior inválido)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["login_corto"])
        assert response.status_code == 400

    def test_create_courier_login_largo(self):
        """400: Login con 11 caracteres (límite superior inválido)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["login_largo"])
        assert response.status_code == 400

    def test_create_courier_login_muy_largo(self):
        """400: Login con 50 caracteres (valor muy largo)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["login_muy_largo"])
        assert response.status_code == 400

    # --- Login inválido por caracteres ---
    def test_create_courier_login_con_numeros(self):
        """400: Login con números (solo letras latinas)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["login_con_numeros"])
        assert response.status_code == 400

    def test_create_courier_login_con_especiales(self):
        """400: Login con caracteres especiales (solo letras latinas)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["login_con_especiales"])
        assert response.status_code == 400

    def test_create_courier_login_vacio(self):
        """400: Login vacío (campo obligatorio)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["login_vacio"])
        assert response.status_code == 400

    # --- Password inválido ---
    def test_create_courier_password_corto(self):
        """400: Password con 3 dígitos (límite inferior inválido)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["password_corto"])
        assert response.status_code == 400

    def test_create_courier_password_largo(self):
        """400: Password con 5 dígitos (límite superior inválido)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["password_largo"])
        assert response.status_code == 400

    def test_create_courier_password_con_letras(self):
        """400: Password con letras (solo números)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["password_con_letras"])
        assert response.status_code == 400

    def test_create_courier_password_vacio(self):
        """400: Password vacío (campo obligatorio)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["password_vacio"])
        assert response.status_code == 400

    # --- FirstName inválido ---
    def test_create_courier_firstName_corto(self):
        """400: FirstName con 1 carácter (límite inferior inválido)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["firstName_corto"])
        assert response.status_code == 400

    def test_create_courier_firstName_largo(self):
        """400: FirstName con 14 caracteres (límite superior inválido)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["firstName_largo"])
        assert response.status_code == 400

    def test_create_courier_firstName_vacio(self):
        """400: FirstName vacío (campo obligatorio)"""
        response = sender_stand_request.post_create_courier(data.invalid_couriers["firstName_vacio"])
        assert response.status_code == 400