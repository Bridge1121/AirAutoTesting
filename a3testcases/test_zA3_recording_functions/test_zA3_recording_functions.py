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

pytestmark = [allure.feature("A3录音模块用例"), allure.epic("办公本A3")]




#录音原文时，离线，会后总结默认离线模式

@pytest.mark.testcase
@allure.description("录音原文时，离线，会后总结默认离线模式")
@allure.title("录音原文时，离线，会后总结默认离线模式")
def test_offline_summary_after_the_meeting():
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco(text="录音原文").click()
    sleep(2)
    sleep(3)
    if poco(text="转离线").exists():
        poco(text="转离线").click()
        sleep(2)
        if poco(text="转换为离线模式录音？").exists():
            # 点击确认
            poco(text="确定").click()
            sleep(2)
            # 切换回实时模式
    poco(text="转在线").click()
    # poco(text="转离线").click()
    # poco(text="确定").click()
    poco(text="结束").click()
    sleep(10)
    poco(text="会后总结").click()
    sleep(10)
    poco("返回").click()
    poco("更多设置").wait_for_appearance(timeout=TIME_OUT)
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="首页").click()





#实时录音是在线模式时，会后总结默认模型是智能模型dfmpro

@pytest.mark.testcase
@allure.description("实时录音是在线模式时，会后总结默认模型是智能模型dfmpro")
@allure.title("实时录音是在线模式时，会后总结默认模型是智能模型dfmpro")
def test_online_summary_after_the_meeting(default_group="默认笔记", default_note="测试录音"):
    if is_login() == True:
        login()
    # 网络正常情况下
    poco(text="笔记").click()
    poco(text=default_group).click()
    sleep(1)
    # 点击准备好的录音笔记
    poco(text=default_note).click()
    sleep(2)
    poco(text="会后总结").click()
    sleep(2)
    if poco(text="智能模型").exists():
        poco(text="智能模型").click()
    poco("返回").click()
    sleep(2)
    #     poco("更多设置").wait_for_appearance(timeout=TIME_OUT)
    #     poco("更多设置").click()
    #     poco(text="删除").click()
    #     poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()


#网络正常时，可正常切换会后总结中的转写模型,未联网时，切换转写模型，提示无网，总结失败

@pytest.mark.testcase
@allure.description("网络正常时，可正常切换会后总结中的转写模型,未联网时，切换转写模型，提示无网，总结失败")
@allure.title("网络正常时，可正常切换会后总结中的转写模型,未联网时，切换转写模型，提示无网，总结失败")
def test_diff_internet_summary_after_the_meeting(default_group="默认笔记", default_note="测试录音"):
    #     if is_login()==True:
    #         login()
    # 网络正常情况下
    poco(text="笔记").click()
    poco(text=default_group).click()
    sleep(1)
    # 点击准备好的录音笔记
    poco(text=default_note).click()
    sleep(2)
    poco(text="会后总结").click()
    sleep(2)
    # 切换AI模型
    if poco(text="智能模型").exists():
        poco(text="智能模型").click()
        sleep(1)
        poco(text="Deepseek-R1").click()
        sleep(1)
        poco(text="确定").click()
        sleep(10)
        # 断开网络
        swipe((1036, 0), (886, 432))
        (poco("com.aispeech.ccui.systemui:id/cellGrid").child("android.widget.LinearLayout")[0].child(
            "com.aispeech.ccui.systemui:id/iv_cell_icon")).click()
        sleep(1)
        touch((523, 2208))
        # 再次切换AI模型
        poco(text="Deepseek-R1").click()
        sleep(1)

    #     poco("更多设置").wait_for_appearance(timeout=TIME_OUT)
    #     poco("更多设置").click()
    #     sleep(1)
    #     poco(text="删除").click()
    #     sleep(1)
    #     poco(text="确认").click()
        sleep(1)

        # 恢复网络
        swipe((1036, 0), (886, 432))
        poco("com.aispeech.ccui.systemui:id/cellGrid") \
            .child("android.widget.LinearLayout")[0] \
            .child("com.aispeech.ccui.systemui:id/iv_cell_icon") \
            .click()
        sleep(5)
        touch((523, 2208))
        # 切换回智能模型
        poco(text="Deepseek-R1").click()
        sleep(1)
        poco(text="智能模型").click()
        sleep(1)
        poco(text="确定").click()

    #     poco("com.zlt.zltsettings:id/sw_airplane").click()
    #     sleep(2)
    #     poco(text="已连接").wait_for_appearance(timeout=TIME_OUT)
    #     poco("android.widget.FrameLayout") \
    #     .child("android.widget.LinearLayout") \
    #     .offspring("android:id/content") \
    #     .offspring("com.zlt.zltsettings:id/ll_back") \
    #     .child("android.widget.ImageView").click()
    poco("返回").click()
    sleep(2)
    poco(text="全部笔记").click()
    poco(text="首页").click()


#精转前后查看录音原文tap页自动分析说话人展示，关闭说话人1的分析结果再重新生成

@pytest.mark.testcase
@allure.description("精转前后查看录音原文tap页自动分析说话人展示，关闭说话人1的分析结果再重新生成")
@allure.title("精转前后查看录音原文tap页自动分析说话人展示，关闭说话人1的分析结果再重新生成")
def test_ai_analyze_speaker(default_group="默认笔记", default_note="测试录音"):
    #     if is_login()==True:
    #         login()
    # 未精转时
    poco(text="笔记").click()
    poco(text=default_group).click()
    sleep(1)
    # 点击准备好的录音笔记
    poco(text=default_note).click()
    sleep(2)
    poco(text="录音原文").click()
    sleep(1)
    poco(text="AI分析说话人").wait_for_appearance(timeout=TIME_OUT)
    poco(text="AI分析说话人").click()
    sleep(10)
    # 关闭说话人1的分析结果再重新生成
    touch(Template(r"tpl1751531691118.png", record_pos=(0.403, 0.006), resolution=(1600, 2560)))
    sleep(10)
    poco(text="AI分析说话人").wait_for_appearance(timeout=TIME_OUT)
    poco(text="AI分析说话人").click()
    sleep(10)
    # 完成说话人1的分析结果
    touch(Template(r"tpl1751531711686.png", record_pos=(0.451, 0.007), resolution=(1600, 2560)))
    sleep(1)
    poco("返回").click()
    sleep(2)
    #     poco("更多设置").wait_for_appearance(timeout=TIME_OUT)
    #     poco("更多设置").click()
    #     sleep(1)
    #     poco(text="删除").click()
    #     poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()


#点击查找替换时，隐藏AI分析说话人卡片；点击编辑按钮进入编辑状态时，隐藏AI分析说话人卡片

@pytest.mark.testcase
@allure.description("点击查找替换时，隐藏AI分析说话人卡片；点击编辑按钮进入编辑状态时，隐藏AI分析说话人卡片")
@allure.title("点击查找替换时，隐藏AI分析说话人卡片；点击编辑按钮进入编辑状态时，隐藏AI分析说话人卡片")
def test_hide_ai_analyze_speaker(default_group="默认笔记",default_note="测试录音"):
#     if is_login()==True:
#         login()
    poco(text="笔记").click()
    sleep(1)
    poco(text=default_group).click()
    sleep(1)
    #点击准备好的录音笔记
    poco(text=default_note).click()
    sleep(2)
    poco(text="录音原文").click()
    sleep(1)
    poco(text="AI分析说话人").wait_for_appearance(timeout=TIME_OUT)
    poco(text="AI分析说话人").click()
    poco(text="查找/替换").click()
    touch(Template(r"tpl1751531691118.png", record_pos=(0.403, 0.006), resolution=(1600, 2560)))
    sleep(5)
    poco(text="AI分析说话人").wait_for_appearance(timeout=TIME_OUT)
    poco(text="AI分析说话人").click()
    poco("编辑").click()
    poco(text="取消").click()
    poco("返回").click()
    sleep(2)
#     poco("更多设置").wait_for_appearance(timeout=TIME_OUT)
#     poco("更多设置").click()
#     sleep(1)
#     poco(text="删除").click()
#     poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()





#分析前，【隐藏说话人】开时，返回结果后，自动关闭全部【隐藏说话人】开关;分析后，【隐藏说话人】开时，则隐藏说话人及分析结果

@pytest.mark.testcase
@allure.description("分析前，【隐藏说话人】开时，返回结果后，自动关闭全部【隐藏说话人】开关;分析后，【隐藏说话人】开时，则隐藏说话人及分析结果")
@allure.title("分析前，【隐藏说话人】开时，返回结果后，自动关闭全部【隐藏说话人】开关;分析后，【隐藏说话人】开时，则隐藏说话人及分析结果")
def test_Transcription_settings_effect_ai_analyze_speaker(default_group="默认笔记",default_note="测试录音"):
#     if is_login()==True:
#         login()
    poco(text="笔记").click()
    sleep(1)
    poco(text=default_group).click()
    sleep(1)
    #点击准备好的录音笔记
    poco(text=default_note).click()
    sleep(2)
    poco(text="录音原文").click()
    sleep(2)
    poco(text="转写设置").click()
    (poco("android:id/content")
     .child("android.view.View")
     .child("android.view.View")
     .offspring("android.widget.ScrollView")
     .child("android.view.View")[1]).click()
    touch((523,2208))
    sleep(2)
    poco(text="AI分析说话人").wait_for_appearance(timeout=TIME_OUT)
    poco(text="AI分析说话人").click()
    sleep(10)
    poco(text="转写设置").click()
    touch((523,2208))
    sleep(5)
    poco(text="AI分析说话人").wait_for_appearance(timeout=TIME_OUT)
    poco(text="AI分析说话人").click()
    sleep(2)
    poco(text="转写设置").click()
    (poco("android:id/content")
     .child("android.view.View")
     .child("android.view.View")
     .offspring("android.widget.ScrollView")
     .child("android.view.View")[1]).click()
    touch((523,2208))
    poco("返回").click()
    sleep(1)
#     poco("更多设置").wait_for_appearance(timeout=TIME_OUT)
#     poco("更多设置").click()
#     poco(text="删除").click()
#     poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()




if __name__=="__main__":
    test_offline_summary_after_the_meeting()
    test_online_summary_after_the_meeting()
    test_diff_internet_summary_after_the_meeting()
    test_ai_analyze_speaker()
    test_hide_ai_analyze_speaker()
    test_Transcription_settings_effect_ai_analyze_speaker()


