# import os
# import json      #用于处理JSON数据
# from models import StudentInfoSystem        #逻辑分离，存储模块只负责读写文件
#
# def load_students(file_path):
#     """从指定文件加载学生列表，如果文件不存在则返回空列表"""
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:       #with：自动关闭文件
#             data_list = json.load(f)
#             # 把字典列表转成对象列表
#             return [StudentInfoSystem(item["name"], item["age"], item["sex"], item["student_id"]) for item in data_list]
#     except FileNotFoundError:
#         return []  # 第一次运行没有文件，返回空列表
#
#
# def save_students(students, file_path):
#     """把学生对象列表保存到指定文件"""
#     # ===== 加这行保险丝 ===== 这是防御性编程。以后如果你在生产环境里写日志，传了一个 /var/log/myapp/error.log 路径，但 myapp 文件夹还没建，这行代码就会救你一命。
#     # 如果文件所在的目录不存在，就创建它（exist_ok=True 防止目录已存在时报错）
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#
#     dict_list = [s.__dict__ for s in students]
#     with open(file_path, "w", encoding="utf-8") as f:
#         json.dump(dict_list, f, ensure_ascii=False, indent=4)

import os
import pymysql
from models import StudentInfoSystem  # ⚠️ 必须导入 Student

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Hds060608@",  # ⚠️ 换成你自己的 MySQL 密码！
    "database": "student_system",
    "charset": "utf8mb4"
}


def get_connection():
    return pymysql.connect(**DB_CONFIG)


def load_students():
    """从数据库加载所有学生，返回 Student 对象列表"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, sex, student_id FROM students")
    rows = cursor.fetchall()

    students = []
    for row in rows:
        s = StudentInfoSystem(name=row[1], age=row[2], sex=row[3], student_id=row[4], id=row[0])
        students.append(s)

    cursor.close()
    conn.close()
    return students


def save_students(students):
    """把内存里的学生列表全量覆盖写入数据库"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students")  # 先清空原表
    for s in students:
        cursor.execute(
            "INSERT INTO students (name, age, sex, student_id) VALUES (%s, %s, %s, %s)",
            (s.name, s.age, s.sex, s.student_id)
        )
    conn.commit()  # ⚠️ 必须提交事务，否则数据不会真正写入！
    cursor.close()
    conn.close()

