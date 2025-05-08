import time

import grpc
import test_pb2 as pb2
import test_pb2_grpc as pb2_grpc
from concurrent import futures


class demo(pb2_grpc.demoServicer):
    def hellojlc(self, request, context):
        name = request.name
        age = request.age

        #context.set_details('bug')   #添加错误描述
        #context.set_code(grpc.StatusCode.DATA_LOSS)  #设置错误码
        #raise context   #抛出异常

        result = f'my name is {name}, i am {age} years old'
        return pb2.hellojlcReply(result=result)
    def TestClientRecvStream(self, request, context):
        index = 0
        while context.is_active():   #监听客户端是不是一个活跃的状态
            data = request.data
            if data == 'close':    #收到close数据，服务器端停止运行
                print('data is close, request will cancel')
                context.cancek()
            time.sleep(1)
            index += 1
            result = 'send %d %s' % (index, data)
            print(result)
            yield pb2.TestClientRecvStreamResponse(  # 服务器端要给客户端返回一种流的形式，通过yield形式发送
                result=result
            )
    def TestClientSendStream(self, request_iterator, context):   #request_iterator表示迭代器，来使服务器获取客户端信息
        index = 0
        for request in request_iterator:
            print(request.data, ':',index)
            if index == 10:         #index为10，断开连接
                break
            index += 1
        return pb2.TestClientSendStreamResponse(result='ok')   #断开连接后，给客户端返回一个ok

    def TestTwoWayStream(self, request_iterator, context):
        index = 0
        for request in request_iterator:   #从客户端获取数据的方式
            data = request.data
            if index == 3:
                context.cancel()     #服务器强制断开命令，客户端会收到异常报错
            index += 1
            yield pb2.TestTwoWayStreamResponse(result='service send client %s' % data)

def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    pb2_grpc.add_demoServicer_to_server(demo(),grpc_server)
    grpc_server.add_insecure_port('127.0.0.1:5000')
    print('server will start at 127.0.0.1:5000')
    grpc_server.start()

    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)

if __name__ == '__main__':
    run()