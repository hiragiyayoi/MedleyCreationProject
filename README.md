# MedleyCreationProject
メドレーを作成するpythonプロジェクト

## 概要
.wav、.mp3、.oggのいずれかの形式のファイルをつなげてメドレーとして制作するPythonのプロジェクトです。  
メドレーにおける楽曲の再生順番はOSの標準機能で並び替えてください。  
エクスプローラーなどで表示されたファイルを上から順番にメドレーとして制作します。

## 前提条件
Python 3.11.9以降のバージョンとvenv、pipの実行環境が入っているものとする。
最新バージョンでの実行をおすすめします。


## 使い方
ここでは、Ubuntuでの実行方法を記載します。  

1. MedleyCreationProjectのルートディレクトリに移動する
```sh
$ cd [MedleyCreationProjectのパス]
```

2. venvをアクティベートする。
```sh
$ . ./bin/activate 
```

3. 以下のpipコマンドよりパッケージをインストールする
```sh
$ pip install librosa soundfile numpy
```

4. Linux環境では、FastRun.sh、Windows環境ではFastRun.batを実行して必要なフォルダを作成する。（music-list、output-musicの２つ）  

**Linuxの場合**
```sh
$ ./scripts/FastRun.sh
```
**Windowsの場合**
```
$ ./scripts/FastRun.bat
```

5. "music-list"にメドレーに入れたい楽曲（.wav、.mp3、.ogg）を配置する

6. main.pyを実行する
```sh
$ python3 ./scripts/main.py
```

7. pythonの処理停止後に"output-music"にmedley.wavが出力されている


## Q＆A
**Q.** メドレーに加える楽曲の形式は統一しなければならないのでしょうか？  
**A.** wav、.mp3、.oggのいずれかの形式であれば混在していても大丈夫です

**Q.** メドレーの総再生時間に制限はありますか？  
**A.** 制限はありません。ただし、メドレーの総再生時間が長くなると実行時間が長くなるため、ご自身の実行環境とご相談ください。

**Q.** メドレーに加える１楽曲の長さに制限はありますか？  
**A.** ありません。ただし、メドレーの総再生時間が長くなると実行時間が長くなるため、ご自身の実行環境とご相談ください。

**Q.** GUIによる操作に対応させる予定はありますか？  
**A.** Pythonの標準ライブラリによるウィンドウを作成予定です。



