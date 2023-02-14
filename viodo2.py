# 把照片合成视频

import os
import cv2
import uuid


def read_picture():
    path = 'C:\\Users\\Administrator\\Desktop'
    file_list = os.listdir('C:\\Users\\Administrator\\Desktop')

    fps = 2 # 视频每秒2帧
    height = 70
    weight = 190
    size = (int(height), int(weight))  # 需要转为视频的图片的尺寸
    return [path, fps, size, file_list]


def write_video():
    path, fps, size, file_list = read_picture()
    # AVI格式编码输出 XVID
    four_cc = cv2.VideoWriter_fourcc(*'XVID')
    save_path = path + '\\' + '%s.avi' % str(uuid.uuid1())
    video_writer = cv2.VideoWriter(save_path, four_cc, float(fps), size)
    # 视频保存在当前目录下
    for item in file_list:
        if item.endswith('.jpg') or item.endswith('.png'):
            # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
            item = path + '\\' + item
            img = cv2.imread(item)
            re_pics = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)  # 定尺寸
            if len(re_pics):
                video_writer.write(re_pics)

    video_writer.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    write_video()

