from time import sleep

from RPi import GPIO


class Pin:
    pin_id: int
    gpio_type: GPIO

    def __init__(self, pin_id: int, gpio_type: GPIO):
        self.pin_id = pin_id
        self.gpio_type = gpio_type
        GPIO.setup(self.pin_id, self.gpio_type)

    def get_id(self) -> int:
        return self.pin_id

    def get_type(self) -> GPIO:
        return self.gpio_type


class Output(Pin):
    def __init__(self, pin_id: int):
        super().__init__(pin_id, GPIO.OUT)

    def set_high(self):
        GPIO.output(self.pin_id, GPIO.HIGH)

    def set_low(self):
        GPIO.output(self.pin_id, GPIO.LOW)

    def flash(self):
        self.set_high()
        sleep(0.5)
        self.set_low()


class Input(Pin):
    def __init__(self, pin_id: int):
        super().__init__(pin_id, GPIO.IN)


class Gpio:
    pins: [Pin] = []

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def add_output(self, pin_id: int) -> int:
        return self.add_pin(Output(pin_id))

    def add_input(self, pin_id: int) -> int:
        return self.add_pin(Input(pin_id))

    def add_pin(self, pin: Pin) -> int:
        self.pins.append(pin)
        return len(self.pins) - 1

    def get_inputs(self) -> [Input]:
        result: [Input] = []
        for pin in self.pins:
            if pin.gpio_type == GPIO.IN:
                result.append(pin)
        return result

    def get_outputs(self) -> [Output]:
        result: [Output] = []
        for pin in self.pins:
            if pin.gpio_type == GPIO.OUT:
                result.append(pin)
        return result

    def __del__(self):
        GPIO.cleanup()
