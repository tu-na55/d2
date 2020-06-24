import subprocess
import glob
pythonの場合、 type(moji) としたときで取得できる型が str であっても、
cp932なstrだったり、utf - 8なstrだったりと、すべてが同じ文字コードとは限らないわけですが
そのおかげで 実は違うstrだったものを＋したりしてしまってErrorになってしまうので
なにで取得して、どう使うのか意識しつつ
日本WINのパスはcp932で扱ってあげるとOKというわけですね。

上の例の場合

# coding: utf-8
# 日本語を含む文字ファイルを取得
exec_files = glob.glob(u"E:/趣味/test/*.txt")
for i in exec_files:
    # 標準出力を取得
get_val = subprocess.check_output(['test.exe', i.encode("cp932")])


# coding: utf-8


# 日本語を含む文字ファイルを取得
exec_files = glob.glob(u"E:/趣味/test/*.txt")

for i in exec_files:
    # 標準出力を取得
    get_val = subprocess.check_output(['test.exe', i.encode("cp932")])

こうすればいけました。

さらなるトラップ
この場合、globはutf - 8のunicodeを引数にしているためか帰ってくる値もunicodeになります。
ですが、

# coding: utf-8
# 日本語を含む文字ファイルを取得
exec_files = glob.glob("S:/趣味/test/*.*")
print exec_files


# coding: utf-8


# 日本語を含む文字ファイルを取得
exec_files = glob.glob("S:/趣味/test/*.*")
print exec_files

こうすると、ファイルは存在するのにファイルの一覧は取得できませんでした。
これは、utf - 8なstrを引数にしているため
WINDOWSが文字を認識できずに取得できなかったためです。
なので、

# coding: utf-8
# 日本語を含む文字ファイルを取得
exec_files = glob.glob(u"S:/趣味/test/*.*".encode('cp932'))
print exec_files


# coding: utf-8


# 日本語を含む文字ファイルを取得
exec_files = glob.glob(u"S:/趣味/test/*.*".encode('cp932'))
print exec_files

まぁまずこんな書き方しねーよwwwっていう気もしますが、
日本語ありのstrでglobを使う時はcp932にしないとNGという話ですね。

・  # coding: utf-8　の場合は、ファイル内で u”” にすると、utf-8になる
・Windowsはcp932で解釈される

なので、Twitterでも指摘があったとおり
・Windowsから取得するstrならば unicode(val, ’cp932′) で、unicodeに変換してあげる
・strであわせるなら　str(utf - 8) -> unicode -> str(cp932) のようにunicodeを介してcp932にあわせてあげる
すると、安全だよ　という事でした

けっこうPythonさわってますが、今更知りました。やっぱり適当な解釈でなんとなく進めちゃだめですね（汗
