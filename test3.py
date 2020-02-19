from gensim.models import KeyedVectors
import numpy as np

model = KeyedVectors.load_word2vec_format('./entity_vector.model.bin', binary=True)
a = np.zeros((len(), 200))
cnt = 0
with open('./set_word_list.txt') as file:
    a = np.zeros((len(),200))
    for vo in file:
        # print(vo)
        try:
            cnt += 1
            vo_model = model[vo.rstrip('\n')]
        except:
            continue
        a = np.vstack((a, np.array(vo_model)))
        # print(vo.rstrip('\n'))
np.save('word_vector.npy', a)
print(cnt)
