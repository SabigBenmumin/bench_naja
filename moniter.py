import tkinter as tk
import psutil
import os

def update_stats():
    # อัปเดตค่า CPU, หน่วยความจำ, และดิสก์
    cpu_label.config(text=f"CPU Usage: {psutil.cpu_percent()}%")
    memory_label.config(text=f"Memory Usage: {psutil.virtual_memory().percent}%")
    disk_label.config(text=f"Disk Usage: {psutil.disk_usage('/').percent}%")

    # อัปเดตทุก 1000 มิลลิวินาที
    root.after(1000, update_stats)

#สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("System Performance Monitor")

#สร้างและวาง Widgets
cpu_label = tk.Label(root, text="CPU Usage: ", font=("Arial", 14))
cpu_label.pack()
memory_label = tk.Label(root, text="Memory Usage: ", font=("Arial", 14))
memory_label.pack()
disk_label = tk.Label(root, text="Disk Usage: ", font=("Arial", 14))
disk_label.pack()

#เริ่มอัปเดตสถิติ
update_stats()

#เริ่ม main loop
root.mainloop()