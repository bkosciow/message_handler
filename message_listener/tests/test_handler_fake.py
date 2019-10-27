#pylint: skip-file

__author__ = 'Bartosz Kościów'
import socket
from nose.tools import assert_equal, assert_is_not_none, assert_in
from message_listener.server import Server
from message_listener.abstract.handler_interface import Handler
from unittest.mock import MagicMock
from nose.tools import assert_raises
from message_listener.tests.handler_fake import HandlerFake


class TestHandlerFake(object):
    def test_init_one_worker(self):
        w = MagicMock()
        h = HandlerFake(w)
        assert_in(w, h.workers)

    def test_init_two_workers(self):
        w1 = MagicMock()
        w2 = MagicMock()
        h = HandlerFake(w1, w2)
        assert_in(w1, h.workers)
        assert_in(w2, h.workers)

    def test_handle_call(self):
        w1 = MagicMock()
        w2 = MagicMock()
        h = HandlerFake(w1, w2)
        h.handle("rambo")
        w1.set.assert_called_with("rambo")
        w2.set.assert_called_with("rambo")

    def test_add_worker_via_add(self):
        w1 = MagicMock()
        w2 = MagicMock()
        h = HandlerFake(w1)
        h.add_worker(w2)
        h.handle("rambo")
        w1.set.assert_called_with("rambo")
        w2.set.assert_called_with("rambo")

