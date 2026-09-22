import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    """测试获取文章接口"""
    resp = requests.get(f"{BASE_URL}/posts/1")
    assert resp.status_code == 200
    assert resp.json()["id"] == 1

def test_create_post():
    """测试创建文章接口"""
    payload = {"title": "foo", "body": "bar", "userId": 1}
    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code == 201