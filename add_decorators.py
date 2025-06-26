import os
import re

#为指定路径下所有测试函数添加统一注解

def add_decorators_to_tests(py_file):
    with open(py_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for i, line in enumerate(lines):
        if re.match(r'\s*def test_', line):
            # 在函数定义前插入装饰器
            new_lines.append('@pytest.mark.testcase\n')
            new_lines.append('@allure.description("TODO: 填写描述")\n')
            new_lines.append('@allure.title("TODO: 填写标题")\n')
        new_lines.append(line)

    with open(py_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# 遍历所有 aircases 下的 .py 文件
for root, dirs, files in os.walk('./aircase'):
    for file in files:
        if file.endswith('.py'):
            add_decorators_to_tests(os.path.join(root, file))
