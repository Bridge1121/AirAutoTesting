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

#判断回收站是否为空
def recycle_bin_is_null():
    return poco(text="暂无文件").exists()

#回收站删除全部文件
def del_all_files():
    poco("笔记").click()
    #点击回收站
    poco("show recycle").click()
    sleep(1)
    if recycle_bin_is_null()==False:
        poco("编辑").click()
        poco(text="全部选中").click()
        poco(text="彻底删除").click()
        poco(text="确认").click()
    poco("<").click()

    


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
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
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
            
            
# 编辑标题后，点击返回，保存笔记
def test_note_title_edit():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    #点击修改标题
    touch((187,57))
    #修改标题
    for i in range(0,16):
        keyevent("DEL")
    sleep(1)
    text("编辑标题",enter=False)
    #按回车保存修改
    keyevent("ENTER")
    #返回
    poco("返回").click()
    #删除新建的笔记
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

    
    
    
    
            
            
if __name__=="__main__":
    test_note_title_edit()
    