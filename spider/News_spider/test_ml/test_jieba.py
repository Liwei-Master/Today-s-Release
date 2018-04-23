# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 16:23
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : test_jieba.py

import pymysql
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import jieba
import lda
import numpy as np


def mysql_run_sql(sql):
    db = pymysql.connect(host='***.18.***.51', port=3306, user='root', password='****', database='****',
        charset='utf8', )
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    # # 关闭数据库连接
    db.close()
    return data


# 导入停用词库
stopwords = open('D:\****\stop_words.txt', 'r', encoding='utf-8').readlines()
stops = [stopword.strip() for stopword in stopwords]

content = mysql_run_sql("SELECT c_content FROM math_compute.news_result_02")


# atl_list = json_to_list(content)

def text_to_words(text):
    words = jieba.lcut(str(text).strip())
    meaningful_words = [w for w in words if not w in stops]
    return ' '.join(meaningful_words)


clean_content = [text_to_words(raw_review) for raw_review in content[1]]

# 从文本中提取1000个最重要的特征关键词

# vectorizer = CountVectorizer(analyzer="word", tokenizer=None, \
# preprocessor=None, stop_words=None, token_pattern=r"(?u)\b\w+\b", ngram_range=(1,1), max_features=None)
# tf = vectorizer.fit_transform(clean_content)
n_features = 1000
tf_vectorizer = TfidfVectorizer(strip_accents='unicode', max_features=n_features, stop_words='english')
tf = tf_vectorizer.fit_transform(clean_content)

# 定义主题数量
n_topics = 1
lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=50, learning_method='online', learning_offset=50,
                                random_state=0)
lda.fit(tf)
# n_topics = 5
# model = lda.LDA(n_topics = n_topics,n_iter = 500,random_state = 1)
# model.fit(tf)
''''' 
#主题-单词分布 
topic_word = model.topic_word_ 
print("type(topic_word): {}".format(type(topic_word)))   
print("shape: {}".format(topic_word.shape))   
print(clean_content[:3])  
print(topic_word[:, :3])   

for n in range(5):   
    sum_pr = sum(topic_word[n,:])   
    print("topic: {} sum: {}".format(n, sum_pr))   

#计算各主题Top-N个单词 
n = 5  
for i ,topic_dist in enumerate(topic_word): 
    topic_words = np.array(tf)[np.argsort(topic_dist)][:-(n+1):-1] 
    print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))   
'''


###将每个主题里面的前若干个关键词显
def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)

        print(" ".join([feature_names[i]

                        for i in topic.argsort()[:-n_top_words - 1:-1]]))

    print()


n_top_words = 20
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)