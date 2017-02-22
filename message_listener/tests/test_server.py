#!/usr/bin/python3
#pylint: skip-file

__author__ = 'Bartosz Kościów'
import socket
from nose.tools import assert_equal
from message_listener.server import Server


class TestServer(object):
    def test_init(self):
        a = Server('mesg', 1024, '127.0.0.1')
        assert_equal(a.port, 1024)
        assert_equal(a.ip, '127.0.0.1')
        assert_equal(type(a.socket), type(socket.socket()))