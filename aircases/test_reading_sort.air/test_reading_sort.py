# -*- encoding=utf8 -*-
__author__ = "cailin.liao_sx"

import os
import sys

import allure
import pytest
from airtest.core.api import *
# 设置导入路径（确保能找到 utils 目录）
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "utils")))

from utils.commen import *

auto_setup(__file__, logdir=True, project_root=os.path.dirname(__file__))

pytestmark = [allure.feature("阅读排序模块用例"), allure.epic("办公本v2.4.0")]



#阅读内支持排序（我的文档）
@pytest.mark.testcase
@allure.description("阅读内支持排序（我的文档）")
@allure.title("阅读内支持排序（我的文档）")
def test_my_documents_reading_sort():
    poco(text="阅读").click()
    poco("list view type").click()
    #按创建时间升序排序
    poco("排序").click()
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[2].child("android.view.View")[1].click()
    #按创建时间降序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[2].child("android.view.View")[0].click()
    #按修改时间升序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[3].child("android.view.View")[1].click()
    #按修改时间降序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[3].child("android.view.View")[0].click()
    #测试按文件名升序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[1].child("android.view.View")[1].click()
    #按文件名降序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[1].child("android.view.View")[0].click()
    touch((600,1500))
    poco(text="首页").click()




#阅读内支持排序（批注截图）
@pytest.mark.testcase
@allure.description("阅读内支持排序（批注截图）")
@allure.title("阅读内支持排序（批注截图）")
def test_approve_screenshots_reading_sort():
    poco(text="阅读").click()
    poco(text="批注截图").click()
    poco("list view type").click()
    #按创建时间升序排序
    poco("排序").click()
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[2].child("android.view.View")[1].click()
    #按创建时间降序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[2].child("android.view.View")[0].click()
    #按修改时间升序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[3].child("android.view.View")[1].click()
    #按修改时间降序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[3].child("android.view.View")[0].click()
    #测试按文件名升序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[1].child("android.view.View")[1].click()
    #按文件名降序排序
    poco("android:id/content").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[1].child("android.view.View")[0].click()
    touch((600,1500))
    poco(text="首页").click()







if __name__=="__main__":
    test_my_documents_reading_sort()
    test_approve_screenshots_reading_sort()
    


