# -*-coding: utf-8 -*-
from __future__ import unicode_literals

from . import oauth2
from .bind import bind_method


SUPPORTED_FORMATS = ["", "json"]


class WeixinAPI(oauth2.OAuth2API):

    host = "open.weixin.qq.com"
    base_path = ""
    access_token_field = "access_token"
    authorize_url = "https://open.weixin.qq.com/connect/qrconnect"
    access_token_url = "https://api.weixin.qq.com/sns/oauth2/access_token"
    jscode2session_url = "https://api.weixin.qq.com/sns/jscode2session"
    refresh_token_url = "https://api.weixin.qq.com/sns/oauth2/refresh_token"
    protocol = "https"
    api_name = "Weixin"
    x_ratelimit_remaining = None
    x_ratelimit = None

    def __init__(self, *args, **kwargs):
        format = kwargs.get("format", "")
        if format in SUPPORTED_FORMATS:
            self.format = format
        else:
            raise Exception("Unsupported format")
        super(WeixinAPI, self).__init__(*args, **kwargs)

    validate_token = bind_method(
        path="/sns/auth", accepts_parameters=["openid"], response_type="entry"
    )

    user = bind_method(
        path="/sns/userinfo", accepts_parameters=["openid"], response_type="entry"
    )
