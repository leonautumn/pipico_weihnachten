import utime

import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

SLEEP_TIME = 5

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    

lcd.clear()

text = [
#----------------END
"Lieber Dennis,\n\
ich wuensche dir\n\
ein schoenes Weih-\n\
nachtsfest.",
"Viel Spass auch\n\
morgen bei deiner\n\
Familie und komm \n\
gut ins Jahr 2025.",
"Hoffentlich klappt\n\
eure USA-Reise! Be-\n\
stimmt werdet ihr\n\
auch noch ein paar\n",
"Musicals besuchen.\n\
Wenn dann noch Zeit\n\
bleibt: Viel Spass\n\
beim Programmieren.",
"Bleib so wie du\n\
bist :-).\n\n\
Leon"
]
while True:
    for i in text:
        print(i)
        lcd.clear()
        lcd.putstr(i)
        utime.sleep(SLEEP_TIME)
    utime.sleep(5)