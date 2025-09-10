import pyautogui
import time
import sys

def auto_click(interval: float = 0.5, clicks: int = 10):
    """
    Auto clicker sederhana.
    
    Args:
        interval (float): Waktu tunggu antar klik (detik)
        clicks (int): Jumlah klik
    """
    print(f"Mulai auto-click: {clicks} klik, interval {interval}s")
    try:
        for i in range(clicks):
            pyautogui.click()
            print(f"Klik ke-{i+1}")
            time.sleep(interval)
        print("Selesai!")
    except KeyboardInterrupt:
        print("Dihentikan user")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Ambil argumen dari terminal jika ada
    interval = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    clicks = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    auto_click(interval, clicks)
