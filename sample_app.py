from flask import Flask
from flask import Markup
from flask import redirect
from flask import request
from flask import jsonify

from weixin.client import WeixinAPI

app = Flask(__name__)

APP_ID = ''
APP_SECRET = ''
REDIRECT_URI = 'http://localhost.com/authorization'


@app.route("/authorization")
def authorization():
    code = request.args.get('code')
    api = WeixinAPI(appid=APP_ID,
                    app_secret=APP_SECRET,
                    redirect_uri=REDIRECT_URI)
    auth_info = api.exchange_code_for_access_token(code=code)
    api = WeixinAPI(access_token=auth_info['access_token'])
    resp = api.user(openid=auth_info['openid'])
    return jsonify(resp)


@app.route("/login")
def login():
    api = WeixinAPI(appid=APP_ID,
                    app_secret=APP_SECRET,
                    redirect_uri=REDIRECT_URI)
    code = request.args.get('code')
    redirect_uri = api.exchange_code_for_session_key(code)
    return redirect(redirect_uri)


@app.route("/")
def hello():
    return Markup('<a href="%s">weixin login!</a>') % '/login'


if __name__ == "__main__":
    app.run(debug=True)
