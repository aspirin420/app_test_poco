# -*- coding: utf-8 -*-

import base64
import unittest
from airtest.core.api import home
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.ios import iosPoco
from airtest.core.android.adb import *
from lib.utils import Data

abs_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(abs_dir)


class BaseAppCase(unittest.TestCase):
    """
    基类：整个用例执行前的操作以及公共的方法
    """

    @classmethod
    def setUpClass(cls):
        """
        整个用例执行的前置条件
        """

        super(BaseAppCase, cls).setUpClass()
        if Data.device_type == 'android':
            cls.poco = AndroidUiautomationPoco()
        else:
            cls.poco = iosPoco()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        """
        整个用例执行的后置条件
        """

        home()
        print('tearDownClass!!!')

    @classmethod
    def save_img(cls, img_name):
        """
        保存图片
        保存的图片同时可用于展示在报告里
        :param img_name: 要保存的图片的名称
        """

        b64img, fmt = cls.poco.snapshot()
        img_path = abs_dir + '/img/{}-{}.png'.format(img_name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        with open(img_path, 'wb') as f:
            f.write(base64.b64decode(b64img))
        print("<img src='" + img_path + "' width=600 />")  # 把图片发送到 BR 报告里，BR 的特性
