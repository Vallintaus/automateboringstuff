import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        master.title("Stopwatch")

        self.startTime = 0
        self.elapsedTimePaused = 0
        self.running = False

        # Timer display
        self.timer_label = tk.Label(master, text="00:00:00.0", font=("Arial", 30))
        self.timer_label.pack()

        # Start/Pause button
        self.start_button = tk.Button(master, text="Start", command=self.start_pause, width=10)
        self.start_button.pack(side=tk.LEFT)

        # Lap button
        self.lap_button = tk.Button(master, text="Lap", command=self.record_lap, state=tk.DISABLED, width=10)
        self.lap_button.pack(side=tk.LEFT)

        # Stop button (Reset)
        self.stop_button = tk.Button(master, text="Clear", command=self.stop, state=tk.DISABLED, width=10)
        self.stop_button.pack(side=tk.LEFT)

        # Laps listbox
        self.laps_listbox = tk.Listbox(master, width=30, height=5)
        self.laps_listbox.pack()

        self.update_clock()

    def update_clock(self):
        if self.running:
            current_time = time.time()
            elapsed_time = (current_time - self.startTime) + self.elapsedTimePaused
            self.timer_label.config(text="{:.1f}".format(elapsed_time))
        self.master.after(10, self.update_clock)

    def start_pause(self):
        if self.running:
            # Pause the stopwatch
            self.running = False
            self.start_button.config(text="Start")
            self.elapsedTimePaused += time.time() - self.startTime
            self.lap_button.config(state=tk.DISABLED)
        else:
            # Start or resume the stopwatch
            self.running = True
            self.startTime = time.time()
            self.start_button.config(text="Pause")
            self.lap_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)

    def stop(self):
        # Reset the stopwatch
        self.running = False
        self.startTime = 0
        self.elapsedTimePaused = 0
        self.timer_label.config(text="00:00:00.0")
        self.laps_listbox.delete(0, tk.END)
        self.start_button.config(text="Start")
        self.lap_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

    def record_lap(self):
        if self.running:
            current_time = time.time()
            lap_time = (current_time - self.startTime) + self.elapsedTimePaused
            self.laps_listbox.insert(tk.END, "Lap {}: {:.1f}".format(self.laps_listbox.size() + 1, lap_time))

root = tk.Tk()
app = StopwatchApp(root)
root.mainloop()
