# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))

    
# 分屏后，滑动浏览页面，完整显示录音原文    
def test_recording_top_bottom_split_screen():
    if is_login()==True:
        login()
    #点击应用
    poco("应用").click()
    #打开wps
    poco("WPS Office图标").click()

    swipe((1036,0),(886,432))
    poco(text="分屏笔记").click()
    #点击录音
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].child("手写笔").click()
    #点击录音原文
    poco(text="录音原文").click()
    sleep(1)
    #恢复笔记全屏
    poco("com.android.systemui:id/docked_divider_handle").swipe([-0.0686, -0.578])
    #结束录音
    poco(text="结束").click()
    sleep(1)
    #点击返回
    poco("返回").click()
    sleep(1)
    poco("笔记").click()
    del_file()
    #4、回到首页
    poco("首页").click()

    
# 分屏后，滑动浏览页面，完整显示AI笔记    
def test_ai_top_bottom_split_screen():
    if is_login()==True:
        login()
    #点击应用
    poco("应用").click()
    #打开wps
    poco("WPS Office图标").click()

    swipe((1036,0),(886,432))
    poco(text="分屏笔记").click()
    #点击录音
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].child("手写笔").click()
    sleep(1)
    #恢复笔记全屏
    poco("com.android.systemui:id/docked_divider_handle").swipe([-0.0686, -0.578])
    sleep(1)
    poco("返回").click()
    sleep(1)
    poco("笔记").click()
    #删除笔记
    del_file()
    #4、回到首页
    poco("首页").click()
    
    
    
# 分屏后，滑动浏览页面，完整显示会后总结    
def test_post_meeting_summary_top_bottom_split_screen():
    if is_login()==True:
        login()
    #点击应用
    poco("应用").click()
    #打开wps
    poco("WPS Office图标").click()
    swipe((1036,0),(886,432))
    poco(text="分屏笔记").click()
    #点击录音
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].child("手写笔").click()

    sleep(5)
    #点击结束
    poco(text="结束").click()
    sleep(1)
    #点击会后总结
    poco(text="会后总结").click()
    #恢复笔记全屏
    poco("com.android.systemui:id/docked_divider_handle").swipe([-0.0686, -0.578])
    sleep(1)
    poco("返回").click()
    sleep(1)
    poco("笔记").click()
    #删除笔记
    del_file()
    #4、回到首页
    poco("首页").click()

    


# 分屏后，滑动浏览页面，滚动插入图片    
def test_insert_pic_top_bottom_split_screen():
    if is_login()==True:
        login()
    #点击应用
    poco("应用").click()
    #打开wps
    poco("WPS Office图标").click()
    #下拉菜单
    swipe((1036,0),(886,432))
    poco(text="分屏笔记").click()
    #点击右上角更多
    poco("更多设置").click()
    #点击插入图片
    poco(text="插入图片").click()
    #点击近期图片第一张
    poco("android.widget.FrameLayout")\
        .child("android.widget.LinearLayout")\
        .offspring("com.android.documentsui:id/drawer_layout")\
        .child("android.widget.ScrollView")\
        .offspring("2025-05-19 17_05_66.jpg, 3.46 MB, 5月19日")\
        .offspring("com.android.documentsui:id/icon_mime_lg").click()
    #滑动屏幕查看图片
    poco("androidx.compose.ui.viewinterop.ViewFactoryHolder").swipe([-0.0882, -0.3166])
    sleep(1)
    #恢复笔记全屏
    poco("com.android.systemui:id/docked_divider_handle").swipe([-0.0686, -0.578])
    sleep(1)
    poco("返回").click()
    sleep(1)
    poco("笔记").click()
    #删除笔记
    del_file()
    #4、回到首页
    poco("首页").click()
    
#上下分屏滚动保存笔记后搜索
def test_create_notes_and_search_top_bottom_split_screen():
    if is_login()==True:
        login()
    #点击应用
    poco("应用").click()
    #打开wps
    poco("WPS Office图标").click()
    sleep(1)
    #下拉菜单
    swipe((1036,0),(886,432))
    sleep(1)
    poco(text="分屏笔记").click()
    sleep(1)
    #输入文字
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    timestamp = time.strftime("%Y%m%d%H%M%S")  # 年月日时分秒
    text(timestamp, enter=False)
    poco("返回").click()
    #退出应用
    stop_app("cn.wps.moffice_eng")
    sleep(1)
    #点击笔记
    poco("笔记").click()
    #点击搜索
    poco("search").click()
    #输入搜索内容
    sleep(2)
    text("2025", enter=False)
    #点击笔记
    poco(text="笔记").click()
    #判断是否搜索到笔记
#     assert poco("android.widget.LinearLayout")\
#         .offspring("androidx.compose.ui.platform.ComposeView")\
#         .child("android.view.View")\
#         .child("android.view.View")\
#         .child("android.view.View")[5]\
#         .child("android.view.View").child("android.view.View").exists()
    sleep(1)
   #点击返回
    poco("Back").click()
    #点击笔记
    poco(text="笔记").click()
    del_file()
   #点击首页
    poco("首页").click()
    
    
# 上下分屏时使用AI助手
def test_ai_helper_top_bottom_split_screen():
    if is_login()==True:
        login()
    #点击应用
    poco("应用").click()
    #打开wps
    poco("WPS Office图标").click()
    sleep(1)
    #下拉菜单
    swipe((1036,0),(886,432))
    sleep(1)
    poco(text="分屏笔记").click()
    sleep(1)
    #点击录音
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].child("手写笔").click()
    sleep(1)
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[12]\
    .child("android.widget.Button").click()

    #点击ai助手
    touch(Template(r"tpl1748243386961.png", record_pos=(-0.444, 0.731), resolution=(1200, 1920)))
    #长按录音
    poco(text="按住说话").click()
    sleep(1)
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[2].offspring("返回")[0].click()
    sleep(1)
    #退出wps
    stop_app("cn.wps.moffice_eng")
    #结束录音
    poco(text="结束").click()
    #返回
    poco("返回").click()
    poco("笔记").click()
    #删除笔记
    del_file()
    #点击首页
    poco("首页").click()



    
    


if __name__=="__main__":
    test_recording_top_bottom_split_screen()
    test_ai_top_bottom_split_screen()
    test_create_notes_and_search_top_bottom_split_screen()
    test_ai_helper_top_bottom_split_screen()
#     swipe_press()
