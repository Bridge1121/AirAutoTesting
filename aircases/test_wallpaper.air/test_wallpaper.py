# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

import allure
import pytest
from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))



#验证能否成功访问壁纸设置，验证能否选择图片，验证无图片可选择时的处理，添加新墙纸导入.txt文件
@allure.description("验证能否成功访问壁纸设置，验证能否选择图片，验证无图片可选择时的处理，添加新墙纸导入.txt文件")
@pytest.mark.testcase
def test_wallpaper_choose_pic():
    if is_login()==True:
        login()
    poco("应用").click()
    poco("设置图标").click()
    poco(text="显示与亮度").click()
    poco(text="壁纸").click()
    #点击添加图片
    poco("com.zlt.zltsettings:id/btn_new_wallpaper").click()
    sleep(1)
    if exists(Template(r"tpl1750821729163.png", record_pos=(0.422, -0.472), resolution=(1200, 1920))):
        touch(Template(r"tpl1750821729163.png", record_pos=(0.422, -0.472), resolution=(1200, 1920)))
    pic_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.android.documentsui:id/drawer_layout")\
    .child("android.widget.ScrollView")\
    .offspring("com.android.documentsui:id/container_directory")\
    .offspring("com.android.documentsui:id/dir_list")\
    .child("com.android.documentsui:id/item_root")
    if pic_list and len(pic_list)>0:
        for p in pic_list:
            p.click()
            break
        poco("应用裁切").click()
        poco(text="完成").click()
    else:
        #右滑返回
        swipe((3,900),(200,900))
    #点击添加不支持的文件
    poco("com.zlt.zltsettings:id/btn_new_wallpaper").click()
    sleep(1)
    poco(text="WPS Office").click()
    file_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .offspring("cn.wps.moffice_eng:id/layout_fit_pad_outer_root_node")\
    .child("android.widget.LinearLayout")\
    .child("cn.wps.moffice_eng:id/phone_home_root")\
    .offspring("android.widget.FrameLayout")\
    .offspring("cn.wps.moffice_eng:id/file_select_recent_content_list")\
    .child("cn.wps.moffice_eng:id/fb_listview_item_layout")
    if file_list and len(file_list)>0:
        poco("android.widget.FrameLayout")\
        .child("android.widget.LinearLayout")\
        .offspring("android:id/content")\
        .offspring("cn.wps.moffice_eng:id/layout_fit_pad_outer_root_node")\
        .child("android.widget.LinearLayout")\
        .child("cn.wps.moffice_eng:id/phone_home_root")\
        .offspring("android.widget.FrameLayout")\
        .offspring("cn.wps.moffice_eng:id/file_select_recent_content_list")\
        .child("cn.wps.moffice_eng:id/fb_listview_item_layout")[0]\
        .offspring("cn.wps.moffice_eng:id/fb_filename_text").click()
        poco("android.widget.Button").click()
        poco(text="完成").swipe([0.0, -0.0049])
    else:
        poco("cn.wps.moffice_eng:id/titlebar_back_icon").click()
    sleep(1)
    #点击返回
    poco(text="系统设置").click()
    poco("首页").click()
    

    


if __name__=="__main__":
    test_wallpaper_choose_pic()





