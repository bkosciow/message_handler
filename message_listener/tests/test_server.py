#!/usr/bin/python3
#pylint: skip-file

__author__ = 'Bartosz Kościów'
import socket
from nose.tools import assert_equal, assert_is_not_none, assert_in
from message_listener.server import Server
from message_listener.abstract.handler_interface import Handler
from unittest.mock import MagicMock
from nose.tools import assert_raises


class TestServer(object):
    def test_init(self):
        a = Server(1024, '127.0.0.1')
        assert_equal(a.port, 1024)
        assert_equal(a.ip_address, '127.0.0.1')
        assert_equal(type(a.socket), type(socket.socket()))

    def test_it_should_add_handler(self):
        class SampleHandler(Handler):
            def handle(self, message):
                pass
        sh = SampleHandler(None)

        a = Server(1024, '127.0.0.1')
        a.add_handler('sample', sh)
        assert_equal(a.handlers['sample'], [sh])

    def test_it_should_add_two_handlers(self):
        class SampleHandler(Handler):
            def handle(self, message):
                pass

        a = Server(1024, '127.0.0.1')
        sh1 = SampleHandler(None)
        sh2 = SampleHandler(None)
        a.add_handler('sample', sh1)
        a.add_handler('sample', sh2)

        assert_in(sh1, a.handlers['sample'])
        assert_in(sh2, a.handlers['sample'])

    def test_it_should_add_two_handlers_at_once(self):
        class SampleHandler(Handler):
            def handle(self, message):
                pass

        a = Server(1024, '127.0.0.1')
        sh1 = SampleHandler(None)
        sh2 = SampleHandler(None)
        a.add_handler('sample', sh1, sh2)

        assert_in(sh1, a.handlers['sample'])
        assert_in(sh2, a.handlers['sample'])

    def test_it_should_pass_message_to_handlers(self):
        a = Server(1024, '127.0.0.1')
        sh1 = MagicMock(spec=Handler)
        sh2 = MagicMock(spec=Handler)
        a.add_handler('sample', sh1, sh2)
        a.serve_message('miau')
        sh1.handle.assert_called_with('miau')
        sh2.handle.assert_called_with('miau')
