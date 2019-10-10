#!/usr/bin/env python3

from concurrent import futures
import time
import grpc
import echo_pb2
import echo_pb2_grpc


# 实现 proto 文件中定义的 GreeterServicer
class Echo(echo_pb2_grpc.EchoServicer):
    # 实现 proto 文件中定义的 rpc 调用

    def Hi(self, request, context):
        print(request)
        return echo_pb2.SimpleMessage(message='replyhi {msg}'.format(msg=request.message))


def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_pb2_grpc.add_EchoServicer_to_server(Echo(), server)
    server.add_insecure_port('[::]:9090')
    print('start listening at', ':9090')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
