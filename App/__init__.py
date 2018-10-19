


from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import config
from App.views import init_blue


def createApp(envName=None):
    app = Flask(__name__)

    app.config.from_object(config.get(envName or 'default'))

    init_blue(app)

    init_ext(app)

    init_api(app)

    return app
