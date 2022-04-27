import pyecb

def test_class_loads():
    ecb = pyecb.ECB(
            username="test",
            api_key="test")

    assert ecb.username == "test"
    assert ecb.api_key == "test"
