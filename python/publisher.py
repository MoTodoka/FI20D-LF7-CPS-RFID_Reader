from time import sleep

import RFID_tag
import mqtt


class Publisher:
    def __init__(self, host: str):
        self.host: str = host

    def read_card_to_mqtt(self):
        while True:
            text: str = RFID_tag.Reader.read()
            split_text: [str] = text.split(' ')
            self.send(split_text[0], split_text[1])
            sleep(1)

    def send(self, topic: str, message: str):
        conn: mqtt.Conn = mqtt.Conn(self.host)
        conn.publish(topic, message)
