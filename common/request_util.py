import requests


class RequestUtil:

    def __init__(self):

        #初始化基本路径
        #self.base_url = read_config_yaml('url','base_url')
        #初始化请求数据（如果不初始化这个变量，则get,post,delete,put方法传参数时会报错）
        self.last_data = {}

    def get(self,url,headers,data):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        res = requests.get(url=url,headers=headers,params=data)
        return res

    def post(self,url,headers,data):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        res = requests.post(url=url,headers=headers,json=data)
        return res

    def delete(self,url,headers,data):
        """
        Delete请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        res = requests.delete(url=url,headers=headers,json=data)
        return res

    def put(self,url,headers,data):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        res = requests.put(url=url,headers=headers,json=data)
        return res


    def send_request(self,method,url,data=None,headers=None):
        """
        请求封装
        :param method:请求方法
        :param url:url地址
        :param data:参数
        :param header:请求头
        :return:

        """
        try:
            self.last_data = str(method).lower()

            if self.last_data == 'get':
                res = self.get(url,headers,data)
                return res
            elif self.last_data == 'post':
                res = self.post(url,headers,data)
                return res
            elif self.last_data == 'delete':
                res = self.delete(url,headers,data)
                return res
            elif self.last_data == 'put':
                res = self.put(url, headers, data)
                return res
        except AttributeError:
            print("找不到对应的对象的属性")
        except Exception as ex:
            print("出现如下异常:%s" % ex)

