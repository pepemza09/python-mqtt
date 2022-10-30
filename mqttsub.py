# lo primero que hay que hacer es instalar paho-mqtt: pip install paho-mqtt pip install termcolor pip install emoji
import paho.mqtt.client as mqtt
from termcolor import colored
from threading import Thread
import emoji

def ante_con_exitosa(client, userdata, flag, rc):
    print('Conectado con el servidor')
    client.subscribe('/chat/mensaje')
    

def ante_llegada_mensaje(client, userdata, msg):
    print('llegó el siguiente mensaje: ' + msg.payload.decode("utf-8")) #se imprime el mensaje que viene en el tópico

print(colored("Bienvenidos al cliente de mosquitto" + emoji.emojize(':thumbs_up:'),"red"))
nombre = input("Primero, escribe tu nombre: ")

if (nombre.isspace() or len(nombre) <= 1):
    #en el caso de que no ingrese nombre, lo que hacemos es terminar el script
    print('debes ingrear un nombre')
else:
    #pedimos los datos para ingresar al servidor
    print(colored("ok, " + nombre.capitalize() + " te vamos a pedir unos datos adicionales","green"))
    servidor = input('Ingresa el nombre/IP del servidor MQTT: ')
    usuario = input('Ingresa el usuario: ')
    clave = input('Ingresa la clave: ')
    #incializamos el cliente
    cliente = mqtt.Client()
    #nos conectamos al tópico
    cliente.on_connect = ante_con_exitosa
    cliente.username_pw_set(usuario,clave)
    cliente.connect(servidor,1883,60)
    while True:
        cliente.on_message = ante_llegada_mensaje #imprimimos el mensaje que llega
        cliente.loop()
        