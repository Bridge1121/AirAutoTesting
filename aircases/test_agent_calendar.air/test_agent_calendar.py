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

pytestmark = [allure.feature("代办日历模块用例"), allure.epic("办公本v2.4.0")]
            
            
            
            
    
#查看待办周日历视图，默认为本周当天的年月日星期农历
@pytest.mark.testcase
@allure.description("查看待办周日历视图，默认为本周当天的年月日星期农历")
@allure.title("查看待办周日历视图，默认为本周当天的年月日星期农历")
def test_view_weekly_calendar_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    poco("首页").click()
    
    
    
#代办日历视图为周时，点击左右切换键切换日期
@pytest.mark.testcase
@allure.description("代办日历视图为周时，点击左右切换键切换日期")
@allure.title("代办日历视图为周时，点击左右切换键切换日期")
def test_switch_weekly_calendar_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[7].child("android.widget.Button").click()
    poco("首页").click()
    
    
    
#代办日历视图为周时，左右滑动切换日期
@pytest.mark.testcase
@allure.description("代办日历视图为周时，左右滑动切换日期")
@allure.title("代办日历视图为周时，左右滑动切换日期")
def test_slide_weekly_calendar_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[0].swipe([0.4301, 0.0194])
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[6].swipe([-0.5285, -0.0097])
    poco("首页").click()
    
    
    
#代办日历视图为周时，连续多次点击左切换键切换日期
@pytest.mark.testcase
@allure.description("代办日历视图为周时，连续多次点击左切换键切换日期")
@allure.title("代办日历视图为周时，连续多次点击左切换键切换日期")
def test_left_switch_weekly_calendar_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    for i in range(5):
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.widget.Button").click()
    poco("首页").click()
    
    
    
#代办日历视图为周时，连续多次点击右切换键切换日期
@pytest.mark.testcase
@allure.description("代办日历视图为周时，连续多次点击右切换键切换日期")
@allure.title("代办日历视图为周时，连续多次点击右切换键切换日期")
def test_right_switch_weekly_calendar_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    for i in range(5):
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[7].child("Next").click()
    poco("首页").click()
    
    
    
#代办日历视图为周时，连续多次左滑切换日期
@pytest.mark.testcase
@allure.description("代办日历视图为周时，连续多次左滑切换日期")
@allure.title("代办日历视图为周时，连续多次左滑切换日期")
def test_left_slide_weekly_calendar_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    for i in range(5):
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[6].swipe([-0.6736, 0.013])
    poco("首页").click()
    
    
    
#代办日历视图为周时，连续多次右滑切换日期
@pytest.mark.testcase
@allure.description("代办日历视图为周时，连续多次右滑切换日期")
@allure.title("代办日历视图为周时，连续多次右滑切换日期")
def test_right_slide_weekly_calendar_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    for i in range(5):
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[0].swipe([0.7461, 0.0065])
    poco("首页").click()

    
    
    
#代办日历视图切换为月，默认显示该月1号
@pytest.mark.testcase
@allure.description("代办日历视图切换为月，默认显示该月1号")
@allure.title("代办日历视图切换为月，默认显示该月1号")
def test_view_monthly_calendar_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    poco(text="月").click()
    poco("首页").click()

    
    
#点击年月处左右切换键切换日期
@pytest.mark.testcase
@allure.description("点击年月处左右切换键切换日期")
@allure.title("点击年月处左右切换键切换日期")
def test_switch_monthly_calendar_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    poco(text="月").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[4].child("android.widget.Button").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[5].child("android.widget.Button").click()
    poco("首页").click()



#日历视图由周切换为月时保留周切换前的日期
@pytest.mark.testcase
@allure.description("日历视图由周切换为月时保留周切换前的日期")
@allure.title("日历视图由周切换为月时保留周切换前的日期")
def test_switch_weeekly_to_monthly_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[2].click()
    poco(text="月").click()
    poco("首页").click()



#日历视图由周切换为月再切回周时保留显示为月时的日期
@pytest.mark.testcase
@allure.description("日历视图由周切换为月再切回周时保留显示为月时的日期")
@allure.title("日历视图由周切换为月再切回周时保留显示为月时的日期")
def test_switch_weeekly_to_monthly_to_weekly_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[2].click()
    poco(text="月").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[5].click()
    poco(text="周").click()
    poco("首页").click()
    
    
    
#日历视图由月切换为周时保留月切换前的日期
@pytest.mark.testcase
@allure.description("日历视图由月切换为周时保留月切换前的日期")
@allure.title("日历视图由月切换为周时保留月切换前的日期")
def test_switch_monthly_to_weekly_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    poco(text="月").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[2].click()
    poco(text="周").click()
    poco("首页").click()


    
#日历视图由月切换为周再切回月时保留显示为月时的日期
@pytest.mark.testcase
@allure.description("日历视图由月切换为周再切回月时保留显示为月时的日期")
@allure.title("日历视图由月切换为周再切回月时保留显示为月时的日期")
def test_switch_monthly_to_weekly_to_monthly_agent():
    poco("待办").click()
    poco(text="日历视图").click()
    poco(text="月").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[2].click()
    poco(text="周").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[5].click()
    poco(text="月").click()
    poco("首页").click()



#为周日历时有待办内容的日期下显示绿色小点
@pytest.mark.testcase
@allure.description("为周日历时有待办内容的日期下显示绿色小点")
@allure.title("为周日历时有待办内容的日期下显示绿色小点")
def test_weekly_agent_text():
    #创建代办
    poco("待办").click()
    sleep(2)
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text("我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办",enter=False)
    #修改日期
    choose_n_days_date(1)
    sleep(1)
    poco(text="确认").click()
    sleep(1)
    #查看周日历有代办内容的日期
    poco(text="列表视图").click()
    poco(text="日历视图").click()
    poco(text="周").click()
    touch(Template(r"tpl1750300034472.png", record_pos=(0.421, -0.215), resolution=(1200, 1920)))
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[11].swipe([0.052, -0.3226])
    sleep(1)
    poco(desc="").click()
    # touch(Template(r"tpl1750239890001.png", record_pos=(0.449, 0.134), resolution=(1200, 1920)))
    if poco(text="删除").exists():
        poco(text="删除").click()
        poco(text="确认").click()
    poco("首页").click()
    


#为月日历时有待办内容的日期下显示绿色小点
@pytest.mark.testcase
@allure.description("为月日历时有待办内容的日期下显示绿色小点")
@allure.title("为月日历时有待办内容的日期下显示绿色小点")
def test_monthly_agent_text():
    #创建代办
    poco("待办").click()
    sleep(2)
    #for i in range(2):
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text("我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办",enter=False)
    #修改日期
    choose_n_days_date(1)
    poco(text="确认").click()
    sleep(1)
    #查看周日历有代办内容的日期
    poco(text="列表视图").click()
    poco(text="日历视图").click()
    poco(text="月").click()
    touch(Template(r"tpl1750300034472.png", record_pos=(0.421, -0.215), resolution=(1200, 1920)))
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[11].swipe([0.052, -0.3226])
    sleep(1)
    poco(desc="").click()
    if poco(text="删除").exists():
        poco(text="删除").click()
        poco(text="确认").click()
    poco("首页").click()
    
    
    
#当天无待办内容时日历视图待办页面显示为空
@pytest.mark.testcase
@allure.description("当天无待办内容时日历视图待办页面显示为空")
@allure.title("当天无待办内容时日历视图待办页面显示为空")
def test_today_weekly_agent_no_text():
    poco("待办").click()
    poco(text="日历视图").click()
    sleep(1)
    poco(text="周").click()
    sleep(1)
    touch(Template(r"tpl1750296442447.png", record_pos=(0.165, -0.28), resolution=(1200, 1920)))
    sleep(2)
    if poco("首页").exists():
        poco("首页").click()
    


    
#当天有多条待办内容时,日历视图待办页面显示为当天的代办项和已完成且后面有数字显示
@pytest.mark.testcase
@allure.description("当天有多条待办内容时,日历视图待办页面显示为当天的代办项和已完成且后面有数字显示")
@allure.title("当天有多条待办内容时,日历视图待办页面显示为当天的代办项和已完成且后面有数字显示")
def test_today_weekly_agent_many_text():
    # if is_login()==True:
    #     login()
    #创建代办
    if poco("待办").exists():
        poco("待办").click()
        for i in range(3):
            sleep(2)
            poco(text="请在下方书写待办或点击此处新建待办").click()
            text("这里有一条代办",enter=False)
            poco(text="确认").click()
        #查看当天代办
        poco(text="日历视图").click()
        poco(text="周").click()
        sleep(2)
        touch(Template(r"tpl1750296442447.png", record_pos=(0.165, -0.28), resolution=(1200, 1920)))
        sleep(2)
        poco("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View").child("android.view.View")\
        .child("android.view.View")[11].child("android.view.View")[0].click()
        sleep(1)
        for i in range(3):
            poco(desc="").click()
            # touch(Template(r"tpl1750239890001.png", record_pos=(0.449, 0.134), resolution=(1200, 1920)))
            if poco(text="删除").exists():
                poco(text="删除").click()
                poco(text="确认").click()
        sleep(1)
        poco("首页").click()
    
    
    
#无待办内容时,日历视图待办页面显示为空
@pytest.mark.testcase
@allure.description("无待办内容时,日历视图待办页面显示为空")
@allure.title("无待办内容时,日历视图待办页面显示为空")
def test_no_today_weekly_agent_no_text():
    poco("待办").click()
    poco(text="日历视图").click()
    poco(text="周").click()
    #假设选择这周六
    poco(text="周六").click()
    sleep(1)
    poco("首页").click()
    
    
    
#有多条待办内容时,日历视图待办页面显示为代办项和已完成且后面有数字显示
@pytest.mark.testcase
@allure.description("有多条待办内容时,日历视图待办页面显示为代办项和已完成且后面有数字显示")
@allure.title("有多条待办内容时,日历视图待办页面显示为代办项和已完成且后面有数字显示")
def test_no_today_weekly_agent_many_text():
    #创建代办
    poco("待办").click()
    for i in range(3):
        sleep(2)
        poco(text="请在下方书写待办或点击此处新建待办").click()
        text("这里有一条代办", enter=False)
    #修改日期
        choose_n_days_date(1)
        poco(text="确认").click()
    #查看当天代办    
    poco(text="列表视图").click()
    poco(text="日历视图").click()
    poco(text="周").click()
    sleep(2)
    touch(Template(r"tpl1750300034472.png", record_pos=(0.421, -0.215), resolution=(1200, 1920)))
    sleep(1)
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[11].child("android.view.View")[0].click()
    sleep(1)
    for i in range(3):
        poco(desc="").click()
        # touch(Template(r"tpl1750239890001.png", record_pos=(0.449, 0.134), resolution=(1200, 1920)))
        if poco(text="删除").exists():
            poco(text="删除").click()
            poco(text="确认").click()
    sleep(1)
    poco("首页").click()
    
    
    

#当天有多条待办内容时,由周切换为月,查看日历视图待办页面显示
@pytest.mark.testcase
@allure.description("当天有多条待办内容时,由周切换为月,查看日历视图待办页面显示")
@allure.title("当天有多条待办内容时,由周切换为月,查看日历视图待办页面显示")
def test_today_weekly_to_monthly_agent_many_text():
    #创建代办
    poco("待办").click()
    for i in range(3):
        sleep(2)
        poco(text="请在下方书写待办或点击此处新建待办").click()
        text("这里有一条代办",enter=False)
        poco(text="确认").click()
    #查看当天代办    
    poco(text="日历视图").click()
    poco(text="周").click()
    sleep(1)
    #touch(Template(r"tpl1751248556492.png", record_pos=(-0.171, -0.427), resolution=(1200, 1920)))
    poco(text="月").click()
    sleep(1)
    #touch(Template(r"tpl1751248556492.png", record_pos=(-0.171, -0.427), resolution=(1200, 1920)))
    for i in range(3):
        poco(desc="").click()
        # touch(Template(r"tpl1750239890001.png", record_pos=(0.449, 0.134), resolution=(1200, 1920)))
        if poco(text="删除").exists():
            poco(text="删除").click()
            poco(text="确认").click()
    sleep(1)
    poco("首页").click()

    
    

#当天有多条待办内容时,由月切换为周查看日历视图待办页面显示
@pytest.mark.testcase
@allure.description("当天有多条待办内容时,由月切换为周查看日历视图待办页面显示")
@allure.title("当天有多条待办内容时,由月切换为周查看日历视图待办页面显示")
def test_today_monthly_to_weekly_agent_many_text():
    #创建代办
    poco("待办").click()
    for i in range(3):
        sleep(2)
        poco(text="请在下方书写待办或点击此处新建待办").click()
        text("这里有一条代办",enter=False)
        poco(text="确认").click()
    #查看当天代办    
    poco(text="日历视图").click()
    poco(text="月").click()
    sleep(1)
    poco(text="周").click()
    sleep(1)
    for i in range(3):
        poco(desc="").click()
        # touch(Template(r"tpl1750239890001.png", record_pos=(0.449, 0.134), resolution=(1200, 1920)))
        if poco(text="删除").exists():
            poco(text="删除").click()
            poco(text="确认").click()
    sleep(1)
    poco("首页").click()



    
#有多条待办内容时,由周切换为月,查看日历视图待办页面显示
@pytest.mark.testcase
@allure.description("有多条待办内容时,由周切换为月,查看日历视图待办页面显示")
@allure.title("有多条待办内容时,由周切换为月,查看日历视图待办页面显示")
def test_no_today_weekly_to_monthly_agent_many_text():
    #创建代办
    poco("待办").click()
    for i in range(2):
        sleep(2)
        poco(text="请在下方书写待办或点击此处新建待办").click()
        text("这里有一条代办", enter=False)
    #修改日期
        choose_n_days_date(1)
        poco(text="确认").click()
    #查看当天代办
    poco(text="列表视图").click()
    poco(text="日历视图").click()
    poco(text="周").click()
    sleep(2)
    touch(Template(r"tpl1750300034472.png", record_pos=(0.421, -0.215), resolution=(1200, 1920)))
    poco(text="月").click()
    #touch(Template(r"tpl1750300034472.png", record_pos=(0.421, -0.215), resolution=(1200, 1920)))
    #poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[20].click()
    for i in range(2):
        poco(desc="").click()
        # touch(Template(r"tpl1750239890001.png", record_pos=(0.449, 0.134), resolution=(1200, 1920)))
        if poco(text="删除").exists():
            poco(text="删除").click()
            poco(text="确认").click()
    sleep(1)
    poco("首页").click()



#有多条待办内容时由月切换为周查看日历视图待办页面显示
@pytest.mark.testcase
@allure.description("有多条待办内容时由月切换为周查看日历视图待办页面显示")
@allure.title("有多条待办内容时由月切换为周查看日历视图待办页面显示")
def test_no_today_monthly_to_weekly_agent_many_text():
    #创建代办
    poco("待办").click()
    for i in range(2):
        sleep(2)
        poco(text="请在下方书写待办或点击此处新建待办").click()
        text("这里有一条代办", enter=False)
        #修改日期
        choose_n_days_date(1)
        poco(text="确认").click()
    #查看当天代办
    poco(text="列表视图").click()
    poco(text="日历视图").click()
    poco(text="月").click()
    sleep(1)
    touch(Template(r"tpl1750300034472.png", record_pos=(0.421, -0.215), resolution=(1200, 1920)))        
    poco(text="周").click()
    sleep(1)
    #poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[6].click()
    for i in range(2):
        poco(desc="").click()
        # touch(Template(r"tpl1750239890001.png", record_pos=(0.449, 0.134), resolution=(1200, 1920)))
        if poco(text="删除").exists():
            poco(text="删除").click()
            poco(text="确认").click()
    sleep(1)
    poco("首页").click()



#日历视图为当天时,新建当天待办
@pytest.mark.testcase
@allure.description("日历视图为当天时,新建当天待办")
@allure.title("日历视图为当天时,新建当天待办")
def test_today_weekly_agent_new_text():
    poco("待办").click()
    poco(text="日历视图").click()
    sleep(1)
    poco(text="周").click()
    sleep(1)
    touch(Template(r"tpl1750296442447.png", record_pos=(0.165, -0.28), resolution=(1200, 1920)))
    sleep(2)
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text("今天下午六点准时下班",enter=False)
    poco(text="确认").click()
    sleep(1)
    poco(desc="").click()
    # touch(Template(r"tpl1750239890001.png", record_pos=(0.449, 0.134), resolution=(1200, 1920)))
    if poco(text="删除").exists():
        poco(text="删除").click()
        poco(text="确认").click()
    sleep(1)
    poco("首页").click()

    


#日历视图为当天时手写新建下一天待办
@pytest.mark.testcase
@allure.description("日历视图为当天时手写新建下一天待办")
@allure.title("日历视图为当天时手写新建下一天待办")
def test_next_day_weekly_agent_new_text():
    poco("待办").click()
    poco(text="日历视图").click()
    poco(text="周").click()
    sleep(1)
    touch(Template(r"tpl1750296442447.png", record_pos=(0.165, -0.28), resolution=(1200, 1920)))
    sleep(2)
    agent_name = "明天下午六点准时下班"
    sleep(2)
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text(agent_name,enter=False)
    #修改日期
    choose_n_days_date(1)
    poco(text="确认").click()
    poco(text="列表视图").click()
        #删除新增的代办
    find_del_agent(agent_name)
    #回到日历视图
    poco(text="日历视图").click()
    sleep(1)
    poco("首页").click()




#日历视图为下周时手写新建待办
@pytest.mark.testcase
@allure.description("日历视图为下周时手写新建待办")
@allure.title("日历视图为下周时手写新建待办")
def test_weekly_agent_new_text_on_next_week():
    poco("待办").click()
    poco(text="日历视图").click()
    poco(text="周").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[6].swipe([-0.7546, -0.0244])
    agent_name = "今天下午六点准时下班"
    sleep(2)
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text(agent_name,enter=False)
    poco("date").click()
    if exists(Template(r"tpl1750327182161.png", record_pos=(0.052, -0.037), resolution=(1200, 1920))):
        touch(Template(r"tpl1750327182161.png", record_pos=(0.052, -0.037), resolution=(1200, 1920)))
    else:
              poco("转到上个月").click()
              if exists(Template(r"tpl1750327182161.png", record_pos=(0.052, -0.037), resolution=(1200, 1920))):
                touch(Template(r"tpl1750327182161.png", record_pos=(0.052, -0.037), resolution=(1200, 1920)))
    poco(text="确认").click()
    poco(text="确认").click()
    sleep(1)
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[8].child("android.view.View")[0].swipe([0.8804, 0.0136])
        #删除新增的代办
    find_del_agent(agent_name)
    sleep(1)
    poco("首页").click()



#日历视图为月视图时，在当天新建当天待办
@pytest.mark.testcase
@allure.description("日历视图为月视图时，在当天新建当天待办")
@allure.title("日历视图为月视图时，在当天新建当天待办")
def test_today_monthly_agent_new_text():
    poco("待办").click()
    poco(text="日历视图").click()
    poco(text="月").click()
    touch(Template(r"tpl1750296442447.png", record_pos=(0.165, -0.28), resolution=(1200, 1920)))
    sleep(2)
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text("今天下午六点准时下班",enter=False)
    poco(text="确认").click()
    sleep(1)
    poco(desc="").click()
    # touch(Template(r"tpl1750239890001.png", record_pos=(0.449, 0.134), resolution=(1200, 1920)))
    if poco(text="删除").exists():
        poco(text="删除").click()
        poco(text="确认").click()
    sleep(1)
    poco("首页").click()




#日历视图为当天时手写新建下一天待办
@pytest.mark.testcase
@allure.description("日历视图为当天时手写新建下一天待办")
@allure.title("日历视图为当天时手写新建下一天待办")
def test_monthly_agent_new_text_next_day():
    poco("待办").click()
    sleep(1)
    poco(text="日历视图").click()
    sleep(1)
    poco(text="月").click()
    sleep(1)
    touch(Template(r"tpl1750296442447.png", record_pos=(0.165, -0.28), resolution=(1200, 1920)))
    agent_name = "明天下午六点准时下班"
    sleep(1)
    poco(text="请在下方书写待办或点击此处新建待办").click()
    sleep(1)
    text(agent_name,enter=False)
    #修改日期
    choose_n_days_date(1)
    poco(text="确认").click()
    sleep(1)
    poco(text="列表视图").click()
    poco(text="日历视图").click()
    sleep(1)
    touch(Template(r"tpl1750300034472.png", record_pos=(0.421, -0.215), resolution=(1200, 1920))) 
        #删除新增的代办
    find_del_agent(agent_name)
    sleep(1)
    poco("首页").click()




#日历视图为下月时手写新建待办
@pytest.mark.testcase
@allure.description("日历视图为下月时手写新建待办")
@allure.title("日历视图为下月时手写新建待办")
def test_monthly_agent_new_text_on_next_month():
    poco("待办").click()
    sleep(2)
    poco(text="日历视图").click()
    sleep(1)
    if poco(text="月").exists():
        poco(text="月").click()
        sleep(1)
        touch(Template(r"tpl1750296442447.png", record_pos=(0.165, -0.28), resolution=(1200, 1920)))
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[5].child("Next").click()
        agent_name = "今天下午六点准时下班"
        sleep(2)
        poco(text="请在下方书写待办或点击此处新建待办").click()
        text(agent_name,enter=False)
        poco("date").click()
        poco("转到上个月").click()
        sleep(1)
        touch(Template(r"tpl1750327182161.png", record_pos=(0.052, -0.037), resolution=(1200, 1920)))
        sleep(1)
        poco(text="确认").click()
        poco(text="确认").click()
        poco("Previous").click()
            #删除新增的代办
        find_del_agent(agent_name)
        sleep(1)
    poco("首页").click()




#待办信息加入待办后在周日历视图上查看
@pytest.mark.testcase
@allure.description("待办信息加入待办后在周日历视图上查看")
@allure.title("待办信息加入待办后在周日历视图上查看")
def test_weekly_agent_new_text_on_agent():
    poco("待办").click()
    sleep(1)
    touch(Template(r"tpl1750296442447.png", record_pos=(0.165, -0.28), resolution=(1200, 1920)))
    agent_name = "这里有一条代办"
    sleep(2)
    poco(text="请在下方书写待办或点击此处新建待办").click()
    sleep(1)
    text(agent_name,enter=False)
    choose_n_days_date(1)
    poco(text="确认").click()
    poco(text="列表视图").click()
    poco(text="日历视图").click()
    sleep(1)
    poco(text="周").click()
    sleep(1)
    touch(Template(r"tpl1750300034472.png", record_pos=(0.421, -0.215), resolution=(1200, 1920)))
    sleep(1)
    #find_del_agent(agent_name)
    poco(desc="").click()
    # touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    if poco(text="删除").exists():
        poco(text="删除").click()
        poco(text="确认").click()
    sleep(1)
    poco("首页").click()





#待办信息加入待办后在月日历视图上查看
@pytest.mark.testcase
@allure.description("待办信息加入待办后在月日历视图上查看")
@allure.title("待办信息加入待办后在月日历视图上查看")
def test_monthly_agent_new_text_on_agent():
    poco("待办").click()
    sleep(1)
    touch(Template(r"tpl1750296442447.png", record_pos=(0.165, -0.28), resolution=(1200, 1920)))
    sleep(1)
    agent_name = "这里有一条代办"
    poco(text="请在下方书写待办或点击此处新建待办").click()
    sleep(1)
    text(agent_name,enter=False)
    choose_n_days_date(1)
    poco(text="确认").click()
    poco(text="列表视图").click()
    poco(text="日历视图").click()
    sleep(1)
    poco(text="月").click()
    sleep(1)
    touch(Template(r"tpl1750300034472.png", record_pos=(0.421, -0.215), resolution=(1200, 1920)))
    sleep(1)
    #find_del_agent(agent_name)
    poco(desc="").click()
    # touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    if poco(text="删除").exists():
        poco(text="删除").click()
        poco(text="确认").click()
    sleep(1)
    poco("首页").click()




if __name__=="__main__":
    test_view_weekly_calendar_agent()
    test_switch_weekly_calendar_agent()
    test_slide_weekly_calendar_agent()
    test_left_switch_weekly_calendar_agent()
    test_right_switch_weekly_calendar_agent()
    test_left_slide_weekly_calendar_agent()
    test_right_slide_weekly_calendar_agent()
    test_view_monthly_calendar_agent()
    test_switch_monthly_calendar_agent()
    test_switch_weeekly_to_monthly_agent()
    test_switch_weeekly_to_monthly_to_weekly_agent()
    test_switch_monthly_to_weekly_agent()
    test_switch_monthly_to_weekly_to_monthly_agent()
    test_weekly_agent_text()
    test_monthly_agent_text()
    test_today_weekly_agent_no_text()
    test_today_weekly_agent_many_text()
    test_no_today_weekly_agent_no_text()
    test_no_today_weekly_agent_many_text()
    test_today_weekly_to_monthly_agent_many_text()
    test_today_monthly_to_weekly_agent_many_text()
    test_no_today_weekly_to_monthly_agent_many_text()
    test_no_today_monthly_to_weekly_agent_many_text()
    test_today_weekly_agent_new_text()
    test_next_day_weekly_agent_new_text()
    test_weekly_agent_new_text_on_next_week()
    test_today_monthly_agent_new_text()
    test_monthly_agent_new_text_next_day()
    test_monthly_agent_new_text_on_next_month()
    test_weekly_agent_new_text_on_agent()
    test_monthly_agent_new_text_on_agent()
    
    
    
    
    
    
