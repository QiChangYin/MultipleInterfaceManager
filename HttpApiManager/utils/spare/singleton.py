# /usr/bin/env python
# -*- coding:utf-8 -*-

class Borg(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            ob = super(Borg, cls)
            cls._instance = ob.__new__(cls, *args, **kwargs)
        return cls._instance

class Borg(object):

    _instance = None

    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            ob = super(Borg,cls)
            print(ob)
            print(type(ob))
            cls._instance = ob.__new__(cls,*args,**kwargs)
            print(cls._instance)
            print(type(cls._instance))
        return  cls._instance

class shared_attribute(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        print(cls)
        ob = super(shared_attribute, cls).__new__(cls, *args, **kwargs)
        print(ob)
        print(ob.__dict__ )
        ob.__dict__ = cls._state
        return ob

class  Borg2(object):

    _state ={}

    def __new__(cls, *args, **kwargs):
        ob = super(Borg2,cls).__new__(cls,*args,**kwargs)
        ob.__dict__ = cls._state




def singleton(cls):
    """
    :param cls: 单例名称
    :return:
    """
    _instance = {}

    def _singleton(*args, **kwargs):

        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        print(_instance[cls])
        print(type(_instance[cls]))
        return _instance[cls]
    return _singleton


@singleton
class A(object):
    a = 1
    def __init__(self, x=0):
        self.x = x


class B(shared_attribute):
    a = 1
    def __init__(self, x=0):
        self.x = x

class C(object):
    __metaclass__ = shared_attribute
    a = 1
    def __init__(self, x=0):
        self.x = x



if __name__ == "__main__":
    print("aaa")
    # a1 = A(2)
    # a2 = A(3)
    # print(a1)
    # print(a2)
    # A.a = 1000
    # print(a1.__dict__)
    # print(a2.__dict__)
    # print(A.a)
    b1 = B()
    b2 = B()
    print(b1)
    print(b2)

    b1.a = 10
    print(b1.a)
    print(b2.a)
    print(b1.__dict__)
    print(b2.__dict__)