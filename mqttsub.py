# lo primero que hay que hacer es instalar paho-mqtt: pip install paho-mqtt pip install termcolor pip install emoji
import paho.mqtt.client as mqtt
from termcolor import colored
from threading import Thread
import emoji

print(colored("Bienvenidos al chat " + emoji.emojize(':thumbs_up:'),"red"))
nombre = input("Hola dime tu nombre: ")
nombre = nombre.capitalize()

def ante_conexion_exitosa(client, userdata, flag, rc):
    print("Conectados con el broker" + emoji.emojize(':grinning_face:')) 
    client.subscribe("/chat/mensajes") #indicamos al tópico que me quiero conectar
    client.publish("/chat/mensajes", nombre + "se unió al chat")

def ante_llegada_mensaje(client, userdata, msg):
    print(msg.payload.decode("utf-8")) #se imprime el mensaje que viene en el tópico

cliente = mqtt.Client() #instancia del cliente
cliente.on_connect = ante_conexion_exitosa #cuando se conecta que tiene que hacer
cliente.on_message = ante_llegada_mensaje #cuando llegue un mensaje

cliente.username_pw_set("","") #configuramos el usuario y la clave para el servidor
cliente.connect("localhost", 1883, 60) #configuramos ip, puerto y keep_alive

while True:
    a_enviar = input("escribe mensaje ->")
    a_enviar = nombre + " dice " + a_enviar
    cliente.publish("/chat/mensajes", a_enviar) # publicamos el mensaje que queremos enviar en el tópico
    cliente.loop()





