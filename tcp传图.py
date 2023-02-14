import network, usocket
import sensor, image, time, os, tf, math,machine
from pyb import UART
import json
from pyb import LED
import lcd,sys,struct,socket

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((200, 200))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking

blue_lab=(30,75,-20,20,-60,-20)#蓝色

clock = time.clock()

#返回最大色块（也就是返回最近的垃圾）
def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob[2]*blob[3] > max_size:
            max_blob=blob
            max_size = blob[2]*blob[3]
    return max_blob

def pack_pic():
    #包头标志
    arrBuf = bytearray(b'\xff\xaa\xff\xaa')

    #以二进制方式读取图片
    picData = open('example.jpg', 'rb')
    picBytes = picData.read()

    #图片大小
    picSize = len(picBytes)

    #数据体长度 = guid大小(固定) + 图片大小
    datalen = 64 + picSize

    #组合数据包
    arrBuf += bytearray(datalen.to_bytes(4, 'little'))
    guid = 23458283482894382928948
    arrBuf += bytearray(guid.to_bytes(64,'little'))
    arrBuf += picBytes
    return arrBuf


while(True):#连接wifi
    #连接wifi获取ip地址
    try:
        SSID='dada' # Network SSID
        KEY='12345678'  # Network key
        wlan = network.WINC()
        wlan.connect(SSID, key=KEY, security=wlan.WPA_PSK)
        print('wifi连接成功')
    except:
        print('wifi连接失败')
        break
    while(True):#绑定ip端口号
        #tcp通信-------------------------
        try:
            sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
            sock.connect(('10.32.3.158',7788))
            print('绑定成功')
        except:
            print('绑定失败')
            break
        while(True):#保存传输图片
            time.sleep_ms(5000)
            #保存图片
            sensor.snapshot().save("example.jpg")
            #打包图片
            arrBuf=pack_pic()
            #传输图片
            #try中发生异常-》被except捕获并执行except片段中的代码-》
            try:
                sock.send(arrBuf)
                print('传输成功')
            except:
                print('传输失败')
                break

        #关闭连接
        sock.close()

