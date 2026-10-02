import pytest
import requests
from storage import clear_students, load_students

API_URL = "http://127.0.0.1:8000/add_student"
TEST_DB = "test_student_system"


@pytest.fixture(autouse=True)
def clean_db():
    clear_students(TEST_DB)  # 测试前清空
    yield
    clear_students(TEST_DB)  # 测试后清理


def test_api_add_student_and_verify_db():
    """测试：调用接口添加学生，并断言数据库中确实存在该数据"""
    # 1. 准备测试数据
    payload = {
        "name": "接口测试王五",
        "age": 25,
        "sex": "男",
        "student_id": "API001"
    }

    # 2. 调用接口（发 POST 请求）
    response = requests.post(API_URL, json=payload)

    # 3. 断言接口返回成功
    assert response.status_code == 200
    assert response.json()["status"] == "success"

    # 4. 去数据库里查账（最核心的一步！）
    db_students = load_students(TEST_DB)
    assert len(db_students) == 1
    assert db_students[0].name == "接口测试王五"
    assert db_students[0].student_id == "API001"