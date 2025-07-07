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

pytestmark = [allure.feature("笔记录音模块用例"), allure.epic("办公本v2.4.0")]


def test():
    poco("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View").child("android.view.View") \
        .child("android.view.View")[10].child("android.view.View") \
        .child("android.view.View")[0] \
        .child("android.widget.TextView")[0].click()



# 录音时返回后，再进入该笔记
@pytest.mark.testcase
@allure.description("录音时返回后，再进入该笔记")
@allure.title("录音时返回后，再进入该笔记")
# def test_note_recording_back():
#     if is_login() == True:
#         login()
#     # 点击笔记
#     poco("笔记").click()
#     sleep(1)
#     # 新建笔记
#     poco(text="新建笔记").click()
#     # 输入笔记内容
#     poco("更多设置").click()
#     poco(text="插入文字").click()
#     sleep(2)
#     touch((581, 997))
#     sleep(2)
#     note_name = "测试录音返回"
#     text(note_name, enter=False)
#     sleep(1)
#     # 点击录音
#     poco("android.widget.LinearLayout") \
#         .offspring("androidx.compose.ui.platform.ComposeView") \
#         .child("android.view.View").child("android.view.View") \
#         .child("android.view.View")[6].child("手写笔").click()
#     sleep(2)
#     # 返回
#     poco("返回").click()
#
#     sleep(2)
#     # 点击新建的笔记
#     poco(text=note_name).click()
#     #     poco("androidx.compose.ui.platform.ComposeView")\
#     #     .child("android.view.View").child("android.view.View")\
#     #     .child("android.view.View")[10].child("android.view.View")\
#     #     .child("android.view.View")[0]\
#     #     .child("android.widget.TextView")[0].click()
#     # 验证是否弹窗
#     #     assert poco(text="是否继续录音？").exists()
#     #     sleep(1)
#     #     #点击确定，继续录音
#     poco(text="继续录音").click()
#     sleep(1)
#     # 点击暂停录音
#     poco(text="暂停").click()
#     sleep(1)
#     #     点击继续录音
#     poco(text="暂停").click()
#     # 返回
#     poco("返回").click()
#     # 删除新建的笔记
#     poco("更多设置").click()
#     poco(text="删除").click()
#     poco(text="确认").click()
#     sleep(1)
#     poco("首页").click()



# 无网络时开启录音
@pytest.mark.testcase
@allure.description("无网络时开启录音")
@allure.title("无网络时开启录音")
def test_note_recording_no_internet():
    if is_login() == True:
        login()
    # 点击笔记
    poco("笔记").click()
    sleep(1)
    # 断网
    # 下拉菜单
    swipe((1036, 0), (886, 432))
    sleep(1)
    poco("com.aispeech.ccui.systemui:id/cellGrid") \
        .child("android.widget.LinearLayout")[0] \
        .child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    touch((867, 1450))
    # 新建笔记
    poco(text="新建笔记").click()
    # 点击录音
    poco("android.widget.LinearLayout") \
        .offspring("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View").child("android.view.View") \
        .child("android.view.View")[6].child("手写笔").click()
    sleep(1)
    assert poco(text="*当前网络不可用，请检查您的网络").exists()
    # 返回
    poco("返回").click()
    # 联网
    # 恢复网络
    swipe((1036, 0), (886, 432))
    poco("com.aispeech.ccui.systemui:id/cellGrid") \
        .child("android.widget.LinearLayout")[0] \
        .child("com.aispeech.ccui.systemui:id/iv_cell_icon") \
        .long_click(duration=2)
    sleep(4)
    poco("com.zlt.zltsettings:id/sw_airplane").click()
    poco(text="已连接").wait_for_appearance(timeout=TIME_OUT)
    poco("android.widget.FrameLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("android:id/content") \
        .offspring("com.zlt.zltsettings:id/ll_back") \
        .child("android.widget.ImageView").click()
    sleep(1)
    # 删除新建的笔记
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)
    poco("首页").click()

    
#录音原文中查找功能  
@pytest.mark.testcase
@allure.description("录音原文中查找功能")
@allure.title("录音原文中查找功能")
def test_note_original_recording_find():
    if is_login() == True:
        login()
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco(text="录音原文").click()
    sleep(10)
    if poco(textMatches=".*智能.*").exists():
        poco(text="查找/替换").click()
        #录音原文中存在“智能”关键词
        text("智能",enter=False)
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[12].child("android.widget.Button")[1].click()
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[12].child("android.widget.Button")[1].click()
    poco(text="结束").click()
    poco("更多设置").click()
    poco(text="删除笔记").click()
    poco(text="确认").click()
    poco(text="首页").click()




    
    
#录音原文查找后进行替换，结果为第一个，替换时，选择【替换当前】;查找替换时，选择【替换全部】
@pytest.mark.testcase
@allure.description("录音原文查找后进行替换，结果为第一个，替换时，选择【替换当前】;查找替换时，选择【替换全部】")
@allure.title("录音原文查找后进行替换，结果为第一个，替换时，选择【替换当前】;查找替换时，选择【替换全部】")
def test_note_original_recording_replace():
    if is_login() == True:
        login()
    #已有含录音内容“智能”的笔记
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child(
        "android.view.View").child("android.view.View").child("android.view.View")[6].child(
        "android.widget.Button").click()
    poco(text="录音原文").click()
    sleep(10)
    poco(text="结束").click()
    sleep(5)
    if poco(textMatches=".*智能.*").exists():
        poco(text="录音原文").click()
        poco(text="查找/替换").click()
        poco(text="输入您要查找的内容").click()
        text("智能",enter=False)
        poco(text="替换").click()
        poco(text="输入您要替换的内容").click()
        text("测试",enter=False)
        poco(text="替换当前").click()
        sleep(1)
        poco(text="替换全部").click()
        #还原
        poco(text="录音原文").click()
        poco(text="查找/替换").click()
        poco(text="输入您要查找的内容").click()
        text("测试",enter=False)
        poco(text="替换").click()
        poco(text="输入您要替换的内容").click()
        text("智能",enter=False)
        poco(text="替换全部").click()
    poco("更多设置").click()
    poco(text="删除笔记").click()
    poco(text="确认").click()
    poco(text="首页").click()
    
    
    
    
#录音窗口AI笔记tab页的替换按钮变成【查找/替换】,点击【查找】功能时，自动进入输入状态，调起输入法键盘,输入框输入存在的关键词，页面滚动到第一个搜索结果，高亮显示,连续点击右侧的 > 下一个,查找后进行替换    
@pytest.mark.testcase
@allure.description("录音窗口AI笔记tab页【查找/替换】功能")
@allure.title("录音窗口AI笔记tab页【查找/替换】功能")
def test_note_ai_note_replace():
    if is_login() == True:
        login()
    #已有含录音内容“智能”的笔记
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child(
        "android.view.View").child("android.view.View").child("android.view.View")[6].child(
        "android.widget.Button").click()
    poco(text="录音原文").click()
    sleep(10)
    poco(text="结束").click()
    sleep(5)
    if poco(textMatches=".*智能.*").exists():
        poco(text="AI笔记").click()
        poco(text="查找/替换").click()
        poco(text="智能").click()
        poco(text="输入您要查找的内容").click()
        text("智能",enter=False)
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[13].child("android.widget.Button")[1].click()
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").child("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[13].child("android.widget.Button")[1].click()
        poco(text="替换").click()
        poco(text="输入您要替换的内容").click()
        text("测试",enter=False)
        poco(text="替换当前").click()
        sleep(1)
        poco(text="替换全部").click()
        #还原
        poco(text="AI笔记").click()
        poco(text="查找/替换").click()
        poco(text="输入您要查找的内容").click()
        text("测试",enter=False)
        poco(text="替换").click()
        poco(text="输入您要替换的内容").click()
        text("智能",enter=False)
        poco(text="替换全部").click()
    poco("更多设置").click()
    poco(text="删除笔记").click()
    poco(text="确认").click()
    poco(text="首页").click()


    
    
#笔记设置中新增【在笔记列表展示识别后的手写文本】开关，关闭【在笔记列表展示识别后的手写文本】，在笔记列表不显示手写识别文本
@pytest.mark.testcase
@allure.description("笔记设置中新增【在笔记列表展示识别后的手写文本】功能")
@allure.title("笔记设置中新增【在笔记列表展示识别后的手写文本】功能")
def test_note_display_handwritten_text():
    if is_login() == True:
        login()
    poco(text="笔记").click()
    poco("show catalogs").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[3].child("android.view.View").click()
    poco(text="笔记设置").click()
    poco("show catalogs").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[3].child("android.view.View").click()
    poco(text="笔记设置").click()
    poco(text="首页").click()




#会后支持筛选说话人
@pytest.mark.testcase
@allure.description("会后支持筛选说话人")
@allure.title("会后支持筛选说话人")
def test_note_recording_filter_speakers():
    if is_login() == True:
        login()
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco(text="录音原文").click()
    sleep(10)
    poco("stop icon").click()
    sleep(10)
    #目前测试结果：录音过程中转写无法筛选说话人
#     poco(text="继续录音").click()
#     poco(text="录音原文").click()
#     poco(text="转写设置").click()
#     poco(text="筛选说话人").click()
#     poco(text="说话人1").click()
#     poco(text="结束").click()
    #录音结束后筛选说话人
    poco(text="录音原文").click()
    poco(text="转写设置").click()
    poco(text="筛选说话人").click()
    if poco(textMatches=".*说话人1.*").exists():
        poco(text="说话人1").click()
        touch((500,1700))
        touch((500,1700))
        #录音结束后，依次取消筛选说话人
        poco(text="转写设置").click()
        poco(text="筛选说话人").click()
        poco("android:id/content").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.widget.CheckBox").click()
        results = find_all(Template(r"tpl1750821282208.png", record_pos=(0.257, 0.136), resolution=(1200, 1920)))
        count = len(results)-1
        for i in range(count-1):
            #string_value=str(i+1)
            poco(text=f"说话人{i+1}").click()
            sleep(1)
    else:
        touch((500, 1700))
    touch((500,1700))
    touch((500,1700))
    sleep(1)
    poco("更多设置").click()
    poco(text="删除笔记").click()
    poco(text="确认").click()
    poco(text="首页").click()



    

#隐藏说话人与筛选说话人冲突
@pytest.mark.testcase
@allure.description("隐藏说话人与筛选说话人冲突")
@allure.title("隐藏说话人与筛选说话人冲突")
def test_note_recording_speakers():
    if is_login() == True:
        login()
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco(text="录音原文").click()
    sleep(10)
    poco("stop icon").click()
    sleep(10)
    poco(text="转写设置").click()
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[1].click()
    sleep(1)
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[1].click()
    poco(text="筛选说话人").click()
    if poco(textMatches=".*说话人1.*").exists():
        results = find_all(Template(r"tpl1750821282208.png", record_pos=(0.257, 0.136), resolution=(1200, 1920)))
        count = len(results)-1
        for i in range(count-1):
            #string_value=str(i+1)
            poco(text=f"说话人{i+1}").click()
        touch((500,1700))
        poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[1].click()
        touch((500,1700))
    else:
        touch((500, 1700))
    poco("更多设置").click()
    poco(text="删除笔记").click()
    poco(text="确认").click()
    poco(text="首页").click()



#打开/关闭口语顺滑开关
@pytest.mark.testcase
@allure.description("打开/关闭口语顺滑开关")
@allure.title("打开/关闭口语顺滑开关")
def test_note_recording_smooth_speaking():
    if is_login() == True:
        login()
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco(text="录音原文").click()
    poco(text="转写设置").click()
    touch((500,1700))
    #口语顺滑开关默认打开
    poco(text="结束").click()
    poco(text="继续录音").click()
    #打开口语顺滑后，再继续录音
    poco(text="录音原文").click()
    poco(text="转写设置").click()
    #录音过程中关闭【口语顺滑】之后，结束后继续录音时，默认是关闭状态
    touch(Template(r"tpl1750831015961.png", record_pos=(-0.067, -0.172), resolution=(1200, 1920)))
    touch((500,1700))
    poco(text="结束").click()
    poco(text="继续录音").click()
    poco(text="录音原文").click()
    poco(text="转写设置").click()
    #录音过程中打开【口语顺滑】之后，结束后新建一条笔记开启录音，默认是打开状态
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[0].click()
    touch((500,1700))
    poco(text="结束").click()
    poco("返回").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco(text="录音原文").click()
    poco(text="转写设置").click()
    #录音过程中关闭【口语顺滑】之后，结束后新建一条笔记开启录音，默认是关闭状态
    touch(Template(r"tpl1750831015961.png", record_pos=(-0.067, -0.172), resolution=(1200, 1920)))
    touch((500,1700))
    poco(text="结束").click()
    poco("返回").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco(text="录音原文").click()
    poco(text="转写设置").click()
    touch((500,1700))
    poco("返回").click()
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="首页").click()



#AI笔记——导出思维导图
@pytest.mark.testcase
@allure.description("AI笔记——导出思维导图")
@allure.title("AI笔记——导出思维导图")
def test_note_recording_ai_note_mind_mapping():
    if is_login() == True:
        login()
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    sleep(10)
    poco(text="结束").click()
    sleep(10)
    poco(text="AI笔记").click()
    if poco(textMatches=".*思维导图.*").exists():
        poco(text="思维导图").click()
        poco("分享").click()
        #点击扫码下载，弹出分享二维码，扫码后下载文件
        poco("扫码下载").click()
        poco("close dialog").click()
        #点击保存到本地，导出完成弹窗选项“立即打开”验证
        poco("分享").click()
        poco("保存到本地").click()
        poco(text="立即打开").click()
        #更多分享方式验证
        poco(text="笔记").click()
        touch((600,400))
        poco(text="AI笔记").click()
        poco(text="思维导图").click()
        poco("分享").click()
        poco("更多").click()
        poco(text="图片转PDF").click()
        #已确认始终打开WPS情况下
        poco("cn.wps.moffice_eng:id/pdf_pic_preview_save_btn").click()
        poco(text="我的文档").click()
        poco("cn.wps.moffice_eng:id/btn_save").click()
        poco("cn.wps.moffice_eng:id/pdf_main_toolbar_backBtn").click()
        sleep(1)
        swipe((0,1100),(400,1100))
        #还原
        poco(text="文件").click()
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[0].child("more icon").click()
        poco(text="删除").click()
        poco(text="确认").click()
        poco(text="图片").click()
        poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.view.View")[0].child("more icon").click()
        poco(text="删除").click()
        poco(text="确认").click()
        poco("返回").click()
        poco(text="笔记").click()
    else:
        poco("返回").click()
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="首页").click()
    
    
    

#会后总结思维导图到出入口验证；扫码下载、保存到本地、导出方式-更多三种导出方式验证
@pytest.mark.testcase
@allure.description("会后总结思维导图到出入口验证；扫码下载、保存到本地、导出方式-更多三种导出方式验证")
@allure.title("会后总结思维导图到出入口验证；扫码下载、保存到本地、导出方式-更多三种导出方式验证")
def test_note_recording_meeting_summary_mind_mapping():
    if is_login() == True:
        login()
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    sleep(10)
    poco(text="结束").click()
    poco(text="会后总结").click()
    if poco(textMatches=".*当前没有内容可生成总结.*").exists():
        poco("返回").click()
    else:    
        sleep(10)
        poco("思维导图").click()
        poco("分享").click()
        #扫码下载
        poco("扫码下载").click()
        poco("close dialog").click()
        #保存到本地
        poco("分享").click()
        poco("保存到本地").click()
        poco(text="立即打开").click()
        #更多分享方式验证
        poco(text="笔记").click()
        touch((600,400))
        poco(text="会后总结").click()
        poco("思维导图").click()
        poco("分享").click()
        poco("更多").click()
        poco(text="图片转PDF").click()

        #已确认始终打开WPS情况下
        poco("cn.wps.moffice_eng:id/pdf_pic_preview_save_btn").click()
        poco(text="我的文档").click()
        poco("cn.wps.moffice_eng:id/btn_save").click()
        poco("cn.wps.moffice_eng:id/pdf_main_toolbar_backBtn").click()
        sleep(1)
        swipe((0,1100),(400,1100))
        #还原
        poco(text="文件").click()
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[0].child("more icon").click()
        poco(text="删除").click()
        poco(text="确认").click()
        poco(text="图片").click()
        poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.view.View")[0].child("more icon").click()
        poco(text="删除").click()
        poco(text="确认").click()
        poco("返回").click()
        poco(text="笔记").click()
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="首页").click()




#AI笔记支持重新生成
@pytest.mark.testcase
@allure.description("AI笔记支持重新生成")
@allure.title("AI笔记支持重新生成")
def test_note_recording_ai_note_rebuild():
    if is_login()==True:
        login()
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    sleep(10)
    poco(text="结束").click()
    sleep(10)
    poco(text="AI笔记").click()
    if not poco(textMatches=".*思维导图.*").exists():
        poco(text="重新生成").click()
        poco(text="确定").click()
        poco(text="我知道了").click()
    else:
        poco(text="重新生成").click()
        poco(text="确定").click()
        sleep(10)
    #重新生成过程中，断开网络
    if not poco(textMatches=".*思维导图.*").exists():
        poco(text="重新生成").click()
        poco(text="确定").click()
        poco(text="我知道了").click()
    else:
        poco(text="重新生成").click()
        poco(text="确定").click()
        swipe((1036,0),(886,432))
        poco("com.aispeech.ccui.systemui:id/cellGrid").child("android.widget.LinearLayout")[0].child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
        swipe((900,1269),(900,1200))
        sleep(5)
        swipe((1036,0),(886,432))
        poco("com.aispeech.ccui.systemui:id/cellGrid").child("android.widget.LinearLayout")[0].child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
        swipe((900,1269),(900,1200))
    #重新生成过程中，点击继续录音
    if not poco(textMatches=".*思维导图.*").exists():
        poco(text="重新生成").click()
        poco(text="确定").click()
        poco(text="我知道了").click()
    else:
        poco(text="重新生成").click()
        poco(text="确定").click()
        poco(text="继续录音").click()
        poco(text="结束").click()
    poco("更多设置").click()
    poco(text="删除笔记").click()
    poco(text="确认").click()
    poco(text="首页").click()


    


#未登录时录音，结束录音重新登录后，显示【重新生成】按钮    
@pytest.mark.testcase
@allure.description("未登录时录音，结束录音重新登录后，显示【重新生成】按钮")
@allure.title("未登录时录音，结束录音重新登录后，显示【重新生成】按钮")
def test_not_logged_in_note_recording_ai_note_rebuild():
    #退出登录
    if is_login()==False:
        sign_out()
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco(text="取消").click()
    sleep(10)
    poco(text="结束").click()
    poco("返回").click()
    #重新登录
    login()
    poco(text="笔记").click()
    touch((600,400))
    poco(text="AI笔记").click()
    if not poco(textMatches=".*思维导图.*").exists():
        poco(text="重新生成").click()
        poco(text="确定").click()
        poco(text="我知道了").click()
    else:
        poco(text="重新生成").click()
        poco(text="确定").click()
        sleep(10)
    poco("更多设置").click()
    poco(text="删除笔记").click()
    poco(text="确认").click()
    poco(text="首页").click()




#无网络时，开启录音，录音结束后，显示【重新生成】按钮
@pytest.mark.testcase
@allure.description("无网络时，开启录音，录音结束后，显示【重新生成】按钮")
@allure.title("无网络时，开启录音，录音结束后，显示【重新生成】按钮")
def test_no_internet_note_recording_ai_note_rebuild():
    if is_login() == True:
        login()
    #断网
    swipe((1036,0),(886,432))
    poco("com.aispeech.ccui.systemui:id/cellGrid").child("android.widget.LinearLayout")[0].child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    swipe((900,1269),(900,1200))
    poco(text="笔记").click()
    poco(text="新建笔记").click()
    poco("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco(text="录音原文").click()
    sleep(10)
    poco(text="结束").click()
    #重新联网
    swipe((1036,0),(886,432))
    poco("com.aispeech.ccui.systemui:id/cellGrid").child("android.widget.LinearLayout")[0].child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    swipe((900,1269),(900,1200))
    sleep(10)
    poco(text="AI笔记").click()
    if not poco(textMatches=".*思维导图.*").exists():
        poco(text="重新生成").click()
        poco(text="确定").click()
        poco(text="我知道了").click()
    else:
        poco(text="重新生成").click()
        poco(text="确定").click()
        sleep(10)
    poco("更多设置").click()
    poco(text="删除笔记").click()
    poco(text="确认").click()
    clear_recycle_bin()
    poco(text="首页").click()


    



    


    





if __name__=="__main__":
    #test_note_recording_back()
    test_note_recording_no_internet()
    test_note_original_recording_find()
    test_note_original_recording_replace()
    test_note_ai_note_replace()
    test_note_recording_ai_note_mind_mapping()
    test_note_recording_smooth_speaking()
    test_note_recording_speakers()
    test_note_recording_filter_speakers()
    test_note_display_handwritten_text()
    test_note_recording_meeting_summary_mind_mapping()
    test_note_recording_ai_note_rebuild()
    test_not_logged_in_note_recording_ai_note_rebuild()
    test_no_internet_note_recording_ai_note_rebuild()
    clear_recycle_bin()
    

    
    
    
    
    



