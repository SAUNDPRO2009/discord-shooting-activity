from pypresence import Presence
import time

CLIENT_ID = 1508009803023122547

try:
    RPC = Presence(CLIENT_ID)
    RPC.connect()
    print("✅ Подключено к Discord!")
    
    RPC.update(
        state="🔫 На полигоне",
        details="Тренирую точность стрельбы",
        large_image="shooting",
        large_text="Стрелковая активность",
        start=int(time.time())
    )
    
    print("✅ Rich Presence установлен!")
    
    while True:
        time.sleep(15)
        
except KeyboardInterrupt:
    print("\n❌ Отключено")
    RPC.close()
except Exception as e:
    print(f"❌ Ошибка: {e}")
