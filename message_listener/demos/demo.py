import sys
from iot_message.message import Message
sys.path.append("../../")

from message_listener.server import Server
from charlcd.drivers.i2c import I2C
from charlcd import buffered as lcd
from charlcd.handler import Handler

i2c_20x4 = I2C(0x3b, 1)
i2c_20x4.pins = {
    'RS': 6,
    'E': 4,
    'E2': None,
    'DB4': 0,
    'DB5': 1,
    'DB6': 2,
    'DB7': 3
}

lcd = lcd.CharLCD(20, 4, i2c_20x4)
lcd.init()

msg = Message('rpi1')

svr = Server(msg)
svr.add_handler('20x4', Handler(lcd))
while True:
    svr.run()

svr.join()
