import paho.mqtt.client as mqtt
import json
import time

pub_topic ="azioni"
sub_topic ="reazioni"

def on_connect(client, userdata, flags, rc):
    print("Client che invia comandi attivato con codice:"+str(rc))
    client.subscribe(sub_topic)
    

def on_message(client, userdata, msg):
        messaggio = msg.payload.decode("utf-8")
        print("Risposta ottenuta:"+ messaggio)
    

def on_publish(mosq,obj,mid):
    print("Comando inviato con messaggio id:{}".format(str(mid)))




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    scelta=input("""
    Azioni possibili:
    areaq ->se vuoi calcolare l'area del quadrato
    arear ->se vuoi calcolare l'area del rettangolo 
    """)
    if scelta=="areaq":
        lato=int(input("Inserisci il lato del quadrato:"))
        messaggio = {"scelta" : scelta, "lato" : lato}
        messaggiostr = json.dumps(messaggio)
        client.publish(pub_topic,messaggiostr)
    else:
        time.sleep(1)
        

