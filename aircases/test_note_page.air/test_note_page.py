# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"

from airtest.core.api import *
from airtest.core.android.touch_methods.base_touch import *
import random
import string
import re


auto_setup(__file__,logdir=True,devices=["Android://127.0.0.1:5037/AINOTEA224042300042"])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
dev=device()


def extract_url_and_password(text):
    # 定义正则表达式，提取链接和密码
    url_pattern = r"(https?://[^\s]+)"
    password_pattern = r"密码：(\S+)"
    
    # 使用正则表达式查找网址
    url = re.search(url_pattern, text)
    password = re.search(password_pattern, text)
    
    # 如果找到了网址和密码，返回它们；否则返回 None
    return url.group(0) if url else None, password.group(1) if password else None

import pyperclip
def test():
#     poco(text="复制链接和密码").click()
#     #关闭对话框
#     sleep(1)
#     poco("close dialog").click()
#     poco("close dialog").click()
#     touch((600,600),duration=2)
#     #点击粘贴
#     poco("com.aispeech.tablet:id/tv_selection_paste").click()
#     #点击复制
#     poco("com.aispeech.tablet:id/tv_selection_copy").click()
    #获取剪贴板的网址和密码
    

    content = poco("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("androidx.compose.ui.viewinterop.ViewFactoryHolder")\
    .offspring("androidx.viewpager.widget.ViewPager")\
    .offspring("com.aispeech.tablet:id/editor_scroll_view")\
    .child("android.widget.FrameLayout")\
    .child("android.widget.FrameLayout")\
    .child("android.widget.RelativeLayout")[1]\
    .child("com.aispeech.tablet:id/editTextView").get_text()
    print(content)
    uu,pa = extract_url_and_password(content)
    print("url是：",uu)
    print("密码是：",pa)




#判断当前是否登录
def is_login():
    #点击应用
    poco("应用").click()
    #点击设置
    poco("设置图标").click()
    username = poco("com.zlt.zltsettings:id/user_name").get_text()
    #返回到首页
    poco(text="系统设置").click()
    #点击首页
    poco("首页").click()
    #判断是否已登录,true未登录，false已登录
    return username == "未登录"


#点击并拖动ai图标到文本
def swipe_press_ai(start_point=(49,1732),end_point=(410,990)):
    #拖动ai图标
    steps = 10  # 拖动的分段数
    multitouch_event = [
    DownEvent(start_point), SleepEvent(0.1)]
    dev.touch_proxy.perform(multitouch_event)
    sleep(1)
    # 2. swipe
    swipe_event = [DownEvent(start_point), SleepEvent(0.1)]
    for i in range(1, steps + 1):
        # 计算插值坐标，实现平滑拖动
        x = start_point[0] + (end_point[0] - start_point[0]) * i // steps
        y = start_point[1] + (end_point[1] - start_point[1]) * i // steps
        swipe_event.append(MoveEvent((x, y)))
        swipe_event.append(SleepEvent(0.05))  # 每步间隔，可微调
    swipe_event.append(UpEvent())
    dev.touch_proxy.perform(swipe_event)



#登录账号
def login(phoneNumber="18662682224",code="123456"):
    #点击应用
    poco("应用").click()

    #点击设置
    poco("设置图标").click()
    #点击登陆头像
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("android.widget.LinearLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.zlt.zltsettings:id/account")[0]\
    .child("android.widget.ImageView").click()
    poco("android.widget.CheckBox").click()
    poco(text="请输入手机号码").click()
    text(phoneNumber, enter=False)
    poco(text="请输入短信验证码").click()
    text(code, enter=False)                     
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    sleep(2)
    #点击账户
    poco("返回").click()
    sleep(1)
    #点击系统设置
    poco(text="系统设置").click()
    #点击首页
    poco("首页").click()
    sleep(1)
    
    
# 点击页面排序，弹出预览缩略视图，显示当前笔记的所有手写页面
def test_note_page_order():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    for i in range(2):
        #手指左滑，新增页面
        poco("后一页").click()
    poco("更多设置").click()
    poco(text="页面排序").click()
    #关闭
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[3].child("返回").click()
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    


    
    
    
# 清空页面 - 确定,内容清除后，返回列表再进入，不显示已清除的内容
def test_note_clear():
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    #插入文字
    touch((581,997))
    sleep(2)
    text("清除本页内容",enter=False)
    sleep(1)
    poco("更多设置").click()
    #点击清空本页
    poco(text="清空页面").click()
    #取消
    poco(text="取消").click()
    poco("更多设置").click()
    #点击清空本页
    poco(text="清空页面").click()
    poco(text="确认").click()
    #返回再次进入
    poco("返回").click()
    touch((490,390))
    assert not poco(text="清除本页内容").exists()
    sleep(1)
    poco("返回").click()
    #删除
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()




# 删除本页- 确定,点击删除本页后，只删除当前页面，其他页面不会被删除
def test_note_page_del():
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    for i in range(2):
        poco("更多设置").click()
        poco(text="插入文字").click()
        sleep(2)
        #插入文字
        touch((581,997))
        sleep(2)
        content = f"这是第{i}页"
        text(content,enter=False)
        #手指左滑，新增页面
        poco("后一页").click()
        
    poco("更多设置").click()
    poco(text="删除本页").click()
    poco(text="确认").click()
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
        



# 更多功能中复制本页,页面排序中，更多功能里的复制当前页
def test_note_page_copy():
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="复制本页").click()
#     更多功能里的复制当前页
    poco("更多设置").click()
    poco(text="页面排序").click()
    #点击更多，复制当前页
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[5].child("更多设置")[1].click()
    poco(text="复制当前页").click()
    #关闭
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[3].child("返回").click()
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()


    


# 默认字号是标准,切换字号为“大”,切换字号为“超大”
def test_font_size_change():
    poco("应用").click()
    poco("设置图标").click()
    poco(text="显示与亮度").click()
    #点击切换字号
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("android.widget.LinearLayout")\
    .offspring("com.zlt.zltsettings:id/fl_info")\
    .offspring("android.widget.ScrollView")\
    .offspring("com.zlt.zltsettings:id/ll_font_size")\
    .child("android.widget.ImageView").click()
    #点击标准
    poco(text="标准").click()
    #点击大
    poco(text="大").click()
    #点击超大
    poco(text="超大").click()
    #返回
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .offspring("com.zlt.zltsettings:id/ll_back")\
    .child("android.widget.ImageView").click()
    poco("首页").click()

# 开启录音转写，语种为普通话，查看词库
def test_note_recording_lexicon():
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #开始语音转写
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].child("手写笔").click()
    poco(text="词库").click()
    sleep(1)
    #关闭词库
    poco("close dialog").click()
    sleep(2)
    #切换语言
    poco(text="普通话").click()
    poco(text="普通话").click()
    poco(text="英语").click()
    poco(text="开始记录").click()
    sleep(2)
    #校验不存在词库
    assert not poco(text="词库").exists()
    #切换回普通话
    poco(text="英语").click()
    poco(text="英语").click()
    poco(text="普通话").click()
    poco(text="开始记录").click()
    sleep(2)
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    

# 导出分享链接--音频回听
def test_note_export_audio(note_name="测试录音中文"):
    poco(text=note_name).click()
    poco("更多设置").click()
    poco(text="分享笔记").click()
    sleep(1)
    #直接点击复制分享链接
    poco(text="分享链接").click()
    poco("close dialog").click()
    #获取剪贴板的网址和密码
    touch((600,1170),duration=2)
    #点击粘贴
    poco("com.aispeech.tablet:id/tv_selection_paste").click()
    #点击复制
    poco("com.aispeech.tablet:id/tv_selection_copy").click()
    #获取剪贴板的网址和密码
    content = poco("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("androidx.compose.ui.viewinterop.ViewFactoryHolder")\
    .offspring("androidx.viewpager.widget.ViewPager")\
    .offspring("com.aispeech.tablet:id/editor_scroll_view")\
    .child("android.widget.FrameLayout")\
    .child("android.widget.FrameLayout")\
    .child("android.widget.RelativeLayout")[1]\
    .child("com.aispeech.tablet:id/editTextView").get_text()
    url,password = extract_url_and_password(content)
    print("提取出来的链接是：",url)
    sleep(1)
    #删除复制的内容
    touch((600,1170))
    poco("com.aispeech.tablet:id/tv_selection_del").click()
    poco("返回").click()
    #打开浏览器
    poco("应用").click()
    poco("浏览器图标").click()
    sleep(5)
    #输入网址
    poco("com.ume.browser:id/search_engine_icon").click()
    text(text=url,enter=True)
    sleep(5)
    #点击回听音频
    poco(text="").click()
    poco("android.widget.LinearLayout")\
    .offspring("com.ume.browser:id/compositor_view_holder")\
    .offspring("android.widget.FrameLayout")\
    .child("android.view.ViewGroup")\
    .child("android.webkit.WebView")\
    .offspring("app").child("android.view.View")\
    .child("android.view.View")[3].swipe([0.1353, -0.0035])
    sleep(2)
    poco(text="").click()
    poco("com.ume.browser:id/nav_backward").click()
    #右滑退出
    swipe((9,848),(700,848))
    poco("com.ume.browser:id/exit_confirm").click()
    poco("首页").click()


    
# 笔记首页更换笔记模板
def test_note_template_change():
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="更改模板").click()
    #更换成空白页
    poco("模板-空白").click()
    poco(text="确认").click()
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()


#手指长按AI笔记文本选中后使用工具栏AI助手
def test_ai_helper():
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    #插入文字
    touch((581,997))
    sleep(2)
    text("测试ai助手",enter=False)
    touch((581,1197))
    touch((581,997))
    poco("com.aispeech.tablet:id/tv_selection_ask").click()
    sleep(1)
    #关闭ai助手
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[2].offspring("返回")[0].click()
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

    
    







    
    
if __name__=="__main__":
#     test_note_page_order()
#     test_note_clear()
#     test_note_page_del()
#     test_font_size_change()
#     test_note_page_copy()
#     test_note_recording_lexicon()
#     test()
    test_note_export_audio()
    test_note_template_change()
    test_ai_helper()
    
    
    
    