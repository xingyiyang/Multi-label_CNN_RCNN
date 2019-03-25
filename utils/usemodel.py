# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import gensim
import numpy as np


def cidianjuzhen():
    model = gensim.models.Word2Vec.load('../data/wiki.model')
    print(type(model))
    print(len(model.wv.vocab.items()))
    print(model.vector_size)


# 参数解释 https://blog.csdn.net/angus_monroe/article/details/76999920
if __name__ == '__main__':
    # model = word2vec.Word2Vec.load("sw_cut_std_zh_wiki_01.model")
    # print(model.similarity("跑步", "散步"))
    # model = gensim.models.Word2Vec.load('../data/sw_cut_std_wiki_00.model')
    # word1 = '屏幕'
    # word2 = '计算机'
    # if word1 in model:
    #     print("'%s'的词向量为： " % word1)
    #     print(model[word1])
    # else:
    #     print('单词不在字典中！')
    #
    # result = model.most_similar(word2)
    # print("\n与'%s'最相似的词为： " % word2)
    # for e in result:
    #     print('%s: %f' % (e[0], e[1]))
    #
    # print("\n'%s'与'%s'的相似度为： " % (word1, word2))
    # print(model.similarity(word1, word2))
    #
    # print("\n'早餐 晚餐 午餐 中心'中的离群词为： ")
    # print(model.doesnt_match("早餐 晚餐 午餐 中心".split()))
    #
    # print("\n与'%s'最相似，而与'%s'最不相似的词为： " % (word1, word2))
    # temp = (model.most_similar(positive=[u'篮球'], negative=[u'计算机'], topn=1))
    # print('%s: %s' % (temp[0][0], temp[0][1]))
    cidianjuzhen()

