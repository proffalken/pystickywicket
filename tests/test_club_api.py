import os
import pystickywicket


def test_get_club_Data():
    stickywicket = pystickywicket.ECB(api_key="test")
    cd = stickywicket.get_club_data(club_id="Monmouth")
    assert cd['status'] == 401
