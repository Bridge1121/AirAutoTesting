# -*- encoding=utf8 -*-
import sys

import allure
import pytest
from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))


pytestmark = [allure.feature("文件传输模块用例"), allure.epic("办公本v2.4.0")]
    
    
#遍历列表，找到一个指定后缀名的大文件
def find_index_of_big_docx(dir_list,suffix="docx"):
    
    for i in range(len(dir_list)):
        node_text = dir_list[i].child("android.widget.LinearLayout")\
                .child("android.widget.LinearLayout")\
                .offspring("android:id/title").get_text()
        print(node_text)
        if node_text.endswith(suffix):
            return i
    return -1

    
    
    
    
#连接wifi时，微信已绑定文件传输，从微信端选择多种格式的文件发送到办公本
@pytest.mark.testcase
@allure.description("连接wifi时，微信已绑定文件传输，从微信端选择多种格式的文件发送到办公本")
@allure.title("连接wifi时，微信已绑定文件传输，从微信端选择多种格式的文件发送到办公本")
def test_wifi_wechat_file_transfer():
    if is_login()==True:
        login()
    poco("文件").click()
    #点击微信传输
    poco(text="微信传输").click()
    sleep(1)
    if poco(text="微信未绑定").exists():
        #没有绑定微信，直接返回
        poco("返回").click()
        poco("首页").click()
    else:
        #已经绑定微信，可以传输文件
        #返回打开微信，选择文件传输
        poco("返回").click()
        poco("应用").click()
        #打开微信
        poco("微信图标").click()
        #打开微信传输助手
        sleep(2)
        poco(text="文件传输助手").click()
        #选择文件传输
        sleep(2)
        poco("com.tencent.mm:id/bjz").click()
        #点击文件
        poco(text="文件").click()
        sleep(1)
        poco("com.tencent.mm:id/ot").click()
        sleep(1)
        poco(text="手机存储").click()
        #选择导出文件
        poco(text="导出文件").click()
        sleep(3)
        for i in range(5):
            if exists(Template(r"tpl1750402574412.png", record_pos=(0.449, -0.648), resolution=(1200, 1920))):
                touch(Template(r"tpl1750402574412.png", record_pos=(0.449, -0.648), resolution=(1200, 1920)))
        poco("com.tencent.mm:id/fp").click()
        sleep(1)
        file_list = poco("android.widget.FrameLayout")\
        .child("android.widget.LinearLayout")\
        .offspring("com.tencent.mm:id/jlt")\
        .offspring("com.tencent.mm:id/bki")\
        .child("android.widget.FrameLayout")\
        .offspring("com.tencent.mm:id/bp0")[0]\
        .child("com.tencent.mm:id/bn1")
        for f in file_list:
            if f.offspring("com.tencent.mm:id/a1l")\
            .offspring("com.tencent.mm:id/biy")\
            .child("android.widget.LinearLayout")\
            .offspring("com.tencent.mm:id/bju").get_text().endswith("docx"):
                f.offspring("com.tencent.mm:id/bjy").click()
                break
        #保存到本地
        #文件
        if poco("com.tencent.mm:id/pt0").exists():
            poco("com.tencent.mm:id/pt0").click()
            poco(text="保存").click()
            #返回
            poco("com.tencent.mm:id/pt7").click()
        else:#图片
            poco("com.tencent.mm:id/fq").click()
            sleep(1)
            poco(text="保存到手机").click()
            poco("com.tencent.mm:id/hf").click()
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
#         #上滑退出
#         swipe((600,1900),(600,1500))
#         sleep(1)
#         touch(((600,1800)))
        poco("首页").click()
    
    
#确认删除未下载文件未勾选同时删除本地文件，长按删除已下载的文件
@pytest.mark.testcase
@allure.description("确认删除未下载文件未勾选同时删除本地文件，长按删除已下载的文件")
@allure.title("确认删除未下载文件未勾选同时删除本地文件，长按删除已下载的文件")
def test_wifi_wechat_long_click_del():
    if is_login()==True:
        login()
    poco("文件").click()
    #点击微信传输
    poco(text="微信传输").click()
    sleep(1)
    if poco(text="微信未绑定").exists():
        #没有绑定微信，直接返回
        poco("返回").click()
        poco("首页").click()
    else:
        #已经绑定微信，可以传输文件
        #返回打开微信，选择文件传输
        poco("返回").click()
        poco("应用").click()
        #打开微信
        poco("微信图标").click()
        #打开微信传输助手
        sleep(2)
        poco(text="文件传输助手").click()
        #选择文件传输
        sleep(2)
        poco("com.tencent.mm:id/bjz").click()
        #点击文件
        poco(text="文件").click()
        sleep(1)
        poco("com.tencent.mm:id/ot").click()
        sleep(1)
        poco(text="手机存储").click()
        #选择导出文件
        poco(text="导出文件").click()
        sleep(3)
        for i in range(2):
            if exists(Template(r"tpl1750402574412.png", record_pos=(0.449, -0.648), resolution=(1200, 1920))):
                touch(Template(r"tpl1750402574412.png", record_pos=(0.449, -0.648), resolution=(1200, 1920)))
        poco("com.tencent.mm:id/fp").click()
        sleep(1)
        #长按删除未下载的文件
        #长按
        touch((800,1696),duration=2)
        #点击删除
        sleep(1)
        poco(text="删除").click()
        sleep(1)
        poco("com.tencent.mm:id/jln").click()
        sleep(1)
        #长按删除已下载的文件
        touch((800,1696))
        sleep(5)
        #保存到本地
        #文件
        if poco("com.tencent.mm:id/pt0").exists():
            poco("com.tencent.mm:id/pt0").click()
            poco(text="保存").click()
            #返回
            poco("com.tencent.mm:id/pt7").click()
        else:#图片
            poco("com.tencent.mm:id/fq").click()
            sleep(1)
            poco(text="保存到手机").click()
            poco("com.tencent.mm:id/hf").click()
        #长按
        touch((800,1696),duration=2)
        #删除
        poco(text="删除").click()
        sleep(1)
        poco("com.tencent.mm:id/jln").click()
        #返回
        poco("com.tencent.mm:id/a4p").click()
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        poco("首页").click()

        



        
            
#         file_list = poco("com.tencent.mm:id/nsv")\
#         .child("android.widget.FrameLayout")\
#         .child("android.widget.LinearLayout")\
#         .offspring("android:id/content")\
#         .offspring("com.tencent.mm:id/gde")\
#         .offspring("com.tencent.mm:id/hwa")\
#         .child("android.widget.FrameLayout")\
#         .offspring("com.tencent.mm:id/hw_")[1]\
#         .offspring("com.tencent.mm:id/e24")\
#         .child("android.widget.RelativeLayout")
#         if len(file_list)>0:
#             file_list[0].child("more icon").click()
#             for f in file_list:
#                 if f.offspring("com.tencent.mm:id/hjn").get_text().endswith("docx"):
#                     #点击选择
#                     f.child("com.tencent.mm:id/hje").click()
        

        
        
def test():
    
    file_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.tencent.mm:id/jlt")\
    .offspring("com.tencent.mm:id/bki")\
    .child("android.widget.FrameLayout")\
    .offspring("com.tencent.mm:id/bp0")[0]\
    .child("com.tencent.mm:id/bn1")
    for f in file_list:
        if f.offspring("com.tencent.mm:id/a1l")\
        .offspring("com.tencent.mm:id/biy")\
        .child("android.widget.LinearLayout")\
        .offspring("com.tencent.mm:id/bju").get_text().endswith("docx"):
            f.offspring("com.tencent.mm:id/bjy").click()
            break

    
#     if exists(Template(r"tpl1750402574412.png", record_pos=(0.449, -0.648), resolution=(1200, 1920))):
#             touch(Template(r"tpl1750402574412.png", record_pos=(0.449, -0.648), resolution=(1200, 1920)))
#     poco("com.tencent.mm:id/nsv").wait_for_appearance(timeout=10)
#     file_list = poco("com.tencent.mm:id/nsv")\
#     .child("android.widget.FrameLayout")\
#     .child("android.widget.LinearLayout")\
#     .offspring("android:id/content")\
#     .offspring("com.tencent.mm:id/gde")\
#     .offspring("com.tencent.mm:id/hwa")\
#     .child("android.widget.FrameLayout")\
#     .offspring("com.tencent.mm:id/hw_")[1]\
#     .offspring("com.tencent.mm:id/e24")\
#     .child("android.widget.RelativeLayout")
#     if len(file_list)>0:
#         file_list[0].child("more icon").click()
#         for f in file_list:
#             if f.offspring("com.tencent.mm:id/hjn").get_text().endswith("docx"):
#                 #点击选择
#                 f.child("com.tencent.mm:id/hje").click()
        



#微信传输确认删除已下载成功文件
@pytest.mark.testcase
@allure.description("微信传输确认删除已下载成功文件")
@allure.title("微信传输确认删除已下载成功文件")
def test_wechat_transfer_del():
    if is_login()==True:
        login()
    poco("文件").click()
    poco(text="微信传输").click()
    sleep(1)
    file_list = poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[2]\
    .child("android.view.View")
    if len(file_list)>0:
        #删除第一个文件
        file_list[0].child("more icon").click()
        #点击删除
        poco(text="删除").click()
        poco(text="确认").click()
        poco("返回").click()
    else:
        #没有下载成功的文件，直接返回
        poco("返回").click()
    poco("首页").click()
    
    
    
#微信传输已下载文件移至书架
@pytest.mark.testcase
@allure.description("微信传输已下载文件移至书架")
@allure.title("微信传输已下载文件移至书架")
def test_wechat_download_move_to_bookshelf():
    if is_login()==True:
        login()
    poco("文件").click()
    poco(text="微信传输").click()
    sleep(1)
    file_list = poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[2]\
    .child("android.view.View")
    if len(file_list)>0:
        #点击更多，移动至书架
        for f in file_list:
            
            if f.child("android.widget.TextView")[0].get_text().endswith("docx"):
#                 print(f.child("android.widget.TextView")[0].get_text())
                #点击更多
                f.child("more icon").click()
                poco(text="加入书架").click()
                break
        poco("返回").click()
        poco("首页").click()

#导出笔记至文件传输-打开目录
@pytest.mark.testcase
@allure.description("导出笔记至文件传输-打开目录")
@allure.title("导出笔记至文件传输-打开目录")
def test_note_export():
    if is_login()==True:
        login()
    #新建笔记
    #点击笔记
    poco("笔记").click()
    #点击新建笔记
    poco(text="新建笔记").click()
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name="导出笔记"
    text(note_name, enter=False)
    sleep(1)
    poco("更多设置").click()
    poco(text="分享笔记").click()
    poco(text="导出文件").wait_for_appearance(timeout=100)
    poco(text="导出文件").click()
    sleep(2)
    poco(text="保存到本地").click()
    poco("android.widget.FrameLayout")\
    .offspring("android.view.ViewGroup")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[0]\
    .child("android.widget.Button").click()
    poco("返回").wait_for_appearance(timeout=TIME_OUT)
    poco("返回").click()
    #删除创建的笔记
    wait(Template(r"tpl1750409220183.png", record_pos=(0.461, -0.492), resolution=(1200, 1920)),timeout=100)
    touch(Template(r"tpl1750409220183.png", record_pos=(0.461, -0.492), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()




    

if __name__=="__main__":
    test_wechat_transfer_del()
#     test_wifi_wechat_file_transfer()
    test_wifi_wechat_long_click_del()
    test_wechat_download_move_to_bookshelf()
    test_note_export()
#     test()
    
    
    
