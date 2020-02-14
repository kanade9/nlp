from gensim.models import KeyedVectors
import numpy as np

model = KeyedVectors.load_word2vec_format('./entity_vector.model.bin', binary=True)
#
# print(model['カレー'].shape)
# print(np.array((model['こんにちは'])))
# results = model.most_similar(u'[]')
# for result in results:
#     print(result)
m = ['カレー', 'おにぎり']
a = np.zeros((1, 200))

for i in m:
    a = np.vstack((a, np.array(model[i])))

print(a)