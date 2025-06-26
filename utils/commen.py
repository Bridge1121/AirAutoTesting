import re
from datetime import datetime, timedelta

from airtest.core.api import *
from airtest.core.android.touch_methods.base_touch import *
import random
import string


auto_setup(__file__, logdir=True, devices=["Android://127.0.0.1:5037/AINOTEA224042300042"])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
dev=device()
TIME_OUT=100


def try_back_to_home(max_try=5, interval=1):
    """
    尝试多次返回首页，如果返回成功则返回 True，失败则返回 False
    """
    for i in range(max_try):
        if poco("首页").exists():  # 判断首页元素是否存在
            print("✅ 已回到首页")
            return True
        print(f"⚠️ 第 {i + 1} 次尝试返回")
        keyevent("BACK")  # 返回上一层
        sleep(interval)
    #否则直接返回主页
    keyevent("HOME")

    print("❌ 未能返回到首页")
    return False


# 提取日期中的日
def extract_day(date_str):
    match = re.search(r'(\d+)日', date_str)
    if match:
        return int(match.group(1))
    return None


def choose_n_days_date(n):
    # 1. 当前日期
    today = datetime.today()

    # 2. 加 n 天后目标日期
    target_date = today + timedelta(days=n)
    target_year = target_date.year
    target_month = target_date.month
    target_day = target_date.day

    print(f"目标日期是：{target_year}-{target_month:02d}-{target_day:02d}")

    # 3. 点击日期控件进入日历
    poco("date").click()
    poco(text="时间段").click()
    sleep(2)
    # 点击日期，打开日历
    poco("android.widget.FrameLayout") \
        .offspring("android.view.ViewGroup") \
        .child("android.view.View") \
        .offspring("android.widget.ScrollView") \
        .child("android.widget.TextView")[0].click()
    sleep(2)
    # 4. 获取当前选中的日期
    date_list = poco("android.widget.FrameLayout") \
        .offspring("android.view.ViewGroup") \
        .child("android.view.View") \
        .child("android.view.View") \
        .child("android.view.View")[0] \
        .child("android.view.View") \
        .child("android.view.View")[3] \
        .child("android.widget.TextView")

    current_selected_day = None
    for i in range(len(date_list)):
        if date_list[i].attr("checked"):
            print(date_list[i].get_text())
            dd = date_list[i].get_text()
            current_selected_day = int(extract_day(dd))
            print("当前选中日期：", current_selected_day)
            break

    current_month = today.month
    current_year = today.year

    # 5. 判断是否同一个月
    if target_year == current_year and target_month == current_month:
        # 在本月，可以直接点击目标日期
        for d in date_list:
            d_day = int(extract_day(d.get_text()))
            if int(d_day) == target_day:
                d.click()
                break
    else:
        # 不在本月
        print(f"目标日期不在本月，请翻页至 {target_year} 年 {target_month} 月，然后点击 {target_day} 日")
        # 跳转到下个月
        poco("android.widget.FrameLayout") \
            .offspring("android.view.ViewGroup") \
            .child("android.view.View") \
            .child("android.view.View") \
            .child("android.view.View")[0] \
            .child("android.view.View") \
            .child("android.view.View")[2] \
            .child("android.widget.Button").click()
        # 选择对应日期
        poco("android.widget.FrameLayout") \
            .offspring("android.view.ViewGroup") \
            .child("android.view.View") \
            .child("android.view.View") \
            .child("android.view.View")[0] \
            .child("android.view.View") \
            .child("android.view.View")[3] \
            .child("android.widget.TextView")[target_day].click()

    # 6. 确认选择
    poco(text="确定").click()
    poco(text="确认").click()


# 删除创建的代办
def find_del_agent(agent_name):
    agents = poco("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View") \
        .child("android.view.View") \
        .child("android.view.View")[7] \
        .children()
    for i in range(len(agents)):
        if agents[i].get_text() == agent_name:
            agents[i + 2].click()
            #             touch(Template(r"tpl1749637230158.png", record_pos=(0.448, 0.182), resolution=(1200, 1920)))
            # 删除新增的代办
            poco(text="删除").click()
            poco(text="确认").click()


# 点击并拖动ai图标到文本
def swipe_press_ai(start_point=(49, 1732), end_point=(410, 990)):
    # 拖动ai图标
    steps = 10  # 拖动的分段数
    multitouch_event = [
        DownEvent(start_point), SleepEvent(0.1)]
    dev.touch_proxy.perform(multitouch_event)
    sleep(1)
    # 2. swipe
    swipe_event = [DownEvent(start_point), SleepEvent(0.1)]
    for i in range(1, steps + 1):
        # 计算插值坐标，实现平滑拖动
        x = start_point[0] + (end_point[0] - start_point[0]) * i // steps
        y = start_point[1] + (end_point[1] - start_point[1]) * i // steps
        swipe_event.append(MoveEvent((x, y)))
        swipe_event.append(SleepEvent(0.05))  # 每步间隔，可微调
    swipe_event.append(UpEvent())
    dev.touch_proxy.perform(swipe_event)


def extract_url_and_password(text):
    # 定义正则表达式，提取链接和密码
    url_pattern = r"(https?://[^\s]+)"
    password_pattern = r"密码：(\S+)"

    # 使用正则表达式查找网址
    url = re.search(url_pattern, text)
    password = re.search(password_pattern, text)

    # 如果找到了网址和密码，返回它们；否则返回 None
    return url.group(0) if url else None, password.group(1) if password else None

#点击并拖动ai图标到文本
def swipe_press_ai(start_point=(49,1732),end_point=(410,990)):
    #拖动ai图标
    steps = 10  # 拖动的分段数
    multitouch_event = [
    DownEvent(start_point), SleepEvent(0.1)]
    dev.touch_proxy.perform(multitouch_event)
    sleep(1)
    # 2. swipe
    swipe_event = [DownEvent(start_point), SleepEvent(0.1)]
    for i in range(1, steps + 1):
        # 计算插值坐标，实现平滑拖动
        x = start_point[0] + (end_point[0] - start_point[0]) * i // steps
        y = start_point[1] + (end_point[1] - start_point[1]) * i // steps
        swipe_event.append(MoveEvent((x, y)))
        swipe_event.append(SleepEvent(0.05))  # 每步间隔，可微调
    swipe_event.append(UpEvent())
    dev.touch_proxy.perform(swipe_event)

# 生成4位随机字符
def random_string(length=4):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


# 判断回收站是否为空
def recycle_bin_is_null():
    return poco(text="暂无文件").exists()


# 回收站删除全部文件
def del_all_files():
    poco("笔记").click()
    # 点击回收站
    poco("show recycle").click()
    sleep(1)
    if recycle_bin_is_null() == False:
        poco("编辑").click()
        poco(text="全部选中").click()
        poco(text="彻底删除").click()
        poco(text="确认").click()
    poco("<").click()


# 删除文件
def del_file():
    touch(Template(r"tpl1748938545309.png", record_pos=(0.287, -0.606), resolution=(1200, 1920)))
    poco(text="全部选中").click()
    poco(text="删除").click()
    poco(text="确认").click()
    sleep(1)


# 判断当前是否登录
def is_login():
    # 点击应用
    poco("应用").click()
    # 点击设置
    poco("设置图标").click()
    username = poco("com.zlt.zltsettings:id/user_name").get_text()
    # 返回到首页
    poco(text="系统设置").click()
    # 点击首页
    poco("首页").click()
    # 判断是否已登录,true未登录，false已登录
    return username == "未登录"


# 新建笔记
def create_new_notes():
    # 点击笔记
    poco("笔记").click()
    # 点击新建笔记
    poco(text="新建笔记").click()
    # 输入笔记内容
    poco("更多设置").click()
    poco(text="插入文字").click()
    sleep(2)
    touch((581, 997))
    sleep(2)
    timestamp = time.strftime("%Y%m%d%H%M%S")  # 年月日时分秒
    text(timestamp, enter=False)
    poco("返回").click()
    sleep(1)
    # 4、回到首页
    poco("首页").click()
    return timestamp


# 退出登录
def logout():
    # 点击应用
    poco("应用").click()

    # 点击设置
    poco("设置图标").click()
    # 点击登陆头像
    poco("android.widget.FrameLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("android:id/content") \
        .child("android.widget.LinearLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("com.zlt.zltsettings:id/account")[0] \
        .child("android.widget.ImageView").click()
    # 点击账号管理
    poco("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View").offspring("android.widget.ScrollView") \
        .child("android.view.View")[0].click()
    # 点击退出登录
    poco(text="退出登录").click()
    # 点击确定
    poco(text="确定").click()
    sleep(1)
    # 点击账户
    poco("返回").click()
    # 点击系统设置
    poco(text="系统设置").click()
    # 点击首页
    poco("首页").click()


# 登录账号
def login(phoneNumber="18662682224", code="123456"):
    # 点击应用
    poco("应用").click()

    # 点击设置
    poco("设置图标").click()
    # 点击登陆头像
    poco("android.widget.FrameLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("android:id/content") \
        .child("android.widget.LinearLayout") \
        .child("android.widget.LinearLayout") \
        .offspring("com.zlt.zltsettings:id/account")[0] \
        .child("android.widget.ImageView").click()
    poco("android.widget.CheckBox").click()
    poco(text="请输入手机号码").click()
    text(phoneNumber, enter=False)
    poco(text="请输入短信验证码").click()
    text(code, enter=False)
    poco("android.widget.FrameLayout") \
    .offspring("androidx.compose.ui.platform.ComposeView") \
    .child("android.view.View").child("android.view.View") \
    .child("android.view.View")[1].child("android.widget.TextView").click()
    sleep(2)
    # 点击账户
    poco("返回").click()
    sleep(1)
    # 点击系统设置
    poco(text="系统设置").click()
    # 点击首页
    poco("首页").click()
    sleep(1)


# 根据分组名删除分组
def find_group_by_name_and_del(ss):
    list = poco("androidx.compose.ui.platform.ComposeView") \
        .child("android.view.View").child("android.view.View") \
        .child("android.view.View")[3] \
        .child("android.view.View").children()
    for i in range(0, len(list)):
        text_node = poco("androidx.compose.ui.platform.ComposeView") \
            .child("android.view.View").child("android.view.View") \
            .child("android.view.View")[3] \
            .child("android.widget.TextView")[i * 3]

        if text_node.get_text() == ss:
            poco("androidx.compose.ui.platform.ComposeView") \
                .child("android.view.View").child("android.view.View") \
                .child("android.view.View")[3] \
                .child("android.view.View")[i].click()
            poco(text="删除").click()
            poco(text="确认").click()
            break