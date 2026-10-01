import os
import json      #用于处理JSON数据
from models import StudentInfoSystem        #逻辑分离，存储模块只负责读写文件

def load_students(file_path):
    """从指定文件加载学生列表，如果文件不存在则返回空列表"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:       #with：自动关闭文件
            data_list = json.load(f)
            # 把字典列表转成对象列表
            return [StudentInfoSystem(item["name"], item["age"], item["sex"], item["student_id"]) for item in data_list]
    except FileNotFoundError:
        return []  # 第一次运行没有文件，返回空列表


def save_students(students, file_path):
    """把学生对象列表保存到指定文件"""
    # ===== 加这行保险丝 ===== 这是防御性编程。以后如果你在生产环境里写日志，传了一个 /var/log/myapp/error.log 路径，但 myapp 文件夹还没建，这行代码就会救你一命。
    # 如果文件所在的目录不存在，就创建它（exist_ok=True 防止目录已存在时报错）
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    dict_list = [s.__dict__ for s in students]
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(dict_list, f, ensure_ascii=False, indent=4)