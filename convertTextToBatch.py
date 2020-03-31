from torchtext import data, datasets

textPath = "../Data/kokoro.txt"
TEXT = data.Field(sequential=True, use_vocab=True)
pos = data.TabularDataset(
    path=textPath, format='csv',
    fields=[('text', TEXT)])

# 辞書を作成する
TEXT.build_vocab(pos)
