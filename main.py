import json
from model import StudentInfoSystem
from storage import load_students, save_students
""""
要求：学生信息管理系统，包含以下功能：
1. 添加学生信息
有姓名、年龄、性别、学号等信息 用字典（键值对）存储


2. 删除学生信息
3. 修改学生信息
4. 查询学生信息
5. 显示所有学生信息
6. 退出系统
"""



def show_menu():
    print("======欢迎使用学生信息管理系统=====")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("6. 退出系统")
    print("====================================")


def main():
    #加载数据（文件不存在返回列表）
    student_list = load_students("students.json")





















    #=============================启动初始化与数据加载-纯文本（CSV风格）==============
    # 启动时，尝试从文件加载数据
    # student_list = []
    # try:
    #     with open("students.txt", "r", encoding="utf-8") as f:
    #         for line in f:
    #             line = line.strip()  # 去掉行尾的换行符
    #             if not line:
    #                 continue         # 跳过空行
    #             data = line.split(",")  # 按逗号拆分
    #             # 假设我们的 Student 类初始化接收 4 个参数
    #             name, age, sex, student_id = data
    #             s = StudentInfoSystem(name, int(age), sex, student_id)
    #             student_list.append(s)
    # except FileNotFoundError:
    #     pass  # 第一次运行，文件还不存在，什么都不做
    #=============================finish 初始化与数据加载-纯文本（CSV风格）===================================


    #=============================启动初始化与数据加载-纯文本（JSON风格）==================================
    # 启动时，尝试从文件加载数据
    # student_list = []
    # try:
    #     with open("students.json", "r", encoding="utf-8") as f:
    #         data_list = json.load(f)
    #         for item in data_list:
    #             s = StudentInfoSystem(item["name"], item["age"], item["sex"], item["student_id"])
    #             student_list.append(s)
    # except FileNotFoundError:
    #     print("文件不存在！")
    #     pass  # 第一次运行，文件还不存在，什么都不做

    # =============================finish 初始化与数据加载-纯文本（JSON风格）===================================

    while True:                  # 无限循环，直到用户选择退出系统为止
        show_menu()
        choice = input("请输入您的选择：")
        if choice == "1":
            name = input("请输入你的名字:")
            try:
                age = int(input("请输入你的年龄"))
                sex = input("请输入你的性别")
                student_id = input("请输入你的学号")
                new_student = StudentInfoSystem(name,age,sex,student_id)
                student_list.append(new_student)
                print(
                f"学生信息添加成功，姓名：{name} 年龄：{age} 性别：{sex} 学号：{student_id}"
                )
            except ValueError:
                print("请输入正确的年龄！")
        # elif choice == "2":
        #     name = input("请输入你要删除的学生名字：")
        #     found = False              # 标志变量，用于判断是否找到要删除的学生
        #     for i in student_list:
        #         if i.name == name:
        #             student_list.remove(i)
        #             print(f"学生信息删除成功，姓名：{i.name} 年龄：{i.age} 性别：{i.sex} 学号：{i.student_id}")
        #             found = True
        #             break
        #     if not found:
        #             print("没有找到该学生信息！")
        elif choice == "3":
            name = input("请输入你要修改的学生名字：")
            found = False              # 标志变量，用于判断是否找到要修改的学生
            for i in student_list:
                if i.name == name:
                    found = True# 使用 for 循环遍历 student_list 列表，找到要删除的学生
                    try:
                        i.age = int(input("请输入新的年龄"))
                    except ValueError:
                        print("请输入正确的年龄！")
                    try:
                        i.sex = input("请输入新的性别")
                    except ValueError:
                        print("请输入正确的性别！")
                    try:
                        i.student_id = input("请输入新的学号")
                    except ValueError:
                        print("请输入正确的学号！")
                    print(f"学生信息修改成功，姓名：{i.name} 年龄：{i.age} 性别：{i.sex} 学号：{i.student_id}")
                    break
                if not found:
                    print("没有找到该学生信息！")
        elif choice == "2":
            name = input("请输入你要删除的学生名字：")
            for i in student_list:
                if i.name == name:  # 使用 for 循环遍历 student_list 列表，找到要删除的学生
                    student_list.remove(i)  # 使用 remove() 方法删除找到的学生
                    print(f"学生信息删除成功，姓名：{i.name} 年龄：{i.age} 性别：{i.sex} 学号：{i.student_id}")
                    break
            else:
               print("没有找到该学生信息！")
        elif choice == "4":
            name = input("请输入你要查询的学生名字")

            for i in student_list:
                if i.name == name:  # 使用 for 循环遍历 student_list 列表，找到要查询的学生
                    print(f"姓名：{i.name} 年龄：{i.age} 性别：{i.sex} 学号：{i.student_id}")
                    break
            else:
                print("没有找到该学生信息！")
        elif choice == "5":
            for i in student_list:
                 # 使用 not_none() 函数过滤掉 None 值，避免打印 None 值
                print(i)                   # 使用 for 循环遍历 student_list 列表，打印所有学生信息
        elif choice == "6":
            # ========== 保存 JSON 数据（原始方法）=============
            # # 用列表推导式，把每个对象转成字典
            # dict_list = [s.__dict__ for s in student_list]   # [要保持的对象，要执行的函数，要执行的参数]
            #
            # with open("students.json", "w", encoding="utf-8") as f:
            #     # 将字典列表写入 JSON 文件
            #     # ensure_ascii=False：允许写入中文
            #     # indent=4：缩进4个空格，便于阅读
            #     # json.dump() 函数将 Python 对象转换为 JSON 字符串并写入文件
            #     # json.load() 函数将 JSON 字符串转换为 Python 对象
            #     #f是文件对象，dict_list是字典列表
            #     json.dump(dict_list, f, ensure_ascii=False, indent=4)
            # =========== 保存 JSON 数据（简化方法）=============
            save_students(student_list, "students.json")
            print("数据已保存，感谢使用，再见！")
            break








            """            
            with open("students.txt", "w", encoding="utf-8") as f:
                for s in student_list:
                    f.write(f"{s.name},{s.age},{s.sex},{s.student_id}\n")  # 将学生信息写入文件

            print("系统退出，学生信息已保存到文件中！")
            break                            # 退出循环，结束程序
        else:
            print("输入错误，请重新输入！")
            """


if __name__ == "__main__":               #只有直接运行这个文件时，才执行 main()
    main()                                  #调用 main()函数，开始程序运行
"""
把主逻辑放进 main() 函数，结构更清晰。
避免模块被导入时自动执行测试代码或主程序。
让同一个文件既能当脚本运行，也能当模块被导入。
"""