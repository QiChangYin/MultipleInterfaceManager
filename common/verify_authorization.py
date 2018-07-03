#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import request, g
from functools import wraps
import logging
from common.format_render import json_detail_render
from HttpApiManager.models import UserInfo
logger = logging.getLogger('MultipleInterfaceManager')


def is_admin():
    return 'admin' in [r.get('name') for r in g.role]

def required(func):

    def dec(func):
        @wraps(func)
        def _(*args, **kwargs):
            username = request.get('account')
            password = request.get('password')
            if UserInfo.objects.filter(username__exact=username).filter(password__exact=password).count() == 1:
                logger.info('{username} 登录成功'.format(username=username))
                request.session["login_status"] = True
                request.session["now_account"] = username
                return func(*args, **kwargs)
            else:
                return json_detail_render(403)
        return _
    return dec

