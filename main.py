import requests

BASE_URL = "https://cnt-00fa3276-3aa5-4cb8-a8ea-6bf26c311b3a.containerhub.tripleten-services.com"

courier_data = {
    "login": "juancho",
    "password": "1234",
    "firstName": "Juan"
}

url = f"{BASE_URL}/api/v1/courier"

print(f"Enviando POST a: {url}")
print(f"Datos: {courier_data}")

try:
    response = requests.post(url, json=courier_data, timeout=10)
    print(f"\nCódigo de estado: {response.status_code}")
    print(f"Respuesta: {response.text}")

    if response.status_code == 201:
        print("\n✅ Repartidor creado exitosamente.")
        print(f"   Usuario: {courier_data['login']}")
        print(f"   Contraseña: {courier_data['password']}")
    elif response.status_code == 409:
        print("\n⚠️ El login ya existe. Cambia el 'login' por otro.")
    elif response.status_code == 400:
        print("\n❌ Datos inválidos. Revisa las restricciones.")
    else:
        print("\n⚠️ Respuesta inesperada.")

except requests.exceptions.ConnectionError:
    print("\n❌ Error de conexión. Verifica que el servidor esté encendido.")
except requests.exceptions.Timeout:
    print("\n❌ Timeout. El servidor tardó demasiado.")