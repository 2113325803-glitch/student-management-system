import pytest
from models import StudentInfoSystem     #导入StudentInfoSystem类
def test_create_student():
    #1. 创建对象，传入参数
    s = StudentInfoSystem("张三", 20, "男", "1234567890")
    #2. 断言 对象属性是否正确 , 用 assert 断言 （验证属性是否正确）
    assert s.name == "张三"                       #如果条件是ture，程序继续执行，如果条件是false，程序会抛出AssertionError异常
    assert s.age == 20
    assert s.sex == "男"
    assert s.student_id == "1234567890"
def test_student_str():
    #1. 创建对象，传入参数
    s = StudentInfoSystem("张三", 20, "男", "1234567890")
    #2. 断言 对象属性是否正确 , 用 assert 断言 （验证属性是否正确）
    assert str(s) == "姓名：张三 年龄：20 性别：男 学号：1234567890"
def test_invalid_age_negative():
    with pytest.raises(ValueError) as exception_info:
        StudentInfoSystem("张三", -20, "男", "1234567890")
    assert "年龄必须在0到150之间" in str(exception_info.value)

def test_empty_name():
    with pytest.raises(ValueError):
        StudentInfoSystem("", 20, "男", "1234567890")