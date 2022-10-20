# lo primero que hay que hacer es instalar paho-mqtt: pip install paho-mqtt pip install termcolor pip install emoji
import paho.mqtt.client as mqtt
from termcolor import colored
from threading import Thread
import emoji

print(colored("Bienvenidos al chat","red"))
print(emoji.emojize(':thumbs_up:'))
nombre = input("Hola dime tu nombre: ")

