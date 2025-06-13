# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))
    
    

#已转写富文本点击回撤，文案整体支持回撤验证,笔记删除再恢复，富文本文案编辑后支持回撤验证
def test_note_rich_text_drawdown():
    if is_login()==True:
        login()
    #清空回收站
    del_all_files()
#     #点击笔记
#     poco("笔记").click()
    sleep(1)
    #新建笔记
    poco(text="新建笔记").click()
    sleep(1)
    #插入多段文字
    pos = (581,997)
    for i in range(3):
        poco("更多设置").click()
        #输入文字
        poco(text="插入文字").click()
        sleep(1)
        touch((pos[0],pos[1]+i*150))
        sleep(2)
        tt = f"添加一段文本哈哈哈_{i}"
        text(tt,enter=False)
    #点击顶部回撤
    poco("撤销").click()
    #点击更多删除笔记
    poco("更多设置").click()
    poco(text="删除笔记").click()
    poco(text="确认").click()
    #点击回收站
    poco("show recycle").click()
    #恢复笔记
    poco("编辑").click()
    poco(text="全部选中").click()
    poco(text="恢复").click()
    sleep(1)
    poco("<").click()
    #点击恢复的笔记
    touch((380,350))
    sleep(1)
    touch(pos)
    #点击编辑
    poco("com.aispeech.tablet:id/tv_selection_edit").click()
    text("编辑一下",enter=False)
    touch((pos[0],pos[1]-150))
    #点击回撤
    poco("撤销").click()
    #返回
    poco("返回").click()
    touch(Template(r"tpl1748339487185.png", record_pos=(0.458, -0.484), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    

    
    
    
    
    
    
if __name__=="__main__":
    test_note_rich_text_drawdown()
    
    
    