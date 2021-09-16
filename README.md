### 接口自动化测试框架

欢迎使用 接口自动化测试框架，通过阅读以下内容，你可以快速熟悉 框架 ，并立即开始今天的工作。

### 框架组成

Pytest + Requests + yaml + logging + allure 

### 接口测试用例书写格式

-
  name: 用例标题
  request:
    method: 请求方式
    url: "http://xxxxxxx/xxxx/xxxx"
    data: 请求参数 json格式
    headers:
      token: 1  #1 不需要token 0 需要token
  assert_code: 0  #0代表断言值相等 1代表断言被包含关系
  vaildate:
    eq: 
      "mainTitle": "100" 断言

