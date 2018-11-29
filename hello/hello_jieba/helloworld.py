# coding: utf-8
import jieba


lines = [
    '鑫茂天财酒店',
    '天穆镇买房',
    '宅教授',
]


for line in lines:
    words = jieba.cut(line)
    print('|'.join(words))
