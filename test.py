import MeCab
# 動作確認用コード
# tagger = MeCab.Tagger("-Owakati")
tagger = MeCab.Tagger("-Ochasen")
text = 'おはようございます。'
print(tagger.parse(text))
