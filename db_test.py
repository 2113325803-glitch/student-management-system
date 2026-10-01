import pymysql

# 1. 建立数据库连接
try:
    conn = pymysql.connect(
        host='localhost',  # 数据库地址（本机就是 localhost）
        port=3306,  # 端口号
        user='root',  # 用户名
        password='Hds060608@',  # ⚠️ 改成你自己的 MySQL 密码！
        database='student_system',  # 要连接的数据库名
        charset='utf8mb4'  # 字符集，防止中文乱码
    )
    print("数据库连接成功！")

    # 2. 创建游标（用来执行 SQL 语句）
    cursor = conn.cursor()

    # 3. 执行 SQL 查询
    cursor.execute("SELECT * FROM students")

    # 4. 获取查询结果
    results = cursor.fetchall()
    print("查询结果：")
    for row in results:
        print(row)

    # 5. 关闭连接
    cursor.close()
    conn.close()
    print("数据库连接已关闭。")

except pymysql.MySQLError as e:
    print(f"连接失败，报错信息：{e}")