# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"

import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *


auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))
 

def test():
    poco("更多设置").click()
    poco(text="分享笔记").click()
    poco("close dialog").click()

    



# 二维码自动生成验证
def test_qr_code_gengerate():
    # if is_login()==True:
    #     login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name="生成二维码"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(2)
    #点击更多
    poco("更多设置").click()
    poco(text="分享笔记").click()
    #校验是否生成二维码
    sleep(1)
    assert poco("二维码").exists()
    poco("close dialog").click()
    #删除新建的笔记
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()

# 分享设置入口验证
def test_share_portals():
    # if is_login()==True:
    #     login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581,997))
    sleep(2)
    note_name="分享设置入口验证"
    text(note_name, enter=False)
    poco("返回").click()
    sleep(2)
    #点击更多
    poco("更多设置").click()
    poco(text="分享笔记").click()
    #点击分享设置
    poco(text="分享设置").click()
    sleep(1)
    poco("android.widget.FrameLayout")\
    .offspring("android.view.ViewGroup")\
    .child("android.view.View").child("android.view.View")\
    .child("android.view.View").child("android.view.View")[0]\
    .child("close dialog").click()
    poco("close dialog").click()
    #删除新建的笔记
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
#会后总结分享验证
# def test_post_meeting_summary(default_group="测试笔记",default_note = "测试分享"):
#     if is_login()==True:
#         login()
#     #点击笔记
#     poco("笔记").click()
#     sleep(1)
#     #点击默认分组
#     poco(text=default_group).click()
#     #点击测试笔记更多
#     poco("更多设置").click()
#     poco(text="分享笔记").click()
#     #点击会后总结
#     poco(text="会后总结").click()
#     sleep(1)
#     #校验是否生成二维码
#     sleep(1)
#     assert poco("二维码").exists()
#     #点击分享设置
#     poco(text="分享设置").click()
#     poco("android.widget.FrameLayout")\
#     .offspring("android.view.ViewGroup")\
#     .child("android.view.View").child("android.view.View")\
#     .child("android.view.View").child("android.view.View")[0]\
#     .child("close dialog").click()
#     poco("close dialog").click()
#     #点击全部笔记
#     poco(text="全部笔记").click()
#     poco("首页").click()



            
            
            
if __name__=="__main__":
    test_qr_code_gengerate()
    test_share_portals()
#     test_post_meeting_summary()
