#!/usr/bin/python3

__author__ = 'Bartosz Kościów'

import socket
from threading import Thread


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

    def add_handler(self, handler, name):
        #chek if implements iface & add to dict
        self.handlers[name] = handler

    def run(self):
        try:
            while self.work:
                try:
                    data, address = self.socket.recvfrom(1024)
                    message = self.message.decode_message(data.decode())
                    if message:
                        print("Message from %s: %s" % (address, message))
                except socket.timeout:
                    pass
        finally:
            self.socket.close()

    def join(self, timeout=None):
        """stop server and all listeners"""
        self.work = False
        self.socket.close()
        Thread.join(self, timeout)
