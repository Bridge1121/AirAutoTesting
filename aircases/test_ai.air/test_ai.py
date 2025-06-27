# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"

import sys

import allure
import pytest
from airtest.core.api import *
from airtest.core.android.touch_methods.base_touch import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))

pytestmark = [allure.feature("ai对话模块用例"), allure.epic("办公本v2.4.0")]

#点击并拖动ai图标到文本
# def swipe_press_ai():
#     #拖动ai图标
#     start_point = (49,1732)
#     end_point = (410,990)
#     steps = 10  # 拖动的分段数
#     multitouch_event = [
#     DownEvent(start_point), SleepEvent(0.1)]
#     dev.touch_proxy.perform(multitouch_event)
#     sleep(1)
#     # 2. swipe
#     swipe_event = [DownEvent(start_point), SleepEvent(0.1)]
#     for i in range(1, steps + 1):
#         # 计算插值坐标，实现平滑拖动
#         x = start_point[0] + (end_point[0] - start_point[0]) * i // steps
#         y = start_point[1] + (end_point[1] - start_point[1]) * i // steps
#         swipe_event.append(MoveEvent((x, y)))
#         swipe_event.append(SleepEvent(0.05))  # 每步间隔，可微调
#     swipe_event.append(UpEvent())
#     dev.touch_proxy.perform(swipe_event)




    
    
# 用手点击AI按钮,AI会话窗页面显示
@pytest.mark.testcase
@allure.description("用手点击AI按钮,AI会话窗页面显示")
@allure.title("用手点击AI按钮,AI会话窗页面显示")
def test_ai_open():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    #点击ai按钮
    touch((46,1729))
    sleep(1)
    #关闭会话框
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[2].offspring("返回")[0].click()
    poco("返回").click()
    #删除新建的笔记
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)
    poco("首页").click()

    
# 用笔按住AI图标拖至手写处，然后松手,点击复制按钮复制答案
@pytest.mark.testcase
@allure.title("用笔按住AI图标拖至手写处，然后松手,点击复制按钮复制答案")
@allure.description("用笔按住AI图标拖至手写处，然后松手,点击复制按钮复制答案")
def test_ai_answer_copy():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    text("你是谁", enter=False)
    sleep(1)
    touch((581,1217))
    sleep(1)
    #拖动ai图标
    swipe_press_ai()
    sleep(12)
    #点击复制
    touch(Template(r"tpl1749435894639.png", record_pos=(-0.337, -0.143), resolution=(1200, 1920)))
#     copy_btn = poco("android.widget.LinearLayout")\
#     .offspring("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View").child("android.view.View")\
#     .offspring("android.widget.ScrollView")[2]\
#     .child("复制")[1]
#     copy_btn.wait_for_appearance(timeout=5)
#     copy_btn.click()
    #点击关闭
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[2].offspring("返回")[0].click()
    touch((781,1017),duration=1)
    poco("com.aispeech.tablet:id/tv_selection_paste").click()
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

    
#ai回答点击摘录到手写区，并进行编辑
@pytest.mark.testcase
@allure.description("ai回答点击摘录到手写区，并进行编辑")
@allure.title("ai回答点击摘录到手写区，并进行编辑")
def test_ai_answer_excerpt_to_handwriting_area_edit():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    text("你是谁", enter=False)
    sleep(1)
    touch((581,1217))
    sleep(1)
    #拖动ai图标
    swipe_press_ai()
    sleep(10)
    #点击摘录到手写区
    touch(Template(r"tpl1749436239092.png", record_pos=(-0.266, -0.142), resolution=(1200, 1920)))
    #点击关闭
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[2].offspring("返回")[0].click()
    #点击编辑
    poco("com.aispeech.tablet:id/tv_selection_edit").click()
    sleep(1)
    text("编辑编辑",enter=False)
    sleep(1)
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
#点击赞图标按钮，弹出反馈信息弹窗,在反馈弹窗中勾选选项、文本框输入内容
@pytest.mark.testcase
@allure.description("点击赞图标按钮，弹出反馈信息弹窗,在反馈弹窗中勾选选项、文本框输入内容")
@allure.title("点击赞图标按钮，弹出反馈信息弹窗,在反馈弹窗中勾选选项、文本框输入内容")
def test_ai_answer_support():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    text("你是谁", enter=False)
    sleep(1)
    touch((581,1217))
    sleep(1)
    #拖动ai图标
    swipe_press_ai()
    sleep(10)
    #点赞
    touch(Template(r"tpl1749436583382.png", record_pos=(-0.194, -0.138), resolution=(1200, 1920)))
    poco(text="回答准确且专业").click()
    sleep(1)
    poco(text="您为什么喜欢这条回答？").click()
    text("言简意赅", enter=False)
    poco(text="提交").click()
    #点击关闭
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[2].offspring("返回")[0].click()
    sleep(1)
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()



#点击踩图标按钮，弹出反馈信息弹窗,在反馈弹窗中勾选选项、文本框输入内容
@pytest.mark.testcase
@allure.description("点击踩图标按钮，弹出反馈信息弹窗,在反馈弹窗中勾选选项、文本框输入内容")
@allure.title("点击踩图标按钮，弹出反馈信息弹窗,在反馈弹窗中勾选选项、文本框输入内容")
def test_ai_answer_oppose():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    text("你是谁", enter=False)
    sleep(1)
    touch((581,1217))
    sleep(1)
    #拖动ai图标
    swipe_press_ai()
    sleep(10)
    touch(Template(r"tpl1749437209644.png", record_pos=(-0.122, -0.145), resolution=(1200, 1920)))
    poco(text="存在不安全或违法信息").click()
    poco(text="您认为更优答案应该是什么？").click()
    text("不知道", enter=False)
    poco(text="提交").click()
    #点击关闭
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[2].offspring("返回")[0].click()
    sleep(1)
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()


#点击重新提取按钮,点击举报按钮，弹出举报弹窗,在举报弹窗中勾选选项、文本框输入内容
@pytest.mark.testcase
@allure.description("点击重新提取按钮,点击举报按钮，弹出举报弹窗,在举报弹窗中勾选选项、文本框输入内容")
@allure.title("点击重新提取按钮,点击举报按钮，弹出举报弹窗,在举报弹窗中勾选选项、文本框输入内容")
def test_ai_answer_rextract_and_report():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    text("你是谁", enter=False)
    sleep(1)
    touch((581,1217))
    sleep(1)
    #拖动ai图标
    swipe_press_ai()
    sleep(10)
    #点击重新提取
    touch(Template(r"tpl1749437777006.png", record_pos=(-0.053, -0.141), resolution=(1200, 1920)))
    sleep(10)
    #点击举报
    touch(Template(r"tpl1749437868167.png", record_pos=(0.018, -0.141), resolution=(1200, 1920)))
    poco(text="有害/不安全").click()
    poco(text="我们想知道你举报的原因，你可以描述你遇到的问题").click()
    text("答非所问", enter=False)
    poco(text="提交").click()
    #点击关闭
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[2].offspring("返回")[0].click()
    sleep(1)
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
#ai回答输入框包括键盘输入，语音输入,点击输入框中语音图标热区，切换到语音输入
@pytest.mark.testcase
@allure.title("ai回答输入框包括键盘输入，语音输入,点击输入框中语音图标热区，切换到语音输入")
@allure.description("ai回答输入框包括键盘输入，语音输入,点击输入框中语音图标热区，切换到语音输入")
def test_ai_answer_input_ui():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    text("你是谁", enter=False)
    sleep(1)
    touch((581,1217))
    sleep(1)
    #拖动ai图标
    swipe_press_ai()
    sleep(10)
    #点击语音输入
    pos = poco(text="按住说话").get_position()
    touch(pos,duration=2)
    #点击关闭
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[2].offspring("返回")[0].click()
    sleep(1)
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

    
    
    
    
if __name__=="__main__":
    test_ai_open()
    test_ai_answer_copy()
    test_ai_answer_excerpt_to_handwriting_area_edit()
    test_ai_answer_oppose()
    test_ai_answer_rextract_and_report()
    test_ai_answer_input_ui()
    
    
    