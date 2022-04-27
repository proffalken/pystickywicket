import os
import pyecb


def test_class_loads():
    ecb = pyecb.ECB(api_key="test")

    assert ecb.api_key == "test"

def test_get_content_failing_login():
    ecb = pyecb.ECB(api_key="test")
    gc = ecb._get_api_content(api_name="clubs", club_id="Monmouth")
    assert gc['status'] == 401

def test_get_content_successful_login():
    ecb = pyecb.ECB(api_key=os.getenv("ECB_API_KEY"))
    gc = ecb._get_api_content(api_name="clubs", club_id="Monmouth")
    assert gc['status'] == 401
