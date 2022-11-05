from djangosnippets.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-(zuo!g9cok9y03$!pg7xg15u9hqjv%wpi!cj_fze$eg^&ryb+&"
)


ALLOWED_HOSTS = ["*"]


DEBUG = False


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# PostgreSQLを使用するようにする
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "djangodatabase",  # データベース名
        "USER": "djangouser",  # ユーザー名
        "PASSWORD": "djangopassword",  # パスワード
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# collectstaticしたときに集めたstaticファイルを置く場所 絶対パス
# OSのルートからの絶対パス
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'


# ログ設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    # ログ出力フォーマットの設定
    "formatters": {
        "dev": {
            "format": "%(asctime)s [%(levelname)s] %(process)d %(thread)d "
            "%(pathname)s:%(lineno)d %(message)s"
        },
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
    },
    # ハンドラの設定
    "handlers": {
        "file_info": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/var/log/django_snippets/info.log",
            "formatter": "dev",
        },
        "file_debug": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/var/log/django_snippets/debug.log",
            "formatter": "dev",
        },
    },
    # ロガーの設定
    "loggers": {
        # 自分で追加したアプリケーション全般のログを拾うロガー
        "": {
            "handlers": ["file_info"],
            "level": "INFO",
            "propagate": False,
        },
        # Django自身が出力するログ全般を拾うロガー
        "django": {
            "handlers": ["file_info"],
            "level": "INFO",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["file_debug"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
