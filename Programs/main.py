# -*- coding: utf-8 -*-

import subprocess
import time

def main():
    subprocess.call('julius')
    print("julius起動中")
    #ここに起動完了をチェックする処理

    while (result != 0):
        result = 0
        #ここにjuliusの起動後の<PleaseSpeak>と文字列を表示する処理
        result = ""#読み取った文字列
    if(result == "本を探して"):
        print("")
