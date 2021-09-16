import json
import pytest
from common.common_util import write_extract_yaml, read_extract_yaml, get_testcase_list, write_variable_yaml, \
    read_variable_yaml
from common.db_util import DB
from common.logger import Log
from common.request_util import RequestUtil
from common.assert_util import Assertions


class TestApi:

    @pytest.mark.parametrize('args',get_testcase_list())
    @pytest.mark.usefixtures('set_up')
    def test_api(self, args):
        global res
        log = Log()
        log.info("caseName: <%s>" % args['name'])
        '''遍历每一个yaml测试用例集'''

        #如果当前接口不需要token and 参数为空
        try:
            if args['request']['headers']['token'] == 1 and args['request']['data'] is None:

                res = RequestUtil().send_request(args['request']['method'], args['request']['url'])

                # 若接口调用存在问题则主动抛出异常
                if json.loads(res.text)["code"] == 1:
                    raise Exception("")
                #断言方式判断
                Assertions().assert_handle(args['assert_code'],args['vaildate']['eq'],res)

                # 判断当前接口是否需要存储变量
                if args['variable'] == 0:
                    # 是否通过数据库来提取变量
                    if args['db_operate'] == 0:
                        variable = DB(args['st_name']).check_user(args['value'],args['tb_name'],args['term'],args['t_value'])[0][args['value']]
                        write_variable_yaml(variable)
                    else:
                        pass
                else:
                    pass


            #如果当前接口需要token and 参数为空
            elif args['request']['headers']['token'] == 0 and args['request']['data'] is None:
                res = RequestUtil().send_request(args['request']['method'],args['request']['url'],headers=read_extract_yaml('extract.yaml'))

                # 若接口调用存在问题则主动抛出异常
                if json.loads(res.text)["code"] == 1:
                    raise Exception("")
                #断言方式判断
                Assertions().assert_handle(args['assert_code'], args['vaildate']['eq'], res)

                # 判断当前接口是否需要存储变量
                if args['variable'] == 0:
                    # 是否通过数据库来提取变量
                    if args['db_operate'] == 0:
                        variable = DB(args['st_name']).check_user(args['value'],args['tb_name'],args['term'],args['t_value'])[0][args['value']]
                        write_variable_yaml(variable)
                    else:
                        pass
                else:
                    pass


            #如果当前接口不需要token and 参数不为空
            elif args['request']['headers']['token'] == 1 and args['request']['data'] is not None:

                # 判断当前接口是否需要传递变量
                if args['request']['data_replace'] == 0:
                    args['request']['data'][args['request']['repalce']] = read_variable_yaml('variable.yaml')
                    res = RequestUtil().send_request(args['request']['method'], args['request']['url'],
                                                     args['request']['data'])
                else:
                    res = RequestUtil().send_request(args['request']['method'], args['request']['url'],
                                                     args['request']['data'])

                # 若接口调用存在问题则主动抛出异常
                if json.loads(res.text)["code"] == 1:
                    raise Exception("")
                #判断当前接口是否为登录接口
                if args['name'] == '登录接口':
                    write_extract_yaml(res.headers['authorization'])


                #断言方式判断
                Assertions().assert_handle(args['assert_code'],args['vaildate']['eq'],res)

                # 判断当前接口是否需要存储变量
                if args['variable'] == 0:
                    # 是否通过数据库来提取变量
                    if args['db_operate'] == 0:
                        variable = DB(args['st_name']).check_user(args['value'],args['tb_name'],args['term'],args['t_value'])[0][args['value']]
                        write_variable_yaml(variable)
                    else:
                        pass
                else:
                    pass


            #如果当前接口需要token and 参数不为空
            elif args['request']['headers']['token'] == 0 and args['request']['data'] is not None:

                #判断当前接口是否需要传递变量
                if args['request']['data_replace'] == 0:
                    args['request']['data'][args['request']['repalce']] = read_variable_yaml('variable.yaml')
                    res = RequestUtil().send_request(args['request']['method'], args['request']['url'],
                                                     args['request']['data'],
                                                     headers=read_extract_yaml('extract.yaml'))
                else:
                    res = RequestUtil().send_request(args['request']['method'], args['request']['url'],args['request']['data'],
                                                headers=read_extract_yaml('extract.yaml'))

                #若接口调用存在问题则主动抛出异常
                if json.loads(res.text)["code"] == 1:
                    raise Exception("")

                #断言方式判断
                Assertions().assert_handle(args['assert_code'],args['vaildate']['eq'],res)

                #判断当前接口是否需要存储变量
                if args['variable'] == 0:
                    #是否通过数据库来提取变量
                    if args['db_operate'] == 0:
                        variable = DB(args['st_name']).check_user(args['value'],args['tb_name'],args['term'],args['t_value'])[0][args['value']]
                        write_variable_yaml(variable)
                    else:
                        pass
                else:
                    pass

        except AttributeError as e:
            log.warning("出现如下异常:%s" % e)
        except Exception:
            log.error(res.text)




