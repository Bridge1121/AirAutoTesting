# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))


# AI助手对话详情页上传文件过程中返回后点击确认
def test_ai_upload_file():
    if is_login() == True:
        login()
    poco("AI助手").click()
    # 上传文件
    poco("文件输入").click()
    # 点击文档
    poco(text="文档").click()
    # 点击上传列表第一个文档
    poco("android.widget.FrameLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("com.android.documentsui:id/drawer_layout") \
        .child("android.widget.ScrollView") \
        .offspring("com.android.documentsui:id/container_directory") \
        .offspring("com.android.documentsui:id/dir_list") \
        .child("com.android.documentsui:id/item_root")[0] \
        .child("android.widget.LinearLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("android:id/title").click()
    sleep(2)
    # 删掉上传的文件
    poco("删除").click()
    poco("首页").click()


# 查看AI助手历史会话为时间倒序显示且仅展示问题首句
def test_ai_history_view():
    if is_login() == True:
        login()
    poco("AI助手").click()
    sleep(1)
    # 点击历史记录
    poco(text="历史记录").click()
    sleep(1)
    poco("返回").click()
    # 进行一次会话
    poco("键盘输入").click()
    text("我们来聊天吧", enter=False)
    poco("分享").click()
    sleep(4)
    # 返回
    poco("返回").click()
    # 点击历史记录删除记录
    poco(text="历史记录").click()
    sleep(1)
    poco("android.widget.LinearLayout") \
        .offspring("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View").child("android.view.View") \
        .child("android.view.View")[1] \
        .child("android.view.View")[0].child("删除").click()
    poco(text="确认").click()
    # 点击返回
    poco("返回").click()
    poco("首页").click()


# 办公本有历史会话时点击AI助手历史会话后加载失败弹出test
def test_ai_history_view_no_internet():
    if is_login() == True:
        login()
    poco("AI助手").click()
    poco(text="历史记录").click()
    # 下拉菜单,断开网络
    swipe((1036, 0), (886, 432))
    poco("com.aispeech.ccui.systemui:id/cellGrid") \
        .child("android.widget.LinearLayout")[0] \
        .child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    touch((1000, 1600))
    # 恢复网络
    swipe((1036, 0), (886, 432))
    poco("com.aispeech.ccui.systemui:id/cellGrid") \
        .child("android.widget.LinearLayout")[0] \
        .child("com.aispeech.ccui.systemui:id/iv_cell_icon") \
        .click()
    sleep(5)
    touch((1000, 1600))
    # 点击返回
    poco("返回").click()
    poco("首页").click()


# 点击历史会话的文件在云端时下载后点击直接打开，文件上传后预览
def test_ai_history_file_open():
    poco("AI助手").click()
    poco("文件输入").click()
    poco(text="文档").click()
    # 点击上传列表第一个文档
    poco("android.widget.FrameLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("com.android.documentsui:id/drawer_layout") \
        .child("android.widget.ScrollView") \
        .offspring("com.android.documentsui:id/container_directory") \
        .offspring("com.android.documentsui:id/dir_list") \
        .child("com.android.documentsui:id/item_root")[0] \
        .child("android.widget.LinearLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("android:id/title").click()
    # 点击预览文件
    poco("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View") \
        .child("android.view.View") \
        .child("android.view.View")[2].offspring("文件").click()
    sleep(2)
    # 关闭文件
    if poco("cn.wps.moffice_eng:id/writer_maintoolbar_backBtn").exists():
        poco("cn.wps.moffice_eng:id/writer_maintoolbar_backBtn").click()
    else:
        poco("cn.wps.moffice_eng:id/pdf_main_toolbar_backBtn").click()
    # 右滑返回
    swipe((0, 778), (999, 778))
    sleep(2)
    # 点击键盘
    poco("键盘输入").click()
    text("总结这个文档内容", enter=False)
    poco("分享").click()
    sleep(5)
    # 返回
    poco("返回").click()
    # 点击历史记录删除记录
    poco(text="历史记录").click()
    sleep(1)
    # 点击会话
    poco("android.widget.LinearLayout") \
        .offspring("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View").child("android.view.View") \
        .child("android.view.View")[1] \
        .child("android.view.View")[0].click()
    sleep(1)
    # 点击打开文件
    poco("android.widget.LinearLayout") \
        .offspring("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View") \
        .child("android.view.View") \
        .child("android.view.View")[0].child("android.view.View") \
        .child("android.view.View").click()
    sleep(1)
    # 关闭文件
    if poco("cn.wps.moffice_eng:id/pdf_main_toolbar_backBtn").exists():
        poco("cn.wps.moffice_eng:id/pdf_main_toolbar_backBtn").click()
    else:
        poco("cn.wps.moffice_eng:id/writer_maintoolbar_backBtn").click()
    sleep(1)
    # 右滑返回
    swipe((0, 778), (999, 778))
    # 返回
    poco("返回").click()
    poco("首页").click()


# 在首页AI进行的对话能够在AI助手页历史会话页面查看
def test_index_ai_history():
    if poco(text="在此输入您的想法~").exists():
        poco(text="在此输入您的想法~").click()
    else:
        # 首页点击ai键盘
        poco("androidx.compose.ui.platform.ComposeView") \
            .child("android.view.View") \
            .child("android.view.View") \
            .child("android.view.View")[6].click()
    ques = "我在首页跟你聊天"
    text(ques, enter=False)
    #todo------为什么找不到分享？？？
    poco("分享").click()
    sleep(2)
    poco("返回").click()
    # 查看ai历史
    poco("AI助手").click()
    poco(text="历史记录").click()
    assert poco(text="我在首页跟你聊天").exists()
    sleep(1)
    poco("返回").click()
    poco("首页").click()


# 语音输入模式下点击上传文件时会跳转到AI助手页
def test_index_ai_upload_file():
    if poco(text="在此输入您的想法~").exists():
        # 点击语音模式
        poco("androidx.compose.ui.platform.ComposeView") \
            .child("android.view.View") \
            .child("android.view.View") \
            .child("android.view.View")[6].click()
    # 上传文件
    poco("文件输入").click()
    poco("首页").click()


# 在笔记页AI进行的对话不能在AI助手页历史会话页面查看
def test_note_ai_history():
    # 点击笔记
    poco("笔记").click()
    sleep(1)
    # 新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    # 插入文字
    touch((581, 997))
    sleep(2)
    text("我是在笔记页面跟你聊天", enter=False)
    touch((581, 1217))
    sleep(1)
    # 拖动ai图标
    swipe_press_ai()
    sleep(10)
    # 关闭
    poco("android.widget.LinearLayout") \
        .offspring("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View") \
        .child("android.view.View") \
        .child("android.view.View")[2] \
        .offspring("返回")[0].click()
    # 返回笔记列表
    poco("返回").click()
    poco("AI助手").click()
    poco(text="历史记录").click()
    poco("返回").click()
    # 删除笔记
    poco("笔记").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()


if __name__=="__main__":
#     test_ai_upload_file()
#     test_ai_history_view()
#     test_ai_history_view_no_internet()
    test_ai_history_file_open()
    test_index_ai_history()
    test_note_ai_history()
    test_note_ai_history()
    
    