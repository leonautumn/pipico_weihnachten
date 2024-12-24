# Raspberry Pi Pico RP2040

Moin Dennis,

du hast einen Pi Pico RP2040 vor dir liegen. Damit kann man viele Kleinigkeiten machen. Im Internet findet man einiges an Inspirationen.

Und das beste: Die Programmierung erfolgt auf Python-Basis (da bist du ja quasi schon Experte!).

## Nützliche Links
Als Einstieg empfehle ich folgende Seiten:
- [Beschreibung der Hardware auf raspberrypi.com](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pico-1-family)
- [Blog-Eintrag für die Anwendung, die ich gewählt habe](https://how2electronics.com/interfacing-16x2-lcd-display-with-raspberry-pi-pico/)
- [How do I run a script at Pico poweron?](https://forums.raspberrypi.com/viewtopic.php?t=301927)

## Dateien
Die Dateien, die auf dem Gerät sind, sind in diesem Repository hochgeladen:
- RPI_PICO-20241129-v1.24.1.uf2 => MicroPython-Firmware
- check_i2c.py => Skript, um angeschlossene I2C-Geräte zu finden
- lcd_api.py => API für die Schnittstelle zum Display
- pico_i2c_lcd.py => Schnittstellenfunktionen
- pico_i2c_lcd_test.py => Test des Displays
- **main.py => Diese Datei wird beim Hochlauf aufgerufen (Dort findest du auch den Text wieder)**
