from natto import MeCab

# 動作確認用コード
tagger = MeCab("-Owakati")
# tagger = Mecab.Tagger("-Ochasen")
text = 'おはようございます。'
print(tagger.parse(text))

with MeCab() as nm:
    for n in nm.parse('あらゆるピンチの時には必ずヒーローが現れる。', as_nodes=True):
        # ignore any end-of-sentence nodes
        if not n.is_eos():
            # n.featureはstring型なので品詞を取得するために','を探してそこまでを取得する。
            print('{}\t{}'.format(n.surface, n.feature[:n.feature.find(',')]))
