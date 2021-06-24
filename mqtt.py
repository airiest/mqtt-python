import paho.mqtt.client as mqtt
import sys


class MQTTClient:

    def __init__(self, clientid):
        # MQTT CLIENT初期化
        self._mqttc = mqtt.Client(clientid)
        self._mqttc.on_message = self.mqtt_on_message
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_publish = self.mqtt_on_publish
        self._mqttc.on_subscribe = self.mqtt_on_subscribe
        self._mqttc.on_log = self.mqtt_on_log

    def mqtt_on_connect(self, client, userdata, flags, rc):
        print("on_connect: result={0}".format(rc))

    def mqtt_on_message(self, client, userdata, msg):
        print("on_message: topic={0}, qos={1}, payload={2}".format(
            msg.topic, msg.qos, msg.payload))

        # receive message.
        recv_msg = str(msg.payload.decode("utf-8"))
        print("receive message = " + recv_msg)

    def mqtt_on_publish(self, client, userdata, mid):
        print("on_publish: mid={0}".format(mid))

    def mqtt_on_subscribe(self, client, userdata, mid, granted_qos):
        print("on_subscribe: mid={0}, granted_qos={1}".format(
            mid, granted_qos))

    def mqtt_on_log(self, client, userdata, level, buf):
        print("on_log: " + buf)

    def run_publish(self, host, port, topic, qos):
        self._mqttc.connect(host, port, 60)

        while True:
            try:
                # send message
                msg = input()
                self._mqttc.publish(topic, msg, qos)
            except KeyboardInterrupt:
                print("interrupted")
                self._mqttc.disconnect()
                sys.exit()

    def run_subscribe(self, host, port, topic, qos):
        self._mqttc.connect(host, port, 60)
        self._mqttc.subscribe(topic, qos)

        try:
            self._mqttc.loop_forever()
        except KeyboardInterrupt:
            print('interrupted')
            sys.exit()


if __name__ == "__main__":
    args = sys.argv

    if (len(args) != 2):
        print("Argument is not correct")
        sys.exit(0)

    mqttc = MQTTClient(None)
    if (args[1] == "pub"):
        mqttc.run_publish("127.0.0.1", 1883, "tp/test", 0)
    elif (args[1] == "sub"):
        mqttc.run_subscribe("127.0.0.1", 1883, "tp/test", 0)
    else:
        print("Unknown option")
