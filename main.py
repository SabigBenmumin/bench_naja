import tkinter as tk
import bencher

def update_scoretime(score):
    cpu_label.config(text=f"CPU test: {score[2]:.4f} seconds")
    memory_label.config(text=f"Memory test: {score[0]:.4f} seconds")
    disk_label.config(text=f"Disk test: {score[1]:.4f} seconds")

def benchmark():
    time_usage = bencher.benching() #(mem time, disk time, cpu time)
    update_scoretime(time_usage)

app = tk.Tk()
app.title('bencher naja')

cpu_label = tk.Label(text="CPU test: Null", font=("Arial", 14))
cpu_label.pack()
memory_label = tk.Label(text="Memory test: Null", font=("Arial", 14))
memory_label.pack()
disk_label = tk.Label(text="Disk test: Null", font=("Arial", 14))
disk_label.pack()
button = tk.Button(text = 'Start bench', command = benchmark)
button.pack()

app.mainloop()