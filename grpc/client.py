import time
import random
import grpc
import test_pb2 as pb2
import test_pb2_grpc as pb2_grpc

def test():
    index = 0
    while 1:
        time.sleep(1)
        data = str(random.random())
        if index == 5:   #index为5，断开连接，客户端不向服务端主动发送数据
            break
        print(index)
        index += 1
        yield pb2.TestClientSendStreamRequest(data=data)

def run():
    conn = grpc.insecure_channel('127.0.0.1:5000')
    client = pb2_grpc.demoStub(channel=conn)
    #普通rpc协议传输方式
    try:
        resposne = client.hellojlc(pb2.hellojlcReq(
            name='jlc',
            age=23
        ))
        print(resposne.result)
    except Exception as e:
        print(e.code().name, e.code().value)
        print(e.details())

    #单向服务端发送客户端流传输方式
    #response = client.TestClientRecvStream(pb2.TestClientRecvStreamRequest(
    #    data = 'jlc'
    #))
    #for item in response:
    #    print(item.result)

    #单向客户端发送给服务器端流传输方式
    #response = client.TestClientSendStream(test())
    #print(response.result)

    #双向流的方式传输
    #response = client.TestTwoWayStream(test())    #客户端以流的形式不停的发信息给服务器
    #for res in response:
    #    print(res.result)

if __name__ == '__main__':
    run()