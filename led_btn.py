from machine import Pin  # type: ignore

# 黄色のLEDを14番ピンに設定
led_yellow = Pin(14, Pin.OUT)

# 赤色のLEDを10番ピンに設定
led_red = Pin(10, Pin.OUT)

# 緑色のLEDを2番ピンに設定
led_green = Pin(2, Pin.OUT)

# ボタンを28番ピンに入力として設定し、プルダウン抵抗を有効にする
btn = Pin(28, Pin.IN, Pin.PULL_DOWN)

# 黄色LEDの状態を保存する変数
led_yellow_state = 0

# 赤色LEDの状態を保存する変数
led_red_state = 0

# 緑色のLEDの状態を保存する変数
led_green_state = 0  # 修正しました

# ボタンの状態を保存する変数
btn_state = 0

# 無限ループ
while True:
    # ボタンが押されたかを確認
    if btn.value() == 1:
        btn_state = 1

    # ボタンが押された場合
    if btn_state == 1:
        # 黄色LEDの状態を切り替える
        led_yellow_state = 0 if led_yellow_state == 1 else 1
        led_yellow.value(led_yellow_state)

        # 赤色LEDの状態を切り替える
        led_red_state = 0 if led_red_state == 1 else 1
        led_red.value(led_red_state)

        # 緑色LEDの状態を切り替える
        led_green_state = 0 if led_green_state == 1 else 1
        led_green.value(led_green_state)

        # ボタンの状態をリセット
        btn_state = 0

    # エラーチェック
    if btn_state != 0 and btn_state != 1:
        print("Error!!!!")
        break  # ループを抜けてプログラムを終了
