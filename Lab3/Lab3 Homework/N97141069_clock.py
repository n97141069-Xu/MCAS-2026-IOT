import tm1637
from datetime import datetime
from time import sleep

# 請根據實際接線修改 GPIO 腳位 (BCM 模式)
CLK = 23
DIO = 24

# 初始化 TM1637 顯示器
tm = tm1637.TM1637(clk=CLK, dio=DIO)
tm.brightness(3) # 設定亮度 (0-7)

print("時鐘運作中... (按 Ctrl+C 結束)")

try:
    while True:
        # 取得當前真實時間
        now = datetime.now()
        
        show_colon = now.microsecond < 500000
   
        tm.numbers(now.hour, now.minute, show_colon)
        
        sleep(0.1)

except KeyboardInterrupt:
    print("\n關閉時鐘")
    tm.write([0, 0, 0, 0])