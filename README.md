# 学生信息管理系统 (Student Management System)

一个基于 Python 的命令行学生信息管理系统，支持增删改查、JSON 持久化存储，并配备完善的 pytest 自动化测试。

## 🚀 功能特性
- 添加、删除、修改、查询学生信息（姓名、年龄、性别、学号）
- 数据持久化：使用 JSON 格式存储，重启不丢数据
- 数据校验：年龄范围、姓名非空等异常处理
- 自动化测试：基于 pytest 的单元测试与边界测试

## 📂 项目结构
- `models.py`: 数据模型层 (OOP 设计)
- `storage.py`: 存储层 (JSON 文件读写)
- `main.py`: 交互层 (菜单逻辑)
- `test_models.py`: 模型层单元测试
- `test_storage.py`: 存储层单元测试

## 🛠️ 如何运行
1. 克隆仓库：
   `git clone https://github.com/2113325803-glitch/student-management-system.git`
2. 安装依赖：
   `pip install pytest`
3. 运行程序：
   `python main.py`
4. 运行测试：
   `python -m pytest -v`

## 📝 开发者
- 姓名：郝得胜
- 目标岗位：测试开发 / Python 后端