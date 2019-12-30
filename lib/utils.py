# -*- coding: utf-8 -*-

from airtest.core.android.adb import *
from airtest.core.api import connect_device, start_app


class Data(object):
    """
    公用数据
    """

    android_package = '**.android.debug'
    iOS_package = 'com.apple.calculator'
    device_type = ''


def connect_android():
    """
    连接 Android 手机
    :return: 是否连接设备并启动了 app
    """

    adb = ADB()
    device_list = adb.devices()
    if len(device_list) >= 1:
        try:
            androd_device = 'Android://127.0.0.1:5037/' + device_list[0][0]
            connect_device(androd_device)
            Data.device_type = 'android'
            start_app(Data.android_package)
            return True
        except Exception as e:
            print('连接 android 失败：', e)
            return False
    else:
        return False


def connect_iOS():
    """
    连接 iOS 手机
    :return: 是否连接设备并启动了 app
    """

    try:
        iOS_device = 'IOS:http://127.0.0.1:8100'
        connect_device(iOS_device)
        Data.device_type = 'iOS'
        start_app(Data.iOS_package)
        return True
    except Exception as e:
        print('连接 iOS 失败：', e)
        return False
