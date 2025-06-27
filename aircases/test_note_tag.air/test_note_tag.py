__author__ = "wenxiu.tian_sx"
import sys

import allure
import pytest
from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))

pytestmark = [allure.feature("笔记标签模块用例"), allure.epic("办公本v2.4.0")]


def find_tag(tag_name):
    tag_pos = poco(text=tag_name).get_position()
    touch(tag_pos,duration=2)


    
#在删除笔记之前删除添加的所有标签
def del_all_tags_before_del_note():
    touch(Template(r"tpl1749785507158.png", record_pos=(0.458, -0.494), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    list = poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.widget.ScrollView")[1].children()
    for i in range(len(list)):
        list[i].long_click(duration=2)
        poco(text="删除").click()
        if poco(text="提示").exists():
            poco(text="确认").click()
    
    #返回
    poco(text="完成").click()


    
    
#点击更多>编辑标签，跳转到编辑标签页,输入内容后点√后标签添加成功
@pytest.mark.testcase
@allure.description("点击更多>编辑标签，跳转到编辑标签页,输入内容后点√后标签添加成功")
@allure.title("点击更多>编辑标签，跳转到编辑标签页,输入内容后点√后标签添加成功")
def test_add_tag_and_rename():
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
    sleep(2)
    #插入文字
    touch((581,997))
    sleep(2)
    text("测试添加标签",enter=False)
    poco("返回").click()
    #编辑标签
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    tag_name="标签1"
    text(tag_name,enter=True)
    poco(text="完成").click()
    sleep(1)
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    #重命名标签
    list = poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.widget.ScrollView")[1].children()
    for i in range(len(list)):
        if list[i].get_text() == tag_name:
            list[i].long_click(duration=2)
            break
    sleep(2)
    poco(text="重命名").click()
    text("23",enter=False)
    #点击完成
    poco(text="完成").click()
    #点击返回
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View").click()
    sleep(1)
    #删除创建的所有标签
    del_all_tags_before_del_note()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    

    
    
    
#长按标签点击标签菜单栏中删除后选择确认
@pytest.mark.testcase
@allure.description("长按标签点击标签菜单栏中删除后选择确认")
@allure.title("长按标签点击标签菜单栏中删除后选择确认")
def test_note_tag_del():
#     if is_login()==True:
#         login()
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
    text("测试添加标签",enter=False)
    poco("返回").click()
    #编辑标签
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    tag_name="33243"
    text(tag_name,enter=True)
    poco(text="完成").click()
    sleep(1)
    #删除新建的标签
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    #重命名标签
    list = poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.widget.ScrollView")[1].children()
    for i in range(len(list)):
        if list[i].get_text() == tag_name:
            list[i].long_click(duration=2)
            break
    sleep(2)
    #点击删除
    poco(text="删除").click()
    poco(text="确认").click()
    #返回
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View").child("android.view.View").click()
    poco(text="保存").click()
    #删除新建的笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

    
#无标签笔记详情页点标题后下方显示笔记分组和添加标签,点击标题后点击添加标签
@pytest.mark.testcase
@allure.description("无标签笔记详情页点标题后下方显示笔记分组和添加标签,点击标题后点击添加标签")
@allure.title("无标签笔记详情页点标题后下方显示笔记分组和添加标签,点击标题后点击添加标签")
def test_note_title_add_tag():
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #点击标题
    touch((175,40))
    sleep(1)
    #添加标签
    poco(text="添加标签").click()
    tag_name="标题添加标签"
    text(tag_name,enter=False)
    poco(text="完成").click()
    poco("返回").click()
    #返回到笔记列表页
    poco("返回").click()
    sleep(1)
    #删除创建的所有标签
    del_all_tags_before_del_note()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
#有标签笔记进入详情页点击标题后点击默认分组后进入分组编辑页,修改分组后在添加标签
@pytest.mark.testcase
@allure.description("有标签笔记进入详情页点击标题后点击默认分组后进入分组编辑页,修改分组后在添加标签")
@allure.title("有标签笔记进入详情页点击标题后点击默认分组后进入分组编辑页,修改分组后在添加标签")
def test_note_with_tag_edit_group_add_tag(group_name="测试修改分组一"):
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #返回添加标签
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    tag_name1="标签123"
    text(tag_name1,enter=False)
    poco(text="完成").click()
    #再次打开笔记
    touch((400,380))
    sleep(1)
    #点击标题
    touch((175,40))
    sleep(1)
    #点击默认分组
    poco(text="默认笔记").click()
    #修改分组
    poco(text=group_name).click()
    poco(text="移动至此").click()
    #点击添加标签
    poco(text="添加标签").click()
    tag_name2="标题添加标签"
    text(tag_name2,enter=False)
    poco(text="完成").click()
    sleep(1)
    poco("返回").click()
    sleep(1)
    poco("返回").click()
    sleep(1)
    #删除创建的所有标签
    del_all_tags_before_del_note()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    

#笔记列表页笔记标签显示为蓝色字体验证，标签列表取消标签后，笔记列表不再显示已取消的标签验证
@pytest.mark.testcase
@allure.description("笔记列表页笔记标签显示为蓝色字体验证，标签列表取消标签后，笔记列表不再显示已取消的标签验证")
@allure.title("笔记列表页笔记标签显示为蓝色字体验证，标签列表取消标签后，笔记列表不再显示已取消的标签验证")
def test_note_tag_ui_cancel():
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
    sleep(2)
    #插入文字
    touch((581,997))
    sleep(2)
    text("测试添加标签",enter=False)
    poco("返回").click()
    #编辑标签
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    tag_name1="未知少年"
    text(tag_name1,enter=True)
    poco(text="完成").click()
    sleep(1)
    
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    #再新增一个标签
    tag_name2="已知少女"
    text(tag_name2,enter=True)
    poco(text="完成").click()
    #删除一个标签
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    #重命名标签
    list = poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.widget.ScrollView")[1].children()
    for i in range(len(list)):
        if list[i].get_text() == tag_name1:
            list[i].long_click(duration=2)
            break
    poco(text="删除").click()
    poco(text="确认").click()
    #返回
    poco(text="完成").click()
    sleep(1)
    #删除创建的所有标签
    del_all_tags_before_del_note()
    #删除文件
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()


    
#笔记标签数量为10个限制超出后toast提示验证
@pytest.mark.testcase
@allure.description("笔记标签数量为10个限制超出后toast提示验证")
@allure.title("笔记标签数量为10个限制超出后toast提示验证")
def test_note_tag_num():
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
    sleep(2)
    #插入文字
    touch((581,997))
    sleep(2)
    text("测试添加标签",enter=False)
    poco("返回").click()
    #编辑10个标签
    for i in range(10):
        touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
        poco(text="编辑标签").click()
        tag_name1=f"标签数量{i}{i}"
        text(tag_name1,enter=True)
        poco(text="完成").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    text("超额标签",enter=True)
    sleep(1)
    assert not poco(text="超额标签").exists()
    #返回
    poco(desc="").click()
    sleep(1)
    #删除创建的所有标签
    del_all_tags_before_del_note()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()


# 二次确认弹窗点击确认后，关联的笔记不再显示该标签验证
@pytest.mark.testcase
@allure.description("二次确认弹窗点击确认后，关联的笔记不再显示该标签验证")
@allure.title("二次确认弹窗点击确认后，关联的笔记不再显示该标签验证")
def test_note_ass_tag_del():
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
    sleep(2)
    #插入文字
    touch((581,997))
    sleep(2)
    text("测试添加标签",enter=False)
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    tag_name1="关联标签"
    text(tag_name1,enter=True)
    poco(text="完成").click()
    #删除关联标签
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    #点击关联的标签
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.widget.ScrollView")[0].child("android.view.View")\
    .child("android.widget.TextView").click()
    #点击删除
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.widget.ScrollView")[0]\
    .child("android.view.View").click()
    poco(desc="").click()
    poco(text="保存").click()
    sleep(1)
    #删除创建的所有标签
    del_all_tags_before_del_note()
    #删除
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()


    
# 标签页增加筛选结果可筛选出标签对应的笔记验证,所有标签（标签列表）支持长按显示悬浮菜单“重命名”“删除”按钮验证
@pytest.mark.testcase
@allure.description("标签页增加筛选结果可筛选出标签对应的笔记验证,所有标签（标签列表）支持长按显示悬浮菜单“重命名”“删除”按钮验证")
@allure.title("标签页增加筛选结果可筛选出标签对应的笔记验证,所有标签（标签列表）支持长按显示悬浮菜单“重命名”“删除”按钮验证")
def test_note_tag_sift():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #创建三条笔记并分别设置标签
    for i in range(3):
        #新建笔记
        poco(text="新建笔记").click()
        sleep(2)
        poco("更多设置").click()
        poco(text="插入文字").click()
        sleep(2)
        #插入文字
        touch((581,997))
        sleep(2)
        note_name=f"测试标签筛选_{i}"
        text(note_name,enter=False)
        sleep(1)
        poco("返回").click()
        sleep(1)
        touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
        poco(text="编辑标签").click()
        tag_name1=chr(97+i)
        text(tag_name1,enter=True)
        sleep(1)
        poco(text="完成").click()
        touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
        poco(text="编辑标签").click()
        list = poco("android.widget.FrameLayout")\
        .offspring("androidx.compose.ui.platform.ComposeView")\
        .child("android.view.View")\
        .child("android.view.View")\
        .child("android.widget.ScrollView")[1].children()
        for i in range(len(list)):
            if list[i].get_text() == tag_name1:
                list[i].long_click(duration=2)
                break
        touch((337,1762))
        poco(desc="").click()
        sleep(1)
    #删除创建的所有标签
    del_all_tags_before_del_note()
    #删除笔记
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

    
def test():
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="编辑标签").click()
    poco("android.widget.FrameLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.widget.ScrollView")[1]\
    .child("android.widget.TextView")[25].long_click(duration=2)
    
    
if __name__=="__main__":
#     test_add_tag_and_rename()
#     test_note_tag_del()
#     test_note_title_add_tag()
#     test_note_with_tag_edit_group_add_tag()
#     test_note_tag_ui_cancel()
#     test_note_tag_num()
#     test_note_ass_tag_del()
    test_note_tag_sift()
#     del_all_tags_before_del_note()
#     test()
    