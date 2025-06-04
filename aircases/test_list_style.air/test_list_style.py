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
    #点击登录
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[1].child("android.widget.TextView").click()
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
    
    

# 我的笔记，默认是列表模式的样式,点击右侧的更多按钮，显示分享笔记、移动分组、重命名、编辑标签、加密笔记、删除按钮
def test_default_list_style():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(2)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name="笔记123"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(1)
    touch(Template(r"tpl1748253848403.png", record_pos=(0.461, -0.482), resolution=(1200, 1920)))
    sleep(1)
    #删除笔记
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    

# 点击移动文件夹弹出移动小弹窗，在弹窗中点击新建文件夹，移动笔记
def test_note_move_to_new_folder_in_dialog():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #新建笔记
    poco(text="新建笔记").click()
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name="笔记123"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(1)
    #点击移动分组
    touch(Template(r"tpl1748253848403.png", record_pos=(0.461, -0.482), resolution=(1200, 1920)))
    #点击移动分组，弹窗中新建文件夹
    poco(text="移动分组").click()
    poco(text="新建文件夹").click()
    folder_name = "弹窗新建123"
    text(folder_name, enter=False)
    poco(text="确认").click()
    #上滑
    for i in range(0,2):
        swipe((477,1150),(477,640))
    #点击，将新建的笔记移动到其中
    poco(text=folder_name).click()
    poco(text="移动至此").click()
    sleep(3)
    #分组栏左滑
    for i in range(0,2):
        swipe((947,85),(184,88))
    sleep(1)
    #校验是否存在移动的笔记
    poco(text=folder_name).click()
    sleep(1)
    # assert poco(text=note_name).exists()
    #右滑
    for i in range(0,2):
        swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    #删除创建的分组
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("show catalogs").click()
    find_group_by_name_and_del(folder_name)
    poco(desc="").click()
    #返回首页
    poco("首页").click()
    
    
    
# 将默认文件夹中的笔记移动到新建的文件夹下(新建分组，新建一个文件夹创建笔记，在移动笔记到另一个新建的文件夹下）
def test_note_move_to_new_folder(default_group="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #新建分组
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].click()
    sleep(1)
    poco(text="新建文件夹").click()
    group_name="测试移动分组"
    text(group_name,enter=False)
    poco(text="确认").click()
    poco(desc="").click()
    #分组栏左滑
    for i in range(0,2):
        swipe((947,85),(184,88))
    sleep(1)
    poco(text=group_name).click()
    sleep(1)
    folder_name=None
    #新建两个文件夹
    for i in range(0,2):
        poco("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View").child("android.view.View")\
        .child("android.view.View")[4].child("search").click()
        folder_name = f"列表新建文件_{i}"
        text(folder_name, enter=False)
        poco(text="确认").click()
    #点击最后新建的文件夹
    poco(text=folder_name).click()
    #新建笔记
    poco(text="新建笔记").click()
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name="默认文件夹笔记"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(1)
    #点击更多，移动分组
    touch(Template(r"tpl1748253848403.png", record_pos=(0.461, -0.482), resolution=(1200, 1920)))
    sleep(1)
    #点击移动分组，弹窗中新建文件夹
    poco(text="移动分组").click()
    #上滑
    for i in range(0,2):
        swipe((477,1150),(477,640))
    poco(text=group_name).click()
    #点击最初新建的文件夹
    touch((357,787))
    poco(text="移动至此").click()
    sleep(1)
    #返回
    poco("<").click()
#     poco(text="测试移动分组").click()
#     poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View").child("android.view.View")\
#     .child("android.view.View")[10].child("android.view.View")\
#     .child("android.view.View")[1].click()
#     sleep(2)
#     #校验是否存在移动的笔记
#     assert poco(text=note_name).exists()
    sleep(1)
    # poco("<").click()
    
    #右滑
    for i in range(0,2):
        swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    #删除创建的分组
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("show catalogs").click()
    find_group_by_name_and_del(group_name)
    poco(desc="").click()
    #返回首页
    poco("首页").click()
    


# 删除二次确认
def test_del_file_confirm():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(1)
    touch((581,997))
    sleep(2)
    note_name="删除二次确认"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(1)
    #点击更多
    touch(Template(r"tpl1748253848403.png", record_pos=(0.461, -0.482), resolution=(1200, 1920)))
    sleep(1)
    #点击删除
    poco(text="删除").click()
    #校验是否存在确认弹窗
    assert poco(text="提示").exists()
    sleep(1)
    #点击取消
    poco(text="取消").click()
    sleep(1)
    #校验要删除的笔记是否还在列表中
    # assert poco(text=note_name).exists()
    #再次点击删除
    touch(Template(r"tpl1748253848403.png", record_pos=(0.461, -0.482), resolution=(1200, 1920)))
    sleep(1)
    #点击删除
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)
    #校验是否成功删除
#     assert not poco(text=note_name).exists()
    poco("首页").click()

    
    
    


    
    
if __name__=="__main__":
    test_default_list_style()
    test_note_move_to_new_folder_in_dialog()
    test_note_move_to_new_folder()
    test_del_file_confirm()
    


