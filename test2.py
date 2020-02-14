from pathlib import Path
from natto import MeCab
from gensim.models import KeyedVectors
import re, chakin

# chakin.search(lang='Japanese')
# chakin.download(number=6, save_dir='./')

# model = KeyedVectors.load_word2vec_format("./downloadfile", binary=False)
path = Path(__file__).parent

path /= './Data'
print(path.resolve())

tagger = MeCab("-Owakati")

hinshi_list = ['名詞', '動詞', '形容詞', '副詞', '助詞', '接続詞', '助動詞', '連体詞', '感動詞']


def extract_words(tex):
    with MeCab() as nm:
        for n in nm.parse(tex, as_nodes=True):
            # print(n)
            if not n.is_eos():
                # n.featureはstring型なので品詞を取得するために','を探してそこまでを取得する。
                surface = n.surface
                hinshi = n.feature[:n.feature.find(',')]
                # print(surface, hinshi)
                if hinshi in hinshi_list:
                    return surface


#
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
        f = open('output.txt', 'w')
        f.write(text)
        f.close()

        sentences = text.split('。')
        word_list = [extract_words(sentence) for sentence in sentences]
        word_list.pop(-1)  # リスト末尾はNoneとなるため取り除く

        # 単語リスト生成確認
        set_word_list = set(word_list)
        print(set_word_list)
        f = open('set_word_list.txt', 'w')
        for l in set_word_list:
            f.write(str(l) + "\n")
        f.close()
