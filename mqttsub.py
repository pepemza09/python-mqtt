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


'''
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


'''


