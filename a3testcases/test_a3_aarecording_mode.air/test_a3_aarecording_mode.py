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

pytestmark = [allure.feature("A3录音模式模块用例"), allure.epic("办公本A3")]
    
    
    
#录音原文转写，默认转写方式是默认在线，切换至离线录音模式事弹出二次确认弹窗
@pytest.mark.testcase
@allure.description("录音原文转写，默认转写方式是默认在线，切换至离线录音模式事弹出二次确认弹窗")
@allure.title("录音原文转写，默认转写方式是默认在线，切换至离线录音模式事弹出二次确认弹窗")
def test_recording_default_open():
    if is_login()==True:#未登录
        login()
    #新建笔记
    poco("笔记").click()
    sleep(2)
    poco(text="新建笔记").click()
    sleep(1)
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[6]\
    .child("手写笔").wait_for_appearance(timeout=TIME_OUT)

    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[6]\
    .child("手写笔").click()
    sleep(5)
    #切换离线录音
    #点击录音原文
    poco(text="录音原文").click()
    sleep(1)
    if poco(text="转离线").exists():
        poco(text="转离线").click()
        sleep(2)
        if poco(text="转换为离线模式录音？").exists():
            #点击确认
            poco(text="确定").click()
            sleep(2)
            #切换回实时模式
    sleep(2)
    if poco(text="转在线").exists():
        poco(text="转在线").click()
    sleep(1)
    poco("返回").click()
    #删除笔记
    poco("更多设置").click()
    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    poco("首页").click()



    
#无网络时启动离线录音,切换在线模式,切换离线模式，中英混合语言转写时，切换成
@pytest.mark.testcase
@allure.description("无网络时启动离线录音,切换在线模式,切换离线模式，中英混合语言转写时，切换成")
@allure.title("无网络时启动离线录音,切换在线模式,切换离线模式，中英混合语言转写时，切换成")
def test_recording_no_Internet_change():
    if is_login() == True:  # 未登录
        login()
    # 断开网络
    # 下拉菜单,断开网络
    swipe((1036, 0), (886, 432))
    poco("com.aispeech.ccui.systemui:id/cellGrid") \
        .child("android.widget.LinearLayout")[0] \
        .child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    touch((1000, 1600))
    # 新建笔记
    poco("笔记").click()
    sleep(2)
    poco(text="新建笔记").click()
    sleep(1)
    poco("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View") \
        .child("android.view.View") \
        .child("android.view.View")[6] \
        .child("手写笔").click()
    sleep(5)
    # 切换离线录音
    # 点击录音原文
    poco(text="录音原文").click()
    sleep(2)
    if poco(text="转离线").exists():
        poco(text="转离线").click()
        sleep(2)
        if poco(text="转换为离线模式录音？").exists():
            #点击确认
            poco(text="确定").click()
            sleep(2)
    #切换回实时模式
    sleep(2)
    if poco(text="转在线").exists():
        poco(text="转在线").click()
    sleep(1)
    poco("返回").click()
    # 删除笔记
    poco("更多设置").click()
    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    poco("首页").click()
    # 恢复网络
    # 恢复网络
    swipe((1036, 0), (886, 432))
    poco("com.aispeech.ccui.systemui:id/cellGrid") \
        .child("android.widget.LinearLayout")[0] \
        .child("com.aispeech.ccui.systemui:id/iv_cell_icon") \
        .long_click(duration=2)
    sleep(6)
    poco("com.zlt.zltsettings:id/sw_airplane").click()
    sleep(2)
    poco(text="已连接").wait_for_appearance(timeout=TIME_OUT)
    poco("android.widget.FrameLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("android:id/content") \
        .offspring("com.zlt.zltsettings:id/ll_back") \
        .child("android.widget.ImageView").click()


#普通话语言转写时切换成离线模式，英文转写时切换成离线模式，中英混合语言转写时，切换成离线，非普通话、英文、中英混合 转写时切换成离线模式
@pytest.mark.testcase
@allure.description("普通话语言转写时切换成离线模式，英文转写时切换成离线模式，中英混合语言转写时，切换成离线，非普通话、英文、中英混合 转写时切换成离线模式")
@allure.title("普通话语言转写时切换成离线模式，英文转写时切换成离线模式，中英混合语言转写时，切换成离线，非普通话、英文、中英混合 转写时切换成离线模式")
def test_recording_diff_language_offline():
    if is_login() == True:  # 未登录
        login()
    poco("笔记").click()
    sleep(2)
    poco(text="新建笔记").click()
    sleep(1)
    poco("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View") \
        .child("android.view.View") \
        .child("android.view.View")[6] \
        .child("手写笔").click()
    sleep(5)
    # 切换离线录音
    # 点击录音原文
    poco(text="录音原文").click()
    sleep(3)
    if poco(text="转离线").exists():
        poco(text="转离线").click()
        sleep(2)
        if poco(text="转换为离线模式录音？").exists():
            #点击确认
            poco(text="确定").click()
            sleep(2)
            #切换回实时模式
    sleep(1)
    if poco(text="转在线").exists():
        poco(text="转在线").click()
    # 切换语言为英语
    poco(text="AI笔记").click()
    sleep(2)
    if poco(text="普通话").exists():
        poco(text="普通话").click()
        sleep(2)
        poco(text="普通话").wait_for_appearance(timeout=TIME_OUT)
        poco(text="普通话").click()
        sleep(2)
        poco(text="英语").wait_for_appearance(timeout=TIME_OUT)
        poco(text="英语").click()
        sleep(2)
        poco(text="开始记录").click()
    sleep(1)
    poco(text="录音原文").click()
    sleep(3)
    if poco(text="转离线").exists():
        poco(text="转离线").click()
        sleep(2)
        if poco(text="转换为离线模式录音？").exists():
            #点击确认
            poco(text="确定").click()
            sleep(2)
            #切换回实时模式
    sleep(1)
    if poco(text="转在线").exists():
        poco(text="转在线").click()
    # 切换语言为苏州话
    poco(text="AI笔记").click()
    sleep(2)
    if poco(text="英语").exists():
        # poco(text="英语").wait_for_appearance(timeout=TIME_OUT)
        poco(text="英语").click()
        sleep(2)
        poco("android.widget.FrameLayout") \
            .offspring("android.view.ViewGroup") \
            .child("android.view.View") \
            .child("android.view.View") \
            .child("android.view.View")[0] \
            .child("android.view.View")[1] \
            .child("android.widget.TextView").click()
        sleep(2)
        poco(text="苏州话").wait_for_appearance(timeout=TIME_OUT)
        poco(text="苏州话").click()
        sleep(2)
        poco(text="开始记录").click()
    sleep(2)
    poco(text="录音原文").click()
    sleep(3)
    if poco(text="转离线").exists():
        poco(text="转离线").click()
        sleep(2)
        if poco(text="转换为离线模式录音？").exists():
            #点击确认
            poco(text="确定").click()
            sleep(2)
            #切换回实时模式
    sleep(1)
    if poco(text="转在线").exists():
        poco(text="转在线").click()
    # 切换回普通话
    if poco(text="苏州话").exists():
        poco(text="苏州话").click()
        sleep(2)
        # poco(text="苏州话").wait_for_appearance(timeout=TIME_OUT)
        poco(text="苏州话").click()
        sleep(2)
        if poco(text="普通话").exists():
            # poco(text="普通话").wait_for_appearance(timeout=TIME_OUT)
            poco(text="普通话").click()
        sleep(2)
        poco(text="开始记录").click()
    sleep(2)
    poco("返回").click()
    # 删除笔记
    poco("更多设置").click()
    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    poco("首页").click()


#离线会后总结
# def test_meeting_summary_offline(default_note="离线会后总结"):
#     if is_login()==True:#未登录
#         login()
#     poco(text="默认笔记").click()
#     sleep(1)
#     if poco(text=default_note).exists():
#         #打开默认的笔记
#         poco(text=default_note).click()
#         sleep(1)
#         poco(text="会后总结").click()
#         sleep(1)
#         poco("返回").click()
#         #删除笔记
#         poco("更多设置").click()
#         sleep(1)
#         poco(text="删除").click()
#         sleep(1)
#         poco(text="确认").click()

#     else:
#         poco(text="全部笔记").click()
#     sleep(1)
#     poco("首页").click()

    
    
    
    
    

#开启录音，AI笔记默认模型是智能模型dfmpro
@pytest.mark.testcase
@allure.description("开启录音，AI笔记默认模型是智能模型dfmpro")
@allure.title("开启录音，AI笔记默认模型是智能模型dfmpro")
def test_ai_note_default_model():
    if is_login()==True:#未登录
        login()
    sleep(2)
    poco(text="新建笔记").click()
    sleep(1)
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[6]\
    .child("手写笔").click()
    sleep(5)
    poco("返回").click()
    sleep(3)
    #删除笔记
    #直接返回到首页了？？？
    poco("笔记").click()
    sleep(1)
    poco("更多设置").wait_for_appearance(timeout=TIME_OUT)
    poco("更多设置").click()
    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    poco("首页").click()

if __name__=="__main__":
#     test_recording_default_open()
#     test_recording_no_Internet_change()
    test_ai_note_default_model()
    
    
