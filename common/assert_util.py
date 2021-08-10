import json
import pytest

from common.common_util import get_json_value_by_key
from common.logger import Log


class Assertions:

    def assert_text(self, body, expected_msg):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:

        """
        assert body == expected_msg

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:

        """
        assert expected_msg in body

    def get_expected_msg_list(self,vaildate):
        """
        获取用例中断言数据list
        :param vaildate:
        :return:

        """
        assert_list = list(vaildate)
        expected_msg_list =[]

        for i in assert_list:
            expected_msg = " ".join('%s' % id for id in get_json_value_by_key(vaildate, i))
            expected_msg_list.append(expected_msg)
        return expected_msg_list

    def get_body_msg_list(self,vaildate,res):
        """
        获取body中断言数据list
        :param vaildate:eq
        :param res:
        :return:

        """
        expected_msg_list = []
        assert_list = list(vaildate)
        for i in assert_list:
            expected_msg = " ".join('%s' % id for id in get_json_value_by_key(json.loads(res.text), i))
            expected_msg_list.append(expected_msg)

        return expected_msg_list

    @pytest.mark.usefixtures()
    def assert_handle(self,assert_code,eq,res):
        """
        根据assert_code进行不同的断言处理
        :param assert_code:断言方式验证码
        :param eq:断言数据
        :param res:返回boby
        :return:

        """
        log = Log()
        try:
            if assert_code == 0:
                expected_msg_list = self.get_expected_msg_list(eq)

                for i in expected_msg_list:
                    self.assert_in_text(res.text, i)
                    log.info("断言结果：pass (%s in Response Body)"%i)

            elif assert_code == 1:
                list_2 = Assertions().get_body_msg_list(eq, res)
                list_1 = Assertions().get_expected_msg_list(eq)

                dict_1 = {}
                """ zip打包用法,同时遍历两个list """
                for symbol, digit in zip(list_1, list_2):
                    dict_1[symbol] = digit

                for key, value in dict_1.items():
                    self.assert_text(key, value)
                    log.info("断言结果：pass (%s == %s)" % (key,value))
        except AssertionError:
            log.warning("断言失败，请查看用例内断言数据")
        except Exception as ex:
            log.warning("出现如下异常:%s" % ex)


