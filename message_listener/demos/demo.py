import sys
from iot_message.message import Message
sys.path.append("../../")

from message_listener.server import Server

msg = Message('rpi1')
svr = Server(msg)
svr.run()