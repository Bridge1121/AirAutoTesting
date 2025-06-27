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

pytestmark = [allure.feature("代办重点关注模块用例"), allure.epic("办公本v2.4.0")]


#新建一条代办，重点关注，清空待办所有内容确定，提示无法保存，不能为空
@pytest.mark.testcase
@allure.description("新建一条代办，重点关注，清空待办所有内容确定，提示无法保存，不能为空")
@allure.title("新建一条代办，重点关注，清空待办所有内容确定，提示无法保存，不能为空")
def test_clear_focus_on_agent():
    if is_login()==True:
        login()
    poco("待办").click()
    #新建一条重点关注的代办
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是一条要清空的重点关注的代办"
    text(agent_name,enter=False)
    #点击重点关注
    poco("重点模式").click()
    poco(text="确认").click()
    #切换视图
    poco(text="列表视图").click()
    poco(text="重点").click()
    #点击修改代办内容
    poco(text=agent_name).click()
    #清空代办内容
    for i in range(len(agent_name)):
        keyevent("DEL")
    #点击确认保存
    poco(text="确认").click()
    #保存失败
    text(agent_name,enter=False)
    #点击确认
    poco(text="确认").click()
    #删除新建的代办
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #切换视图
    poco(text="日历视图").click()
    poco("首页").click()

    
def test():
    agent_name = "这是一条要清空的重点关注的代办"
    for i in range(len(agent_name)):
        keyevent("DEL")



#在重点标记列表中修改待办内容，会同步到全部待办列表中
@pytest.mark.testcase
@allure.description("在重点标记列表中修改待办内容，会同步到全部待办列表中")
@allure.title("在重点标记列表中修改待办内容，会同步到全部待办列表中")
def test_focus_on_agent_edit_sync():
    if is_login()==True:
        login()
    poco("待办").click()
    #新建一条重点关注的代办
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是一条要修改的重点关注的代办"
    text(agent_name,enter=False)
    #点击重点关注
    poco("重点模式").click()
    poco(text="确认").click()
    #切换视图
    poco(text="列表视图").click()
    #点击重点关注列表
    poco(text="重点").click()
    poco(text=agent_name).click()
    text("编辑一下",enter=False)
    poco(text="确认").click()
    #点击待处理列表，查看是否同步编辑
    poco(text="待处理").click()
    sleep(1)
    #删除代办
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #切换视图
    poco(text="日历视图").click()
    poco("首页").click()
    


    
    
    


#修改重点关注的待办日期，月份，年份，
@pytest.mark.testcase
@allure.description("修改重点关注的待办日期，月份，年份，")
@allure.title("修改重点关注的待办日期，月份，年份，")
def test_focus_on_agent_edit_date():
    if is_login()==True:
        login()
    poco("待办").click()
    #新建一条重点关注的代办
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是一条要修改年月日的重点关注的代办"
    text(agent_name,enter=False)
    #点击重点关注
    poco("重点模式").click()
    poco(text="确认").click()
    poco(text=agent_name).click()
    #点击修改年月日
    poco("date").click()
    poco(text="时间段").click()
    #点击日期
    poco("android.widget.FrameLayout")\
    .offspring("android.view.ViewGroup")\
    .child("android.view.View")\
    .offspring("android.widget.ScrollView")\
    .child("android.widget.TextView")[0].click()
    poco("切换为选择年份").click()
    #切换年份
    touch(Template(r"tpl1750229209384.png", record_pos=(-0.187, -0.248), resolution=(1200, 1920)))
    #切换月份
    poco("转到下个月").click()
    #切换日期
    poco("android.widget.FrameLayout")\
    .offspring("android.view.ViewGroup")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[0]\
    .child("android.view.View")\
    .child("android.view.View")[3]\
    .child("android.widget.TextView")[5]\
    .child("android.view.View").click()
    #点击确定
    poco(text="确定").click()
    poco(text="确认").click()
    poco(text="确认").click()
    #切换视图，删除代办
    poco(text="列表视图").click()
    sleep(1)
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="日历视图").click()
    poco("首页").click()
    
    

#重点关注列表,完成的未设日期的待办显示,完成的已设日期的待办显示,已完成的待办再点击左侧勾选
@pytest.mark.testcase
@allure.description("重点关注列表,完成的未设日期的待办显示,完成的已设日期的待办显示,已完成的待办再点击左侧勾选")
@allure.title("重点关注列表,完成的未设日期的待办显示,完成的已设日期的待办显示,已完成的待办再点击左侧勾选")
def test_focus_on_finish_agent():
    if is_login()==True:
        login()
    #新建有日期的代办，点击完成，2s内再次点击
    poco("待办").click()
     #新建一条重点关注的代办
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是一条要测试完成的重点关注的代办"
    text(agent_name,enter=False)
    #点击重点关注
    poco("重点模式").click()
    poco(text="确认").click()
    #切换视图
    poco(text="列表视图").click()
    agents = poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .children()
    for i  in range(len(agents)):
        if agents[i].get_text() == agent_name:
            #点击勾选完成
            agents[i+1].click()
            #2s内再次点击
            agents[i+1].click()
            break
    sleep(2)
    #删除日期，点击完成
    poco(text=agent_name).click()
    poco("clean").click()
    poco(text="确认").click()
    #点击完成
    agents = poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .children()
    for i  in range(len(agents)):
        if agents[i].get_text() == agent_name:
            #点击勾选完成
            agents[i+1].click()
    poco(text="已完成").click()
    sleep(1)
    #删除代办
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="待处理").click()
    poco(text="日历视图").click()
    poco("首页").click()
    
    


    



    



if __name__=="__main__":
    test_clear_focus_on_agent()
    test_focus_on_agent_edit_sync()
    test_focus_on_agent_edit_date()
    test_focus_on_finish_agent()




    

