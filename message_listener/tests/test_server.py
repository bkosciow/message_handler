#!/usr/bin/python3
#pylint: skip-file

__author__ = 'Bartosz Kościów'
import socket
from nose.tools import assert_equal
from message_listener.server import Server
from message_listener.abstract.handler_interface import Handler
from nose.tools import assert_raises


class TestServer(object):
    def test_init(self):
        a = Server('mesg', 1024, '127.0.0.1')
        assert_equal(a.port, 1024)
        assert_equal(a.ip_address, '127.0.0.1')
        assert_equal(type(a.socket), type(socket.socket()))

    def test_it_should_add_handler(self):
        class SampleHandler(Handler):
            def handle(self, message):
                pass

        a = Server('mesg', 1024, '127.0.0.1')
        a.add_handler('sample', SampleHandler(None))

    def test_it_should_raise_exception_add_handler(self):
        class SampleHandler(object):
            def handle(self, message):
                pass

        a = Server('mesg', 1024, '127.0.0.1')
        assert_raises(AttributeError, a.add_handler, 'sample', SampleHandler)

