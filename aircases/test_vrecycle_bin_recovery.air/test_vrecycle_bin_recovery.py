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

    
#删除文件
def del_file():
    touch(Template(r"tpl1748938545309.png", record_pos=(0.287, -0.606), resolution=(1200, 1920)))
    poco(text="全部选中").click()
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)


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
            
            
            
def test():
    touch(Template(r"tpl1748318230851.png", record_pos=(0.459, -0.487), resolution=(1200, 1920)))
    sleep(1)
    poco(text="删除").click()
    sleep(2)
    poco(text="确认").click()
    
# 笔记列表“全部笔记”tab下新建笔记删除在回收站恢复验证
def test_note_not_in_folder_recovery():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #删除回收站笔记
    del_all_files()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name = "恢复笔记"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(1)
    #删除
    del_file()
    #点击回收站
    poco("show recycle").click()
    #点击恢复
    poco("更多设置").click()
    poco(text="恢复").click()
    sleep(1)
    assert recycle_bin_is_null()
    poco("<").click()
    #删除创建的笔记
    del_file()
    sleep(1)
    poco("首页").click()
    


    
# 新建文件夹内笔记删除后在回收站恢复验证
def test_note_in_folder_recovery(default_group="默认笔记"):
    if is_login()==True:
        login()
    #删除回收站笔记
    del_all_files()
    #点击默认分组
    poco(text=default_group).click()
    #新建文件夹
    touch(Template(r"tpl1748249870254.png", record_pos=(0.048, -0.608), resolution=(1200, 1920)))
    folder_name = "文件夹恢复笔记"
    text(folder_name,enter=False)
    poco(text="确认").click()
    poco(text=folder_name).click()
    #新建笔记
    poco(text="新建笔记").click()
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name = "笔记13243"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(1)
    #删除笔记
    del_file()
    #返回到默认分组
    poco("<").click()
    poco("show recycle").click()
    #恢复笔记
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="恢复").click()
    poco("<").click()
    #点击新建的文件夹
    poco(text=folder_name).click()
    sleep(1)
    #校验是否存在笔记
    assert not poco(text="暂无文件").exists()
    poco("<").click()
    #删除文件
    del_file()
    poco(text="全部笔记").click()
    poco("首页").click()





# 新建笔记批量删除恢复
def test_del_notes_recovery(default_group="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #删除回收站笔记
    del_all_files()
    #点击默认分组
    poco(text=default_group).click()
    #新建文件夹
    touch(Template(r"tpl1748249870254.png", record_pos=(0.048, -0.608), resolution=(1200, 1920)))
    text("新建文件",enter=False)
    poco(text="确认").click()
    #点击新建的文件夹
    poco(text="新建文件").click()
    #新建几个笔记
    for i in range(0,2):
        poco(text="新建笔记").click()
        #输入笔记内容
        poco("更多设置").click()
        poco(text="插入文字").click()
        sleep(2)
        touch((581,997))
        sleep(2)
        note_name = f"恢复笔记_{random_string()}"
        text(note_name, enter=False)
        poco("返回").click()
        sleep(1)
    #批量删除
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco("<").click()
    #批量恢复
    poco("show recycle").click()
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="恢复").click()
    sleep(1)
    poco("<").click()
    del_file()
    poco(text="全部笔记").click()
    poco("首页").click()


    
# 根目录新建文件夹删除（包含文件和不包含文件）恢复验证
def test_del_root_folder_no_subfolder_recovery():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #删除回收站笔记
    del_all_files()
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("show catalogs").click()
    #新建分组
    poco(text="新建文件夹").click()
    group_name = "新建分组"
    text(group_name,enter=False)
    poco(text="确认").click()
    #删除分组
    find_group_by_name_and_del(group_name)
    sleep(1)
    #返回，去回收站恢复
    poco(desc="").click()
    poco("show recycle").click()
    poco("更多设置").click()
    poco(text="恢复").click()
    assert recycle_bin_is_null()
    poco("<").click()
    #左滑
    swipe((947,86),(250,86))
    poco(text=group_name).click()
    #新建笔记
    poco(text="新建笔记").click()
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name = f"恢复笔记_{random_string()}"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(1)
    #右滑
    swipe((250,86),(947,86))
    sleep(1)
    poco(text="全部笔记").click()
    #删除分组
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].click()
    find_group_by_name_and_del(group_name)
    #返回，去回收站恢复
    poco(desc="").click()
    poco("show recycle").click()
    poco("更多设置").click()
    poco(text="恢复").click()
    assert recycle_bin_is_null()
    poco("<").click()
    swipe((250,86),(947,86))
    sleep(1)
    poco(text="全部笔记").click()
    find_group_by_name_and_del(group_name)
    poco("首页").click()

    


# 新建二级文件夹删除（包含文件）恢复验证
def test_del_folder_and_subfile_recovery(default_group="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #删除回收站笔记
    del_all_files()
    #新建文件夹
    poco(text=default_group).click()
    touch(Template(r"tpl1748249870254.png", record_pos=(0.048, -0.608), resolution=(1200, 1920)))
    file_name = "文件夹_134"
    text(file_name,enter=False)
    poco(text="确认").click()
    #点击新建文件夹
    poco(text=file_name).click()
    poco(text="新建笔记").click()
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name = f"恢复笔记_{random_string()}"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(1)
    poco("<").click()
    sleep(1)
    #删除文件夹
    touch(Template(r"tpl1748938545309.png", record_pos=(0.287, -0.606), resolution=(1200, 1920)))
    poco(text="全部选中").click()
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)
    #恢复
    poco("show recycle").click()
    poco("更多设置").click()
    poco(text="恢复").click()
    poco("<").click()
    #删除文件夹
    del_file()
    poco(text="全部笔记").click()
    poco("首页").click()

 
    
    
# 新建二级文件夹删除（不包含文件）恢复验证
def test_del_folder_recovery(default_group="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #删除回收站笔记
    del_all_files()
    #新建文件夹
    poco(text=default_group).click()
    touch(Template(r"tpl1748249870254.png", record_pos=(0.048, -0.608), resolution=(1200, 1920)))
    file_name = "文件夹_13234"
    text(file_name,enter=False)
    poco(text="确认").click()
    #删除新建的文件夹
    del_file()
    poco("show recycle").click()
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="恢复").click()
    sleep(1)
    # assert recycle_bin_is_null()
    poco("<").click()
    #删除文件
    del_file()
    poco(text="全部笔记").click()
    poco("首页").click()
    

    
    
#回收站列表右侧更多按钮彻底删除验证
def test_del_note_forever():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    poco(text="新建笔记").click()
    sleep(1)
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name = "彻底删除笔记"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(1)
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    #回收站彻底删除
    poco("show recycle").click()
    sleep(1)
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="彻底删除").click()
    poco(text="确认").click()
    poco("<").click()
    poco("首页").click()
    

    
    
    


if __name__=="__main__":
    test_note_in_folder_recovery()
    test_del_notes_recovery()
    test_del_root_folder_no_subfolder_recovery()
    test_del_folder_recovery()
    test_del_folder_and_subfile_recovery()#报错
    test_del_note_forever()
    test_note_not_in_folder_recovery()
    

