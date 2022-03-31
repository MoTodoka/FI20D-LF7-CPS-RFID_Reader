import mqtt
from gpio import Gpio


class Subscriber:
    def __init__(self, host: str, topic: str, pins: [int]):
        self.host = host
        self.topic = topic
        self.pins = pins

    def listen(self):
        gpio: Gpio = Gpio()
        for pin in self.pins:
            gpio.add_output(pin)
        conn: mqtt.Conn = mqtt.Conn(self.host)
        conn.subscribe(self.topic, gpio.get_outputs())
