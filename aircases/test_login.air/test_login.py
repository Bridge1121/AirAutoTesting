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


pytestmark = [allure.feature("登录模块用例"), allure.epic("办公本v2.4.0")]
        
        
    
#登录未勾选隐私政策和用户协议
@pytest.mark.testcase
@allure.description("登录未勾选隐私政策和用户协议")
@allure.title("登录未勾选隐私政策和用户协议")
def test_login_without_privacy(phoneNumber="18662682224",code="123456"):
    if is_login()==False:
        logout()
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
    poco(text="请输入手机号码").click()
    text(phoneNumber, enter=False)
    poco(text="请输入短信验证码").click()
    text(code, enter=False)
    sleep(2)
    #查看隐私政策
    touch((732,1013))
    #返回
    poco("com.aispeech.tablet.webview:id/iv_back").click()
    #查看用户协议
    touch((877,1016))
    #返回
    poco("com.aispeech.tablet.webview:id/iv_back").click()
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.Button").click()
    #关闭
    poco("关闭").click()
    poco("返回").click()
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .offspring("com.zlt.zltsettings:id/ll_back")\
    .child("android.widget.ImageView").click()
    poco("首页").click()
    



#登录-手机号校验,手机号为空,输入非数字,输入高于11位数字,输入低于11位数字,输入11位格式不对的数字
@pytest.mark.testcase
@allure.description("登录-手机号校验,手机号为空,输入非数字,输入高于11位数字,输入低于11位数字,输入11位格式不对的数字")
@allure.title("登录-手机号校验,手机号为空,输入非数字,输入高于11位数字,输入低于11位数字,输入11位格式不对的数字")
def test_login_phone_num(code="123456"):
    if is_login()==False:
        logout()
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
    #输入验证码
    poco(text="请输入短信验证码").click()
    text(code, enter=False)
    #勾选协议
    poco("android.widget.CheckBox").click()
    #1、输入手机号为空
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    #2、输入非数字
    poco(text="请输入手机号码").click()
    text("andhdk", enter=False)
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    #关闭
    poco("关闭").click()
    #3、输入高于11位数字
    #点击立即登录
    poco(text="立即登录").click()
    poco(text="请输入短信验证码").click()
    text(code, enter=False)
    #勾选协议
    poco("android.widget.CheckBox").click()
    poco(text="请输入手机号码").click()
    text("18662682224123", enter=False)
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    poco("关闭").click()
    #4、输入低于11位
    poco(text="立即登录").click()
    poco(text="请输入短信验证码").click()
    text(code, enter=False)
    #勾选协议
    poco("android.widget.CheckBox").click()
    poco(text="请输入手机号码").click()
    text("1866268222", enter=False)
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    poco("关闭").click()
    #5、输入11位格式不对的数字
    poco(text="立即登录").click()
    poco(text="请输入短信验证码").click()
    text(code, enter=False)
    #勾选协议
    poco("android.widget.CheckBox").click()
    poco(text="请输入手机号码").click()
    text("61862682224", enter=False)
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    #关闭
    poco("关闭").click()
    poco("返回").click()
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .offspring("com.zlt.zltsettings:id/ll_back")\
    .child("android.widget.ImageView").click()
    poco("首页").click()
    
    
#登录-验证码校验
@pytest.mark.testcase
@allure.description("登录-验证码校验")
@allure.title("登录-验证码校验")
def test_login_code(phoneNumber="15996805223"):
    if is_login()==False:
        logout()
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
    poco(text="请输入手机号码").click()
    text(phoneNumber, enter=False)
    poco("android.widget.CheckBox").click()
    #1、验证码为空
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    #2、输入错误验证码1
    #点击发送验证码
    poco(text="发送验证码").click()
    poco(text="请输入短信验证码").click()
    text("12345", enter=False)
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    #关闭
    poco("关闭").click()
    poco(text="立即登录").click()
    poco(text="请输入手机号码").click()
    text(phoneNumber, enter=False)
    poco("android.widget.CheckBox").click()
    #3、输入过期验证码
    poco(text="请输入短信验证码").click()
    text("234567", enter=False)
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    #关闭
    poco("关闭").click()
    poco(text="立即登录").click()
    poco(text="请输入手机号码").click()
    text(phoneNumber, enter=False)
    poco("android.widget.CheckBox").click()
    #4、验证码错误三次
    poco(text="请输入短信验证码").click()
    text("133456", enter=False)
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    #关闭
    poco("关闭").click()
    poco("返回").click()
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .offspring("com.zlt.zltsettings:id/ll_back")\
    .child("android.widget.ImageView").click()
    poco("首页").click()
    
    
#无网络时，点击发送验证码
@pytest.mark.testcase
@allure.description("无网络时，点击发送验证码")
@allure.title("无网络时，点击发送验证码")
def test_login_send_code_no_internet(phoneNumber="15996805223"):
    if is_login()==False:
        logout()
    #点击应用
    poco("应用").click()
    #点击设置
    poco("设置图标").click()
    #断开网络
    #下拉菜单
    swipe((1036,0),(886,432))
    poco("com.aispeech.ccui.systemui:id/cellGrid")\
    .child("android.widget.LinearLayout")[0]\
    .child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    touch((1000,1600))
    #点击登陆头像
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("android.widget.LinearLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("com.zlt.zltsettings:id/account")[0]\
    .child("android.widget.ImageView").click()
    poco(text="请输入手机号码").click()
    text(phoneNumber, enter=False)
    poco("android.widget.CheckBox").click()
    
    #点击发送验证码
    poco(text="发送验证码").click()
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    #查看隐私政策
    touch((732,1013))
    #点击返回
    poco("com.aispeech.tablet.webview:id/iv_back").click()
    #查看用户协议
    touch((877,1016))
    #点击返回
    poco("com.aispeech.tablet.webview:id/iv_back").click()
    #关闭
    poco("关闭").click()
    poco("返回").click()
    poco("android.widget.FrameLayout")\
    .child("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .offspring("com.zlt.zltsettings:id/ll_back")\
    .child("android.widget.ImageView").click()
    poco("首页").click()
    #恢复网络
    #下拉菜单
    # 恢复网络
    swipe((1036, 0), (886, 432))
    poco("com.aispeech.ccui.systemui:id/cellGrid") \
        .child("android.widget.LinearLayout")[0] \
        .child("com.aispeech.ccui.systemui:id/iv_cell_icon") \
        .long_click(duration=2)
    sleep(4)
    poco("com.zlt.zltsettings:id/sw_airplane").click()
    poco(text="已连接").wait_for_appearance(timeout=TIME_OUT)
    poco("android.widget.FrameLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("android:id/content") \
        .offspring("com.zlt.zltsettings:id/ll_back") \
        .child("android.widget.ImageView").click()


    
    
    
    
    
    
    
    
if __name__=="__main__":
#     test_login_without_privacy()
#     test_login_phone_num()
#     test_login_code()
    test_login_send_code_no_internet()
