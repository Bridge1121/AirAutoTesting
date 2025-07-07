# -*- encoding=utf8 -*-
__author__ = "cailin.liao_sx"

import os
import sys

import allure
import pytest
from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))

pytestmark = [allure.feature("下拉菜单模块用例"), allure.epic("办公本v2.4.0")]




#下拉菜单点击静音按钮进行静音,下拉菜单点击解除静音按钮
@pytest.mark.testcase
@allure.description("下拉菜单点击静音按钮进行静音,下拉菜单点击解除静音按钮")
@allure.title("下拉菜单点击静音按钮进行静音,下拉菜单点击解除静音按钮")
def test_down_menu_mute():
    swipe((1036,0),(886,432))
    swipe((800,900),(800,800))
    poco(text="静音").click()
    poco(text="静音").click()
    sleep(1)
    touch((600,1500))


    



#当前在笔记页面与当前不在笔记页面时，分别下拉菜单点击新建笔记按钮，以及下拉菜单点击分屏笔记按钮验证
@pytest.mark.testcase
@allure.description("当前在笔记页面与当前不在笔记页面时，分别下拉菜单点击新建笔记按钮，以及下拉菜单点击分屏笔记按钮验证")
@allure.title("当前在笔记页面与当前不在笔记页面时，分别下拉菜单点击新建笔记按钮，以及下拉菜单点击分屏笔记按钮验证")
def test_down_menu_create_new_note():
    #当前不在笔记页面
    swipe((1036,0),(886,432))
    poco(text="新建笔记").click()
    #当前在笔记页面
    swipe((1036,0),(886,432))
    poco(text="新建笔记").click()
    swipe((1036,0),(886,432))
    poco(text="分屏笔记").click()
    #当前不在笔记页面且不在launcher中
    poco("返回").click()
    poco(text="应用").click()
    poco("图库图标").click()
    swipe((1036,0),(886,432))
    poco(text="分屏笔记").click()
    swipe((600,1900),(600,1300))
    swipe((600,1900),(600,1300))
    poco(text="笔记").click()
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="删除").click()
    poco(text="确认").click()
    clear_recycle_bin()
    poco(text="首页").click()


    
    
#下拉菜单点击文件传输按钮
@pytest.mark.testcase
@allure.description("下拉菜单点击文件传输按钮")
@allure.title("下拉菜单点击文件传输按钮")
def test_down_menu_file_transfers():
    swipe((1036,0),(886,432))
    poco(text="文件传输").click()
    poco("返回").click()



#启用全局禁触功能，检查下拉菜单操作在禁触状态下的反应;在禁触状态下点击第三方应用
@pytest.mark.testcase
@allure.description("启用全局禁触功能，检查下拉菜单操作在禁触状态下的反应;在禁触状态下点击第三方应用")
@allure.title("启用全局禁触功能，检查下拉菜单操作在禁触状态下的反应;在禁触状态下点击第三方应用")
def test_down_menu_do_not_touch():
    swipe((1036,0),(886,432))
    poco(text="关闭手触").click()
    swipe((900,1269),(900,1200))
    poco(text="笔记").click()
    touch((500,1770),duration=2)
    swipe((1036,0),(886,432))
    poco(text="关闭手触").click()
    swipe((900,1269),(900,1200))

    


#全屏手势验证禁触
@pytest.mark.testcase
@allure.description("全屏手势验证禁触")
@allure.title("全屏手势验证禁触")
def test_full_screen_gestures_do_not_touch():
    swipe((1036,0),(886,432))
    poco(text="关闭手触").click()
    swipe((900,1269),(900,1200))
    #全屏手势左滑
    swipe((1160,1000),(0,1000))
    #全屏手势右滑
    swipe((0,1000),(1160,1000))
    #全屏手势上滑
    swipe((600,1900),(600,1000))
    swipe((600, 1900), (600, 1000))

    
    
    





if __name__=="__main__":
    test_down_menu_mute()
    test_down_menu_create_new_note()
    test_down_menu_file_transfers()
    test_down_menu_do_not_touch()
    test_full_screen_gestures_do_not_touch()
    
    
    
