import allure
import pytest

from common.common_util import write_extract_yaml, read_extract_yaml, get_testcase_list
from common.request_util import RequestUtil
from common.assert_util import Assertions
class TestApi:

    @pytest.mark.parametrize('args',get_testcase_list())
    @allure.feature(get_testcase_list()['name'])
    def test_api(self, args):
        '''遍历每一个yaml测试用例集'''

        #如果接口不需要token and 参数为空
        try:
            if args['request']['headers']['token'] == 1 and args['request']['data'] is None:

                res = RequestUtil().send_request(args['request']['method'], args['request']['url'])

                #判断使用哪一种断言方式（0代表断言值相等 1代表断言被包含关系）
                Assertions().assert_handle(args['assert_code'],args['vaildate']['eq'],res)


            #如果接口需要token and 参数为空
            elif args['request']['headers']['token'] == 0 and args['request']['data'] is None:
                res = RequestUtil().send_request(args['request']['method'],args['request']['url'],headers=read_extract_yaml('extract.yaml'))

                #判断使用哪一种断言方式（0代表断言值相等 1代表断言被包含关系）
                Assertions().assert_handle(args['assert_code'], args['vaildate']['eq'], res)

            #如果接口不需要token and 参数不为空
            elif args['request']['headers']['token'] == 1 and args['request']['data'] is not None:
                res = RequestUtil().send_request(args['request']['method'], args['request']['url'],args['request']['data'])
                #判断当前接口是否为登录接口

                if args['name'] == '登录接口':
                    write_extract_yaml(res.headers['authorization'])


                #判断使用哪一种断言方式（0代表断言值相等 1代表断言被包含关系）
                Assertions().assert_handle(args['assert_code'],args['vaildate']['eq'],res)


            #如果接口需要token and 参数不为空
            elif args['request']['headers']['token'] == 0 and args['request']['data'] is not None:
                res = RequestUtil().send_request(args['request']['method'], args['request']['url'],args['request']['data'],
                                                headers=read_extract_yaml('extract.yaml'))

                #判断使用哪一种断言方式（0代表断言值相等 1代表断言被包含关系）
                Assertions().assert_handle(args['assert_code'],args['vaildate']['eq'],res)
        except AttributeError as e:
            print("出现如下异常:%s" % e)


