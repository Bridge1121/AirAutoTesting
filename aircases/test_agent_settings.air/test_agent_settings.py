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

pytestmark = [allure.feature("待办设置模块用例"), allure.epic("办公本v2.4.0")]
    
            
            
#待办页新增“设置项”校验            
@pytest.mark.testcase
@allure.description("待办页新增“设置项”校验 ")
@allure.title("待办页新增“设置项”校验 ")
def test_check_settings_agent():
    poco("待办").click()
    exists(Template(r"tpl1750386624783.png", record_pos=(0.443, -0.703), resolution=(1200, 1920)))
    poco("首页").click()

    

#待办页点击“设置”按钮进入“待办设置”页校验
@pytest.mark.testcase
@allure.description("待办页点击“设置”按钮进入“待办设置”页校验")
@allure.title("待办页点击“设置”按钮进入“待办设置”页校验")
def test_click_settings_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#待办设置页包含如下选项“分组管理”、“显示空分组”、“提醒设置”、“同步到其他日历”、“显示逾期天数”等 校验
# @pytest.mark.testcase
# @allure.description("待办设置页包含选项校验")
# @allure.title("待办设置页包含选项校验")
# def test_check_settings_options_agent():
#     poco("待办").click()
#     poco("设置").click()
#     check_text_exists("分组管理")
#     sleep(1)
#     check_text_exists("显示空分组")
#     sleep(1)
#     check_text_exists("提醒设置")
#     sleep(1)
#     check_text_exists("同步到其他日历")
#     sleep(1)
#     check_text_exists("显示逾期天数")
#     poco(text="待办设置").click()
#     poco("首页").click()
    
    
    
#待办设置页点击“分组管理”跳转“分组管理”页面校验    
@pytest.mark.testcase
@allure.description("待办设置页点击“分组管理”跳转“分组管理”页面校验")
@allure.title("待办设置页点击“分组管理”跳转“分组管理”页面校验")
def test_check_settings_group_management_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#分组管理页面包含“返回按钮”、“排序管理”、“新建分组”等操作按钮校验
# @pytest.mark.testcase
# @allure.description("分组管理页面包含“返回按钮”、“排序管理”、“新建分组”等操作按钮校验")
# @allure.title("分组管理页面包含“返回按钮”、“排序管理”、“新建分组”等操作按钮校验")
# def test_check_group_management_options_agent():
#     poco("待办").click()
#     poco("设置").click()
#     poco(text="分组管理").click()
#     exists(Template(r"tpl1750388421334.png", record_pos=(-0.448, -0.712), resolution=(1200, 1920)))
#     check_text_exists("新建分组")
#     sleep(1)
#     check_text_exists("排序管理")
#     poco(desc="").click()
#     poco(text="待办设置").click()
#     poco("首页").click()
    
    
    
#分组管理页显示“默认分组”校验
@pytest.mark.testcase
@allure.description("分组管理页显示“默认分组”校验")
@allure.title("分组管理页显示“默认分组”校验")
def test_check_group_management_default_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    if poco(textMatches=".*默认分组.*").exists():
#    check_text_exists("默认分组")
        poco(desc="").click()
        poco(text="待办设置").click()
        poco("首页").click()
    
    
    
#分组管理页返回按钮点击响应正常校验
@pytest.mark.testcase
@allure.description("分组管理页返回按钮点击响应正常校验")
@allure.title("分组管理页返回按钮点击响应正常校验")
def test_check_group_management_return_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#分组管理页排序管理按钮点击响应正常校验
@pytest.mark.testcase
@allure.description("分组管理页排序管理按钮点击响应正常校验")
@allure.title("分组管理页排序管理按钮点击响应正常校验")
def test_click_group_management_sort_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="排序管理").click()
    poco(text="完成").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#分组管理页排序管理按钮点击进入分组排序状态校验    
@pytest.mark.testcase
@allure.description("分组管理页排序管理按钮点击进入分组排序状态校验")
@allure.title("分组管理页排序管理按钮点击进入分组排序状态校验")
def test_check_group_management_sort_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="排序管理").click()
    poco("sort").click()
    poco(text="完成").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click() 
    
    
    
#分组管理页进入排序状态，拖动分组全区域可进行排序校验    
@pytest.mark.testcase
@allure.description("分组管理页进入排序状态，拖动分组全区域可进行排序校验")
@allure.title("分组管理页进入排序状态，拖动分组全区域可进行排序校验")
def test_drag_group_management_sort_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="排序管理").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[2].child("android.view.View").swipe([-0.0087, 0.2304])
    sleep(1)
    poco(text="完成").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#排序时拖动超出一屏，页面滑动、显示正常校验
@pytest.mark.testcase
@allure.description("排序时拖动超出一屏，页面滑动、显示正常校验")
@allure.title("排序时拖动超出一屏，页面滑动、显示正常校验")
def test_long_drag_group_management_sort_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="排序管理").click()
    sleep(1)
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[2].child("group")[0].swipe([0.0304, 0.8186])
    sleep(1)
    poco(text="完成").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#分组管理页排序状态，点击左上角“X”按钮退出排序状态，所有排序操作不保留校验
@pytest.mark.testcase
@allure.description("分组管理页排序状态，点击左上角“X”按钮退出排序状态，所有排序操作不保留校验")
@allure.title("分组管理页排序状态，点击左上角“X”按钮退出排序状态，所有排序操作不保留校验")
def test_check_group_management_quit_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    text("分组1",enter=False)
    poco(text="确认").click()
    poco(text="排序管理").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[2].child("android.view.View").swipe([-0.0867, 0.1193])
    poco(desc="").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
    poco(text="删除").click()
    poco(text="确定").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#分组管理页排序状态，点击左上角“完成”按钮退出排序状态，最后排序操作保留校验
@pytest.mark.testcase
@allure.description("分组管理页排序状态，点击左上角“完成”按钮退出排序状态，最后排序操作保留校验")
@allure.title("分组管理页排序状态，点击左上角“完成”按钮退出排序状态，最后排序操作保留校验")
def test_check_group_management_retain_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    text("分组1",enter=False)
    poco(text="确认").click()
    poco(text="排序管理").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[2].child("android.view.View").swipe([-0.0173, 0.1247])

    poco(text="完成").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[0].child("more").click()
    poco(text="删除").click()
    poco(text="确定").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#分组管理页新建分组按钮点击响应正常,调起新建分组命名弹窗,新建分组弹窗展示无异常校验
@pytest.mark.testcase
@allure.description("分组管理页新建分组按钮点击响应正常,调起新建分组命名弹窗,新建分组弹窗展示无异常校验")
@allure.title("分组管理页新建分组按钮点击响应正常,调起新建分组命名弹窗,新建分组弹窗展示无异常校验")
def test_check_group_management_new_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    for i in range(2):    
        poco(text="新建分组").click()
        poco(text="请输入分组名称").click()
        agent_name="a"*(12+i)
        text(agent_name,enter=False)
        poco(text="确认").click()
    for i in range(2):
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
        poco(text="删除").click()
        poco(text="确定").click()    
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    



#新建分组文本输入框字符类型无限制校验
@pytest.mark.testcase
@allure.description("新建分组文本输入框字符类型无限制校验")
@allure.title("新建分组文本输入框字符类型无限制校验")
def test_check_new_group_character_type_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    text("2",enter=False)
    poco(text="确认").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    text("w",enter=False)
    poco(text="确认").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    text("我",enter=False)
    poco(text="确认").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    text("@",enter=False)
    poco(text="确认").click()
    # poco(text="新建分组").click()
    # poco(text="请输入分组名称").click()
    #成功输入表情包，但因需调用输入法，影响后续测试，暂时不测
    # poco("android:id/input_method_nav_ime_switcher").click()
    # poco(text="搜狗输入法").click()
    # touch(Template(r"tpl1750408792782.png", record_pos=(-0.278, 0.275), resolution=(1200, 1920)))
    # poco("android.widget.FrameLayout").offspring("android.widget.RelativeLayout").offspring("androidx.viewpager.widget.ViewPager").child("androidx.recyclerview.widget.RecyclerView").child("android.widget.FrameLayout")[0].child("android.widget.ImageView").click()
    # poco(text="确认").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    text("@w1二 ",enter=False)
    poco(text="确认").click()
    for i in range(5):
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
        poco(text="删除").click()
        poco(text="确定").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    


#新建分组文本输入框操作校验
@pytest.mark.testcase
@allure.description("新建分组文本输入框操作校验")
@allure.title("新建分组文本输入框操作校验")
def test_new_group_input_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    text("这里有一个新建文本",enter=False)
    poco("android.widget.EditText").click()
    poco("android:id/content").swipe([-0.1041, 0.0136])
    text("加入",enter=False)
    # poco("android:id/input_method_nav_ime_switcher").click()
    # poco(text="搜狗输入法").click()
    # touch(Template(r"tpl1750413359903.png", record_pos=(0.423, 0.559), resolution=(1200, 1920)))
    poco("android.widget.EditText").click()
    text("好", enter=False)
    sleep(1)
    # touch(Template(r"tpl1750414889486.png", record_pos=(0.148, 0.672), resolution=(1200, 1920)))
    poco(text="确认").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
    poco(text="删除").click()
    poco(text="确定").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click() 



#新建待办分组文本输入框位数上限校验
@pytest.mark.testcase
@allure.description("新建待办分组文本输入框位数上限校验")
@allure.title("新建待办分组文本输入框位数上限校验")
def test_check_new_group_character_limit_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    agent_name="a"
    text(agent_name,enter=False)
    poco(text="确认").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    agent_name="a"*6
    text(agent_name,enter=False)
    poco(text="确认").click()
    for i in range(2):    
        poco(text="新建分组").click()
        poco(text="请输入分组名称").click()
        agent_name="a"*(12+i)
        text(agent_name,enter=False)
        poco(text="确认").click()
    for i in range(4):
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
        poco(text="删除").click()
        poco(text="确定").click()    
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#文本输入框长按支持全选、粘贴、复制、剪切，点击换行等操作验证    
@pytest.mark.testcase
@allure.description("文本输入框长按支持全选、粘贴、复制、剪切，点击换行等操作验证")
@allure.title("文本输入框长按支持全选、粘贴、复制、剪切，点击换行等操作验证")
def test_check_new_group_input_operate_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    agent_name="a"*12
    text(agent_name,enter=False)
    touch((0.5816666666666667, 0.48125), duration=2)
    #swipe_press_ai(start_point=(0.5, 0.48125),end_point=(410,990))
    poco(text="全选").click()
    poco(text="复制").click()
    touch((0.5816666666666667, 0.48125), duration=2)
    poco(text="粘贴").click()
    # poco("android:id/input_method_nav_ime_switcher").click()
    # poco(text="搜狗输入法").click()
    # touch(Template(r"tpl1750643499111.png", record_pos=(0.421, 0.661), resolution=(1200, 1920)))
    touch((0.5816666666666667, 0.48125), duration=2)
    poco(text="全选").click()
    poco(text="剪切").click()
    poco(text="取消").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco("首页").click()
    
    
    
#分组管理页创建分组成功校验,以及分组命名弹窗点击“确认”“取消”按钮响应正常，分组名称重复校验验证
@pytest.mark.testcase
@allure.description("分组管理页创建分组成功校验,以及分组命名弹窗点击“确认”“取消”按钮响应正常，分组名称重复校验验证")
@allure.title("分组管理页创建分组成功校验,以及分组命名弹窗点击“确认”“取消”按钮响应正常，分组名称重复校验验证")
def test_click_new_group__create_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    #”“确认”按钮验证，创建分组成功
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    poco(text="确认").click()
    agent_name="a"
    text(agent_name,enter=False)
    poco(text="确认").click()
    #“取消”按钮验证
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    poco(text="取消").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    agent_name="a"
    text(agent_name,enter=False)
    poco(text="取消").click()
    #名称重复校验验证
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    agent_name="a"
    text(agent_name,enter=False)
    poco(text="确认").click()
    for i in range(2):
        poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
        poco(text="删除").click()
        poco(text="确定").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco(text="首页").click()
    
    
    
#校验分组列表右侧菜单按钮功能list为：重命名、删除，以及确认、删除功能校验    
@pytest.mark.testcase
@allure.description("校验分组列表右侧菜单按钮功能list为：重命名、删除，以及确认、删除功能校验")
@allure.title("校验分组列表右侧菜单按钮功能list为：重命名、删除，以及确认、删除功能校验")
def test_check_group_list_function_agent():
    poco("待办").click()
    poco("设置").click()
    poco(text="分组管理").click()
    #新建两项代办分组
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    agent_name="a"
    text(agent_name,enter=False)
    poco(text="确认").click()
    poco(text="新建分组").click()
    poco(text="请输入分组名称").click()
    agent_name="b"
    text(agent_name,enter=False)
    poco(text="确认").click()
    #重命名功能验证
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[2].child("more").click()
    poco(text="重命名").click()
    touch((0.5816666666666667, 0.48125), duration=2)
    poco(text="全选").click()
    poco(text="剪切").click()
    agent_name="a"
    text(agent_name,enter=False)
    poco(text="确认").click()
    #删除功能验证
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
    poco(text="删除").click()
    poco(text="取消").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
    poco(text="删除").click()
    poco(text="确定").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
    poco(text="删除").click()
    poco(text="确定").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    poco(text="首页").click()


    
#分组管理页删除包含待办的分组，分组删除，待办也会被删除
@pytest.mark.testcase
@allure.description("分组管理页删除包含待办的分组，分组删除，待办也会被删除")
@allure.title("分组管理页删除包含待办的分组，分组删除，待办也会被删除")
def test_delete_group_includes_agent():
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name="这里有一条代办"
    text(agent_name,enter=False)
    poco("移动分组").click()
    poco(text="新建分组").click()
    text("a",enter=False)
    poco(text="确认").click()
    poco("android.widget.FrameLayout").offspring("android.view.ViewGroup").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[0].child("android.view.View")[1].click()
    poco(text="确认").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text(agent_name,enter=False)
    poco("移动分组").click()
    poco("android.widget.FrameLayout").offspring("android.view.ViewGroup").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[0].child("android.view.View")[1].click()
    poco(text="确认").click()
    poco("设置").click()
    poco(text="分组管理").click()
    poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[3].child("android.view.View")[1].child("more").click()
    poco(text="删除").click()
    poco(text="确定").click()
    poco(desc="").click()
    poco(text="待办设置").click()
    sleep(1)
    poco(text="首页").click()
    
    


    
    
    
if __name__=="__main__":
    test_check_settings_agent()
    test_click_settings_agent()
    test_check_settings_group_management_agent()
    test_check_group_management_default_agent()
    test_check_group_management_return_agent()
    test_click_group_management_sort_agent()
    test_check_group_management_sort_agent()
    test_drag_group_management_sort_agent()
    test_long_drag_group_management_sort_agent()
    test_check_group_management_quit_agent()
    test_check_group_management_retain_agent()
    test_check_group_management_new_agent()
    test_check_new_group_character_type_agent()
    test_new_group_input_agent()
    test_check_new_group_character_limit_agent()
    test_check_new_group_input_operate_agent()
    test_click_new_group__create_agent()
    test_check_group_list_function_agent()
    test_delete_group_includes_agent()
    
    

            