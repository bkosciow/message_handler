What it is
===
App used at Raspberry Pi as receiver of incoming messages and pass them to registered handlers 
(relay, screen, sensors) 

    from message_listener.server import Server
    
    msg = Message('rpi1')
    svr = Server(msg)
    svr.add_handler('20x4', Handler(lcd))
    svr.start()

Initialization:

    __init__(self, message, port=5053, ip_address='0.0.0.0', buffer_size=65535)
    
Read more: [https://koscis.wordpress.com/2017/03/03/raspberry-pi-as-a-node/](https://koscis.wordpress.com/2017/03/03/raspberry-pi-as-a-node/)


