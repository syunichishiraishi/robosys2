# robosys
ロボットシステム学　課題2です。

パブリッシャ(count.py)から出力されたデータをサブスクライバ(twice.py)で加工して表示します。

パブリッシャの内容
・数値データを1から順に、サブスクライバに送信する。
サブスクライバの内容
・パブリッシャから受け取った数値データを5の倍数だけ選んで端末に表示する。

[使い方]

1. 端末を3つ起動させる。

2. 端末(1つ目)で以下のコマンドを実行し、ROSを起動させる。 

  $ roscore 


3. 端末(2つ目)で以下のコマンドを実行
  
  $ ~/catkin_ws/src/mypkg/scripts

  $ vi count.py

  $ vi twice.py

  $ chmod 755 count.py

  $ chmod 755 twice.py

  $ rosrun mypkg count.py


4. 端末(3つ目)で以下のコマンドを実行

  $ rosrun mypkg twice.py
