import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class Reader:
    @staticmethod
    def read():
        reader = SimpleMFRC522()
        try:
            card_id, text = reader.read()
            print(f"card_id={card_id}, text={text}")
            return text
        finally:
            GPIO.cleanup()


class Writer:
    @staticmethod
    def write():
        reader = SimpleMFRC522()
        try:
            text = input('Enter tag data:')
            print("Hold tag to module")
            reader.write(text)
            print("Done...")
        finally:
            GPIO.cleanup()


if __name__ == '__main__':
    Writer.write()
