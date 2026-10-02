from fastapi import FastAPI
from pydantic import BaseModel
from storage import save_students, load_students
from models import StudentInfoSystem

app = FastAPI()


# 定义接口接收的数据格式
class StudentModel(BaseModel):
    name: str
    age: int
    sex: str
    student_id: str


@app.post("/add_student")
def add_student(student: StudentModel):
    """接收学生数据，写入数据库"""
    # 1. 从数据库加载现有数据
    students = load_students("test_student_system")
    # 2. 添加新数据
    students.append(StudentInfoSystem(
        name=student.name, age=student.age, sex=student.sex, student_id=student.student_id
    ))
    # 3. 保存回数据库
    save_students(students, "test_student_system")

    return {"status": "success", "message": "学生添加成功"}