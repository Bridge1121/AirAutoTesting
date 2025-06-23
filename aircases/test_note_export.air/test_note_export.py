# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))


# 保存到本地，导出完成弹窗选项立即打开验证
def test_note_export():
    #点击笔记
    poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    poco("更多设置").click()
    #点击分享笔记
    poco(text="分享笔记").click()
    sleep(2)
    #点击导出文件
    poco(text="导出文件").click()
    poco(text="保存到本地").click()
    sleep(1)
    #关闭
    poco("close dialog").click()
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
#更多分享方式获取可根据当前办公本已下载app进行选择验证
def test_note_share_method():
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
    text("测试网页转pdf",enter=False)
    sleep(1)
    poco("更多设置").click()
    #点击分享笔记
    poco(text="分享笔记").click()
    sleep(2)
    #点击更多
    poco(text="更多").click()
    poco(text="网页转PDF").click()
    sleep(8)
    poco("cn.wps.moffice_eng:id/btn_export").click()
    sleep(2)
    poco("cn.wps.moffice_eng:id/titlebar_back_icon").click()
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
    
    
if __name__=="__main__":
    test_note_export()
    test_note_share_method()
    
    
    
    