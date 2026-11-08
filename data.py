import random
import string


def unique_suffix():
    return ''.join(random.choices(string.ascii_lowercase, k=5))


# Datos válidos para crear repartidor (login único)
valid_courier = {
    "login": f"juancho_{unique_suffix()}",
    "password": "1234",
    "firstName": "Juan"
}

# Datos inválidos (cada uno con login único para evitar duplicados)
invalid_couriers = {
    # Login inválido por longitud
    "login_corto": {"login": random.choice(string.ascii_lowercase), "password": "1234", "firstName": "Juan"},
    "login_largo": {"login": "a" * 10 + random.choice(string.ascii_lowercase), "password": "1234", "firstName": "Juan"},
    # 11 chars únicos
    "login_muy_largo": {"login": "a" * 50, "password": "1234", "firstName": "Juan"},

    # Login inválido por caracteres
    "login_con_numeros": {"login": f"juan{random.randint(100, 999)}", "password": "1234", "firstName": "Juan"},
    "login_con_especiales": {"login": f"juan{random.choice(['@', '#', '!', '$'])}", "password": "1234",
                             "firstName": "Juan"},
    "login_vacio": {"login": "", "password": "1234", "firstName": "Juan"},

    # Password inválido
    "password_corto": {"login": f"test_pass_corto_{unique_suffix()}", "password": "123", "firstName": "Juan"},
    "password_largo": {"login": f"test_pass_largo_{unique_suffix()}", "password": "12345", "firstName": "Juan"},
    "password_con_letras": {"login": f"test_pass_letras_{unique_suffix()}", "password": "abcd", "firstName": "Juan"},
    "password_vacio": {"login": f"test_pass_vacio_{unique_suffix()}", "password": "", "firstName": "Juan"},

    # FirstName inválido
    "firstName_corto": {"login": f"test_fn_corto_{unique_suffix()}", "password": "1234", "firstName": "J"},
    "firstName_largo": {"login": f"test_fn_largo_{unique_suffix()}", "password": "1234", "firstName": "JuanchoMendoza"},
    "firstName_vacio": {"login": f"test_fn_vacio_{unique_suffix()}", "password": "1234", "firstName": ""},
}