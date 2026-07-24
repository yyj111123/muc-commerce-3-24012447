import pytest
from app import app

app.config["TESTING"] = True
client = app.test_client()

# 1.健康接口测试
def test_health():
    res = client.get("/health")
    assert res.status_code == 200

# 2.未登录拦截指标接口
def test_metrics_no_login():
    res = client.get("/api/metrics")
    assert res.status_code != 200

# 3.登录后正常访问指标接口
def test_metrics_login():
    client.post("/login", data={"username":"student","password":"day07"})
    res = client.get("/api/metrics")
    assert res.status_code == 200

# 4.品类筛选接口测试
def test_category_filter():
    client.post("/login", data={"username":"student","password":"day07"})
    res = client.get("/api/categories?category=Fashion")
    assert res.status_code == 200