# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"

import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *


auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))
    
# 回收站列表ui默认展示    
def test_recycle_bin_list():
    # if is_login()==True:
    #     login()
    #点击笔记
    poco("笔记").click()
    #点击回收站
    poco("show recycle").click()
    #返回
    poco("<").click()
    poco("首页").click()

# 非文件夹内新建笔记删除功能验证（全部笔记tab下）
def test_del_note_not_in_folder():
    # if is_login()==True:
    #     login()
    #点击笔记
    poco("笔记").click()
    #新建笔记
    timestamp = create_new_notes()
    #点击笔记
    poco("笔记").click()
    #点击更多
    touch(Template(r"tpl1748318230851.png", record_pos=(0.459, -0.487), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)
    poco("show recycle").click()
    #上滑
    swipe((638,1628),(638,400))
    #返回
    poco("<").click()
    poco("首页").click()
    
# 文件夹内笔记删除功能验证
def test_del_note_in_folder(default_group="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #点击默认分组
    poco(text=default_group).click()
    #新建文件夹
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].click()
    folder_name = "删除笔记"
    text(folder_name,enter=False)
    poco(text="确认").click()
    #点击新建的文件夹
    poco(text=folder_name).click()
    #新建笔记
    poco(text="新建笔记").click()
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    timestamp = time.strftime("%Y%m%d%H%M%S")  # 年月日时分秒
    text(timestamp, enter=False)
    poco("返回").click()
    sleep(1)
    #点击删除
    touch(Template(r"tpl1748318230851.png", record_pos=(0.459, -0.487), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #返回
    poco("<").click()
    #删除新建文件夹
    touch(Template(r"tpl1748318230851.png", record_pos=(0.459, -0.487), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #点击回收站查看
    poco("show recycle").click()
    for i in range(0,5):
        swipe((651,1735),(651,300))
    sleep(1)
    #返回
    poco("<").click()
    #右滑
    swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    poco("首页").click()

    
# 笔记列表，笔记批量删除，回收站可查看验证
def test_del_notes_in_folder(default_group="默认笔记"):
    # if is_login()==True:
    #     login()
    #点击笔记
    poco("笔记").click()
    #点击默认分组
    poco(text=default_group).click()
    #新建文件夹
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].click()
    folder_name = "批量删除笔记"
    text(folder_name,enter=False)
    poco(text="确认").click()
    #点击新建的文件夹
    poco(text=folder_name).click()
    #新建3篇笔记
    for i in range(0,3):
        poco(text="新建笔记").click()
        poco("返回").click()
    #批量删除
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].click()
    poco(text="全部选中").click()
    poco(text="删除").click()
    poco(text="确认").click()
    #返回
    poco("<").click()
    #查看回收站
    poco("show recycle").click()
    for i in range(0,5):
        swipe((651,1735),(651,300))
        sleep(1)
    #返回
    poco("<").click()
    #删除创建的文件夹
    touch(Template(r"tpl1748318230851.png", record_pos=(0.459, -0.487), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #右滑
    swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    poco("首页").click()
    
    
# 查看删除文件夹
def test_del_folder(default_group="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #点击默认分组
    poco(text=default_group).click()
    #新建文件夹
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].click()
    folder_name = "删除文件夹"
    text(folder_name,enter=False)
    poco(text="确认").click()
    #删除新建的文件夹
    # poco("androidx.compose.ui.platform.ComposeView")\
    # .child("android.view.View").child("android.view.View")\
    # .child("android.view.View")[10].child("android.view.View")\
    # .child("android.view.View")[0].offspring("更多设置").click()
    # poco(text="删除").click()
    # poco(text="确认").click()
    # #进入回收站
    # poco("show recycle").click()
    # sleep(1)
    # assert_exists(Template(r"tpl1748326572074.png", record_pos=(-0.152, -0.59), resolution=(1200, 1920)), "校验是否成功删除文件夹")
    # sleep(1)
    # #返回
    # poco("<").click()
    #右滑
    swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    poco("首页").click()

    
   
# 笔记列表，文件夹批量删除，回收站可查看验证
def test_del_folders(default_group="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #点击默认分组
    poco(text=default_group).click()
    #新建多个文件夹
    for i in range(0,3):
        touch(Template(r"tpl1748249870254.png", record_pos=(0.048, -0.608), resolution=(1200, 1920)))
        #输入文件夹名
        name = f"文件夹_{i}"
        text(name, enter=False)
        sleep(1)
        poco(text="确认").click()
    #点击多选
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[7].click()
    for i in range(0,3):
        poco("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View").child("android.view.View")\
        .child("android.view.View")[4].child("android.view.View")\
        .child("android.view.View")[i].click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco("show recycle").click()
    sleep(1)
    #返回
    poco("<").click()
    #右滑
    swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    poco("首页").click()
    




    
    
if __name__=="__main__":
    test_recycle_bin_list()
    test_del_note_not_in_folder()
    test_del_note_in_folder()
    test_del_notes_in_folder()
    test_del_folder()
    test_del_folders()
    
