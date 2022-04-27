# -*- coding: utf-8 -*-
__version__ = '0.1.0'

import requests

class ECB:

    def __init__(
            username=None,
            api_key=None):
        """
        ECB

        Create a new instance of the ECB API

        Args:
            username (str): The Username supplied for the API
            api_key (str): The API Key for authentication

        """
        self.username = username
        self.api_key = api_key

        # login and get the session token
        self.login()

    def login(self):
        pass
