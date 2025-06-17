# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"

import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))


#删除文件
def del_file():
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    

    
# 当前分组下创建文件夹，文件夹所在分组校验
def test_create_folder_and_verify_group_assignment(group_name="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #点击分组
    poco(text=group_name).click()
    #点击新建文件夹
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("android.widget.Button").click()
    #输入文件夹名
    text("测试分组下新建文件夹",enter=False)
    sleep(1)
    poco(text="确认").click()
    #删除文件夹
    del_file()
    #点击全部笔记
    poco(text="全部笔记").click()
    #返回首页
    poco("首页").click()

  
# 笔记列表【更多】移动分组入口创建文件夹验证
def test_move_group_create_folder(group_name="默认笔记",floder_name="移动分组入口创建文件夹"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #点击分组
    poco(text=group_name).click()
    #新建笔记
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
    #点击列表第一个笔记的更多
    poco("更多设置").click()
    #点击移动分组
    poco(text="移动分组").click()
    sleep(1)
    #点击新建文件夹
    poco(text="新建文件夹").click()
    poco(text="请输入文件夹名称").click()
    sleep(1)
    text(floder_name,enter=False)
    poco(text="确认").click()
    poco("Filled.Clear").click()
    #删除第一条笔记
    del_file()
    #点击全部笔记
    sleep(1)
    poco(text="全部笔记").click()
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].click()
    sleep(1)
    find_group_by_name_and_del(floder_name)
    poco(desc="").click()
    #返回首页
    poco("首页").click()
    
#笔记详情页（重命名）移动分组入口创建文件夹验证   
def test_note_info_create_folder(group_name="默认笔记", folder_name="笔记详情页创建文件夹"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    poco(text=group_name).click()
    #点击新建笔记
    poco(text="新建笔记").click()
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name ="笔记详情移动分组"
    text(note_name, enter=False)    
    sleep(1)
    touch((169,52))
    sleep(1)
    #点击所属分组名
    poco(text=group_name).click()
    #点击新建文件夹
    poco(text="新建文件夹").click()
    #输入文件夹名
    text(folder_name,enter=False)
    sleep(1)
    poco(text="确认").click()
    #关闭弹窗
    poco("Filled.Clear").click()
    sleep(1)
    #收起标题栏
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[0].click()
    #返回
    poco("返回").click()
    #删除笔记
    del_file()
    #点击分组名
    poco(text="全部笔记").click()
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].click()
    sleep(1)
    find_group_by_name_and_del(folder_name)
    poco(desc="").click()
    sleep(1)
    #首页
    poco("首页").click()
    
    
# 当前文件夹可创建多级树形子文件夹验证，十级
def test_create_tree_folder(group_name="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    poco(text=group_name).click()
    sleep(1)
    #新建文件夹
    for i in range(0,10):
        touch(Template(r"tpl1748249870254.png", record_pos=(0.048, -0.608), resolution=(1200, 1920)))
        #输入文件夹名
        name = f"文件夹_{i}"
        text(name, enter=False)
        sleep(1)
        poco(text="确认").click()
        #点击新建的文件夹
        poco(text=name).click()
    for i in range(0,10):
        poco("<").click()
    #删除文件夹
    del_file()
    poco(text="全部笔记").click()
    #返回首页
    poco("首页").click()
    


    

#笔记列表右侧菜单功能校验-文件夹重命名，然后删除
def test_rename_folder_and_delete(group_name="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #点击分组
    poco(text=group_name).click()
    #新建文件夹
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("android.widget.Button").click()
    #输入文件夹名
    floder_name="文件夹重命名"
    text(floder_name, enter=False)
    sleep(1)
    #点击确认
    poco(text="确认").click()
    #点击新建文件夹的更多
    poco("更多设置").click()
    #点击重命名
    poco(text="重命名").click()
    sleep(1)
    text("123",enter=False)
    poco(text="确认").click()
    #点击新建文件夹的更多
    poco("更多设置").click()
    sleep(1)
    #点击删除
    poco(text="删除").click()
    #点击确认
    poco(text="确认").click()
    sleep(1)
    poco(text="全部笔记").click()
    #返回首页
    poco("首页").click()



    


# 笔记列表右侧菜单功能校验-文件夹移动分组
def test_folder_move_group(group_name="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    #点击分组
    poco(text=group_name).click()
    #新建文件夹
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("android.widget.Button").click()

    #输入文件夹名
    random_str = random_string()
    str1 = f"文件夹_{random_str}"
    text(str1, enter=False)
    sleep(1)
    #点击确认
    poco(text="确认").click()
    #点击更多
    poco("更多设置").click()
    #点击移动分组
    poco(text="移动分组").click()
    sleep(1)
    #新建分组
    poco(text="新建文件夹").click()
    floder_name = "文件夹移动分组"
    text(floder_name, enter=False)
    sleep(1)
    #点击确认
    poco(text="确认").click()
    #上滑
    swipe((644,1148),(460,780))
    #点击要移动到的分组名
    poco(text=floder_name).click()
    #点击移动至此
    poco(text="移动至此").click()
    #左滑
    swipe((947,85),(184,88))
    #点击移动的分组名
    poco(text=floder_name).click()
    sleep(1)
    #删除文件
    del_file()
    #右滑
    swipe((252,112),(947,112))
    sleep(1)
    poco(text="全部笔记").click()
    #删除新建的分组
    poco(text="全部笔记").click()
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].click()
    sleep(1)
    find_group_by_name_and_del(floder_name)
    poco(desc="").click()
    #返回首页
    poco("首页").click()
    

#文件夹中的笔记可移动至其他笔记验证
def test_note_move(default_group="默认笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #点击默认笔记
    poco(text=default_group).click()
    #新建文件夹，三级
    for i in range(0,3):
        touch(Template(r"tpl1748249870254.png", record_pos=(0.048, -0.608), resolution=(1200, 1920)))
        #输入文件夹名
        name = f"文件夹_{i}"
        text(name, enter=False)
        sleep(1)
        poco(text="确认").click()
        #点击新建的文件夹
        poco(text=name).click()
    #新建笔记
    poco(text="新建笔记").click()
    #输入笔记内容
    poco("更多设置").click()
    sleep(1)
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    ss = "笔记移动至其他笔记"
    text(ss, enter=False)
    poco("返回").click()
    #点击创建笔记的更多
    poco("更多设置").click()
    poco(text="移动分组").click()
    poco(text=default_group).click()
    poco(text="移动至此").click()
    sleep(1)
    for i in range(0,3):
        poco("<").click()
#     sleep(1)
#     assert poco(text=ss).exists()
    sleep(1)
    #删除创建的文件
    del_file()
    del_file()
    #右滑
    swipe((252,112),(947,112))
    poco(text="全部笔记").click()
    poco("首页").click()
    
    

    



    
    
    
if __name__=="__main__":
    test_rename_folder_and_delete()
    test_note_info_create_folder()
    test_create_new_folder()
    test_create_folder_and_verify_group_assignment()
    test_move_group_create_folder()
    test_folder_move_group()
    test_note_info_create_folder()
    test_create_tree_folder()
    test_note_move()
