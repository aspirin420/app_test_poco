# -*- coding: utf-8 -*-

from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class Geetest():
    """
    破解极验
    """

    def __init__(self):
        self.poco = AndroidUiautomationPoco()

    def move_to_gap(self, slider, track):
        """

        :param slider: 滑块
        :param track: 归集
        :return:
        """
        pass

    def get_slider(self):
        """
        获取滑块
        :return:
        """
        slider = ''

    def get_track(self):
        pass

    def is_pixel_equal(self, img1, img2, x, y):
        pass

    def get_gap(self, img1, img2):
        pass

    def get_geetest_img(self):
        pass
