import paho.mqtt.publish as publish
publish.single("ifn649", "LED_OFF", hostname="3.106.213.202")
print("Done")
