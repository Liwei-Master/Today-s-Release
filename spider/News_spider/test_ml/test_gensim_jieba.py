# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 15:29
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : test_gensim_jieba.py

from gensim import corpora, similarities, models
import jieba

question = '马致远是元代领袖群英的散曲作家'
# 训练样本
raw_documents = ['0内容提要  马致远是元代领袖群英的散曲作家。他的散曲飘逸、奔放、老辣、清隽，被后世推为散曲第一家。他拓展了散曲的题材范围，提',
    '高了散曲的意境，在散曲史上享有很高的地位。他的散曲思想内容丰富，元散曲咏史、叹世、归隐、写景、闺情、叙事诸题材他都涉及，并各具',
    '成就。他制曲艺术精湛，风格典雅清丽，本色自然。他的散曲意境高妙，充满画意，语言清丽本色，人物栩栩如生，他长于心理刻划，善于运用', '各种修辞手法，达到很高的艺术境界，将元散曲推向高潮。']
corpora_documents = []
# 分词处理
for item_text in raw_documents:
    item_seg = list(jieba.cut(item_text))
    corpora_documents.append(item_seg)

# 生成字典和向量语料
dictionary = corpora.Dictionary(corpora_documents)
# print(dictionary)
# dictionary.save('dict.txt') #保存生成的词典
# dictionary=Dictionary.load('dict.txt')#加载

# 通过下面一句得到语料中每一篇文档对应的稀疏向量（这里是bow向量）
corpus = [dictionary.doc2bow(text) for text in corpora_documents]
# 向量的每一个元素代表了一个word在这篇文档中出现的次数
# print(corpus)
# corpora.MmCorpus.serialize('corpuse.mm',corpus)#保存生成的语料
# corpus=corpora.MmCorpus('corpuse.mm')#加载

# corpus是一个返回bow向量的迭代器。下面代码将完成对corpus中出现的每一个特征的IDF值的统计工作
tfidf_model = models.TfidfModel(corpus)
corpus_tfidf = tfidf_model[corpus]

'''
# 查看model中的内容  
for item in corpus_tfidf:
    print(item)
# tfidf.save("data.tfidf")  
# tfidf = models.TfidfModel.load("data.tfidf")  
# print(tfidf_model.dfs)  
'''  
print("-------------------下面是tfidf模型(第1个提问)----------------------------------------------------")  

similarity = similarities.Similarity('Similarity-tfidf-index', corpus_tfidf, num_features=600)  
test_data_1 = question  
test_cut_raw_1 = list(jieba.cut(test_data_1))  # ['北京', '雾', '霾', '红色', '预警']  
test_corpus_1 = dictionary.doc2bow(test_cut_raw_1)  # [(51, 1), (59, 1)]，即在字典的56和60的地方出现重复的字段，这个值可能会变化  
similarity.num_best = 5  
test_corpus_tfidf_1 = tfidf_model[test_corpus_1]  # 根据之前训练生成的model，生成query的IFIDF值，然后进行相似度计算  
# [(51, 0.7071067811865475), (59, 0.7071067811865475)]  
print(similarity[test_corpus_tfidf_1])  # 返回最相似的样本材料,(index_of_document, similarity) tuples  


print("-------------------下面是tfidf模型(第2个提问)----------------------------------------------------")  
test_data_2 = question  
test_cut_raw_2 = list(jieba.cut(test_data_2))  
test_corpus_2 = dictionary.doc2bow(test_cut_raw_2)  
test_corpus_tfidf_2 = tfidf_model[test_corpus_2]  
similarity.num_best = 3  
print(similarity[test_corpus_tfidf_2])  # 返回最相似的样本材料,(index_of_document, similarity) tuples  
print("-------------------下面是LSI模型-----------------------------------")  
# 使用LSI模型进行相似度计算  
lsi = models.LsiModel(corpus_tfidf)  
corpus_lsi = lsi[corpus_tfidf]  
similarity_lsi = similarities.Similarity('Similarity-LSI-index', corpus_lsi, num_features=400, num_best=2)  
# save  
# LsiModel.load(fname, mmap='r')#加载  
test_data_3 = question  
test_cut_raw_3 = list(jieba.cut(test_data_3))  # 1.分词  
test_corpus_3 = dictionary.doc2bow(test_cut_raw_3)  # 2.转换成bow向量  
test_corpus_tfidf_3 = tfidf_model[test_corpus_3]  # 3.计算tfidf值  
test_corpus_lsi_3 = lsi[test_corpus_tfidf_3]  # 4.计算lsi值  
# lsi.add_documents(test_corpus_lsi_3) #更新LSI的值  
print(similarity_lsi[test_corpus_lsi_3])
