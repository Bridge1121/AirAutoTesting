# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))
    
    
#AI助手deep seek页打断对话,输入对话后立马点击暂停键打断对话，对话过程中点击暂停键打断对话，AI对话过程中连续多次打断对话
def test_deepseek_interrupt_conversation():
    if is_login()==True:
        login()
    #开始ai对话
    poco("AI助手").click()
    #进入deepseek
    poco(text="发现更多AI助手>>").click()
    poco(text="DeepSeek大模型助手").click()
    #长按语音输入
    poco(text="按住说话").long_click(duration=3)
    poco("返回").click()
    poco("AI助手中心").click()
    poco("首页").click()


    
    
    
    
#在deep seek进行的对话能够在AI助手页历史会话页面查看
def test_deepseek_history():
    if is_login()==True:
        login()
    #开始ai对话
    poco("AI助手").click()
    #进入deepseek
    poco(text="发现更多AI助手>>").click()
    poco(text="DeepSeek大模型助手").click()
    #输入问题
    if poco(text="按住说话").exists():
        poco("键盘输入").click()
    else:
        poco(text="在此输入您的想法~").click()
    ques = "我是deepseek"
    text(ques,enter=False)
    poco("分享").click()
    sleep(5)
    #返回
    poco("返回").wait_for_appearance(timeout=TIME_OUT)
    poco("返回").click()
    poco("AI助手中心").click()
    #打开历史记录查看
    poco(text="历史记录").click()
    sleep(5)
    # assert poco(text=ques).exists()
    sleep(1)
    poco("返回").click()
    poco("首页").click()

    


    


#语音输入模式下点击上传文件时会跳转到AI助手页
def test_deepseek_voice_input_upload():
    if is_login()==True:
        login()
    #开始ai对话
    poco("AI助手").click()
    #进入deepseek
    poco(text="发现更多AI助手>>").click()
    poco(text="DeepSeek大模型助手").click()
    #语音输入模式下，上传文件
    poco("文件输入").click()
    #右滑返回
    swipe((3,900),(200,900))
    sleep(1)
    poco("返回").click()
    poco("AI助手中心").click()
    poco("首页").click()

    
    
    
    

    
if __name__=="__main__":
    test_deepseek_interrupt_conversation()
    test_deepseek_history()
    test_deepseek_voice_input_upload()
    
    
    
    
    
    