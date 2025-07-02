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

pytestmark = [allure.feature("A3ai按键模块用例"), allure.epic("办公本A3")]
    
    
#未打开笔记录音，正常状态下双击AI按键进行录音,已有笔记录音，双击ai按键
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("未打开笔记录音，正常状态下双击AI按键进行录音,已有笔记录音，双击ai按键")
@allure.title("未打开笔记录音，正常状态下双击AI按键进行录音,已有笔记录音，双击ai按键")
def test_double_press_recording():
    if is_login()==True:#未登录
        login()
    #双击ai按键
    os.system("adb shell am broadcast -a android.ai.speech.action.KEY_EVENT_DOUBLE_PRESS")
    sleep(2)
    #返回
    poco("返回").click()
    #删除笔记
    poco("更多设置").click()
    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    #新建笔记开始录音，再双击按键，返回
    #新建笔记
    poco("笔记").click()
    sleep(1)
    poco(text="新建笔记").click()
    sleep(1)
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[6]\
    .child("手写笔").click()
    sleep(5)
    #再次双击
    os.system("adb shell am broadcast -a android.ai.speech.action.KEY_EVENT_DOUBLE_PRESS")
    #返回
    poco("返回").click()
    #删除笔记
    poco("更多设置").click()
    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    sleep(1)
    poco("首页").click()
    
    
    
    
#验证长按AI键1秒以上正常唤醒AI助手,验证密码锁屏下长按无响应
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("验证长按AI键1秒以上正常唤醒AI助手,验证密码锁屏下长按无响应")
@allure.title("验证长按AI键1秒以上正常唤醒AI助手,验证密码锁屏下长按无响应")
def test_long_press_open_ai():
    if is_login()==True:#未登录
        login()
    #长按ai按键
    os.system("adb shell am broadcast -a android.ai.speech.action.KEY_EVENT_LONG_PRESS")
    sleep(1)
    touch(Template(r"tpl1751348232173.png", record_pos=(0.463, -0.732), resolution=(1600, 2560)))
    #返回到首页
    sleep(1)
    poco("首页").click()
    #锁屏
    os.system("adb shell input keyevent KEYCODE_POWER")
    sleep(1)
    #长按ai按键
    os.system("adb shell am broadcast -a android.ai.speech.action.KEY_EVENT_LONG_PRESS")
    sleep(1)
    #解锁
    os.system("adb shell input keyevent KEYCODE_WAKEUP")
    sleep(1)
    swipe((758,2549),(758,1600))
    sleep(1)
    #输入密码
    for i in range(3):
        touch((789,2301))
    sleep(1)
    keyevent("enter")
    
    
#验证密码锁屏下长按无响应,锁屏状态下双击AI按键进行录音
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("验证密码锁屏下长按无响应,锁屏状态下双击AI按键进行录音")
@allure.title("验证密码锁屏下长按无响应,锁屏状态下双击AI按键进行录音")
def test_lock_screen_double_press():
    if is_login()==True:#未登录
        login()
    #锁屏
    os.system("adb shell input keyevent KEYCODE_POWER")
    sleep(1)
    #双击ai按钮
    os.system("adb shell am broadcast -a android.ai.speech.action.KEY_EVENT_DOUBLE_PRESS")
    #解锁
    os.system("adb shell input keyevent KEYCODE_WAKEUP")
    sleep(1)
    swipe((758,2549),(758,1600))
    sleep(1)
    #输入密码
    for i in range(4):
        touch((789,2301))
    sleep(1)
    keyevent("enter")
    #返回删除笔记
    poco("返回").click()
    #删除笔记
    poco("更多设置").click()
    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    sleep(1)
    poco("首页").click()
    
    
    
    
    
#正在录音转写时长按AI助手仍可唤醒
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("正在录音转写时长按AI助手仍可唤醒")
@allure.title("正在录音转写时长按AI助手仍可唤醒")
def test_recording_long_press_open_ai():
    if is_login()==True:#未登录
        login()
    #新建笔记
    poco("笔记").click()
    sleep(1)
    poco(text="新建笔记").click()
    sleep(1)
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[6]\
    .child("手写笔").click()
    sleep(5)
    #长按ai按键，打开ai助手
    os.system("adb shell am broadcast -a android.ai.speech.action.KEY_EVENT_LONG_PRESS")
    #返回
    #关闭，返回首页
    sleep(1)
    touch(Template(r"tpl1751348232173.png", record_pos=(0.463, -0.732), resolution=(1600, 2560)))
    sleep(1)
    #返回
    poco("返回").click()
    #删除笔记
    poco("更多设置").click()
    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    poco("首页").click()
    
    
    
    
    
#验证无网络时AI助手仍可部分使用
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("验证无网络时AI助手仍可部分使用")
@allure.title("验证无网络时AI助手仍可部分使用")
def test_open_ai_helper_no_internet():
    if is_login()==True:#未登录
        login()
    #断开网络
    # 下拉菜单,断开网络
    swipe((1036, 0), (886, 432))
    poco("com.aispeech.ccui.systemui:id/cellGrid")\
    .child("android.widget.LinearLayout")[0]\
    .child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    touch((1000,1600))
    #长按ai按键
    os.system("adb shell am broadcast -a android.ai.speech.action.KEY_EVENT_LONG_PRESS")
    sleep(1)
    touch(Template(r"tpl1751348232173.png", record_pos=(0.463, -0.732), resolution=(1600, 2560)))
    sleep(1)
    # 恢复网络
    swipe((1036, 0), (886, 432))
    poco("com.aispeech.ccui.systemui:id/cellGrid") \
    .child("android.widget.LinearLayout")[0] \
    .child("com.aispeech.ccui.systemui:id/iv_cell_icon") \
    .long_click(duration=2)
    sleep(5)
    poco("com.zlt.zltsettings:id/sw_airplane").click()
    sleep(2)
    poco(text="已连接").wait_for_appearance(timeout=TIME_OUT)
    poco("android.widget.FrameLayout") \
    .child("android.widget.LinearLayout") \
    .offspring("android:id/content") \
    .offspring("com.zlt.zltsettings:id/ll_back") \
    .child("android.widget.ImageView").click()
    
    
    
def test():
    #锁屏
    os.system("adb shell input keyevent KEYCODE_POWER")
    sleep(1)
    #解锁
    os.system("adb shell input keyevent KEYCODE_WAKEUP")
    sleep(1)
    swipe((758,2549),(758,1600))
    sleep(1)
    #输入密码
    for i in range(4):
        touch((789,2301))
    sleep(1)
    keyevent("enter")
    
    
if __name__=="__main__":
    test()
    

    
    

    
    
