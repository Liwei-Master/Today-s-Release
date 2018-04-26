# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 15:40
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : test_.py

cities = {
	'beiJing':{
		'country':'china',
		'popu':'18',
		'place':'palance',
	},
	'shangHai':{
		'country':'china',
		'popu':'20',
		'place':'liJiangTower',
	},
}

for city,cid in cities.items():
    print('*'*20)
    print('City: ',city)
    for k , v in cid.items():
        print(k,': ',v)
