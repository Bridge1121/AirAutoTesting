# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"

import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))
            
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
    