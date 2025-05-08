import paho.mqtt.client as mqtt
import threading
import random
import time
# 连接成功回调
class Mqtt_Subscriber:
    '''
        mqtt消息通讯接口
    '''
    def __init__(self,central_ip='10.234.75.59',port=1883,
                 topic_name='test',callback_func=None,
                 node_name='bci_',anonymous=True,timeout=60):
        '''
            :param central_ip: Broker的地址
            :param port:  端口号
            :param topic_name: 接收的消息名称
            :param callback_func: 指定回调函数
            :param timeout:  连接延时
            :param node_name: 节点名称
            :param anonymous: 是否同时允许多个节点
        '''
        self.topic=topic_name
        self.callback=callback_func
        self.broker_ip=central_ip
        self.broker_port=port
        self.timeout=timeout
        self.connected=False
        self.node_name=node_name
        if anonymous:
            self.node_name=self.node_name+str(random.randint(100000,999999))
        self.Start()
    def Start(self):
        '''
        开启publisher
        :return:
        '''
        self.client = mqtt.Client(self.node_name)     #创建客户端
        self.client.on_connect = self.on_connect  # 指定回调函数
        self.client.on_message=self.default_on_message
        self.client.connect(self.broker_ip, self.broker_port, self.timeout)     #开始连接
        self.client.subscribe(self.topic)
        self.client.loop_start()    #开启一个独立的循环通讯线程。

    '''
                回调函数
    '''
    def default_on_message(self,client, userdata, msg):
        '''
            默认回调函数
        '''
        print(msg.payload.decode('utf-8'))

    def on_connect(self,client, userdata, flags, rc):
        '''
            连接到broker的回调函数
        '''
        if rc==0:
            self.connected=True

        else:
            raise Exception("Failed to connect mqtt server.")

if __name__=='__main__':
    p=Mqtt_Subscriber()
    while not p.connected:
        pass
    while True:
        time.sleep(1)
