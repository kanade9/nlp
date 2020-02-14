from gensim.models import KeyedVectors
import numpy as np

model = KeyedVectors.load_word2vec_format('./entity_vector.model.bin', binary=True)
a = np.zeros((1, 200))
with open('./set_word_list.txt')as file:
    for vo in file:
        # print(vo)
        try:
            vo_model = model[vo.rstrip('\n')]
        except:
            continue
        a = np.vstack((a, np.array(vo_model)))
        # print(vo.rstrip('\n'))
np.save('word_vector.npy', a)
