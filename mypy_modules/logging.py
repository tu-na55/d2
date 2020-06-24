import os
import logging

# from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG

####################
# handler: 出力先や使用するフォーマット、ファイル名など各種設定を用意
# formatters: 具体的な出力時のフォーマットを設定
# loggers: 使用するloggerの定義。上で設定したhandlerやformatterを紐付ける

# NOTSET	0	設定値などの記録（全ての記録）
# DEBUG	10	動作確認などデバッグの記録
# INFO	20	正常動作の記録
# WARNING	30	ログの定義名
# ERROR	40	エラーなど重大な問題
# CRITICAL	50	停止など致命的な問題
####################

# 現在のロギングの情報を取得(引数はファイル名)
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# handler
# get_handler = logging.FileHandler('log/logger.log')
# logger.addHandler(get_handler)

# 従来の出力
# logging.info('error{}'.format('outputting error'))
# logging.info('warning %s %s' % ('was', 'outputted'))
####################

# prj/mypy_modules/logging.py
PROJECT_ROOT = "../"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": PROJECT_ROOT + "log/logger.log",
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 1,
            "backupCount": 5,
        },
    },
    "formatters": {
        "verbose": {
            "format": "\t".join(
                [
                    "[%(levelname)s]",
                    "%(asctime)s",
                    "%(name)s.%(funcName)s:%(lineno)s",
                    "%(message)s",
                ]
            )
        },
    },
    "loggers": {
        "file": {
            "handlers": ["file"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
    },
}


def LogTest1():
    """ logTest"""
    # ログを出力する方法(実際にはログを出力したい場所で記述する)
    logging.debug("test")

    # logger.debug('DEBUGレベルのメッセージです')
    # logger.info('INFOレベルのメッセージです')
    # logger.warning('WARNINGレベルのメッセージです')
    # logger.error('ERRORレベルのメッセージです')
    # logger.critical('CRITICALレベルのメッセージです')


def LogTest2():
    logger = logging.getLogger("file")
    logger.info("ここでログを吐きたい！")
    logger.warn("DB write 失敗しました")
