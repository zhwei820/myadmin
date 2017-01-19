#!/usr/bin/env python
# coding=utf-8

import json
import logging
import time

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.files import File
# from rest_framework.authtoken.models import Token

# from account.models import UserProfile, Account, InviteQcode, UserOpenID, \
#     UserDeviceBind
# from ios_push.msg_pusher import send_push_msg_api
# from trial.models import AtmTask
# from utils.tools import redis_ins, close_db_connection
# from wechat.models import WechatCustomMessage
# from wechat_sdk.basic import WechatBasic

logger = logging.getLogger("cron")

def cronjob():
    logger.info("lalalalalala")
    pass