# Micro:bitで使うパッケージを指定する
from microbit import *

# ずっと入力を待ちます。
while True:
    # pin1がタッチされた時（通電した時）
    if pin1.is_touched():
        # 笑顔を表示する
        display.show(Image.HAPPY)
    # pin1がタッチされていない時（通電していない時）
    else:
        # 泣き顔を表示する
        display.show(Image.SAD)

