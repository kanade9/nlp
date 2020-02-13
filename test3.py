from gensim.models import KeyedVectors
import chakin

# chakin.search(lang='Japanese')
# chakin.download(number=6, save_dir='./')
#
model = KeyedVectors.load_word2vec_format('./cc.ja.300.vec.gz', binary=False)
#
results = model.most_similar(u'[与田祐希]')
for result in results:
    print(result)