import pyecb


def test_class_loads():
    ecb = pyecb.ECB(api_key="test")

    assert ecb.api_key == "test"
