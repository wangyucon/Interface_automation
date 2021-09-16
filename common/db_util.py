import pymysql


class DB:
    def __init__(self,db_name):
        self.conn = pymysql.connect(host='172.17.14.225',
                                    port=13306,
                                    user='root',
                                    passwd='st123456',
                                    db=db_name)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def __del__(self):  # 析构函数，实例删除时触发
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self,field,tb_name,term,name):
        """
        根据条件查询出指定字段的Value
        :param tb_name:table name
        :param field:指定字段
        :param term:条件字段
        :param term:条件
        :return:

        """
        result = self.query("select {} from {} where {}='{}'".format(field,tb_name,term,name))
        return result

    # name
    def del_customer(self, tb_name,term,name):
        self.exec("delete from {} where {}='{}'".format(tb_name,term,name))


if __name__ == '__main__':
    #DB().del_customer("海亮食堂")
    a = DB('st_order').check_user('id','st_customer','name','明康汇有限公司')
    print(a[0]['id'])