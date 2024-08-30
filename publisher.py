import paho.mqtt.publish as publish

publish.single("ifn649", "LED_OFF", hostname="13.211.156.0")
print("Done")
