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

pytestmark = [allure.feature("A3ai助手模块用例"), allure.epic("办公本A3")]
    
    
#入口验证 应用 页面列表显示AI助手应用，下拉系统通知栏，点击AI助手，左侧菜单AI助手
@pytest.mark.testcase
@allure.description("入口验证 应用 页面列表显示AI助手应用，下拉系统通知栏，点击AI助手，左侧菜单AI助手")
@allure.title("入口验证 应用 页面列表显示AI助手应用，下拉系统通知栏，点击AI助手，左侧菜单AI助手")
def test_ai_helper_show():
    if is_login()==True:#未登录
        login()
    poco("应用").click()
    sleep(1)
    poco("AI助手图标").click()
    #打开全屏
    sleep(2)
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")[4]\
    .child("返回").click()
    sleep(1)
    #关闭ai助手
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")[4]\
    .child("返回").click()
    sleep(1)
    #下拉系统通知栏
    swipe((1036,0),(886,432))
    sleep(1)
    #关闭系统通知栏
    touch((675,2279))
    #点击左侧ai助手
    poco("AI助手").click()
    sleep(2)
    #关闭ai助手
    touch(Template(r"tpl1751348232173.png", record_pos=(0.463, -0.732), resolution=(1600, 2560)))
#     poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View")\
#     .child("android.view.View")[4]\
#     .child("返回").wait_for_appearance(timeout=TIME_OUT)
#     poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View")\
#     .child("android.view.View")[4]\
#     .child("返回").click()
    sleep(1)
    poco("首页").wait_for_appearance(timeout=TIME_OUT)
    poco("首页").click()
    
    
#音色默认是超自然女声思凝
@pytest.mark.testcase
@allure.description("音色默认是超自然女声思凝")
@allure.title("音色默认是超自然女声思凝")
def test_ai_voice_default():
    if is_login()==True:#未登录
        login()
    poco("应用").click()
    sleep(1)
    poco("AI助手图标").click()
    #点击设置
    sleep(2)
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")[3]\
    .child("返回").click()
    sleep(1)
    #点击语音播报音色设置
    poco(text="选择语音播报声音").click()
    sleep(2)
    #返回
    poco(desc="").click()
    sleep(1)
    poco(desc="").click()
    #关闭ai助手
    touch(Template(r"tpl1751348232173.png", record_pos=(0.463, -0.732), resolution=(1600, 2560)))
    sleep(1)
    poco("首页").click()


    
    


#TTS功能默认开启,TTS开关开启时，问答时，实时播报,语音播报中途关闭TTS
@pytest.mark.testcase
@allure.description("TTS功能默认开启,TTS开关开启时，问答时，实时播报,语音播报中途关闭TTS")
@allure.title("TTS功能默认开启,TTS开关开启时，问答时，实时播报,语音播报中途关闭TTS")
def test_ai_tts_default_open_ques_and_close():
    if is_login()==True:#未登录
        login()
    poco("应用").click()
    sleep(1)
    poco("AI助手图标").click()
    sleep(1)
    #问答
    if poco(text="按住说话").exists():
        #点击键盘
        poco("键盘输入").click()
    sleep(1)
    words = "李白生平"
    text(words,enter=False)
    sleep(1)
    poco("分享").click()
    sleep(2)
    #关闭语音播报
    touch(Template(r"tpl1751350677196.png", record_pos=(0.314, 0.215), resolution=(1600, 2560)))
    sleep(3)
    #开启语音播报
    touch(Template(r"tpl1751350715759.png", record_pos=(0.313, 0.214), resolution=(1600, 2560)))
    sleep(1)
    #关闭ai助手
    touch(Template(r"tpl1751348232173.png", record_pos=(0.463, -0.732), resolution=(1600, 2560)))
    sleep(1)
    poco("首页").click()

    



#搜索常用关键词
@pytest.mark.testcase
@allure.description("搜索常用关键词")
@allure.title("搜索常用关键词")
def test_ai_search_commen_words():
    if is_login()==True:#未登录
        login()
    poco("应用").click()
    sleep(1)
    poco("AI助手图标").click()
    sleep(1)
    if poco(text="按住说话").exists():
        #点击键盘
        poco("键盘输入").click()
    sleep(1)
    words = "李白生平"
    text(words,enter=False)
    sleep(1)
    poco("分享").click()
    sleep(5)
    #关闭ai助手
    touch(Template(r"tpl1751348232173.png", record_pos=(0.463, -0.732), resolution=(1600, 2560)))
    sleep(1)
    poco("首页").click()
    
    
    
    
#成功添加待办事项
@pytest.mark.testcase
@allure.description("成功添加待办事项")
@allure.title("成功添加待办事项")
def test_ai_add_agent():
    if is_login()==True:#未登录
        login()
    poco("应用").click()
    sleep(1)
    poco("AI助手图标").click()
    sleep(1)
    if poco(text="按住说话").exists():
        #点击键盘
        poco("键盘输入").click()
    sleep(1)
    words = "提醒我明天上午去开会"
    text(words,enter=False)
    sleep(1)
    poco("分享").click()
    #todo 点击时间
    #关闭，返回首页
    sleep(1)
    touch(Template(r"tpl1751348232173.png", record_pos=(0.463, -0.732), resolution=(1600, 2560)))
    sleep(1)
    poco("首页").click()
    
    
    
#AI笔记问答，获取有便签相关信息的话，可将信息自动添加到便签
@pytest.mark.testcase
@allure.description("AI笔记问答，获取有便签相关信息的话，可将信息自动添加到便签")
@allure.title("AI笔记问答，获取有便签相关信息的话，可将信息自动添加到便签")
def test_ai_mood_ques_add_note():
    if is_login()==True:#未登录
        login()
    poco("应用").click()
    sleep(1)
    poco("AI助手图标").click()
    sleep(1)
    if poco(text="按住说话").exists():
        #点击键盘
        poco("键盘输入").click()
    sleep(1)
    words = "帮我写个便签可以吗"
    text(words,enter=False)
    sleep(1)
    poco("分享").click()
    #todo 生成便签
    #关闭，返回首页
    sleep(1)
    touch(Template(r"tpl1751348232173.png", record_pos=(0.463, -0.732), resolution=(1600, 2560)))
    sleep(1)
    poco("首页").click()
    
    
    
#10s倒计时结束后，停止录音并发送
# def test_ai_voice_time_limit():
#     if is_login()==True:#未登录
#         login()
#     poco("应用").click()
#     sleep(1)
#     poco("AI助手图标").click()
#     sleep(1)
#     if poco(text="按住说话").exists():
#         poco(text="按住说话")
    
    
    
    
    
    
def test():
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")[2]\
    .child("返回").click()
    

    

    
    
    
    
if __name__=="__main__":
    test_ai_helper_show()
    test_ai_voice_default()
    test_ai_search_commen_words()
    test_ai_tts_default_open_ques_and_close()
    test_ai_add_agent()
    test_ai_mood_ques_add_note()
#     test()
    
    
    
    
    