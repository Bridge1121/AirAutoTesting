# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

from airtest.core.api import *
from airtest.core.android.touch_methods.base_touch import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))
    
    
# 未登录账号-阅读应用初始化页面,三个tab页签可来回切换，导入文档
def test_logout_reading_init_and_export():
    if is_login == False:
        logout()
    #点击阅读
    poco("阅读").click()
    #来回切换tab页
    poco(text="电子书").click()
    poco(text="批注截图").click()
    poco(text="我的文档").click()
    #导入文档
    poco(text="导入文档").click()
    poco(text="金山wps创建").click()
    #新建文档导入
    poco("cn.wps.moffice_eng:id/pad_newbuild_txt").click()
    poco(text="文字").click()
    poco("cn.wps.moffice_eng:id/new_type_name").click()
    #输入文字
    text("未登录游客导入文档",enter=False)
    #点击保存
    poco("cn.wps.moffice_eng:id/image_save").click()
    poco("cn.wps.moffice_eng:id/btn_save").click()
    #关闭文件
    poco("cn.wps.moffice_eng:id/writer_maintoolbar_backBtn").click()
    #返回到最近文件页面
    poco("cn.wps.moffice_eng:id/back_btn").click()
    poco("cn.wps.moffice_eng:id/title_back").click()
    #退出wps
    #右滑
    swipe((3,800),(700,800))
    #删除导入的文档
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[3].child("更多设置")[0].click()
    poco(text="删除文档").click()
    poco(text="删除").click()
    #点击首页
    poco("首页").click()
    

#已登录账号,阅读页面初始化，切换tab
def test_login_reading_init():
    if is_login==True:
        login()
    #点击阅读
    poco("阅读").click()
    #切换tab
    poco(text="电子书").click()
    poco(text="批注截图").click()
    poco(text="我的文档").click()
    poco("首页").click()


#我的文档列表，列表有数据且超过一屏，上滑显示
def test_my_file_list_swipe():
    if is_login==True:
        login()
    poco("阅读").click()
    #上滑显示
    swipe((700,1800),(700,400))
    poco("首页").click()

#我的文档列表,docx格式文档内容为空可正常打开
def test_my_file_list_empty_docx_open():
    if is_login==True:
        login()
    #点击阅读
    poco("阅读").click()
    #来回切换tab页
    poco(text="电子书").click()
    poco(text="批注截图").click()
    poco(text="我的文档").click()
    #导入文档
    poco(text="导入文档").click()
    poco(text="金山wps创建").click()
    #新建文档导入
    poco("cn.wps.moffice_eng:id/pad_newbuild_txt").click()
    poco(text="文字").click()
    poco("cn.wps.moffice_eng:id/new_type_name").click()
    #点击保存
    poco("cn.wps.moffice_eng:id/image_save").click()
    poco("cn.wps.moffice_eng:id/btn_save").click()
    #关闭文件
    poco("cn.wps.moffice_eng:id/writer_maintoolbar_backBtn").click()
    #返回到最近文件页面
    poco("cn.wps.moffice_eng:id/back_btn").click()
    poco("cn.wps.moffice_eng:id/title_back").click()
    #退出wps
    #右滑
    swipe((3,800),(700,800))
    #点击打开文件
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[3].child("DOCX")[0].click()
    sleep(1)
    #关闭
    poco("cn.wps.moffice_eng:id/writer_maintoolbar_backBtn").click()
    #退出wps
    #右滑
    swipe((3,800),(700,800))
    #我的文档删除导入的文件
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[3].child("更多设置")[0].click()
    poco(text="删除文档").click()
    poco(text="删除").click()
    #点击首页
    poco("首页").click()
    
#通过导入文件方式导入一个后再导入一个，查看排列顺序
def test_reading_export_order_rename():
    if is_login==True:
        login()
    #点击阅读
    poco("阅读").click()
    #来回切换tab页
    poco(text="电子书").click()
    poco(text="批注截图").click()
    poco(text="我的文档").click()
    file_list=("我是先导入的文件","我是后导入的文件")
    for i in range(len(file_list)):
        #导入文档
        poco(text="导入文档").click()
        poco(text="金山wps创建").click()
        #新建文档导入
        poco("cn.wps.moffice_eng:id/pad_newbuild_txt").click()
        poco(text="文字").click()
        poco("cn.wps.moffice_eng:id/new_type_name").click()
        #输入文字
        text(file_list[i],enter=False)
        #点击保存
        poco("cn.wps.moffice_eng:id/image_save").click()
        poco("cn.wps.moffice_eng:id/btn_save").click()
        #关闭文件
        poco("cn.wps.moffice_eng"+
             ":id/writer_maintoolbar_backBtn").click()
        #返回到最近文件页面
        poco("cn.wps.moffice_eng:id/back_btn").click()
        poco("cn.wps.moffice_eng:id/title_back").click()
        #退出wps
        #右滑
        swipe((3,800),(700,800))
    #重命名先导入的文档，查看排列顺序
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[3].child("更多设置")[1].click()
    poco(text="重命名").click()
    text("编辑一下",enter=False)
    poco(text="确认").click()
    #校验导入文件顺序
#     assert poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View").child("android.view.View")\
#     .child("android.view.View")[3]\
#     .child("android.widget.TextView")[4].get_text()==file_list[1]
#     sleep(1)
#     assert poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View")\
#     .child("android.view.View")\
#     .child("android.view.View")[3]\
#     .child("android.widget.TextView")[5].get_text()==file_list[0]+"编辑一下"
    for i in range(len(file_list)):
        #我的文档删除导入的文件
        poco("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View").child("android.view.View")\
        .child("android.view.View")[3].child("更多设置")[0].click()
        poco(text="删除文档").click()
        poco(text="删除").click()
    #点击首页
    poco("首页").click()
    
    

#点击通过文件传输导入
def test_reading_file_trans_import():
    if is_login==True:
        login()
    poco("阅读").click()
    poco(text="导入文档").click()
    #校验存在两个导入入口
    sleep(1)
    assert poco(text="金山wps创建").exists()
    assert poco(text="文件传输导入").exists()
    sleep(1)
    #通过文件传输导入
    poco(text="文件传输导入").click()
    #点击列表第一个，加入书架
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[8]\
    .child("android.view.View")[0].child("more icon").click()
    poco(text="加入书架").click()
    poco("阅读").click()
    sleep(1)
    #删除导入的文件
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[3].child("更多设置")[0].click()
    poco(text="删除文档").click()
    poco(text="删除").click()
    poco("首页").click()
    

#导入pdf格式文件到我的文档,并打开pdf格式文件
# def test_reading_import_pdf_open():
# #     if is_login()==True:
# #         login()
#     poco("阅读").click()
#     poco(text="导入文档").click()
#     #docx转pdf文件
#     poco(text="金山wps创建").click()
#     poco("cn.wps.moffice_eng:id/pad_newbuild_txt").click()
#     poco(text="PDF").click()
#     poco(text="文档转PDF").click()
#     poco("android.widget.FrameLayout")\
#     .child("android.widget.LinearLayout")\
#     .offspring("android:id/content")\
#     .offspring("cn.wps.moffice_eng:id/layout_fit_pad_outer_root_node")\
#     .child("android.widget.LinearLayout")\
#     .child("cn.wps.moffice_eng:id/phone_home_root")\
#     .offspring("android.widget.FrameLayout")\
#     .offspring("cn.wps.moffice_eng:id/file_select_recent_content_list")\
#     .child("cn.wps.moffice_eng:id/fb_listview_item_layout")[0]\
#     .offspring("cn.wps.moffice_eng:id/fb_file_icon").click()
#     sleep(1)
#     #输出为pdf
#     poco("cn.wps.moffice_eng:id/export_pdf_btn").click()
#     #输出为pdf
#     poco("cn.wps.moffice_eng:id/btn_save").click()
#     sleep(1)
#     if poco("cn.wps.moffice_eng:id/dialog_button_positive").exists():
#         poco("cn.wps.moffice_eng:id/dialog_button_positive").click()
#     sleep(2)
#     #关闭文件
#     poco("cn.wps.moffice_eng:id/pdf_main_toolbar_backBtn").click()
#     #返回
#     poco("cn.wps.moffice_eng:id/titlebar_back_icon").click()
#     poco("cn.wps.moffice_eng:id/title_back").click()
#     #右滑退出wps
#     swipe((2,1000),(700,1000))
#     #打开文件
#     poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View").child("android.view.View")\
#     .child("android.view.View")[3]\
#     .child("android.widget.TextView")[0].click()
#     sleep(1)
#     #关闭
#     poco("cn.wps.moffice_eng:id/pdf_main_toolbar_backBtn").click()
#     #右滑退出wps
#     swipe((2,1000),(700,1000))
#     #删除导入的文件
#     poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View").child("android.view.View")\
#     .child("android.view.View")[3].child("更多设置")[1].click()
#     poco(text="删除文档").click()
#     poco(text="删除").click()
#     poco("首页").click()
    


#开启阅读模式,打开文档开启阅读模式和护眼模式文档阅读，开启阅读模式但关闭护眼模式文档阅读，
def test_reading_mode():
    if is_login()==True:
        login()
    poco("阅读").click()
    #打开文档
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[3]\
    .child("android.widget.TextView")[0].click()
    sleep(1)
    #下拉菜单
    swipe((1036,0),(886,432))
    #1、开启阅读模式和护眼模式文档阅读
    #点击开启护眼模式
    poco(text="护眼模式").click()
    sleep(2)
    #点击开启阅读模式
    poco(text="阅读模式").click()
    #关闭下拉菜单
    touch((136,904))
    #2、开启阅读模式但关闭护眼模式文档阅读
    #下拉菜单
    swipe((1036,0),(886,432))
    #关闭护眼模式
    poco(text="护眼模式").click()
    #关闭下拉菜单
    touch((136,904))
    sleep(1)
    #3、关闭阅读模式和护眼模式文档阅读
    #下拉菜单
    swipe((1036,0),(886,432))
    #关闭阅读模式
    poco(text="阅读模式").click()
    #关闭下拉菜单
    touch((136,904))
    sleep(1)
    #4、关闭阅读模式但开启护眼模式文档阅读
    #下拉菜单
    swipe((1036,0),(886,432))
    #点击开启护眼模式
    poco(text="护眼模式").click()
    sleep(2)
    #点击关闭护眼模式
    poco(text="护眼模式").click()
    #关闭下拉菜单
    touch((136,904))
    #关闭文件
    poco("cn.wps.moffice_eng:id/pdf_main_toolbar_backBtn").click()
    #右滑退出wps
    swipe((2,1000),(700,1000))
    poco("首页").click()


    
    
#打开微信读书，搜索书籍
def test_wechat_reading_open_and_search():
    if is_login()==True:
        login()
    #点击应用
    poco("应用").click()
    #打开微信读书
    poco("微信读书图标").click()
    #点击搜索
    poco("com.tencent.weread:id/id_searchTextInput").click()
    text("红楼梦",enter=False)
    sleep(1)
    #返回
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.tencent.weread:id/qmui_activity_root_id")\
    .child("android.widget.FrameLayout")\
    .offspring("com.tencent.weread:id/fragment_id")\
    .child("android.widget.FrameLayout")\
    .offspring("com.tencent.weread:id/rn_modal_root_container_id")\
    .child("android.widget.FrameLayout")\
    .child("android.widget.FrameLayout")\
    .child("android.view.ViewGroup")\
    .child("android.view.ViewGroup")\
    .offspring("id_navigation_bar_back_button")\
    .child("android.view.ViewGroup").click()
    #右滑退出微信读书
    swipe((2,1000),(700,1000))
    poco("首页").click()




#批注截图列表，导出批注截图图片
def test_comments_screenshot_export():
    if is_login()==True:
        login()
    poco("阅读").click()
    poco(text="批注截图").click()
    #验证列表为空的ui
    assert poco(text="暂无文件").exists()
    poco("笔记").click()
    #下拉菜单
    swipe((1036,0),(886,432))
    #截图
    poco(text="截图").click()
    poco(text="完成").click()
    poco("阅读").click()
    #点击更多
    poco("更多设置").click()
    poco(text="导出").click()
    #保存到本地
    poco(text="保存到本地").click()
    #立即打开
    poco(text="立即打开").click()
    poco("阅读").click()
    #删除批注截图
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="删除").click()
    poco(text="我的文档").click()
    poco("首页").click()
    

    
    

    


    



    
    












def test():    
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[3]\
    .child("android.widget.TextView")[0].click()

#     print(poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View").child("android.view.View")\
#     .child("android.view.View")[3]\
#     .child("android.widget.TextView")[4].get_text())

    
#     print(poco("androidx.compose.ui.platform.ComposeView")\
#           .child("android.view.View")\
#           .child("android.view.View")\
#           .child("android.view.View")[3]\
#           .child("android.widget.TextView")[5].get_text())
    
if __name__=="__main__":
    test_logout_reading_init_and_export()
    test_login_reading_init()
    test_my_file_list_empty_docx_open()
    test_reading_export_order_rename()
    test_reading_file_trans_import()
    # test_reading_import_pdf_open()
    test_reading_mode()
    test_wechat_reading_open_and_search()
#     test()
    
