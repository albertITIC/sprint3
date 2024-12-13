from awscrt import mqtt
from awsiot import mqtt_connection_builder
import time
import json
import pymysql

# Configuración de AWS IoT
ENDPOINT = "a3hvwfbfayc3f6-ats.iot.us-east-1.amazonaws.com"   # Tu endpoint MQTT
CLIENT_ID = "iotconsole-210cdda9-5315-48d4-a906-eabcb96eb17d" # Identificador único para tu dispositivo
TOPIC = "esp32/esp32-to-aws"                                  # Topic al que te suscribirás
RESPONSE_TOPIC = "esp32/esp32-to-aws/response"                # Topic para enviar la confirmación
# Tener en cuenta que el path cambia.
CERTIFICATE_PATH = "/home/isard/Escriptori/Projecte/sprint3/certificats_aws/client1-certificate.key"
PRIVATE_KEY_PATH = "/home/isard/Escriptori/Projecte/sprint3/certificats_aws/client1.private.key"
CA_PATH = "/home/isard/Escriptori/Projecte/sprint3/certificats_aws/AmazonRootCA1.key"

# Configuración de MySQL
DB_HOST = "192.168.41.5" 
DB_USER = "usuari1" 
DB_PASSWORD = "pirineus"
DB_NAME = "AppAssistenciesS2"

# Callback para cuando se recibe un mensaje
# def on_message_received(topic, payload, **kwargs):
#     print(f"Mensaje recibido en el topic '{topic}': {payload.decode()}")
#     # Procesar el mensaje y guardarlo en la base de datos
#     try:
#         data = json.loads(payload)
#         insertar_en_base_de_datos(data)
#         enviar_confirmacion(data['nuid'], "nuid rebut")
#     except Exception as e:
#         print(f"Error procesando el mensaje: {e}")
#         enviar_confirmacion(data['NUID'], "error", str(e))
def on_message_received(topic, payload, dup, qos, retain):
    try:
        data = json.loads(payload)  # Convertir el payload en un diccionario
        
        # Verifica si la clave 'nuid' o 'NUID' existe
        nuid = data.get('nuid') or data.get('NUID')
        if nuid is None:
            raise KeyError("Clave 'nuid' o 'NUID' no encontrada en el mensaje.")
        
        enviar_confirmacion(nuid, "ok", "Procesado correctamente")
    except KeyError as e:
        print(f"Error procesando el mensaje: {e}")
        enviar_confirmacion("desconocido", "error", str(e))
    except Exception as e:
        print(f"Error inesperado: {e}")


# Conectar a la base de datos y guardar datos
def insertar_en_base_de_datos(data):
    try:
        conexion = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        with conexion.cursor() as cursor:
            # Comprobar si el NUID está asociado a un usuario
            query_buscar_usuario = "SELECT NUID FROM Usuari WHERE NUID = %s"
            cursor.execute(query_buscar_usuario, (data['NUID'],))
            resultado = cursor.fetchone()

            if resultado:
                idUsuari = resultado[0]  # Extraer el ID del usuario
                # Insertar un registro en la tabla Asistencias
                query_insertar_asistencia = """
                    INSERT INTO Assistencia (idAssistencia, idUsuari, estat, hEntrada, hSortida, dia)
                    VALUES (%s, %s, %s, CURTIME(), NULL, CURDATE())
                """
                cursor.execute(query_insertar_asistencia, (idUsuari,))
                conexion.commit()
                print("Datos insertados correctamente en la base de datos.")
            else:
                print(f"No se encontró un usuario con el NUID: {data['NUID']}")
                raise ValueError("No se encontró el usuario con el NUID")
    except Exception as e:
        print(f"Error insertando en la base de datos: {e}")
        raise e
    finally:
        conexion.close()

# Función para enviar la confirmación de recepción al topic de respuesta
def enviar_confirmacion(NUID, status, error_message=None):
    # Crear el mensaje de confirmación
    response = {
        "NUID": NUID,
        "status": status
    }
    if error_message:
        response["message"] = error_message
    
    # Publicar el mensaje en el topic de respuesta
    try:
        mqtt_connection.publish(
            topic=RESPONSE_TOPIC,
            payload=json.dumps(response),
            qos=mqtt.QoS.AT_LEAST_ONCE
        )
        print(f"Confirmación enviada al topic '{RESPONSE_TOPIC}': {json.dumps(response)}")
    except Exception as e:
        print(f"Error enviando confirmación: {e}")

# Crear conexión MQTT
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=CERTIFICATE_PATH,
    pri_key_filepath=PRIVATE_KEY_PATH,
    ca_filepath=CA_PATH,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=30,
)

print(f"Conectando al endpoint {ENDPOINT} con ID '{CLIENT_ID}'...")
connect_future = mqtt_connection.connect()
connect_future.result()
print("¡Conectado a AWS IoT!")

# Suscribirse al topic
print(f"Suscribiéndose al topic '{TOPIC}'...")
subscribe_future, packet_id = mqtt_connection.subscribe(
    topic=TOPIC,
    qos=mqtt.QoS.AT_LEAST_ONCE,
    callback=on_message_received
)
subscribe_future.result()
print(f"Suscripción al topic '{TOPIC}' completada.")

# Mantener la conexión activa
try:
    print("Esperando mensajes (Ctrl+C para salir)...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Desconectando...")
    mqtt_connection.disconnect()