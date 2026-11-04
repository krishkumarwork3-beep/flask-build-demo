from app import app, add, is_even

def test_add():
    assert add(2, 3) == 5

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False

def test_home_route():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello from CodeBuild demo"

def test_add_route():
    client = app.test_client()
    resp = client.get("/add/10/5")
    assert resp.get_json()["result"] == 15
