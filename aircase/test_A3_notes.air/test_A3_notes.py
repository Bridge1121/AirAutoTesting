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

pytestmark = [allure.feature("A3便签模块用例"), allure.epic("办公本A3")]




#下拉菜单显示新建便签入口
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("下拉菜单显示新建便签入口")
@allure.title("下拉菜单显示新建便签入口")
def test_notes_on_drop_down_menu():
    if is_login()==True:
        login()
    swipe((1036,0),(886,432))
    poco(text="便签").click()
    poco("close").click()
    poco(text="笔记").click()
    poco(text="便签").click()
    sleep(1)
    touch(Template(r"tpl1751523655968.png", record_pos=(-0.203, -0.366), resolution=(1600, 2560)))

    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()




    
    
#笔记列表页面显示新建便签入口
#todo 功能尚未开发完成

@pytest.mark.testcase
@allure.description("笔记列表页面显示新建便签入口")
@allure.title("笔记列表页面显示新建便签入口")
def test_notes_on_note():
    if is_login()==True:
        login()
    poco(text="笔记").click()
    poco(text="便签").click()
    sleep(2)
    poco(text="新建笔记").click()
    sleep(1)
    poco("close").click()
    sleep(1)
    touch(Template(r"tpl1751523655968.png", record_pos=(-0.203, -0.366), resolution=(1600, 2560)))
    sleep(1)
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()





#便签文件夹输入框校验
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("便签文件夹输入框校验")
@allure.title("便签文件夹输入框校验")
def test_check_notes_input():
    if is_login()==True:
        login()
    #在便签分组下点击新建文件夹，弹窗中所有的笔记分组和笔记文件夹都是置灰不可点击
    poco(text="笔记").click()
    poco(text="便签").click()
    sleep(2)
    poco(text="新建笔记").click()
    sleep(1)
    poco("close").click()
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[4].click()
    #未输入内容，点击确定，提示文件夹名称不能为空
    poco(text="确认").click()
    #输入文件夹名称，点击确定
    poco(text="请输入文件夹名称").click()
    file_name="文件夹A"
    text(file_name,enter=False)
    poco(text="确认").click()
    #输入12位数，点击确定，文件夹创建成功
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[4]\
    .child("android.widget.Button").click()
    poco(text="请输入文件夹名称").click()
    agent_name="a"*12
    text(agent_name,enter=False)
    poco(text="确认").click()
    #输入超过12位数，第13位无法输入
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[4]\
    .child("android.widget.Button").click()
    poco(text="请输入文件夹名称").click()
    agent_name="a"*13
    text(agent_name,enter=False)
    poco(text="确认").click()
    #在便签分组下创建二级子文件夹
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[4]\
    .child("android.widget.Button").click()
    poco(text="便签").click()
    sleep(2)
    poco(text=file_name).click()
    sleep(1)
    poco(text="确定").click()
    sleep(1)
    poco(text="请输入文件夹名称").click()
    agent_name="子文件夹B"
    text(agent_name,enter=False)
    poco(text="确认").click()
    #在便签分组下创建三级子文件夹
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[3]\
    .child("android.widget.Button").click()
    poco(text="全部文件夹").click()
    poco(text="便签").click()
    #点击新建的文件夹
    sleep(1)
    poco(text=file_name).click()
    sleep(1)
    #点击新建的二级文件夹
    poco(text=agent_name).click()
    sleep(1)
    poco(text="确定").click()
    poco(text="请输入文件夹名称").click()
    agent_name="子文件夹C"
    text(agent_name,enter=False)
    poco(text="确认").click()
    poco("<").click()
    poco("<").click()
    for i in range(3):
        sleep(1)
        touch(Template(r"tpl1751523655968.png", record_pos=(-0.203, -0.366), resolution=(1600, 2560)))
#         poco("更多设置").click()
        poco(text="删除").click()
        poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()





#全局搜索中笔记标签下可以搜到和看到便签,在笔记tab搜索结果中点击便签打开便签详情,AI搜索中可以看到便签，便签在ai搜索结果中按笔记展示
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("全局搜索中笔记标签下可以搜到和看到便签,在笔记tab搜索结果中点击便签打开便签详情,AI搜索中可以看到便签，便签在ai搜索结果中按笔记展示")
@allure.title("全局搜索中笔记标签下可以搜到和看到便签,在笔记tab搜索结果中点击便签打开便签详情,AI搜索中可以看到便签，便签在ai搜索结果中按笔记展示")
def test_note_search():
    #     if is_login()==True:
    #         login()
    poco(text="笔记").click()
    poco(text="便签").click()
    sleep(2)
    poco(text="新建笔记").click()
    sleep(1)
    poco("Pen").click()
    sleep(1)
    agent_name = "思必驰发布会本周计划"
    text(agent_name, enter=False)
    sleep(1)
    poco("close").click()
    (poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child(
        "android.view.View")[5].child("search")).click()
    poco(text="请输入关键词或具体问题").click()
    agent_name = "思必驰发布会"
    text(agent_name, enter=False)
    sleep(1)
    poco("android.widget.FrameLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View") \
        .child("android.view.View") \
        .child("android.view.View")[6] \
        .child("android.view.View") \
        .child("android.view.View")[1].click()
    sleep(1)
    poco("close").click()
    sleep(1)
    poco("Back").click()
    sleep(1)
    touch(Template(r"tpl1751523655968.png", record_pos=(-0.203, -0.366), resolution=(1600, 2560)))
    #     poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)
    poco(text="全部笔记").click()
    poco(text="首页").click()


#移动加密便签/便签文件夹
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("移动加密便签/便签文件夹")
@allure.title("移动加密便签/便签文件夹")
def test_move_encrypt_sticky_notes(password="123456a"):
    if is_login()==True:
        login()
    poco(text="笔记").click()
    poco(text="便签").click()
    sleep(2)
    if poco(text="新建便签").exists():
        poco(text="新建便签").click()
    else:
        poco(text="新建笔记").click()
    poco("close").click()
    sleep(2)
    touch(Template(r"tpl1751523655968.png", record_pos=(-0.203, -0.366), resolution=(1600, 2560)))
#     poco("更多设置").click()
    poco(text="加密便签").click()
    agent_name="12345"
    if poco(textMatches=".*请设置4-20位数字、字母、符号.*").exists():
        poco(text="请设置4-20位数字、字母、符号").click()
        text(agent_name,enter=False)
        poco(text="再次输入密码").click()
        text(agent_name,enter=False)
        poco(text="确认").click()
    #批量移动时，全选内容包含加密的便签
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="移动至").click()
    poco("<").click()
    poco(text="退出").click()
    #批量移动时，全选内容包含加密的便签文件夹
    (poco("androidx.compose.ui.platform.ComposeView").child("android.view.View").child("android.view.View").child("android.view.View")[4].child("android.widget.Button")).click()
    poco(text="请输入文件夹名称").click()
    text("这里有个文件夹",enter=False)
    poco(text="确认").click()
    touch(Template(r"tpl1751523655968.png", record_pos=(-0.203, -0.366), resolution=(1600, 2560)))
#     poco("更多设置").click()
    poco(text="加密文件夹").click()
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="移动至").click()
    poco("<").click()
    poco(text="删除").click()
    poco(text="请输入密码").click()
    text(password,enter=False)
    poco(text="确认").click()
    poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()



    
    

#【笔记】>【标签】页面编辑功能
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("【笔记】>【标签】页面编辑功能")
@allure.title("【笔记】>【标签】页面编辑功能")
def test_notes_editing_features():
    if is_login()==True:
        login()
    poco(text="笔记").click()
    poco(text="便签").click()
    sleep(2)
    if poco(text="新建便签").exists():
        poco(text="新建便签").click()
    else:
        poco(text="新建笔记").click()
    #文本框输入法输入内容
    poco("Pen").click()
    poco("android:id/input_method_nav_back").click()
    poco("com.aispeech.tablet:id/editTextView").click()
    #点击笔图标，弹出笔的二级弹窗
    poco("软笔").click()
    touch((700,1200))
    #文本输入框输入内容后，点击撤回可撤回内容
    poco("Pen").click()
    agent_name="文本"
    text(agent_name,enter=False)
    poco("撤销").click()
    poco("撤销").click()
    #撤回文本输入框输入内容再点击重做按钮，可恢复撤回的内容
    poco("重做").click()
    poco("close").click()
    sleep(1)
    touch(Template(r"tpl1751523655968.png", record_pos=(-0.203, -0.366), resolution=(1600, 2560)))
#     poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()




#工具栏--删除便签
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("工具栏--删除便签")
@allure.title("工具栏--删除便签")
def test_delete_notes():
    if is_login()==True:
        login()
    poco(text="笔记").click()
    poco(text="便签").click()
    sleep(2)
    if poco(text="新建便签").exists():
        poco(text="新建便签").click()
    else:
        poco(text="新建笔记").click()
    poco("close").click()
    #在便签内删除便签，点击取消
    touch(Template(r"tpl1751523655968.png", record_pos=(-0.203, -0.366), resolution=(1600, 2560)))
#     poco("更多设置").click()
    poco(text="删除").click()
    poco(text="取消").click()
    #点击确认删除便签
    sleep(1)
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()








#画布左下角滑动/插入页面页面
@pytest.mark.skip
@pytest.mark.testcase
@allure.description("画布左下角滑动/插入页面页面")
@allure.title("画布左下角滑动/插入页面页面")
def test_delete_notes():
    if is_login()==True:
        login()
    poco(text="笔记").click()
    poco(text="便签").click()    
    poco(text="新建便签").click()
    #在第一页时，点击向左箭头，新增页面
    poco("前一页").click()
    #在中间页时，点击向左箭头
    poco("后一页").click()
    poco("后一页").click()
    poco("前一页").click()
    poco("前一页").click()
    #在中间页时，点击向右箭头
    poco("后一页").click()
    poco("后一页").click()
    poco("close").click()
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="全部笔记").click()
    poco(text="首页").click()





if __name__=="__main__":
    test_notes_on_drop_down_menu()
    # test_notes_on_note()
    test_check_notes_input()
    test_note_search()
    test_move_encrypt_sticky_notes()
    test_notes_editing_features()
    test_delete_notes()
