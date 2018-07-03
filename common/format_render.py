#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from flask import jsonify
from flask import make_response
from MultipleInterfaceManager.settings import STATUS_CODE


def _render(resp):
    response = make_response(jsonify(resp))
#    response.headers["Access-Control-Allow-Origin"] = "*"
    return response



def json_list_render(code, data, limit, offset, message = None):
    if message is None:
        message = STATUS_CODE.get(code)
    resp = dict(
        code = code,
        limit = limit,
        offset = offset,
        message = message,
        data = data
    )
    return _render(resp)



def json_detail_render(code, data = [], message = None):
    if message is None:
        message = STATUS_CODE.get(code)
    resp = dict(
        code = code,
        message = message,
        data = data
    )
    return _render(resp)


def json_token_render(code, token, message = None):
    if message is None:
        message = STATUS_CODE.get(code)
    resp = dict(
        code = code,
        token = token,
        message = message
    )
    return _render(resp)

def json_detail_render_sse(code, data = [], message = None):
    if message is None:
        message = STATUS_CODE.get(code)
    resp = dict(code=code, message=message, data=data)
    return json.dumps(resp)
