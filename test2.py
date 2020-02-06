from pathlib import Path
import MeCab
import re

path = Path(__file__).parent
path /= './Data'
print(path.resolve())
tagger = MeCab.Tagger("-Owakati")

hinshi_list = ['名詞', '動詞', '形容詞', '副詞', '助詞', '接続詞', '助動詞', '連体詞', '感動詞']


def extract_words(tex):
    node = tagger.parseToNode(tex)
    # print(tex)
    while node:
        surface = node.surface  # これが文字列
        feature = node.feature  # 情報をとってくる
        data = feature.split(',')
        hinshi = data[0]
        if hinshi in hinshi_list:
            return surface
        node = node.next


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
        print(word_list)
        # f = open('word_list.txt', 'w')
        # for l in word_list:
        #     f.write(str(l) + "\n")
        # f.close()
