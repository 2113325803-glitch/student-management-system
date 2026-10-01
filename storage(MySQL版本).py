import os         #用于文件操作
import pymysql    #导入MySQL数据库驱动
import json      #用于处理JSON数据
from models import StudentInfoSystem        #逻辑分离，存储模块只负责读写文件

#数据库连接配置，注意：这里使用的是MySQL数据库
DB_CONFIG = {
    "host": "localhost",          #
    "port": 3306,
    "user": "root",
    "password": "Hds060608@",
    "database": "student_info_system",
    "charset": "utf8mb4"  # 支持中文
}

def get_connection():
    """获取数据库连接"""
    return pymysql.connect(**DB_CONFIG)

#=============用于存储模块的代码（MySQL数据库存储）================
def load_students():
    """从数据库加载所有学生，返回 StudentInfoSystem 对象列表"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id,name,age,sex,student_id FROM students")
    rows = cursor.fetchall()
    students = []
    for row in rows:
        #数据库查出来的每一行都是元组（id,name,age,sex,student_id)
        s = StudentInfoSystem(name=row[1],age=row[2], sex=row[3],student_id=row[4], id=row[0])
        students.append(s)

    cursor.close()    #缩进要和for循环缩进一致
    conn.close()
    return students
#=============用于存储模块的代码（MySQL数据库存储）================

#============以下是save_students函数的代码（MySQL数据库存储）==
def save_students(students):
    """把学生对象列表保存到数据库"""
    conn = get_connection()
    cursor = conn.cursor()
    for s in students:
        #数据库插入一条记录
        cursor.execute(
            "INSERT INTO students (id,name,age,sex,student_id) VALUES (%s,%s,%s,%s,%s)",
            (s.id, s.name, s.age, s.sex, s.student_id)
        )
    cursor.close()
    conn.commit()  # 提交事务
    conn.close()






















# #=======================以下是存储模块的代码（JSON文件存储）================
# def load_students(file_path):
#     """从指定文件加载学生列表，如果文件不存在则返回空列表"""
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:       #with：自动关闭文件
#             data_list = json.load(f)
#             # 把字典列表转成对象列表
#             return [StudentInfoSystem(item["name"], item["age"], item["sex"], item["student_id"]) for item in data_list]
#     except FileNotFoundError:
#         return []  # 第一次运行没有文件，返回空列表
# #=======================以下是存储模块的代码（JSON文件存储）================

#============以下是save_students函数的代码（JSON文件存储）================
# def save_students(students, file_path):
#     """把学生对象列表保存到指定文件"""
#     # ===== 加这行保险丝 ===== 这是防御性编程。以后如果你在生产环境里写日志，传了一个 /var/log/myapp/error.log 路径，但 myapp 文件夹还没建，这行代码就会救你一命。
#     # 如果文件所在的目录不存在，就创建它（exist_ok=True 防止目录已存在时报错）
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#
#     dict_list = [s.__dict__ for s in students]
#     with open(file_path, "w", encoding="utf-8") as f:
#         json.dump(dict_list, f, ensure_ascii=False, indent=4)
#
# #============以下是save_students函数的代码（JSON文件存储）================

