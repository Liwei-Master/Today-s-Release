# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 10:10
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : test_mysql.py
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                            port=3306,
                            user='root',
                            password='root',
                            db='test',
                            charset='utf8',
                            use_unicode=True)
cursor = conn.cursor()

try:
    for x in range(1,10):
        p_id = ''
        # 查重处理
        cursor.execute("""select a_id from tb_user where name = %s and plat = %s """, ['name{}'.format(x),'plat{}'.format(x)])
        # 是否有重复数据
        repetition = cursor.fetchone()
        # 重复
        if repetition:
            if len(repetition) > 0:
                p_id = repetition[0]
            pass
        else:
            req_code  = cursor.execute(
                "UPDATE  tb_user set name=%s,pwd=%s,plat=%s where tb_user.name = %s and tb_user.plat = %s",
                ['name{}'.format(x),'pwd{}'.format(x),'plat{}'.format(x),'name{}'.format(x),'plat{}'.format(x)])

            if not req_code:
                cursor.execute("insert into tb_user (name,pwd,plat) values(%s,%s,%s)", ('name{}'.format(x), 'pwd{}'.format(x),'plat{}'.format(x)))
                p_id = cursor.lastrowid
        print('p_id ', p_id)
except Exception as e:
    print('error ',e)
    pass
else:
    conn.commit()
conn.close()
print('finish ---------- ')

"""
1 插入数据，成功 ---> author_id 
2 再次插入数据，失败（因为是同样的数据）  


"""