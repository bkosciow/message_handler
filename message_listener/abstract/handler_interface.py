#!/usr/bin/python3
# pylint: disable=I0011,R0913,R0902


class Handler(object):
    """Interface for handlers"""
    def handle(self, message):
        """handle a message"""
        raise NotImplementedError("handle not implemented")