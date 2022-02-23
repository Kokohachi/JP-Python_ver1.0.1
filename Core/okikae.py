from fileinput import filename

filename = input("ファイルの名前をどうぞ⇒")
filename = "input/" + filename + ".py"
f = open(filename, "r", encoding="UTF-8")
data = f.read()
NewData=data.replace("もしも", "if").replace("画面表示", "print").replace("その他もしも", "elif").replace("次の間", "while").replace("次を仕入れる", "import").replace("次の中から", "from").replace("次として", "as").replace("関数設定", "def").replace("高さ", "height").replace("幅", "width")
f.close()
f = open(filename, 'w', encoding="UTF-8")
f.write(NewData)
print('変換完了！')
f.close()
