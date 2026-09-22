\# 自动化测试示例项目 (auto\_test\_project)



一个基于 Python 的自动化测试示例项目，包含 \*\*接口测试\*\* 和 \*\*UI 测试基础架构\*\*。



\## ?? 技术栈

\- Python 3.13

\- pytest（测试框架）

\- requests（接口测试）

\- selenium（UI 测试）

\- allure（测试报告）



\## ?? 项目结构

```text

auto\_test\_project/

├── test\_cases/          # 测试用例目录

│   ├── test\_api.py      # 接口测试用例

│   └── test\_login.py    # 登录逻辑测试

├── requirements.txt     # 依赖包

├── pytest.ini           # pytest 配置文件

└── .gitignore           # Git 忽略文件

