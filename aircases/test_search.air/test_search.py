# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"

from airtest.core.api import *
import random
import string

auto_setup(__file__,logdir=True,devices=["Android://127.0.0.1:5037/AINOTEA224042300042"])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#生成4位随机字符
def random_string(length=4):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


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
    

#新建笔记
def create_new_notes():
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
    timestamp = time.strftime("%Y%m%d%H%M%S")  # 年月日时分秒
    text(timestamp, enter=False)
    poco("返回").click()
    sleep(1)
    #4、回到首页
    poco("首页").click()
    return timestamp

#退出登录
def logout():
    #点击应用
    poco("应用").click()

    #点击设置
    poco("设置图标").click()
    #点击登陆头像
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout").offspring("android:id/content")\
    .child("android.widget.LinearLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.zlt.zltsettings:id/account")[0]\
    .child("android.widget.ImageView").click()
    #点击账号管理
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").offspring("android.widget.ScrollView")\
    .child("android.view.View")[0].click()
    #点击退出登录
    poco(text="退出登录").click()
    #点击确定
    poco(text="确定").click()
    sleep(1)
    #点击账户
    poco("返回").click()
    #点击系统设置
    poco(text="系统设置").click()
    #点击首页
    poco("首页").click()

    
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
    poco("登录").click()
    sleep(2)
    #点击账户
    poco("返回").click()
    sleep(1)
    #点击系统设置
    poco(text="系统设置").click()
    #点击首页
    poco("首页").click()
    sleep(1)
    
#删除文件
def del_file():
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    
    
#根据分组名删除分组
def find_group_by_name_and_del(ss):
    list = poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[3]\
    .child("android.view.View").children()
    for i in range(0,len(list)):
        text_node = poco("androidx.compose.ui.platform.ComposeView")\
            .child("android.view.View").child("android.view.View")\
            .child("android.view.View")[3]\
            .child("android.widget.TextView")[i*3]
            
        if text_node.get_text() == ss:
            poco("androidx.compose.ui.platform.ComposeView")\
            .child("android.view.View").child("android.view.View")\
            .child("android.view.View")[3]\
            .child("android.view.View")[i].click()
            poco(text="删除").click()
            poco(text="确认").click()
            break
    
    
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
    if is_login()==True:
        login()
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