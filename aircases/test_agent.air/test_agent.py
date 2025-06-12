# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))
    
    
    
#书写待办
def test_add_agent():
    if is_login()==True:
        login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text("7月15日与市场部讨论新品发布计划",enter=False)
    poco(text="确认").click()
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    #删除新增的代办
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()



#修改待办内容,在弹窗中点击取消，关闭弹窗,修改待办部分内容，点击确定
def test_edit_agent_text():
    if is_login()==True:
        login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent="8月15日与市场部讨论新品发布计划"
    text(agent,enter=False)
    poco(text="确认").click()
    sleep(1)
    #点击新增的代办
    poco(text=agent).click()
    #输入编辑的内容
    text("hhh",enter=False)
    #点击取消
    poco(text="取消").click()
    #再次编辑
    poco(text=agent).click()
    text("啊啊啊",enter=False)
    #点击确认
    poco(text="确认").click()
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    #删除新增的代办
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
# 修改待办日期，点击确定
def test_edit_agent_date():
    if is_login()==True:
        login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent="8月15日与市场部讨论新品发布计划"
    text(agent,enter=False)
    poco(text="确认").click()
    sleep(1)
    #点击新增的代办
    #修改日期
    poco(text="今天 17:00").click()
    sleep(1)
    #点击要修改的日期
    touch(Template(r"tpl1749638112487.png", record_pos=(0.008, 0.033), resolution=(1200, 1920)))
    #点击确定
    poco(text="确认").click()
    poco("首页").click()



# 删除设置日期的待办
def test_del_agent():
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent="12月15日与市场部讨论新品发布计划"
    text(agent,enter=False)
    poco(text="确认").click()
    sleep(1)
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    #删除新增的代办
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

    
    

if __name__=="__main__":
    test_add_agent()
    test_edit_agent_text()
    test_edit_agent_date()
    test_del_agent()
    
    
    