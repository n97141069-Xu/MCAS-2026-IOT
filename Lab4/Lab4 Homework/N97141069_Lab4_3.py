import serial
import time

# 設定 UART 連接埠與參數 (預設使用 /dev/serial0)
ser = serial.Serial(
    port='/dev/serial0',        # 對應 GPIO14 (TX) 和 GPIO15 (RX)
    baudrate=9600,              # 傳輸速率
    timeout=1                   # 讀取逾時設定 (秒)
)

# 傳送資料
def send_data(data):
    if ser.is_open:
        ser.write(data.encode('utf-8'))
        print(f"已傳送：{data}")

# 接收資料
def receive_data():
    if ser.is_open:
        incoming = ser.readline().decode('utf-8').strip()
        if incoming:
            print(f"收到資料：{incoming}")
        return incoming

# 主程式
try:
    print("請在下方輸入想傳送的數字或字元，輸入 'exit' 可結束測試。\n")   
    while True:
        user_input = input("請輸入欲傳送的資料: ")
        
        if user_input.lower() == 'exit':
            break
            
        send_payload = user_input + "\n"
        ser.write(send_payload.encode('utf-8'))
        print(f"[TX 發送端] 已送出 -> {user_input}")
        
        time.sleep(0.2)
        
        if ser.in_waiting > 0:
            incoming = ser.readline().decode('utf-8').strip()
            print(f"[RX 接收端] 成功收到 <- {incoming}\n")
        else:
            print("[RX 接收端] 警告：未收到回傳，請檢查杜邦線是否有確實接好。\n")   
    
except KeyboardInterrupt:
    print("程式中斷")

finally:
    if ser.is_open:
        ser.close()
        print("串列埠已關閉")