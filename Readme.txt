図書館案内ロボット音声認識システム v1.0	H28 10/11

環境:Linux	Julius-4.4.2

音声認識形式

�@モード

ロボットには4つのモードを持っている。
1．待機
特定のワードが発声されるまで待機する。

2．発声
モードが変わるときの境目に移行するモード。主にロボットが喋りだすとき。

3．行動
命令を受けるとその命令を完遂させるために行動する。終了すると待機モードへ移行する。

4．会話
特定のワードが発生されると移行する。簡単な応答はできるようにする。

�Aプロセス例
本の案内：待機→発声→行動→発声→待機
会話：待機→発声→会話→発声→待機

