# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"


import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))
    

#已登录账号创建的笔记，退出登录后，创建的笔记不会显示在笔记列表中
def test_note_not_exist_after_logout():
    if is_login()==True:#未登录
        login()
    #1、创建笔记
    timestamp = create_new_notes()
    #2、退出登录
    logout()
    #3、查看笔记列表
    #点击笔记
    poco("笔记").click()
    assert not poco(text=timestamp).exists()
    sleep(1)
    #4、回到首页
    poco("首页").click()

    
#切换登录账号后，笔记不会合并
# def test_notes_do_not_merge_across_accounts():
#     #1、已登录账号A，新建笔记
#     timestamp = create_new_notes()
#     #2、退出账号
#     logout()
#     #3、登录其它账号B
#     login()
#     #4、查看笔记列表是否有A新建的笔记
#     #点击笔记
#     poco("笔记").click()
#     assert not poco(text=timestamp).exists()
#     #5、返回首页
#     poco("首页").click()


#未登录账号创建的笔记，登录账号时，会自动合并到账号中
def test_guest_notes_merge_into_account_after_login():
    #判断是否登录账号
    if is_login()==True:
        #2、新建笔记
        timestamp = create_new_notes()
        #3、登录账号
        login()
        #4、查看笔记列表是否合并了刚才创建的笔记
        poco("笔记").click()
        assert poco(text=timestamp).exists()
        #回到首页
        poco("首页").click()

    
    
if __name__=="__main__":
#     test_notes_do_not_merge_across_accounts()
    test_note_not_exist_after_logout()
    test_guest_notes_merge_into_account_after_login()
    

    

