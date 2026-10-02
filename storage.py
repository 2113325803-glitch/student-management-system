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


#=========================第二次修改=================优化了代码结构，将文件操作和数据库操作分开，便于维护和扩展=
# import os
# import pymysql
# from models import StudentInfoSystem  # ⚠️ 必须导入 Student
#
# DB_CONFIG = {
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "Hds060608@",  # ⚠️ 换成你自己的 MySQL 密码！
#     "database": "student_system",
#     "charset": "utf8mb4"
# }
#
#
# def get_connection():
#     return pymysql.connect(**DB_CONFIG)
#
#
# def load_students():
#     """从数据库加载所有学生，返回 Student 对象列表"""
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, name, age, sex, student_id FROM students")
#     rows = cursor.fetchall()
#
#     students = []
#     for row in rows:
#         s = StudentInfoSystem(name=row[1], age=row[2], sex=row[3], student_id=row[4], id=row[0])
#         students.append(s)
#
#     cursor.close()
#     conn.close()
#     return students
#
#
# def save_students(students):
#     """把内存里的学生列表全量覆盖写入数据库"""
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM students")  # 先清空原表
#     for s in students:
#         cursor.execute(
#             "INSERT INTO students (name, age, sex, student_id) VALUES (%s, %s, %s, %s)",
#             (s.name, s.age, s.sex, s.student_id)
#         )
#     conn.commit()  # ⚠️ 必须提交事务，否则数据不会真正写入！
#     cursor.close()
#     conn.close()


#==========第三次修改=================优化了代码结构，将文件操作和数据库操作分开，便于维护和扩展=

import pymysql
from models import StudentInfoSystem

DB_CONFIG = {                   #数据库配置信息，包括数据库地址、端口、用户名、密码、数据库名和字符集
    "host": "localhost",         #localhost是本地数据库，可以换成你的数据库地址
    "port": 3306,                  #3306是MySQL默认端口
    "user": "root",               #root是MySQL默认用户名
    "password": "Hds060608@",      # ⚠️ 换成你自己的 MySQL 密码！
    "charset": "utf8mb4"              #utf8mb4是MySQL默认字符集
}

def get_connection(db_name="student_system"): #获取数据库连接，可传入数据库名，默认连生产库
    """获取数据库连接，默认连生产库，可传入测试库名"""      #这里的db_name参数可传入测试库名，如"test_student_system",原因是为了方便测试和开发，可以传入不同的数据库名，这样就不需要修改代码了
    config = DB_CONFIG.copy()          #复制数据库配置信息，避免修改原配置信息
    config["database"] = db_name             #在副本里补上database字段，也就是要连那个库
    return pymysql.connect(**config)        #调用pymysql解释：**config表示将config字典中的键值对作为关键字参数传递给pymysql.connect函数
#pytest.connect()  #调用get_connection函数，传入测试库名，返回测试库连接
#Cursor:游标对象，用于执行SQL语句，获取查询结果
def load_students(db_name="student_system"):
    conn = get_connection(db_name)                 #conn是数据库连接对象,用别名字代替这个conn可以避免与pymysql.connect()函数中的conn混淆
    cursor = conn.cursor()       #这句话是获取游标对象，游标对象用于执行SQL语句，获取查询结果
    cursor.execute("SELECT id, name, age, sex, student_id FROM students")      #execute()方法用于执行SQL语句，这里执行的是查询所有学生信息的SQL语句
    #select * from students;      #SQL语句，查询所有学生信息     *是SQL语句中的通配符，表示所有列
    rows = cursor.fetchall()          #fetchall()方法用于获取查询结果，这里获取的是所有学生信息
    students = []
    for row in rows:
        s = StudentInfoSystem(name=row[1], age=row[2], sex=row[3], student_id=row[4], id=row[0])
        students.append(s)
    cursor.close()
    conn.close()
    return students

def save_students(students, db_name="student_system"):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students")
    #delete from students;      #SQL语句，清空所有学生信息
    #delete from students where id = 1;      #SQL语句，清空id为1的学生信息
    #delete from students where name = '张三';      #SQL语句，清空name为张三的学生信息
    #delete from students where age > 18;      #SQL语句，清空age大于18的学生信息
    #delete from students where sex = '男';      #SQL语句，清空sex为男的学生信息
    #delete from students where student_id = '1234567890';      #SQL语句，清空student_id为1234567890的学生信息
    for s in students:       #遍历学生列表，逐个插入学生信息到数据库
        cursor.execute(                   #execute()方法用于执行SQL语句
            "INSERT INTO students (name, age, sex, student_id) VALUES (%s, %s, %s, %s)",
            (s.name, s.age, s.sex, s.student_id)
        )
    conn.commit()    # ⚠️ 必须提交事务
    cursor.close()
    conn.close()

def clear_students(db_name="student_system"):
    """清空指定库的所有学生（仅用于测试环境清理）"""
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students")
    conn.commit()
    cursor.close()
    conn.close()
