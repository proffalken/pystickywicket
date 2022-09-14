import os
import pystickywicket


def test_class_loads():
    stickywicket = pystickywicket.StickyWicket(api_key="test")

    assert stickywicket.api_key == "test"

def test_get_content_failing_login():
    stickywicket = pystickywicket.StickyWicket(api_key="test")
    gc = stickywicket._get_api_content(api_name="clubs", club_id="Monmouth")
    assert gc['status'] == 401

def test_get_content_successful_login():
    stickywicket = pystickywicket.StickyWicket(api_key=os.getenv("StickyWicket_API_KEY"))
    gc = stickywicket._get_api_content(api_name="clubs", club_id="Monmouth")
    assert gc['status'] == 401
