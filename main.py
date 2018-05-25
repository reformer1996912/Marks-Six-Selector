import tkinter as tk
from tkinter import ttk
from threading import Thread

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Six Marks Selector')
        self.times = 24
        self.directionList = []
        self.target = 0
        self.create_main()

    def kick_left(self):
        self.times -= 1
        self.directionList.append('1')
        self.timeLabel.configure(text=str(self.times))
        if self.times == 0:
            self.start_thread()

    def kick_right(self):
        self.times -= 1
        self.directionList.append('0')
        self.timeLabel.configure(text=str(self.times))
        if self.times == 0:
            self.start_thread()

    def start_thread(self):
        runT = Thread(target=self.second_thread)
        runT.start()

    def second_thread(self):
        self.left.configure(state='disable')
        self.right.configure(state='disable')
        runF = Thread(target=self.combo)
        runF.start()
        
        with open('data.txt', 'r') as f:
            for i, line in enumerate(f):
                if i == self.target:
                    self.timeLabel.configure(text=line.strip('\n'))
                    break
    
    def combo(self, start=1, end=13983816, time= 24):
        if time == 0:
            self.target = start
            return
        direction = self.directionList[24-time]
        if direction == '1':
            return self.combo(start, (end + start)//2, time-1)
        if direction == '0':
            return self.combo((end + start)//2, end, time-1)
    
    def create_main(self):
        self.timeLabel = ttk.Label(self.window, text='Times Left')
        self.timeLabel.grid(row=0, columnspan=2, padx=10, pady= 10)
        self.left = ttk.Button(self.window, text='Left', command=self.kick_left)
        self.left.grid(row=1, column=0, padx=10, pady= 10)
        self.right = ttk.Button(self.window, text='Right', command=self.kick_right)
        self.right.grid(row=1, column=1, padx=10, pady= 10)

app = App()
app.window.mainloop()
