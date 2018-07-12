import json

from django import template

register = template.Library()


@register.filter(name='data_type')
def data_type(value):
    """
    返回数据类型 自建filter
    :param value:
    :return: the type of value
    """
    return str(type(value).__name__)

# 第一个参数是在模板中使用的过滤器的名字
# #第二个就是你的过滤器函数引用名
@register.filter(name='convert_eval')
def convert_eval(value):
    """
    数据eval转换 自建filter
    :param value:
    :return: the value which had been eval
    """
    return eval(value)


@register.filter(name='json_dumps')
def json_dumps(value):
    return json.dumps(value, indent=4, separators=(',', ': '), ensure_ascii=False)
