import time

def traffic_light():
    while True:
        print("🔴 RED - Stop")
        time.sleep(3)

        print("🟡 YELLOW - Get Ready")
        time.sleep(1)

        print("🟢 GREEN - Go")
        time.sleep(3)

        print("-" * 30)
        time.sleep(1)

if _name_ == "_main_":
    print("🚦 Traffic Light Simulator Started")
    traffic_light()
