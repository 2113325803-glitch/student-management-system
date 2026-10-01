# class StudentInfoSystem:                #类名用大驼峰命名法，不用下划线
#     def __init__(self,name,age,sex,student_id):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.student_id = student_id
#     def __str__(self):
#         return f"姓名：{self.name} 年龄：{self.age} 性别：{self.sex} 学号：{self.student_id}"


#=====================================数据校验逻辑======================================
class StudentInfoSystem:
    def __init__(self, name, age, sex, student_id, id=None):
        # 校验1：名字不能为空
        if not name:
            raise ValueError("姓名不能为空")    #raise用于抛出异常，ValueError是异常类，表示值错误

        # 校验2：年龄必须是整数，且在合理范围内
        if age < 0 or age > 150:
            raise ValueError("年龄必须在 0 到 150 之间")
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.student_id = student_id

    def __str__(self):
        return f"姓名：{self.name} 年龄：{self.age} 性别：{self.sex} 学号：{self.student_id}"