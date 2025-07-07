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

pytestmark = [allure.feature("待办搜索模块用例"), allure.epic("办公本v2.4.0")]


    
    

    
#待办页面右上角显示全局搜索图标按钮,搜索结果页，已完成的待办显示在未完成待办的下面（倒序排序），并且可切换勾选框状态，修改完成/未完成状态

@pytest.mark.testcase
@allure.description("待办搜索功能，已完成待办与未完成待办的排序和勾选状态")
@allure.title("待办搜索功能，已完成待办与未完成待办的排序和勾选状态")
def test_search_agent_sort_and_state():
    #创建已完成待办A和待处理待办B
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name="第一个新品发布计划"
    text(agent_name,enter=False)
    poco(text="确认").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text("第二个新品发布计划",enter=False)
    poco(text="确认").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[11].child("android.view.View")[0].click()
    poco("搜索").click()
    sleep(2)
    if poco(text="请输入关键词或具体问题").exists():
        poco(text="请输入关键词或具体问题").click()
        text("新品发布计划",enter=False)
        sleep(1)
        poco(text="待办").click()
        sleep(1)
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.view.View").child("android.view.View")[2].click()
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[6].child("android.view.View").child("android.view.View")[2].click()
        poco("Back").click()
        sleep(1)
        for i in range(2):
            poco("androidx.compose.ui.platform.ComposeView")\
            .child("android.view.View")\
            .child("android.view.View")\
            .child("android.view.View")[11]\
            .child("android.view.View")[1].child("android.view.View").click()
            sleep(1)
            poco(text="删除").click()
            poco(text="确认").click()
    poco(text="首页").click()
    
    
    
#点击待办搜索结果列表页的待办内容，弹出修改待办弹窗,修改待办后，回到待办列表，该待办已是修改后的内容
@pytest.mark.testcase
@allure.description("待办搜索功能，修改待办后的待办状态")
@allure.title("待办搜索功能，修改待办后的待办状态")
def test_search_agent_modify():
    #创建待办A
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name="第一个新品发布计划"
    text(agent_name,enter=False)
    poco(text="确认").click()
    poco("搜索").click()
    poco(text="请输入关键词或具体问题").click()
    text("新品发布计划",enter=False)
    poco(text="待办").click()
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View").child("android.view.View")[6]\
    .child("android.view.View").child("android.widget.TextView").click()
    sleep(1)
    text("需注意",enter=False)
    poco(text="确认").click()
    poco("Back").click()
    sleep(1)
    poco(desc="").click()
    sleep(1)
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="首页").click()
    
    
    
    
  

if __name__=="__main__":
    test_search_agent_sort_and_state()
    test_search_agent_modify()
    
    
    
    
    
    