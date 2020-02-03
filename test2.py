from pathlib import Path
from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import re

path = Path(__file__).parent
path /= './Data'
print(path.resolve())


def extract_words(tex):
    tokens = t.tokenize(tex)
    return [token.base_form for token in tokens if token.part_of_speech.split(',')[0] in ['名詞', '動詞', '形容詞', '副詞']]


for file_name in path.iterdir():
    print(file_name)

    # 一応textはsjisで。
    with open(file_name, encoding='sjis')as file:
        text = file.read()

        # ヘッダ部分の除去
        text = re.split('\-{5,}', text)[2]
        # フッタ部分の除去
        text = re.split('底本：', text)[0]
        # | の除去
        text = text.replace('|', '')
        # ルビの削除
        text = re.sub('《.+?》', '', text)
        # 入力注の削除
        text = re.sub('［＃.+?］', '', text)
        # 空行の削除
        text = re.sub('\n\n', '\n', text)
        text = re.sub('\r', '', text)

        # 文書の整形出力確認
        # f = open('output.txt', 'w')
        # f.write(text)
        # f.close()

        t = Tokenizer()

        sentences = text.split('。')
        word_list = [extract_words(sentence) for sentence in sentences]

        # 単語リスト生成確認
        # f = open('word_list.txt', 'w')
        # for l in word_list:
        #     f.write(str(l)+"\n")
        # f.close()

        # modelの生成実験
        model = word2vec.Word2Vec(word_list, size=100, min_count=5, window=5, iter=3)
        model.save("word2vec_genism_model_kanade_sample")
