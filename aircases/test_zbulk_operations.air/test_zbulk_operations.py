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

pytestmark = [allure.feature("文件批量处理模块用例"), allure.epic("办公本v2.4.0")]
    
    
# 批量处理入口，第一行显示全选/取消全选、移动、删除、退出按钮，全选框未勾选时，移动、删除按钮不可点击，点击退出批量处理按钮，退出批量处理模式，最后执行
@pytest.mark.testcase
@allure.description("批量处理入口，第一行显示全选/取消全选、移动、删除、退出按钮，全选框未勾选时，移动、删除按钮不可点击，点击退出批量处理按钮，退出批量处理模式，最后执行")
@allure.title("批量处理入口，第一行显示全选/取消全选、移动、删除、退出按钮，全选框未勾选时，移动、删除按钮不可点击，点击退出批量处理按钮，退出批量处理模式，最后执行")
def test_batch_processing_portals():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #点击批量操作
    poco("编辑").click()
    #校验是否存在全选/取消全选、移动、删除、退出按钮
    assert poco(text="全部选中").exists()
    assert poco(text="移动至").exists()
    assert poco(text="删除").exists()
    assert poco(text="退出").exists()
    sleep(1)
    #点击退出
    poco(text="退出").click()
    poco("首页").click()

    
# 批量移动，全选移动，最后执行
@pytest.mark.testcase
@allure.description("批量移动，全选移动，最后执行")
@allure.title("批量移动，全选移动，最后执行")
def test_batch_move():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建一个笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name="批量移动笔记1"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(2)
    #点击批量操作
    poco("编辑").click()
    #点击全选
    poco(text="全部选中").click()
    poco(text="移动至").click()
    #弹窗新建文件
    poco(text="新建文件夹").click()
    folder_name = "弹窗新建123"
    text(folder_name, enter=False)
    poco(text="确认").click()
    #上滑
    for i in range(0,1):
        swipe((477,1150),(477,640))
    #点击，将新建的笔记移动到其中
    sleep(1)
    poco(text=folder_name).click()
    poco(text="移动至此").click()
    sleep(3)
    #点击新建的分组
    #分组栏左滑
    for i in range(0,2):
        swipe((947,85),(184,88))
    sleep(2)
    poco(text=folder_name).click()
    sleep(1)
#     校验是否存在移动的笔记
#     assert poco(text=note_name).exists()
    #右滑
    for i in range(0,2):
        swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    #删除创建的分组
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("show catalogs").click()
    find_group_by_name_and_del(folder_name)
    poco(desc="").click()
    #返回首页
    poco("首页").click()


    
    
# 全选删除，取消未删除，确认后全部删除，最后执行
@pytest.mark.testcase
@allure.description("全选删除，取消未删除，确认后全部删除，最后执行")
@allure.title("全选删除，取消未删除，确认后全部删除，最后执行")
def test_batch_del():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建多个笔记
    note_name = None
    for i in range(0,3):
        poco(text="新建笔记").click()
        sleep(2)
        poco("更多设置").click()
        poco(text="插入文字").click()
        sleep(2)
        touch((581,997))
        sleep(2)
        note_name=f"批量删除笔记_{i}{i}"
        text(note_name, enter=False)
        poco("返回").click()
        sleep(2)
    #点击批量操作
    poco("编辑").click()
    #点击全选删除
    poco(text="全部选中").click()
    poco(text="删除").click()
    #点击取消
    poco(text="取消").click()
    poco(text="退出").click()
    sleep(1)
    #验证笔记未被删除
    # assert poco(text=note_name).exists()
    #点击批量操作
    # poco("编辑").click()
    # #点击全选删除
    # poco(text="全部选中").click()
    # poco(text="删除").click()
    # #点击确认
    # poco(text="确认").click()
    # sleep(1)
    # assert not poco(text=note_name).exists()
    poco("首页").click()

    
    
# 点击批量处理,勾选列表中单条笔记的选择框后，可删除
@pytest.mark.testcase
@allure.description("点击批量处理,勾选列表中单条笔记的选择框后，可删除")
@allure.title("点击批量处理,勾选列表中单条笔记的选择框后，可删除")
def test_batch_single_note_del():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(2)
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name="勾选删除一条笔记"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(2)
    #点击批量操作
    poco("编辑").click()
    #勾选第一条，删除
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4]\
    .child("android.view.View").child("android.view.View")\
    .child("android.widget.TextView")[0].click()
    poco(text="删除").click()
    poco(text="确认").click()
    #校验是否删除
    # assert not poco(text=note_name).exists()
    poco("首页").click()


# 依次勾选列表中的每条笔记的勾选框，最后执行
@pytest.mark.testcase
@allure.description("依次勾选列表中的每条笔记的勾选框，最后执行")
@allure.title("依次勾选列表中的每条笔记的勾选框，最后执行")
def test_batch_check_note_del():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建多个笔记
    note_name = None
    for i in range(0,3):
        poco(text="新建笔记").click()
        sleep(2)
        poco("更多设置").click()
        poco(text="插入文字").click()
        sleep(2)
        touch((581,997))
        sleep(2)
        note_name=f"批量删除笔记_{i}{i}"
        text(note_name, enter=False)
        poco("返回").click()
        sleep(2)
    #点击批量操作
    poco("编辑").click()
    #依次勾选
    list = poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4]\
    .child("android.view.View").children()
    for i in range(len(list)):
        list[i].click()
    poco(text="删除").click()
    poco(text="确认").click()
    #校验是否全部删除
    assert poco(text="暂无文件").exists()
    poco("首页").click()



    
if __name__ == "__main__":
    test_batch_processing_portals()
    test_batch_move()#还没调试好
    test_batch_del()
    test_batch_single_note_del()
    test_batch_check_note_del()
    test_batch_check_note_del()




