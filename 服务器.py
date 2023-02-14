import threading
from socket import *
import queue

host_name='10.32.3.158'#IP
port_num=8000
app_data='0'
connectionSocket_stm32=0
stm32_data=0

def sockt_app():
    global app_data
    global stm32_data
    while (True):#为多个客户端服务
        #等待客户端连接
        connectionSocket,address=serverSocket.accept()
        print('app一个客户端连接过来了，地址是：%s'%str(address))
        while (True):#try没有发生错误-》else内的代码-》finally中的代码。
            try:#try中发生异常-》被except捕获并执行except片段中的代码-》执行finally中的代码。
                #接收数据
                message = connectionSocket.recv(1024).decode()
                if message:
                    app_data=message[-3:-2]
                    print('app got the message form the client: '+message[-3:-2])
                    #print('app got the message form the client: '+message[-10:])
                    #发送数据
                    connectionSocket.send(stm32_data.encode())
                    print('向app发送了'+stm32_data)
                    break
                else:break
            except:break
        #关闭，停止对客户端服务
        connectionSocket.close()
    
    while(True):
        app_recv_=threading.Thread(target=app_recv)#开启子线程接受数据
        app_recv_.start()
        if stm32_data!='0':
            send_message=stm32_data
            print(app_data)
            stm32_data='0'
            connectionSocket_app.send(send_message.encode())
def stm32_recv():
    while(True):
        message = connectionSocket_stm32.recv(1024).decode()
        print('stm32 got the message form the client: '+message)
def sockt_stm32():
    global connectionSocket_stm32
    global app_data#引用全局变量
    connectionSocket_stm32,address=serverSocket.accept()
    print('stm32一个客户端连接过来了，地址是：%s'%str(address))
    stm32_recv_=threading.Thread(target=stm32_recv)
    stm32_recv_.start()
    while(True):
        
        if app_data!='0':
            send_message=app_data
            print(app_data)
            app_data='0'
            connectionSocket_stm32.send(send_message.encode())
            
def sockt_openmv():
    connectionSocket,address=serverSocket.accept()
    print('openmv一个客户端连接过来了，地址是：%s'%str(address))
    while(True):
        try:
            message = connectionSocket.recv(1024).decode()
            print('openmv got the message form the client: '+message[-10:])
        except:pass
        send_message='i get openmv'
        connectionSocket.send(send_message.encode())
        
if '_name_'=='_name_':
    #指明用的是ipv4，TCP传输
    serverSocket=socket(AF_INET,SOCK_STREAM)   
    # 设置端口复用
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #绑定ip和端口号
    serverSocket.bind((host_name,port_num))
    serverSocket.listen()#队列最大数为2
    #实例化线程
    app=threading.Thread(target=sockt_app)
    stm32=threading.Thread(target=sockt_stm32)
    openmv=threading.Thread(target=sockt_openmv)
    #开线程
    app.start()
    #stm32.start()
    #openmv.start()
