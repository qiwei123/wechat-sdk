# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath('./'))

from weixin.client import WeixinAPI
from weixin.oauth2 import OAuth2AuthExchangeError

APP_ID = "test"
APP_SECRET = "secret"
REDIRECT_URI = "http://www.exmple.com"


code = "0418f2c46cd26e4f9eee5bf03320662M"

api = WeixinAPI(appid=APP_ID, app_secret=APP_SECRET, redirect_uri=REDIRECT_URI)

try:
    pass
except OAuth2AuthExchangeError as e:
    print(e)


auth_info = {
    "access_token": "OezXcEiiBSKSxW0eoylIeGXVgVFIUy2pK5I7TVatC5MGtVqTIWjtyV5Pax8ZLiWw-NdEN9dPkEX8Yewsve2AktmzS0gmbvzRKO49l6sxHRfhXg1no5ObdGufYhRIubP2m3FUdv-Cop3t3S_xwMbBWQ",
    "refresh_token": "OezXcEiiBSKSxW0eoylIeGXVgVFIUy2pK5I7TVatC5MGtVqTIWjtyV5Pax8ZLiWw44bjXRXdmPsclqGIjWs777H3p00QI9a3hzX265Uq9fPJZttNQApdCRPbySXDfofbjniiwsVJiT7fTv7j5jCAxg",
    "openid": u"oV02tuA8Wt6Kk7S0pVydThYvmSJA",
    "expires_in": 7200,
    "scope": u"snsapi_login",
}

try:
    api.exchange_refresh_token_for_access_token(
        refresh_token=auth_info["refresh_token"]
    )
except OAuth2AuthExchangeError:
    pass
api = WeixinAPI(access_token=auth_info["access_token"])
r = api.user(openid=auth_info["openid"])
print(r)
v = api.validate_token(openid=auth_info["openid"])
print(v)
