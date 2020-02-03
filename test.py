import MeCab
# 動作確認用コード
# tagger = MeCab.Tagger("-Owakati")
tagger = MeCab.Tagger("-Ochasen")
text = '今日はすごく暑いのでアイスクリームが食べたいです。'
print(tagger.parse(text))
