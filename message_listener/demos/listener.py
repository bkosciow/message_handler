from message_listener.server import Server
from iot_message.message import Message
from message_listener.handler_debug import HandlerDebug
from iot_message.cryptor.base64 import Cryptor as B64

Message.node_name = "PC"
Message.add_decoder(B64())
Message.drop_unencrypted = True

svr = Server()
# svr.ignore_missing_decoders = False
svr.add_handler('NodeOne', HandlerDebug({}))
svr.start()

while True:
    pass
