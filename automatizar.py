import requests

# 1. La URL de tu endpoint
URL_ENDPOINT = "http://maniacafeteriaypasteleria.restaurant.pe/restaurant/?old=1#!/ajustes/usuarios/nuevo"

# 2. Los datos que quieres enviar (organizados como un diccionario)
datos_formulario = {
    "nombre": "Carlos Pérez",
    "correo": "carlos@ejemplo.com",
    "mensaje": "Hola, esto es un envío automatizado."
}

# 3. Cabeceras (Headers) - Opcional, pero muy común para indicar que envías JSON
# o para incluir tokens de autenticación si tu API los pide.
cabeceras = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer TU_TOKEN_AQUÍ" # Descomenta si tu API usa Token
}

try:
    # 4. Enviar los datos usando el método POST
    # Usamos 'json=' para que convierta automáticamente el diccionario a formato JSON
    respuesta = requests.post(URL_ENDPOINT, json=datos_formulario, headers=cabeceras)
    
    # 5. Verificar si el servidor recibió todo correctamente
    if respuesta.status_code in [200, 201]:
        print("¡Envío exitoso! 🎉")
        print("Respuesta del servidor:", respuesta.json())
    else:
        print(f"Error en el envío. Código de estado: {respuesta.status_code}")
        print("Detalle del error:", respuesta.text)

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error de red o de conexión: {e}")