from unittest import TestCase

import cv2

from utils.ImageUtils import bytes2cv, image_size
from utils.STFUtils.minicap import MinicapStream
from utils.ScreenUtils import suitable_screensize


class TestMiniCapUtils(TestCase):

    def test_minicap_stream(self):
        builder = MinicapStream.getBuilder("127.0.0.1", 1717)
        builder.run()
        print("show image")
        print(builder.queue.size())
        while True:
            screen = bytes2cv(builder.queue.get())
            # show_adapt(screen, "Screen", 1)
            # 缩放到原来的二分之一，输出尺寸格式为（宽，高）
            adapt_size = tuple(int(i) for i in suitable_screensize(image_size(screen)))
            screen_resize = cv2.resize(screen, adapt_size)
            cv2.imshow("Screen", screen_resize)
            cv2.waitKey(1)
