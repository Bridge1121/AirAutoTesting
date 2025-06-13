# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))
    
    
    
    
def test():
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[10].child("android.view.View")\
    .child("android.view.View")[0]\
    .child("android.widget.TextView")[0].click()
    
    
# 录音时返回后，再进入该笔记
def test_note_recording_back():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    #输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name="测试录音返回"
    text(note_name,enter=False)
    sleep(1)
    #点击录音
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].child("手写笔").click()
    sleep(2)
    #返回
    poco("返回").click()

    sleep(2)
    #点击新建的笔记
    poco(text=note_name).click()
#     poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View").child("android.view.View")\
#     .child("android.view.View")[10].child("android.view.View")\
#     .child("android.view.View")[0]\
#     .child("android.widget.TextView")[0].click()
    #验证是否弹窗
#     assert poco(text="是否继续录音？").exists()
#     sleep(1)
#     #点击确定，继续录音
    poco(text="继续录音").click()
    sleep(1)
    #点击暂停录音
    poco(text="暂停").click()
    sleep(1)
#     点击继续录音
    poco(text="暂停").click()
    #返回
    poco("返回").click()
    #删除新建的笔记
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)
    poco("首页").click()
    


# 无网络时开启录音
def test_note_recording_no_internet():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #断网
    #下拉菜单
    swipe((1036,0),(886,432))
    sleep(1)
    poco("com.aispeech.ccui.systemui:id/cellGrid")\
    .child("android.widget.LinearLayout")[0]\
    .child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    touch((867,1450))
    #新建笔记
    poco(text="新建笔记").click()
    #点击录音
    poco("android.widget.LinearLayout")\
    .offspring("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[6].child("手写笔").click()
    sleep(1)
    assert poco(text="*当前网络不可用，请检查您的网络").exists()
    #返回
    poco("返回").click()
    #联网
    #下拉菜单
    swipe((1036,0),(886,432))
    sleep(1)
    poco("com.aispeech.ccui.systemui:id/cellGrid")\
    .child("android.widget.LinearLayout")[0]\
    .child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    touch((867,1450))
    sleep(1)
    #删除新建的笔记
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)
    poco("首页").click()


#转写过程中点击录音原文的“替换”按钮查看弹窗显示
def test_note_recording_replacement(default_note="测试录音中文",default_group="测试笔记",replaced_text="他",replace_text="狗"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #点击分组
    poco(text=default_group).click()
    sleep(1)
    poco(text=default_note).click()
    sleep(1)
    poco(text="继续录音").click()
    #点击录音原文
    poco(text="录音原文").click()
    #点击替换
    poco(text="查找/替换").click()
    sleep(1)
    #验证ui
    poco(text="替换").click()
    sleep(1)
    assert poco(text="同步替换AI笔记").exists()
    assert poco(text="替换全部").exists()
    poco(text="替换当前").exists()
    sleep(1)
    poco(text="输入您要查找的内容").click()
    text(replaced_text)
    poco(text="输入您要替换的内容").click()
    text(replace_text)
    #勾选ai笔记
    poco(text="同步替换AI笔记").click()
    #替换全部
    poco(text="替换全部").click()
    #结束录音
    poco(text="结束").click()
    #返回
    poco("返回").click()
    poco(text="全部笔记").click()
    poco("首页").click()
    

    
#转写过程中在录音原文中长按文字点击“替换”按钮查看弹窗显示并进行替换内容
def test_note_replacement_long_touch(default_note="测试录音中文",default_group="测试笔记"):
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #点击分组
    poco(text=default_group).click()
    sleep(1)
    poco(text=default_note).click()
    sleep(1)
    poco(text="继续录音").click()
    #点击录音原文
    poco(text="录音原文").click()
    #长按
    touch((56,708), duration=3)
    #点击替换
    poco(text="替换").click()
    sleep(1)
    assert poco(text="同步替换AI笔记").exists()
    assert poco(text="替换全部").exists()
    poco(text="替换当前").exists()
    sleep(1)
    #点击替换
    poco(text="替换全部").click()
    poco(text="结束").click()
    poco("返回").click()
    poco(text="全部笔记").click()
    poco("首页").click()
    
    
    
#长按替换英文字母
# def test_note_alpha_replacement_long_touch(default_note="测试录音英文",default_group="测试笔记"):
#     if is_login()==True:
#         login()
#     #点击笔记
#     poco("笔记").click()
#     sleep(1)
#     #点击分组
#     poco(text=default_group).click()
#     sleep(1)
#     poco(text=default_note).click()
#     sleep(1)
#     poco(text="继续录音").click()
#     #点击录音原文
#     poco(text="录音原文").click()
#     #长按
#     touch((284, 314), duration=3)
#     #点击替换
#     poco(text="替换").click()
#     sleep(1)
#     #点击替换
#     poco(text="替换全部").click()
#     poco(text="结束").click()
#     poco("返回").click()
#     poco(text="全部笔记").click()
#     poco("首页").click()

    
#长按替换英文字母并勾选同步替换ai笔记
# def test_note_alpha_replacement_ai_long_touch(default_note="测试录音英文",default_group="测试笔记"):
#     if is_login()==True:
#         login()
#     #点击笔记
#     poco("笔记").click()
#     sleep(1)
#     #点击分组
#     poco(text=default_group).click()
#     sleep(1)
#     poco(text=default_note).click()
#     sleep(1)
#     poco(text="继续录音").click()
#     #点击录音原文
#     poco(text="录音原文").click()
#     #长按
#     touch((56,708), duration=3)
#     #点击替换
#     poco(text="替换").click()
#     sleep(1)
#     #勾选ai笔记
#     poco(text="同步替换AI笔记").click()
#     #点击替换
#     poco(text="替换全部").click()
#     poco(text="结束").click()
#     poco("返回").click()
#     poco(text="全部笔记").click()
#     poco("首页").click()
    
    
#转写过程中点击管理录音时会有结束录音提示,点击弹窗确认,删除录音
def test_note_recording_manage(note_name="测试管理录音"):
    poco("笔记").click()
    #点击已有录音笔记
    poco(text=note_name).click()
    #点击继续录音
    poco(text="继续录音").click()
    #点击更多设置的管理录音
    poco("更多设置").click()
    poco(text="管理录音").click()
    #验证弹窗
    assert poco(text="结束录音").exists()
    sleep(1)
    #弹窗点击确认
    poco(text="确认").click()
    #跳转到管理界面后，
    #删除一段录音
    #取消全选
    poco("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View").child("Checked").click()
    #删除第一段录音
    poco("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View")[4].child("Checked")[0].click()
    #点击删除
    poco(text="删除录音").click()
    #点击确定
    poco(text="确认").click()
    #退出
    poco("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[2].child("返回").click()
    poco("返回").click()
    poco("首页").click()
    
    

# 点击录音管理默认全选录音后点击“删除录音及文字”再确认删除
def test_note_recording_del_all(note_name="测试管理录音"):
    poco("笔记").click()
    #点击已有录音笔记
    poco(text=note_name).click()
    #点击继续录音
    poco(text="继续录音").click()
    #点击更多设置的管理录音
    poco("更多设置").click()
    poco(text="管理录音").click()
    #验证弹窗
    assert poco(text="结束录音").exists()
    sleep(1)
    #弹窗点击确认
    poco(text="确认").click()
    #跳转到管理界面后，
    #默认全选，点击删除录音
    poco(text="删除录音").click()
    #点击取消
    poco(text="取消").click()
    #退出
    poco("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[2].child("返回").click()
    poco("返回").click()
    poco("首页").click()
    
    
#点击录音管理默认全选录音后点击“删除录音及文字”再确认删除
def test_note_recording_and_text_del(note_name="测试删除录音文字"):
    poco("笔记").click()
    #点击已有录音笔记
    poco(text=note_name).click()
    #点击继续录音
    poco(text="继续录音").click()
    #点击更多设置的管理录音
    poco("更多设置").click()
    poco(text="管理录音").click()
    #验证弹窗
    assert poco(text="结束录音").exists()
    sleep(1)
    #弹窗点击确认
    poco(text="确认").click()
    #跳转到管理界面后，
    poco(text="删除录音及文字").click()
    #点击取消
    poco(text="取消").click()
    #退出
    poco("android.widget.LinearLayout")\
    .offspring("android:id/content")\
    .child("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[2].child("返回").click()
    #点击会后总结
    poco(text="会后总结").click()
    sleep(2)
    poco("返回").click()
    poco("首页").click()
    







    
    
    
    
    
if __name__=="__main__":
    test_note_recording_back()
    test_note_recording_no_internet()
    test_note_recording_replacement()
    test_note_replacement_long_touch()
#     test_note_alpha_replacement_long_touch()
#     test_note_alpha_replacement_ai_long_touch()
    test_note_recording_manage()
    test_note_recording_del_all()
    test_note_recording_and_text_del()
#     test()
    
    
    