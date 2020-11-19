import paho.mqtt.client as mqtt
import json

pub_topic ="reazioni"
sub_topic ="azioni"

def area(client,lato):
    areaq=0
    areaq=lato*lato
    print(areaq)
    client.publish(pub_topic,areaq)


def on_connect(client, userdata, flags, rc):
    print("Ho ricevuto un comando di calcolo con codice:"+str(rc))
    client.subscribe(sub_topic)

def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    risposte=json.loads(message)
    print("comando ricevuto:" + risposte["scelta"])
    if risposte["scelta"]=="areaq":
        area(client,risposte["lato"])
        
    else:
        print("che succede?")
    
def on_publish(mosq,obj,mid):
    print("risposta inviata con message id:"+str(mid))



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.connect("localhost", 1883, 60)
client.loop_forever()


