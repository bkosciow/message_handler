#pylint: skip-file

__author__ = 'Bartosz Kościów'
import socket
from nose.tools import assert_equal, assert_is_not_none, assert_in
from message_listener.server import Server
from message_listener.abstract.handler_interface import Handler
from unittest.mock import MagicMock
from nose.tools import assert_raises
from message_listener.handler_debug import HandlerDebug


class TestHandlerDebug(object):
    def test_init_one_worker(self):
        w = MagicMock()
        h = HandlerDebug(w)
        assert_in(w, h.workers)

    def test_init_two_workers(self):
        w1 = MagicMock()
        h = HandlerDebug(w1)
        assert_in(w1, h.workers)

    def test_handle_call(self):
        h = HandlerDebug()
        h.print = MagicMock()
        h.handle("rambo")
        h.print.assert_called_with("rambo")