import os
import threading
import time
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import keyboard
import mss
import mss.tools

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitör Seçimli SS Aracı")
        self.save_folder = ""
        self.running = False
        self.selected_monitor_index = 1
        self.monitors = self.detect_monitors()

        # GUI
        tk.Label(root, text="Kaydedilecek Klasör:").pack(pady=5)
        self.folder_label = tk.Label(root, text="Seçilmedi", fg="gray")
        self.folder_label.pack()

        tk.Button(root, text="Klasör Seç", command=self.select_folder).pack(pady=5)

        tk.Label(root, text="Monitör Seç:").pack(pady=5)
        self.monitor_combo = ttk.Combobox(root, values=self.monitors_display_names())
        self.monitor_combo.current(0)
        self.monitor_combo.pack()

        tk.Button(root, text="Başlat", command=self.start).pack(pady=5)
        tk.Button(root, text="Durdur", command=self.stop).pack(pady=5)

        self.status_label = tk.Label(root, text="Durum: Bekleniyor", fg="blue")
        self.status_label.pack(pady=10)

    def detect_monitors(self):
        with mss.mss() as sct:
            return sct.monitors[1:]  # [0] tüm ekranlar, biz [1:] kullanacağız

    def monitors_display_names(self):
        return [f"Monitör {i+1}" for i in range(len(self.monitors))]

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.save_folder = folder
            self.folder_label.config(text=self.save_folder, fg="black")

    def get_next_filename(self):
        i = 1
        while True:
            filename = f"ss_{i:03d}.png"
            filepath = os.path.join(self.save_folder, filename)
            if not os.path.exists(filepath):
                return filepath
            i += 1

    def take_screenshot(self, filepath):
        selected_index = self.monitor_combo.current()
        monitor = self.monitors[selected_index]
        with mss.mss() as sct:
            img = sct.grab(monitor)
            mss.tools.to_png(img.rgb, img.size, output=filepath)

    def listen_keys(self):
        while self.running:
            if keyboard.is_pressed("F9"):
                if self.save_folder:
                    filepath = self.get_next_filename()
                    self.take_screenshot(filepath)
                    self.status_label.config(text=f"Kaydedildi: {filepath}", fg="green")
                    time.sleep(1)
                else:
                    self.status_label.config(text="Klasör seçilmedi!", fg="red")
                    time.sleep(1)
            time.sleep(0.1)

    def start(self):
        if not self.save_folder:
            messagebox.showerror("Hata", "Lütfen klasör seçin.")
            return
        self.running = True
        threading.Thread(target=self.listen_keys, daemon=True).start()
        self.status_label.config(text="Dinleniyor... F9 ile ekran görüntüsü alınabilir.", fg="blue")

    def stop(self):
        self.running = False
        self.status_label.config(text="Durdu.", fg="gray")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
import os
import threading
import time
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import keyboard
import mss
import mss.tools

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitör + Tuş Seçimli SS Aracı")
        self.save_folder = ""
        self.running = False
        self.monitors = self.detect_monitors()
        self.hotkey = "F10"

        # GUI
        tk.Label(root, text="Kaydedilecek Klasör:").pack(pady=5)
        self.folder_label = tk.Label(root, text="Seçilmedi", fg="gray")
        self.folder_label.pack()

        tk.Button(root, text="Klasör Seç", command=self.select_folder).pack(pady=5)

        tk.Label(root, text="Monitör Seç:").pack(pady=5)
        self.monitor_combo = ttk.Combobox(root, values=self.monitor_names())
        self.monitor_combo.current(0)
        self.monitor_combo.pack()

        tk.Label(root, text="Tuş Seç (Ekran Görüntüsü Almak İçin):").pack(pady=5)
        self.hotkey_combo = ttk.Combobox(root, values=self.hotkey_options())
        self.hotkey_combo.set("F10")
        self.hotkey_combo.pack()

        tk.Button(root, text="Başlat", command=self.start).pack(pady=5)
        tk.Button(root, text="Durdur", command=self.stop).pack(pady=5)

        self.status_label = tk.Label(root, text="Durum: Bekleniyor", fg="blue")
        self.status_label.pack(pady=10)

    def detect_monitors(self):
        with mss.mss() as sct:
            return sct.monitors[1:]  # 0 = tüm ekranlar, 1+ = tek tek ekranlar

    def monitor_names(self):
        return [f"Monitör {i+1}" for i in range(len(self.monitors))]

    def hotkey_options(self):
        return ["F9", "F10", "F11", "F12", "print_screen", "insert", "home"]

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.save_folder = folder
            self.folder_label.config(text=self.save_folder, fg="black")

    def get_next_filename(self):
        i = 1
        while True:
            filename = f"ss_{i:03d}.png"
            filepath = os.path.join(self.save_folder, filename)
            if not os.path.exists(filepath):
                return filepath
            i += 1

    def take_screenshot(self, filepath):
        selected_monitor = self.monitor_combo.current()
        monitor = self.monitors[selected_monitor]
        with mss.mss() as sct:
            img = sct.grab(monitor)
            mss.tools.to_png(img.rgb, img.size, output=filepath)

    def listen_keys(self):
        self.hotkey = self.hotkey_combo.get()
        while self.running:
            if keyboard.is_pressed(self.hotkey.lower()):
                if self.save_folder:
                    filepath = self.get_next_filename()
                    self.take_screenshot(filepath)
                    self.status_label.config(text=f"Kaydedildi: {filepath}", fg="green")
                    time.sleep(1)
                else:
                    self.status_label.config(text="Klasör seçilmedi!", fg="red")
                    time.sleep(1)
            time.sleep(0.1)

    def start(self):
        if not self.save_folder:
            messagebox.showerror("Hata", "Lütfen klasör seçin.")
            return
        self.running = True
        threading.Thread(target=self.listen_keys, daemon=True).start()
        self.status_label.config(text=f"{self.hotkey_combo.get()} tuşu dinleniyor...", fg="blue")

    def stop(self):
        self.running = False
        self.status_label.config(text="Durduruldu.", fg="gray")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
