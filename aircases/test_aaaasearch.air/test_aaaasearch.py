# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"

import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *


auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))


def del_file():
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()

    
# 点击搜索后跳转到新页面覆盖列表页，模糊搜索，下滑翻页    
def test_note_search_and_open():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #点击搜索
    poco("search").click()
    #输入搜索内容，模糊搜索
    sleep(2)
    text("测试", enter=False)
    sleep(2)
    #校验是否存在AI搜索、笔记、文件三个tab页签
    assert poco(text="AI搜索").exists()
    assert poco(text="笔记").exists()
    assert poco(text="文件").exists()
    assert poco(text="待办").exists()
    sleep(1)
    #下滑查看找到的所有笔记
    swipe((514,1619),(460,405))
    #返回
    
    poco("Back").click()
    #点击首页
    poco("首页").click()
    
#输入文件名称搜索    
def test_file_search():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    note_name=None
    #点击两个新建笔记
    for i in range(0,2):
        poco(text="新建笔记").click()
        #输入笔记内容
        sleep(1)
        poco("更多设置").click()
        poco(text="插入文字").click()
        sleep(2)
        touch((581,997))
        sleep(2)
        note_name = f"搜索笔记_{i}"
        text(note_name, enter=False)
        poco("返回").click()
        sleep(1)
    #点击搜索
    poco("search").click()
    #输入搜索内容，模糊搜索
    sleep(2)
    text("搜索",enter=False)
    poco(text="笔记").click()
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].child("android.view.View")\
    .child("android.view.View")[0]\
    .child("android.widget.TextView")[0].click()
    poco("返回").click()
    #返回
    poco("Back").click()
    for i in range(0,2):
        del_file()
    #点击首页
    poco("首页").click()

# 输入对应笔记标题搜索后进入详情页
def test_note_search_and_open(title="测试"):
    # if is_login()==True:
    #     login()
    #点击笔记
    poco("笔记").click()
    #点击搜索
    poco("search").click()
    #输入搜索内容，模糊搜索
    sleep(2)
    text(title, enter=False)
    #点击某一笔记
    poco(text=title).click()
    sleep(1)
    #返回
    poco("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[2].click()
    #返回
    poco("Back").click()
    #点击首页
    poco("首页").click()


    

    
    
if __name__=="__main__":
    test_note_search_and_open()
    test_file_search()
    test_note_search_and_open()