import os
import pytest
import tempfile
from models import StudentInfoSystem
from storage import load_students, save_students



# 一，  测试：文件不存在时，加载应该返回空列表
# def test_load_no_file(temp_path):                #构造一个不存在的文件路径
#     file_path = temp_path / "not_exist.json"
#     result = load_students(str((file_path)))
#     assert result ==[]      #预期得到空列表
"""
1. Pytest 创建临时目录（temp_path）
2. 构造一个不存在的文件路径
3. 调用 load_students(路径)
4. 函数内部：
   - 尝试打开文件 → 抛出 FileNotFoundError
   - 捕获异常 → 返回 []
5. 断言：result 是否等于 []
6. 测试通过/失败
7. Pytest 自动删除临时目录
"""

#2，
def test_load_no_file():
    # 1. 创建一个临时目录（with 块结束后自动删除）
    with tempfile.TemporaryDirectory() as tmp_dir:
        # 2. 拼接出一个不存在的文件路径
        file_path = os.path.join(tmp_dir, "not_exist.json")
        result = load_students(file_path)
        assert result == []



#测试：保存后能重新加载（往返测试 round-trip test）
def test_save_and_load():                #构造一个不存在的文件路径
    # file_path = temp_path / "test_data.json"
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = os.path.join(tmp_dir, "test_data.json")

    #1.Argument(准备):创建俩个学生对象
    students = [
        StudentInfoSystem("Alice", 20, "Female", "1234567890"),
        StudentInfoSystem("Bob", 22, "Male", "9876543210")
    ]

#2.Act(执行):保存学生对象到文件，然后重新加载
    save_students(students, (file_path))
    loaded_students = load_students(file_path)

# 3. Assert（断言）：验证两个列表长度一致，且每个对象属性一致
    assert len(loaded_students) == 2
    assert loaded_students[0].name == "Alice"
    assert loaded_students[0].age == 20
    assert loaded_students[1].name == "Bob"
    assert loaded_students[1].student_id == "9876543210"

