# FI20D1L - RFID-Reader

## Ziel

Im RFID-Reader-Modus, wird je nach vorgehaltenem Schlüssel ein anderer Dienst im Klassenraum per MQTT aufgerufen.

![](.//docu//DSC05053.JPG "Foto: Header-Quer")

## Rahmenbedingungen

[Rahmenbedingungen](.//docu//rahmen.pdf)

## Modi

Momentan gibt es zwei Modi: sub_channels und read_card_to_mqtt. Die Methode, die den jeweiligen Modus startet, kriegt
die benötigten Argumente in einer Namespace variable übergeben. Es können beliebig weitere Modi hinzugefügt werden.

### read_card_to_mqtt

Liest das Topic und die Message von einer RFID Karte und sendet diese an einen variablen Broker.

#### Aufruf

`main.py read_card_to_mqtt [broker]`

#### Sensoren

##### RFID-Reader

RFID-RC522

###### Pin-Belegung

| RF522 Modul | Raspberry Pi           |
|-------------|------------------------|
| SDA         | Pin 24 / BCM 8 (CE0)   |
| SCK         | Pin 23 / BCM 11 (SCKL) |
| MOSI        | Pin 19 / BCM 10 (MOSI) |
| MISO        | Pin 21 / BCM 9 (MISO)  |
| IRQ         | —                      |
| GND         | Pin6 (GND)             |
| RST         | Pin22 / BCM 25         |
| 3.3V        | Pin 1 (3V3)            |

###### Nutzung
Zur Nutzung der Library `from mfrc522 import SimpleMFRC522` muss das Interface SPI auf dem Raspberry Pi aktiviert werden:
```
sudo raspi-config
-> 3 Interface Options
-> I4 SPI
-> Ja
```

###### RFID-Tags beschreiben
Zum Beschreiben eines RFID-Tags `RFID_tag.py` ausführen und den Anweisungen in der Konsole folgen.

###### Inhalt

Auf dem RFID-Tag werden Topic und Message gespeichert, die an den beim Programmaufruf definierten Broker gesendet werden.

Format: `[topic] [message]`<br/>
Beispiel: `eps/fi20d/2/r/musik odetojoy`

#### Aktoren

Keine

### sub_channels

Subscribed auf ein bestimmtes Topic und lauscht. Der Channel entspricht dem genutzten GPIO-Pin im BCM-Modus.

#### Aufruf

`main.py sub_channels [broker] -t [topic] -c [1..27] ...`

#### Sensoren

Keine

#### Aktoren

LEDs

#### Aufruf

##### Topic

`eps/fi20d/1/l/[channel]`

| Channel | Pin    | LED-Farbe |
|---------|--------|-----------|
| 17      | BCM 17 | Grün      |
| 27      | BCM 27 | Rot       |

##### Message

| Message | Beschreibung              |
|---------|---------------------------|
| HIGH    | Schaltet LED ein          |
| LOW     | Schaltet LED aus          |
| FLASH   | LED Blinkt (0.5 Sekunden) |

## Schnittstellen

### RFID

### Schaltplan

***TODO***

### Bilder des Prototyps

#### Top-Down

![](.//docu//DSC05047.JPG "Foto: Top-Down")

#### RFID-Reader

![](.//docu//DSC05050.JPG "Foto: RFID-Reader")

#### LEDs

![](.//docu//DSC05051.JPG "Foto: LED")