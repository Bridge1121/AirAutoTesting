# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"

import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))


#笔记页面显示（未登录账号）
def notes_logout_init():
    if is_login()==False:
        logout()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #4、回到首页
    poco("首页").click()
    
# 已登录账号，有笔记
def notes_login_init():
    if is_login()==True:
        login()
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #4、回到首页
    poco("首页").click()
    
    

    
        
        
        
        

        
        
        
if __name__=="__main__":
    notes_logout_init()
    notes_login_init()
    

