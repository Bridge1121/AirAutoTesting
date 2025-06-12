import importlib
import os
import subprocess
import time
import datetime
import requests
import schedule

# 钉钉机器人配置
#测试群
DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=93c04271a11ef58697a0af784302016ccbfec2dfc45a0dd08964c022d217efe6"
#hook
# DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=9f4def1f3b64509d35397661e137ec2b463bedaffeb8840b73447fe3b61af383"


TASK_NAME = "办公本自动化测试"
TEAM_NAME = "测试小组"
PROJECT_NAME = "办公本测试项目"
DEVICE_MODEL = "办公本"
APK_VERSION = "V2.2.4.25060901"

def send_to_dingtalk(webhook_url, message):
    headers = {'Content-Type': 'application/json'}
    data = {"msgtype": "text", "text": {"content": message}}
    try:
        response = requests.post(webhook_url, headers=headers, json=data)
        if response.status_code == 200:
            print("测试结果已成功发送到钉钉。")
        else:
            print(f"发送失败，状态码: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"发送过程中出现错误: {e}")

def run_all_scripts():
    success = 0
    failure = 0
    error = 0
    start_time = time.time()

    test_dir = "./aircases"
    import traceback

    for item in os.listdir(test_dir):
        if item.endswith(".air"):
            py_file = os.path.join(test_dir, item, item.replace('.air', '.py'))
            spec = importlib.util.spec_from_file_location("airtest_module", py_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            # 扫描所有 test_ 开头的函数
            test_funcs = [f for f in dir(module) if callable(getattr(module, f)) and f.startswith("test_")]
            for func in test_funcs:
                try:
                    print(f"正在运行 {py_file} 里的 {func}() ...")
                    getattr(module, func)()
                    success += 1
                    print(f"✅ {func}() 运行成功")
                except Exception as e:
                    failure += 1
                    print(f"❌ {func}() 运行失败：{e}")
                    print(traceback.format_exc())

    # for item in os.listdir(test_dir):
    #     if item.endswith(".air"):
    #         air_path = os.path.join(test_dir, item)
    #         print(f"运行：{air_path}")
    #         result = subprocess.run(["airtest", "run", air_path], capture_output=True, text=True,encoding="utf-8")
    #         if result.returncode == 0:
    #             success += 1
    #         else:
    #             if "Traceback" in result.stdout:
    #                 error += 1
    #             else:
    #                 failure += 1

    duration = time.time() - start_time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    msg = f"办公本自动化测试定时任务完成提醒 ({DEVICE_MODEL})\n\n"
    msg += f"测试任务: {TASK_NAME}\n"
    msg += f"所在团队: {TEAM_NAME}\n"
    msg += f"所在项目: {PROJECT_NAME}\n"
    msg += f"设备型号: {DEVICE_MODEL}\n"
    msg += f"apk版本: {APK_VERSION}\n\n"
    msg += f"执行结果:\n"
    msg += f"总测试数: {success + failure + error}\n"
    msg += f"通过: {success}\n失败: {failure}\n错误: {error}\n"
    msg += f"总耗时: {duration:.2f} 秒\n执行时间: {timestamp}\n"
    send_to_dingtalk(DINGTALK_WEBHOOK,msg)

if __name__ == "__main__":
    # schedule.every().day.at("12:09").do(run_all_scripts)
    # print("定时任务已启动，每天早上09:00自动测试并推送钉钉。")
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    run_all_scripts()
