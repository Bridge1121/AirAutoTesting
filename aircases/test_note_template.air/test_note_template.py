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

pytestmark = [allure.feature("笔记模板模块用例"), allure.epic("办公本v2.4.0")]
    
#默认模版二次确认弹窗点击确认，默认模版设置生效校验
@pytest.mark.testcase
@allure.description("默认模版二次确认弹窗点击确认，默认模版设置生效校验")
@allure.title("默认模版二次确认弹窗点击确认，默认模版设置生效校验")
def test_note_default_tempalte_confirm_take_effect():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    sleep(1)
    poco(text="更改模板").click()
    #更改默认模板
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View").child("更多设置")[0].click()
    #点击设为默认
    poco("android.widget.TextView").click()
    poco(text="确认").click()
    sleep(1)
    poco(text="确认").click()
    sleep(1)
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #再次新建笔记
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
    
#默认模版二次确认弹窗点击取消，默认模版设置不生效校验
@pytest.mark.testcase
@allure.description("默认模版二次确认弹窗点击取消，默认模版设置不生效校验")
@allure.title("默认模版二次确认弹窗点击取消，默认模版设置不生效校验")
def test_note_default_template_cancel():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    sleep(1)
    poco(text="更改模板").click()
    #更改默认模板
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View").child("更多设置")[0].click()
    #点击设为默认
    poco("android.widget.TextView").click()
    poco(text="取消").click()
    #退出
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[3].child("返回").click()
    #点击返回
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
    

#设置默认模版后不影响 现有笔记已设置的模版校验
@pytest.mark.testcase
@allure.description("设置默认模版后不影响 现有笔记已设置的模版校验")
@allure.title("设置默认模版后不影响 现有笔记已设置的模版校验")
def test_note_template_config():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记a
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    sleep(2)
    poco(text="插入文字").click()
    touch((581,997))
    sleep(2)
    note_name1="方格纸"
    text(note_name1, enter=False)
    #设置模板为方格纸
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    poco("模板-方格纸").click()
    poco(text="确认").click()
    poco("返回").click()
    #新建笔记b
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name2="点阵纸"
    text(note_name2, enter=False)
    #设置模板为点阵纸
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    poco("模板-点阵纸").click()
    poco(text="确认").click()
    poco("返回").click()
    #新建笔记c，设置默认模板为空白，查看笔记a和b
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name3="空白纸"
    text(note_name3, enter=False)
    #设置默认模板为空白纸
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    sleep(1)
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View").child("更多设置")[0].click()
    poco("android.widget.TextView").click()
    poco(text="确认").click()
    poco(text="确认").click()
    sleep(1)
    poco("返回").click()
    #查看笔记a和b
    poco(text=note_name1).click()
    sleep(1)
    poco("返回").click()
    poco(text=note_name2).click()
    sleep(1)
    poco("返回").click()
    #删除创建的笔记
    for i in range(3):
        touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
        poco(text="删除").click()
        poco(text="确认").click()
    poco("首页").click()

    
    

#新建笔记首次进入笔记系统模版默认模版为“行距纸”校验
@pytest.mark.testcase
@allure.description("新建笔记首次进入笔记系统模版默认模版为“行距纸”校验")
@allure.title("新建笔记首次进入笔记系统模版默认模版为“行距纸”校验")
def test_note_default_template():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(2)
    #将默认笔记设置为行距纸
    poco("更多设置").wait_for_appearance(timeout=TIME_OUT)
    poco("更多设置").click()
    poco(text="更改模板").click()
    sleep(1)
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View").child("更多设置")[1].click()
    poco("android.widget.TextView").click()
    poco(text="确认").click()
    poco(text="确认").click()
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

    
    
#自定义模版tab首位为模版导入入口校验，自定义模版首位显示支持导入模版的格式（jpg、png、bmp）校验
@pytest.mark.testcase
@allure.description("自定义模版tab首位为模版导入入口校验，自定义模版首位显示支持导入模版的格式（jpg、png、bmp）校验")
@allure.title("自定义模版tab首位为模版导入入口校验，自定义模版首位显示支持导入模版的格式（jpg、png、bmp）校验")
def test_note_template_customize_portal_and_export_jpg_and_png():
#     if is_login()==True:
#         login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    #点击自定义模板
    poco(text="自定义模板").click()
    sleep(1)
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View").child("android.view.View").click()
    sleep(4)
    #点击根目录
#     touch(Template(r"tpl1750840211269.png", record_pos=(-0.44, -0.725), resolution=(1200, 1920)))
#     touch(Template(r"tpl1750830649319.png", record_pos=(-0.437, -0.725), resolution=(1200, 1920)))
#     poco("显示根目录").wait_for_appearance(timeout=TIME_OUT)
    poco("显示根目录").click()
    sleep(1)
    #点击图片
    touch((168,324))
#     poco(text="图片").click()
#     poco("android.widget.FrameLayout")\
#     .child("android.widget.LinearLayout")\
#     .offspring("com.android.documentsui:id/roots_list")\
#     .child("android.widget.LinearLayout")[1]\
#     .offspring("android:id/title").click()

    if exists(Template(r"tpl1750821729163.png", record_pos=(0.422, -0.472), resolution=(1200, 1920))):
        touch(Template(r"tpl1750821729163.png", record_pos=(0.422, -0.472), resolution=(1200, 1920)))
    sleep(2)
    #右滑返回
    swipe((3,900),(200,900))
    poco(text="CameraAISpeech").wait_for_appearance(timeout=TIME_OUT)
    poco(text="CameraAISpeech").click()
    #选择jpg图片
    pic_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.android.documentsui:id/drawer_layout")\
    .child("android.widget.ScrollView")\
    .offspring("com.android.documentsui:id/container_directory")\
    .offspring("com.android.documentsui:id/dir_list")\
    .child("com.android.documentsui:id/item_root")
    if pic_list and len(pic_list)>0:
        for p in pic_list:
            if p.child("android.widget.LinearLayout")\
            .child("android.widget.LinearLayout")\
            .offspring("android:id/title").get_text().endswith("jpg"):
                p.click()
                break
        poco("应用裁切").click()
    else:
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
    #点击关闭按钮
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[3]\
    .child("返回").click()
    #再次点击，导入png图片
    poco("更多设置").click()
    poco(text="更改模板").click()
    poco(text="自定义模板").click()
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View")\
    .child("android.view.View").click()
    poco("显示根目录").click()
    #点击图片
    touch((168,324))
#     poco("android.widget.FrameLayout")\
#     .child("android.widget.LinearLayout")\
#     .offspring("com.android.documentsui:id/roots_list")\
#     .child("android.widget.LinearLayout")[1]\
#     .offspring("android:id/title").click()
    sleep(1)
    poco(text="导出文件").click()
    png_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.android.documentsui:id/drawer_layout")\
    .child("android.widget.ScrollView")\
    .offspring("com.android.documentsui:id/container_directory")\
    .offspring("com.android.documentsui:id/dir_list")\
    .child("com.android.documentsui:id/item_root")
    if png_list and len(png_list)>0:
        for p in png_list:
            if p.child("android.widget.LinearLayout")\
            .child("android.widget.LinearLayout")\
            .offspring("android:id/title").get_text().endswith("png"):
                p.click()
                break
        poco("应用裁切").click()
        
    else:
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
    poco(text="确认").click()
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

   
    

    
    
#图片编辑页裁剪比例可调整校验，
@pytest.mark.testcase
@allure.description("图片编辑页裁剪比例可调整校验")
@allure.title("图片编辑页裁剪比例可调整校验")
def test_note_template_cropping():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    #点击自定义模板
    poco(text="自定义模板").click()
    sleep(1)
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View").child("android.view.View").click()
    sleep(2)
    #点击根目录
    poco("显示根目录").click()
    sleep(1)
    #点击图片
    touch((168,324))
    sleep(1)
    poco(text="导出文件").click()
    png_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.android.documentsui:id/drawer_layout")\
    .child("android.widget.ScrollView")\
    .offspring("com.android.documentsui:id/container_directory")\
    .offspring("com.android.documentsui:id/dir_list")\
    .child("com.android.documentsui:id/item_root")
    if png_list and len(png_list)>0:
        for p in png_list:
            if p.child("android.widget.LinearLayout")\
            .child("android.widget.LinearLayout")\
            .offspring("android:id/title").get_text().endswith("png"):
                p.click()
                break
        #拖动进行裁切
#         touch((653,817))
        swipe_press_ai((1109,1745),(507,1057))
#         swipe((1106,1745),(807,1257))
        poco("应用裁切").click()
        
    else:
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
    poco(text="确认").click()
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
    
#图片编辑页点击右上角取消按钮，图片导入失败校验
@pytest.mark.testcase
@allure.description("图片编辑页点击右上角取消按钮，图片导入失败校验")
@allure.title("图片编辑页点击右上角取消按钮，图片导入失败校验")
def test_note_template_cropping_cancel():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    #点击自定义模板
    poco(text="自定义模板").click()
    sleep(1)
    if poco("模板-空白").exists():
        poco("模板-空白").click()
    else:
        poco("android.widget.LinearLayout")\
        .offspring("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View")\
        .child("android.view.View")\
        .child("android.view.View")[7]\
        .child("android.view.View").child("android.view.View").click()
    sleep(2)
    #点击根目录
    poco("显示根目录").click()
    sleep(1)
    #点击图片
    touch((168,324))
    sleep(1)
    poco(text="导出文件").click()
    png_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.android.documentsui:id/drawer_layout")\
    .child("android.widget.ScrollView")\
    .offspring("com.android.documentsui:id/container_directory")\
    .offspring("com.android.documentsui:id/dir_list")\
    .child("com.android.documentsui:id/item_root")
    if png_list and len(png_list)>0:
        for p in png_list:
            if p.child("android.widget.LinearLayout")\
            .child("android.widget.LinearLayout")\
            .offspring("android:id/title").get_text().endswith("png"):
                p.click()
                break
        #拖动进行裁切
#         touch((653,817))
#         swipe_press_ai((1109,1745),(507,1057))
#         swipe((1106,1745),(807,1257))
        poco("取消裁切").click()
        
    else:
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
    poco(text="确认").click()
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    

#自定义模版列表模版倒序排列显示校验，点击更多，查看操作
@pytest.mark.testcase
@allure.description("自定义模版列表模版倒序排列显示校验，点击更多，查看操作")
@allure.title("自定义模版列表模版倒序排列显示校验，点击更多，查看操作")
def test_note_customize_template_desc_and_del():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    #点击自定义模板
    poco(text="自定义模板").click()
    sleep(3)
    #导入新的图片
    if poco("模板-空白").exists():
        poco("模板-空白").click()
    else:
        poco("android.widget.LinearLayout")\
        .offspring("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View")\
        .child("android.view.View")\
        .child("android.view.View")[7]\
        .child("android.view.View").child("android.view.View").click()
    sleep(2)
    #点击根目录
    poco("显示根目录").click()
    sleep(1)
    #点击图片
    touch((168,324))
    sleep(1)
    poco(text="导出文件").click()
    png_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.android.documentsui:id/drawer_layout")\
    .child("android.widget.ScrollView")\
    .offspring("com.android.documentsui:id/container_directory")\
    .offspring("com.android.documentsui:id/dir_list")\
    .child("com.android.documentsui:id/item_root")
    if png_list and len(png_list)>0:
        for p in png_list:
            if p.child("android.widget.LinearLayout")\
            .child("android.widget.LinearLayout")\
            .offspring("android:id/title").get_text().endswith("png"):
                p.click()
                break
        #拖动进行裁切
#         touch((653,817))
        swipe_press_ai((1109,1745),(507,1057))
#         swipe((1106,1745),(807,1257))
        poco("应用裁切").click()
        
    else:
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
    #点击更多校验操作
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View").child("更多设置")[0].click()
    sleep(1)
    #点击删除
    poco(text="删除").click()
    #弹窗点击取消
    poco(text="取消").click()
    sleep(1)
    #点击更多校验操作
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View").child("更多设置")[0].click()
    sleep(1)
    #点击删除
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="确认").click()
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    

#选中自定义模版删除后焦点回到当前笔记应用的模版,默认选中并设置系统默认模版
@pytest.mark.testcase
@allure.description("选中自定义模版删除后焦点回到当前笔记应用的模版,默认选中并设置系统默认模版")
@allure.title("选中自定义模版删除后焦点回到当前笔记应用的模版,默认选中并设置系统默认模版")
def test_note_customize_template_apply_del_and_create():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    #点击自定义模板
    poco(text="自定义模板").click()
    sleep(1)
    #导入新的图片
    if poco("模板-空白").exists():
        poco("模板-空白").click()
    else:
        poco("android.widget.LinearLayout")\
        .offspring("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View")\
        .child("android.view.View")\
        .child("android.view.View")[7]\
        .child("android.view.View").child("android.view.View").click()
    sleep(2)
    #点击根目录
    poco("显示根目录").click()
    sleep(1)
    #点击图片
    touch((168,324))
    sleep(1)
    poco(text="导出文件").click()
    png_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.android.documentsui:id/drawer_layout")\
    .child("android.widget.ScrollView")\
    .offspring("com.android.documentsui:id/container_directory")\
    .offspring("com.android.documentsui:id/dir_list")\
    .child("com.android.documentsui:id/item_root")
    if png_list and len(png_list)>0:
        for p in png_list:
            if p.child("android.widget.LinearLayout")\
            .child("android.widget.LinearLayout")\
            .offspring("android:id/title").get_text().endswith("png"):
                p.click()
                break
        #拖动进行裁切
#         touch((653,817))
        swipe_press_ai((1109,1745),(507,1057))
#         swipe((1106,1745),(807,1257))
        poco("应用裁切").click()
        
    else:
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
    #使用该模板
    touch((431,455))
    poco(text="确认").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    #点击删除
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View")\
    .child("更多设置")[0].click()
    sleep(1)
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="确认").click()
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    


    
#自定义模版删除后，其它已设置的笔记正常显示该模版
@pytest.mark.testcase
@allure.description("自定义模版删除后，其它已设置的笔记正常显示该模版")
@allure.title("自定义模版删除后，其它已设置的笔记正常显示该模版")
def test_note_customize_template_multi_apply_del():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    #点击自定义模板
    poco(text="自定义模板").click()
    sleep(3)
    #导入新的图片
    if poco("模板-空白").exists():
        poco("模板-空白").click()
    else:
        poco("android.widget.LinearLayout")\
        .offspring("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View")\
        .child("android.view.View")\
        .child("android.view.View")[7]\
        .child("android.view.View").child("android.view.View").click()
    sleep(2)
    #点击根目录
    poco("显示根目录").click()
    sleep(1)
    #点击图片
    touch((168,324))
    sleep(1)
    poco(text="导出文件").click()
    png_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.android.documentsui:id/drawer_layout")\
    .child("android.widget.ScrollView")\
    .offspring("com.android.documentsui:id/container_directory")\
    .offspring("com.android.documentsui:id/dir_list")\
    .child("com.android.documentsui:id/item_root")
    if png_list and len(png_list)>0:
        for p in png_list:
            if p.child("android.widget.LinearLayout")\
            .child("android.widget.LinearLayout")\
            .offspring("android:id/title").get_text().endswith("png"):
                p.click()
                break
        #拖动进行裁切
#         touch((653,817))
        swipe_press_ai((1109,1745),(507,1057))
#         swipe((1106,1745),(807,1257))
        poco("应用裁切").click()
        
    else:
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
    #使用该模板
    touch((431,455))
    poco(text="确认").click()
    sleep(1)
    #返回，创建新的笔记
    poco("返回").click()
    poco(text="新建笔记").click()
    poco("更多设置").click()
    poco(text="更改模板").click()
    poco(text="自定义模板").click()
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View").child("更多设置")[0].click()
    poco(text="删除").click()
    sleep(1)
    poco(text="确认").click()
    poco(text="确认").click()
    sleep(1)
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #点击一开始创建的笔记
    touch((471,370))
    sleep(1)
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    


#自定义模版重命名 名称上限40为字符，不限类型
@pytest.mark.testcase
@allure.description("自定义模版重命名 名称上限40为字符，不限类型")
@allure.title("自定义模版重命名 名称上限40为字符，不限类型")
def test_note_customize_template_rename():
    if is_login()==True:
        login()
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    #点击自定义模板
    poco(text="自定义模板").click()
    sleep(1)
    #导入新的图片
    if poco("模板-空白").exists():
        poco("模板-空白").click()
    else:
        poco("android.widget.LinearLayout")\
        .offspring("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View")\
        .child("android.view.View")\
        .child("android.view.View")[7]\
        .child("android.view.View").child("android.view.View").click()
    sleep(2)
    #点击根目录
    poco("显示根目录").click()
    sleep(1)
    #点击图片
    touch((168,324))
    sleep(1)
    poco(text="导出文件").click()
    png_list = poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.android.documentsui:id/drawer_layout")\
    .child("android.widget.ScrollView")\
    .offspring("com.android.documentsui:id/container_directory")\
    .offspring("com.android.documentsui:id/dir_list")\
    .child("com.android.documentsui:id/item_root")
    if png_list and len(png_list)>0:
        for p in png_list:
            if p.child("android.widget.LinearLayout")\
            .child("android.widget.LinearLayout")\
            .offspring("android:id/title").get_text().endswith("png"):
                p.click()
                break
        #拖动进行裁切
#         touch((653,817))
        swipe_press_ai((1109,1745),(507,1057))
#         swipe((1106,1745),(807,1257))
        poco("应用裁切").click()
        
    else:
        #右滑返回
        swipe((3,900),(200,900))
        sleep(1)
        #右滑返回
        swipe((3,900),(200,900))
    #点击更多，进行重命名
    sleep(1)
    touch(Template(r"tpl1750837287356.png", record_pos=(-0.05, -0.262), resolution=(1200, 1920)))
#     poco("android.widget.LinearLayout")\
#     .offspring("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View")\
#     .child("android.view.View")\
#     .child("android.view.View")[7]\
#     .child("android.view.View")\
#     .child("更多设置")[0].click()

    poco(text="重命名").click()
#     keyevent("del")
    #输入超过40个字
    text("我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数",enter=False)
    #清空标题
    poco("关闭").wait_for_appearance(timeout=TIME_OUT)
    poco("关闭").click()
    #重新输入名称
    temp_name = "我在凑字数"
    text(temp_name,enter=False)
    poco(text="确认").click()
    sleep(1)
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View")\
    .child("更多设置")[1].click()
    poco(text="重命名").click()
    #输入超过40个字
    text("我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数我在凑字数",enter=False)
    #清空标题
    poco("关闭").wait_for_appearance(timeout=TIME_OUT)
    poco("关闭").click()
    #输入已存在的名称
    text(temp_name,enter=False)
#     assert poco(text="名称不能重复！").exists()
    poco(text="确认").click()
    #点击取消
    poco(text="取消").click()
    #删除导入的模板
    sleep(1)
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .child("android.view.View")\
    .child("更多设置")[0].click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="确认").click()
    poco("返回").click()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    


    




    

    
    
    
        
def test():
    swipe_press_ai((1109,1745),(507,1057))
    
    


    
    

    
if __name__=="__main__":
#     test_note_default_tempalte_confirm_take_effect()
#     test_note_default_template_cancel()
#     test_note_template_config()
#     test_note_default_template()
#     test_note_template_customize_portal_and_export_jpg_and_png()
#     test_note_template_cropping()
#     test_note_template_cropping_cancel()
    test_note_customize_template_desc_and_del()
    test_note_customize_template_apply_del_and_create()
    test_note_customize_template_rename()
#     test()


