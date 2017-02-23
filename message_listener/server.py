#!/usr/bin/python3

__author__ = 'Bartosz Kościów'

import socket
from threading import Thread
from message_listener.abstract.handler_interface import Handler


class Server(Thread):
    def __init__(self, message, port=5053, ip='0.0.0.0'):
        Thread.__init__(self)
        self.port = port
        self.ip = ip
        self.handlers = {}
        self.work = True
        self.message = message
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.settimeout(0.5)
        self.socket.bind((ip, port))

    def add_handler(self, name, handler):
        """add new handler"""
        if not isinstance(handler, Handler):
            raise AttributeError('not a handler!')

        if name is self.handlers:
            raise AttributeError("name already used!")

        self.handlers['name'] = handler

    def run(self):
        """server loop"""
        try:
            while self.work:
                try:
                    data, address = self.socket.recvfrom(1024)
                    message = self.message.decode_message(data.decode())
                    if message:
                        print("Message from %s: %s" % (address, message))
                        self.serve_message(message)
                except socket.timeout:
                    pass
        finally:
            self.socket.close()

    def serve_message(self, message):
        """pass message to registred handlers"""
        for handler in self.handlers:
            self.handlers[handler].handle(message)

    def join(self, timeout=None):
        """stop server"""
        self.work = False
        self.socket.close()
        Thread.join(self, timeout)
