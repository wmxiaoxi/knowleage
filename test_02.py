# coding:utf-8
import pytest
class TestCase():
    def setup(self):
        print("setup每个用例执行前都执行一次")
    def teardown(self):
        print("teardown每个用例执行后都执行一次")
    def setup_class(self):
        print("setup_class所有用例开始前")
    def teardown_class(self):
        print("teardown_class所有用例结束后")
    def setup_method(self):
        print("")


