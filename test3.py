from gensim.models import KeyedVectors
import numpy as np

model = KeyedVectors.load_word2vec_format('./entity_vector.model.bin', binary=True)
with open('./set_word_list.txt') as file:
    list = [i for i in file]
    print(list)
    a = np.zeros((len(list), 200))
    cnt = -1
    for vo in list:
        cnt += 1
        # print(vo)
        try:
            vo_model = model[vo.rstrip('\n')]
            a[cnt]=vo_model
        except:
            continue
        # print(vo.rstrip('\n'))
np.save('word_vector.npy', a)
print(cnt)
