# -*- encoding=utf8 -*-
__author__ = "wenxiu.tian_sx"
import sys

from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))

    
    
#书写待办
def test_add_agent():
    if is_login()==True:
        login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text("7月15日与市场部讨论新品发布计划",enter=False)
    poco(text="确认").click()
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    #删除新增的代办
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()



#修改待办内容,在弹窗中点击取消，关闭弹窗,修改待办部分内容，点击确定
def test_edit_agent_text():
    if is_login()==True:
        login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent="8月15日与市场部讨论新品发布计划"
    text(agent,enter=False)
    poco(text="确认").click()
    sleep(1)
    #点击新增的代办
    poco(text=agent).click()
    #输入编辑的内容
    text("hhh",enter=False)
    #点击取消
    poco(text="取消").click()
    #再次编辑
    poco(text=agent).click()
    text("啊啊啊",enter=False)
    #点击确认
    poco(text="确认").click()
    #切换列表视图
    poco(text="列表视图").click()
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    #删除新增的代办
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="日历视图").click()
    poco("首页").click()
    
# 修改待办日期，点击确定
def test_edit_agent_date():
    if is_login()==True:
        login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent="8月15日与市场部讨论新品发布计划"
    text(agent,enter=False)
    poco(text="确认").click()
    sleep(1)
    #点击新增的代办
    #修改日期
    poco(text="今天 17:00").click()
    sleep(1)
    #点击要修改的日期
    touch(Template(r"tpl1749638112487.png", record_pos=(0.008, 0.033), resolution=(1200, 1920)))
    #点击确定
    poco(text="确认").click()
    # poco(text="确认").click()
    poco("首页").click()



# 删除设置日期的待办
def test_del_agent():
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent="12月15日与市场部讨论新品发布计划"
    text(agent,enter=False)
    poco(text="确认").click()
    sleep(1)
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    #删除新增的代办
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
# 按紧迫程度排序-今天
def test_add_agent_today():
    if is_login()==True:
        login()
    poco("待办").click()
    agent_name = "这是今天要完成的代办"
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text(agent_name,enter=False)
    poco(text="确认").click()
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    #删除新增的代办
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
# 按紧迫程度排序-当前时间与待办时间相差24小时的待办，再按创建时间排序
def test_add_agent_tomorrow():
#     if is_login()==True:
#         login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是明天要完成的代办"
    text(agent_name,enter=False)
    #修改日期
    choose_n_days_date(1)
    #确认编辑代办
    poco(text="确认").click()
    #换成列表视图
    poco(text="列表视图").click()
    #按照创建时间排序
    poco("排序").click()
    poco(text="按创建时间").click()
    #按照紧迫程度排序
    poco("排序").click()
    poco(text="按紧迫程度").click()
    #删除新增的代办
    find_del_agent(agent_name)
    #回到日历视图
    poco(text="日历视图").click()
    poco("首页").click()

#待办列表新增待办，选择日期时间并选择待办提醒，查看待办提醒
def test_add_agent_and_notice():
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是有提醒要完成的代办"
    text(agent_name,enter=False)
    #修改日期
    choose_n_days_date(1)
    #添加提醒
    poco("date").click()
    poco("android.widget.FrameLayout")\
    .offspring("android.view.ViewGroup")\
    .child("android.view.View")\
    .offspring("android.widget.ScrollView")\
    .child("android.view.View")[0]\
    .child("more").click()
    #点击准时
    poco(text="准时").click()
    poco(text="确认").click()
    poco(text="确认").click()
    #切换视图，删除代办
    poco(text="列表视图").click()
    sleep(1)
    find_del_agent(agent_name)
    poco(text="日历视图").click()
    poco("首页").click()

# 断网情况下，创建待办，创建完成后重新联网
def test_add_agent_no_internet():
    #断开网络
    #下拉菜单,断开网络
    swipe((1036,0),(886,432))
    poco("com.aispeech.ccui.systemui:id/cellGrid")\
    .child("android.widget.LinearLayout")[0]\
    .child("com.aispeech.ccui.systemui:id/iv_cell_icon").click()
    touch((1000,1600))
    #创建代办
    poco("待办").click()
    agent_name = "这是断网时创建的代办"
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text(agent_name,enter=False)
    poco(text="确认").click()
    sleep(1)
    #恢复网络
    swipe((1036,0),(886,432))
    poco("com.aispeech.ccui.systemui:id/cellGrid")\
    .child("android.widget.LinearLayout")[0]\
    .child("com.aispeech.ccui.systemui:id/iv_cell_icon")\
    .click()
    sleep(5)
    touch((1000,1600))
    #删除创建的代办
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()


# # 在录音AI摘要中将包含日期的待办信息加入待办列表
# def test_ai_abstract_add_agent(note_name="测试录音中文"):
#     poco("笔记").click()
#     #打开准备好的笔记
#     poco(text=note_name).click()
#     swipe_press_ai((95,410),(490,410))
#     #点击复制
#     poco(text="复制").click()
#     #返回
#     poco("返回").click()
#     poco("待办").click()
#     poco(text="请在下方书写待办或点击此处新建待办").click()
#     #长按粘贴
#     poco("android.widget.FrameLayout")\
#     .offspring("android.view.ViewGroup")\
#     .child("android.view.View")\
#     .child("android.view.View")\
#     .child("android.view.View")\
#     .child("android.widget.EditText")[0]\
#     .child("android.view.View").long_click(duration=2)
#     poco("android:id/floating_toolbar_menu_item_text").click()
#     poco(text="确认").click()
#     #删除新建代办
#     touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
#     poco(text="删除").click()
#     poco(text="确认").click()
#     poco("首页").click()
    

    
    
    
#按紧迫程度排序-当前时间与待办时间不满24小时但过凌晨逾期待办，再按创建时间排序
def test_add_agent_less_than_24():
#     if is_login()==True:
#         login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是几小时后要完成的代办"
    text(agent_name,enter=False)
    poco("date").click()
    poco(text="时间段").click()
    poco(text="17:00").click()
    #上滑时间轴
#     swipe((807,1492),(750,1492))
    swipe_press_ai((807,1492),(807,1292))
    #点击确认
    poco("android:id/content")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[3]\
    .child("android.widget.TextView").click()
    #再次确认
    poco(text="确认").click()
    #确认编辑代办
    poco(text="确认").click()
    #删除新增的代办
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    



#按紧迫程度排序-待办-还有不到十天，再按创建时间排序
def test_add_agent_less_than_10_days():
#     if is_login()==True:
#         login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是十天以内要完成的代办"
    text(agent_name,enter=False)
    #修改日期
    choose_n_days_date(5)
    #确认编辑代办
    poco(text="确认").click()
    #换成列表视图
    poco(text="列表视图").click()
    #按照创建时间排序
    poco("排序").click()
    poco(text="按创建时间").click()
    #按照紧迫程度排序
    poco("排序").click()
    poco(text="按紧迫程度").click()
    #删除新增的代办
    find_del_agent(agent_name)
    #回到日历视图
    poco(text="日历视图").click()
    poco("首页").click()



#按紧迫程度排序-待办-还有十天以上，再按创建时间排序
def test_add_agent_more_than_10_days():
#     if is_login()==True:
#         login()
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是10天以后要完成的代办"
    text(agent_name,enter=False)
    #修改日期
    choose_n_days_date(11)
    #确认编辑代办
    poco(text="确认").click()
    #换成列表视图
    poco(text="列表视图").click()
    #按照创建时间排序
    poco("排序").click()
    poco(text="按创建时间").click()
    #按照紧迫程度排序
    poco("排序").click()
    poco(text="按紧迫程度").click()
    #删除新增的代办
    find_del_agent(agent_name)
    #回到日历视图
    poco(text="日历视图").click()
    poco("首页").click()


#创建笔记输入文本，增加代办
def test_note_add_agent():
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
    note_name="输入文本添加代办"
    text(note_name, enter=False)
    touch((581,1197))
    sleep(1)
    poco("com.aispeech.tablet:id/editTextView").click()
    #加入代办
    poco("com.aispeech.tablet:id/tv_selection_todo").click()
    poco(text="确认").click()
    poco("返回").click()
    #删除新建的代办
    poco("待办").click()
    poco(text="列表视图").click()
    find_del_agent(note_name)
    poco(text="日历视图").click()
    #删除新增的笔记
    poco("笔记").click()
    #点击默认笔记
    poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[0]\
    .child("android.view.View")[1]\
    .child("android.widget.TextView").click()
    sleep(1)
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="全部笔记").click()
    poco("首页").click()


#新增超长文本内容待办
def test_add_long_text_agent():
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    text("我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办我要添加一个超长文本的代办",enter=False)
    poco(text="确认").click()
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    #删除新增的代办
    poco(text="删除").click()
    poco(text="确认").click()
    poco("首页").click()
    
    
    
def test():
#     choose_n_days_date(20)
#     swipe_press_ai((807,1492),(807,1292))
#     swipe_press_ai((95,410),(490,410))
    poco("更多设置").click()
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="全部笔记").click()

    
    
#待办列表新增待办，选择日期，时间选无，并且进行编辑
def test_add_agent_no_time_and_edit():
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name="这是一条没有时间的代办"
    text(agent_name,enter=False)
    #删除时间
    if poco("clean").exists():
        poco("clean").click()
    # poco("clean").click()
    poco(text="确认").click()
    #切换列表视图
    poco(text="列表视图").click()
    #修改代办的年月日
    agents = poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .children()
    for i  in range(len(agents)):
        if agents[i].get_text() == agent_name:
            agents[i].click()
            break
    #点击编辑年月日
    poco("date").click()
    poco("切换为选择年份").click()
    #切换年份
    poco("android.widget.FrameLayout")\
    .offspring("android.view.ViewGroup")\
    .child("android.view.View")\
    .offspring("android.widget.ScrollView")\
    .child("android.view.View")[0]\
    .child("android.view.View")\
    .child("android.view.View")[1]\
    .child("android.view.View")\
    .child("android.widget.TextView")[8]\
    .child("android.view.View").click()
    touch((685,828))
    poco(text="确认").click()
    poco(text="确认").click()
    #删除新增的代办
    find_del_agent(agent_name)
    #切换回来
    poco(text="日历视图").click()
    poco("首页").click()
            
    
#在待处理列表设置代办重点关注，会同步到重点标记列表中
def test_agent_focus_on():
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是需要重点关注的代办"
    text(agent_name,enter=False)
    poco(text="确认").click()
    poco(text="列表视图").click()
    #设置重点关注
    agents = poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .children()
    for i  in range(len(agents)):
        if agents[i].get_text() == agent_name:
            agents[i+2].click()
            poco(text="重点关注").click()
            break
    #删除新增的代办
    find_del_agent(agent_name)
    poco(text="重点").click()
    poco(text="待处理").click()
    poco(text="日历视图").click()
    poco("首页").click()
    

# 删除所有待办
def test_del_all_agents():
    poco("待办").click()
    poco(text="列表视图").click()
    agents = poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .children()
#     .child("android.widget.TextView")
    
    if len(agents)>0:
        for i in range(len(agents)):
            if agents[i].get_name() == "android.widget.TextView":
                agents[i+2].click()
                #删除新增的代办
                poco(text="删除").click()
                poco(text="确认").click()
                sleep(1)
    poco(text="日历视图").click()
    poco("首页").click()
    
    
# 完成未设日期的待办显示，完成已设日期的待办显示
def test_finish_agent():
    #创建一条有日期的代办，并点击完成
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是一条完成的代办"
    text(agent_name,enter=False)
    poco(text="确认").click()
    poco(text="列表视图").click()
    agents = poco("androidx.compose.ui.platform.ComposeView")\
    .child("android.view.View")\
    .child("android.view.View")\
    .child("android.view.View")[7]\
    .children()
    for i  in range(len(agents)):
        if agents[i].get_text() == agent_name:
            #点击勾选完成
            agents[i+1].click()
            #2s内再次点击
            agents[i+1].click()
            sleep(2)
            agents[i+1].click()
            break
    poco(text="已完成").click()
    sleep(1)
    poco(text="待处理").click()
    poco(text="日历视图").click()
    #创建一条没有时间的代办
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name1 = "这是一条完成的没有时间的代办"
    text(agent_name1,enter=False)
    poco(text="确认").click()
    poco(text="列表视图").click()
    for i  in range(len(agents)):
        if agents[i].get_text() == agent_name1:
            #点击勾选完成
            agents[i+1].click()
            #2s内再次点击
            agents[i+1].click()
            sleep(2)
            agents[i+1].click()
            break
    poco(text="已完成").click()
    sleep(1)
    #删除已完成的代办
    touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="待处理").click()
    poco(text="日历视图").click()
    poco("首页").click()

    
# 重点关注列表有数据，一行最多显示26个字,编辑待办信息后排序不变
def test_long_text_agent_focus_on():
    poco("待办").click()
    poco(text="请在下方书写待办或点击此处新建待办").click()
    agent_name = "这是一条完成的代办这是一条完成的代办这是一条完成的代办这是一条完成的代办"
    text(agent_name,enter=False)
    poco(text="确认").click()
    poco(text="列表视图").click()
    poco(desc="").click()
    poco(text="重点关注").click()
    poco(text="重点").click()
    sleep(1)
    #编辑代办内容
    poco(text=agent_name).click()
    text(agent_name,enter=False)
    poco(text="确认").click()
    sleep(1)
    #删除重点关注的笔记
    touch(Template(r"tpl1750059960404.png", record_pos=(0.449, -0.083), resolution=(1200, 1920)))
    poco(text="删除").click()
    poco(text="确认").click()
    poco(text="待处理").click()
    poco(text="日历视图").click()
    poco("首页").click()


# # 当重点关注列表数据超过一屏时，下翻可查看所有数据
# def test_agent_focus_on_swipe():
#     poco("待办").click()
#     for i in range(6):
#         poco(text="请在下方书写待办或点击此处新建待办").click()
#         agent_name = f"这是一条完成的代办_{i}"
#         text(agent_name,enter=False)
#         #重点关注
#         poco("重点模式").click()
#         poco(text="确认").click()
#     poco(text="列表视图").click()
#     poco(text="重点").click()
#     swipe((630,1700),(630,1300))
#     poco(text="待处理").click()
#     poco(text="日历视图").click()
#     poco("首页").click()

#     focus_agents = poco("androidx.compose.ui.platform.ComposeView")\
#     .child("android.view.View")\
#     .child("android.view.View")\
#     .child("android.view.View")[7].children()
#     num = 5
#     for i in range(len(focus_agents)):
#         if focus_agents[i].get_name == "android.widget.TextView":
#             ss = "这是一条完成的代办_"+num
#             print(ss)
#             if focus_agents[i].get_text() == ss:
#                 focus_agents[i+3].click()
#                 num=num-1
#             if num<0:
#                 break
                
                
    
    

    


    
    

    

    


    

if __name__=="__main__":
    test_add_agent()
    test_edit_agent_text()
    test_edit_agent_date()
    test_del_agent()
    test_add_agent_today()
    test_add_agent_and_notice()
    test_add_agent_less_than_24()
    test_add_agent_tomorrow()
    test_add_agent_less_than_10_days()
    test_add_agent_more_than_10_days()
    test_add_agent_no_internet()
    test_ai_abstract_add_agent()
    test_note_add_agent()
    test_add_agent_no_time_and_edit()
    test_agent_focus_on()
    test_del_all_agents()
    test_finish_agent()
    test_long_text_agent_focus_on()
    test_add_long_text_agent()
#     test()
#     find_del_agent("这是明天要完成的代办")
    
    
    
    