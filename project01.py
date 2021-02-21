
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
      print("{}が見つかりした".format(word))
    else:
      source.append(word)


if __name__ == "__main__":
    search()

print(source)

# CSVからの読み込み
path = "./Book1.csv"

with open(path,encoding="utf-8") as f:
    s = f.read()
    print(type(s))
    print(s)

# CSVへの書き込み
with open(path,mode="a",encoding="utf-8") as f:
    s = ("ぜんいつ")
    f.write(s)
with open(path,encoding="utf-8") as f:
    s = f.read()
    print(s)

