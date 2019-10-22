from message_listener.abstract.handler_interface import \
    Handler as HandlerInterface


class HandlerFake(HandlerInterface):
    def handle(self, message):
        if message is not None:
            {w.set(message) for w in self.workers}
            print(message)
