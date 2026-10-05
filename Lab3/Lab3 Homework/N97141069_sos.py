import RPi.GPIO as GPIO
import time

LED_PIN = 11      
BUZZER_PIN = 12   

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 建立蜂鳴器的 PWM 物件 (頻率 523Hz，大約 C5 音高)
buzzer_pwm = GPIO.PWM(BUZZER_PIN, 523)

# --- 摩斯密碼時間設定 (單位：秒) ---
DOT = 0.2         # 短訊號 (.)
DASH = 0.6        # 長訊號 (-)
GAP = 0.2         # 每個聲光訊號之間的短暫停頓
LETTER_GAP = 0.6  # 字母 (S和O) 之間的停頓

def play_signal(duration):
    GPIO.output(LED_PIN, GPIO.HIGH) # 燈亮
    buzzer_pwm.start(50)            # 發聲 (50% 工作週期)
    
    time.sleep(duration)            # 持續指定的秒數
    
    GPIO.output(LED_PIN, GPIO.LOW)  # 燈滅
    buzzer_pwm.stop()               # 停聲
    time.sleep(GAP)                 # 訊號結束後停頓一下

print("開始發送 SOS 摩斯密碼 (按 Ctrl+C 停止)...")

try:
    while True:
        # 發送 S : 三個短訊號 (...)
        print("S (...)")
        for _ in range(3):
            play_signal(DOT)
        time.sleep(LETTER_GAP - GAP) 

        # 發送 O : 三個長訊號 (---)
        print("O (---)")
        for _ in range(3):
            play_signal(DASH)
        time.sleep(LETTER_GAP - GAP)

        # 發送 S : 三個短訊號 (...)
        print("S (...)")
        for _ in range(3):
            play_signal(DOT)
        
        # 兩次 SOS 循環之間的停頓
        print("--- 暫停 2 秒 ---")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n收到終端機中斷指令 (Ctrl+C)")
finally:
    GPIO.cleanup()
    print("GPIO 狀態已清除，程式結束")