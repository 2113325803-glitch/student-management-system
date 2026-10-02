from models import StudentInfoSystem
from storage import load_students, save_students, clear_students

TEST_DB = "test_student_system"  # 指定用测 试库，绝不碰生产库！


def test_load_empty():
    """测试：空表时加载，应返回空列表"""
    clear_students(TEST_DB)  # 先清空，保证环境干净
    result = load_students(TEST_DB)
    assert result == []


def test_save_and_load():
    """测试：保存后重新加载，数据应完全一致（往返测试）"""
    clear_students(TEST_DB)
    students = [
        StudentInfoSystem("测试张三", 20, "男", "T001"),
        StudentInfoSystem("测试李四", 21, "女", "T002")
    ]
    save_students(students, TEST_DB)
    loaded = load_students(TEST_DB)

    assert len(loaded) == 2
    assert loaded[0].name == "测试张三"
    assert loaded[0].student_id == "T001"
    assert loaded[1].name == "测试李四"


def test_overwrite():
    """测试：全量覆盖，旧数据被新数据替换"""
    clear_students(TEST_DB)
    save_students([StudentInfoSystem("旧数据", 20, "男", "X001")], TEST_DB)
    save_students([StudentInfoSystem("新数据", 30, "女", "X002")], TEST_DB)

    loaded = load_students(TEST_DB)
    assert len(loaded) == 1
    assert loaded[0].name == "新数据"  # 旧数据确实被覆盖了