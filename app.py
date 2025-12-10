import requests
import time

def call_worker():
    print("[APP] Startuję zapytanie do workera...")
    start = time.time()
    try:
        response = requests.get("http://worker:5001/task", timeout=2)
        elapsed = round(time.time() - start, 3)
        data = response.json()

        print("[APP] Otrzymano odpowiedź z workera:")
        print(f"  message:         {data.get('message')}")
        print(f"  generated_value: {data.get('generated_value')}")
        print(f"  processing_time: {data.get('processing_time_s')} s")
        print(f"  timestamp:       {data.get('timestamp')}")
        print(f"  czas całkowity żądania: {elapsed} s")
    except Exception as e:
        print(f"[APP] Błąd komunikacji z workerem: {e}")

if __name__ == "__main__":
    call_worker()
