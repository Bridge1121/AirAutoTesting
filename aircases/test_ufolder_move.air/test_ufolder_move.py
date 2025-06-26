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

pytestmark = [allure.feature("移动文件模块用例"), allure.epic("办公本v2.4.0")]
    
    
#笔记列表同一分组下，文件夹移动至二级文件夹下验证
@pytest.mark.testcase
@allure.description("笔记列表同一分组下，文件夹移动至二级文件夹下验证")
@allure.title("笔记列表同一分组下，文件夹移动至二级文件夹下验证")
def test_move_folder_into_subfolder_in_same_group(default_group="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #点击默认笔记
    poco(text=default_group).click()
    #新建文件夹a,b
    for i in range(0,2):
        touch(Template(r"tpl1748249870254.png", record_pos=(0.048, -0.608), resolution=(1200, 1920)))
        #输入文件夹名
        name = f"同级文件夹_{i}"
        text(name, enter=False)
        sleep(1)
        poco(text="确认").click()
    #点击新建的第一个文件夹，创建三级文件夹
    poco(text="同级文件夹_0").click()
    touch(Template(r"tpl1748249870254.png", record_pos=(0.048, -0.608), resolution=(1200, 1920)))
    #输入文件夹名
    text("三级文件夹_0", enter=False)
    sleep(1)
    poco(text="确认").click()
    #点击返回到默认分组
    poco("<").click()
    #点击新建的第二个文件夹
    touch(Template(r"tpl1748311835817.png", record_pos=(0.459, -0.481), resolution=(1200, 1920)))

    #移动分组
    poco(text="移动分组").click()
    #点击默认分组
    poco(text=default_group).click()
    poco(text="同级文件夹_0").click()
    poco(text="移动至此").click()
    #点击新建的第一个文件夹
    poco(text="同级文件夹_0").click()
    sleep(1)
    #校验是否存在
    # assert poco(text="三级文件夹_0").exists()
    # assert poco(text="同级文件夹_1").exists()
    sleep(1)
    #返回
    poco("<").click()
    touch(Template(r"tpl1748311483114.png", record_pos=(0.457, -0.486), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #右滑
    swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    poco("首页").click()

    
#笔记列表不同分组文件夹移动至其他分组（根目录）验证
@pytest.mark.testcase
@allure.description("笔记列表不同分组文件夹移动至其他分组（根目录）验证")
@allure.title("笔记列表不同分组文件夹移动至其他分组（根目录）验证")
def test_move_folder_into_subfolder_in_diff_group(default_group="默认笔记",move_group="测试修改分组一"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #点击默认笔记
    poco(text=default_group).click()
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("search").click()
    text("笔记移动不同分组",enter=False)
    poco(text="确认").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="移动分组").click()
    poco(text=move_group).click()
    poco(text="移动至此").click()
    #点击移动到的分组
    poco(text="测试修改分组一").click()
    # assert poco(text="笔记移动不同分组").exists()
    sleep(1)
    #删除新建的文件夹
    touch(Template(r"tpl1748314038487.png", record_pos=(0.457, -0.483), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #右滑
    swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    poco("首页").click()


# 笔记列表不同分组文件夹移动至其他分组下二级文件夹目录验证（移动后该文件夹为第三级）
@pytest.mark.testcase
@allure.description("笔记列表不同分组文件夹移动至其他分组下二级文件夹目录验证（移动后该文件夹为第三级）")
@allure.title("笔记列表不同分组文件夹移动至其他分组下二级文件夹目录验证（移动后该文件夹为第三级）")
def test_move_folder_across_groups_into_subfolder_as_third_level(default_group="默认笔记",move_group="测试修改分组一"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #点击默认笔记
    poco(text=default_group).click()
    #新建文件夹
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("search").click()
    folder_name = f"文件夹_{random_string()}"
    text(folder_name,enter=False)
    poco(text="确认").click()
    #点击新建的文件夹
    poco(text=folder_name).click()
    #新建5篇笔记
    note_name = None
    for i in range(0,5):
        poco(text="新建笔记").click()
        poco("更多设置").click()
        poco(text="插入文字").click()
        sleep(2)
        touch((581,997))
        sleep(2)
        ran_str = random_string()
        note_name=f"笔记_{ran_str}"
        text(note_name, enter=False)
        poco("返回").click()
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].click()
    poco(text="全部选中").click()
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1].child("android.widget.Button").click()
    poco(text=move_group).click()
    poco(text="移动至此").click()
    sleep(1)
    poco("<").click()
    #右滑
    swipe((279,89),(920,89))
    #点击到该分组下，校验是否存在
#     poco(text=move_group).click()
#     sleep(1)
#     assert poco(text=note_name).exists()
#     sleep(1)
    #右滑
    swipe((279,89),(920,89))
    poco(text="全部笔记").click()
    poco("首页").click()
    







# 笔记列表文件夹批量移动验证
@pytest.mark.testcase
@allure.description("笔记列表文件夹批量移动验证")
@allure.title("笔记列表文件夹批量移动验证")
def test_folders_move(default_group="默认笔记",move_group="测试修改分组一"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #点击默认笔记
    poco(text=default_group).click()
    file_name=None
    #新建多个文件夹
    for i in range(0,3):
        poco("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View").child("android.view.View")\
        .child("android.view.View")[4].child("search").click()
        file_name = f"文件夹_{i}{i}"
        text(file_name,enter=False)
        poco(text="确认").click()
    #批量选择
    poco("编辑").click()
    for i in range(0,3):
        poco("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View").child("android.view.View")\
        .child("android.view.View")[4].child("android.view.View")\
        .child("android.view.View")[i].click()
    poco(text="移动至").click()
    poco(text=move_group).click()
    poco(text="移动至此").click()
    sleep(1)
    #点击到该分组下，校验是否存在
    poco(text=move_group).click()
    # assert poco(text=file_name).exists()
    sleep(1)
    #右滑
    swipe((279,89),(920,89))
    poco(text="全部笔记").click()
    poco("首页").click()




  


    
    
    
# if __name__=="__main__":
#     test_move_folder_into_subfolder_in_same_group()
#     test_move_folder_into_subfolder_in_diff_group()
#     test_move_folder_across_groups_into_subfolder_as_third_level()
#     test_folders_move()