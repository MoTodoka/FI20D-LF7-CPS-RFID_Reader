from __future__ import annotations

import paho.mqtt.client as mqtt

from gpio import Output


class Conn:
    topic: str
    outputs: [Output]

    def __init__(self, host: str):
        self.host: str = host

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        rec_topic: Topic = Topic(str(msg.topic))
        rec_payload: str = str(msg.payload.decode("utf-8"))

        print(f"{rec_topic}: {rec_payload}")

        for output in self.outputs:
            if rec_topic.channel == str(output.get_id()):
                print(f"Setting {output} to {rec_payload}")
                if "HIGH" in rec_payload:
                    output.set_high()
                if "LOW" in rec_payload:
                    output.set_low()
                if "FLASH" in rec_payload:
                    output.flash()

    def subscribe(self, topic: str, outputs: [Output]):
        client = mqtt.Client()

        self.topic = topic
        client.on_connect = self.on_connect

        self.outputs = outputs
        client.on_message = self.on_message

        client.connect(self.host, 1883, 60)

        client.loop_forever()

    def publish(self, topic, message):
        client = mqtt.Client()
        client.connect(self.host)
        client.publish(topic, message)


class Topic:
    _delimiter: chr
    place: str
    room: str
    table: str
    device: str
    channel: str

    def __init__(self, topic: str, delimiter: chr = '/'):
        self._delimiter = delimiter
        tree = topic.split(self._delimiter)
        self.place = tree[0].lower()  # eps
        self.room = tree[1].lower()  # fi20d
        self.table = tree[2].lower()  # [1..4] (von vorne nach Hinten)
        self.device = tree[3].lower()  # [l|r] (Links@Rechts aus Blickwinkel des Lehrers)
        self.channel = tree[4].lower()  # Definiert von Empfänger

    def __eq__(self, o: object):
        if not isinstance(o, Topic):
            return NotImplemented

        return self.place == o.place and self.room == o.room and self.table == o.table and self.device == o.device and self.channel == o.channel


def __str__(self):
    return "{1}{0}{2}{0}{3}{0}{4}{0}{5}".format(self._delimiter, self.place, self.room, self.table, self.device,
                                                self.channel)
