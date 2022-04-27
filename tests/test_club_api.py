import os
import pyecb


def test_get_club_Data():
    ecb = pyecb.ECB(api_key="test")
    cd = ecb.get_club_data(club_id="Monmouth")
    assert cd['status'] == 401
