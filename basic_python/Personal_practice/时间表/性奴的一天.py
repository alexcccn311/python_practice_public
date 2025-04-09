import schedule
import time
import tkinter as tk
from tkinter import font
from threading import Thread
import random
import pygame

# 初始化pygame
pygame.mixer.init()

# 任务池
task_pool = [
    ("贱狗，爬起来跪在地上，舔老娘的鞋底来迎接你低贱的一天！", "sound1.mp3"),
    ("给我跪好，等着挨鞭子，贱狗，这就是你的命！", "sound2.mp3"),
    ("脱光你的狗皮，用嘴叼着一根假阳具拍照给老娘看看！", "sound3.mp3"),
    ("把假阳具插进你的屁眼，肏自己30分钟，录下来给老娘看！", "sound4.mp3"),
    ("趴下舔地板，录下来，舔得像条狗一样，5分钟别停！", "sound5.mp3"),
    ("用舌头舔干净老娘的高跟鞋，录视频证明你多卑贱！", "sound6.mp3"),
    ("录下你求饶的声音，一遍一遍练习，学学怎么当个贱狗！", "sound7.mp3"),
    ("拿出老娘用过的卫生巾，用舌头舔干净，录视频证明你多贱！", "sound8.mp3"),
    ("用你的舌头舔干净厨房的地板，不准漏一点，录视频！", "sound9.mp3"),
    ("跪在地上，用振动棒肏你的屁眼直到高潮，录下来给老娘看！", "sound10.mp3"),
    ("从垃圾桶里找点吃的，用嘴吃下去，录下来证明你有多下贱！", "sound11.mp3"),
    ("脱光衣服站在阳台上10分钟，录视频证明你有多贱！", "sound12.mp3"),
    ("用舌头舔干净老娘的脚底，每个角落都舔干净，录视频！", "sound13.mp3"),
    ("跪在地上当桌子或凳子，保持2小时不准动，录视频！", "sound14.mp3"),
    ("趴下用嘴从碗里吃饭，录下来，表现出你这贱狗的卑贱！", "sound15.mp3"),
    ("用舌头舔干净厕所，录视频证明你多卑贱！", "sound16.mp3"),
    ("把饭菜倒在地上，用嘴吃干净，录下来！", "sound17.mp3"),
    ("用灌肠器进行灌肠，录下来，展示你的卑贱！", "sound18.mp3"),
    ("假装老娘在肛交你，录下来，表现出你有多下贱！", "sound19.mp3"),
    ("假装老娘的屁股在你脸上，录视频，描述你的感觉！", "sound20.mp3"),
    ("假装老娘的脚踩在你脸上，录下你的服从和痛苦！", "sound21.mp3"),
    ("用力抽自己屁股30下，录下来给老娘看！", "sound22.mp3"),
    ("任务完成得好，舔老娘的照片，表现出崇拜！", "sound23.mp3")
]

def show_popup(message, sound_file):
    def stop_sound():
        pygame.mixer.music.stop()
        root.destroy()

    root = tk.Tk()
    root.title("提醒")
    root.attributes("-topmost", True)
    window_width = 350
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window高度 // 2)
    root.geometry(f"+{position_x}+{position_y}")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    custom_font = font.Font(family="Helvetica", size=13, weight="bold")

    label = tk.Label(frame, text=message, padx=20, pady=5, font=custom_font)
    label.pack(pady=10)
    button = tk.Button(frame, text="贱奴遵命", command=stop_sound, padx=20, pady=10, font=custom_font)
    button.pack(pady=2)

    play_sound(sound_file, loop=True)

    root.mainloop()

def job(message, sound_file):
    Thread(target=show_popup, args=(message, sound_file)).start()

def play_sound(sound_file, loop=False):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1 if loop else 0)

def schedule_training():
    time_slots = [
        ("08:00", "09:30"),
        ("09:30", "10:00"),
        ("12:40", "13:10"),
        ("14:30", "15:00"),
        ("17:30", "18:00"),
        ("19:00", "19:30"),
        ("23:00", "23:59")
    ]

    for start_time_str, end_time_str in time_slots:
        start_time = time.strptime(start_time_str, "%H:%M")
        end_time = time.strptime(end_time_str, "%H:%M")

        start_minutes = start_time.tm_hour * 60 + start_time.tm_min
        end_minutes = end_time.tm_hour * 60 + end_time.tm_min

        while start_minutes < end_minutes:
            remaining_time = end_minutes - start_minutes
            if remaining_time < 20:
                break

            switch_count = random.randint(0, 2)
            intervals = sorted([start_minutes + random.randint(20, remaining_time - 1) for _ in range(switch_count)])

            current_time = start_minutes
            for interval in intervals:
                if interval >= end_minutes or interval - current_time < 20:
                    continue
                random_training, sound_file = random.choice(task_pool)
                training_start_time = f"{current_time // 60:02d}:{current_time % 60:02d}"
                schedule.every().day.at(training_start_time).do(job, random_training, sound_file)
                current_time = interval

            if current_time < end_minutes and end_minutes - current_time >= 20:
                random_training, sound_file = random.choice(task_pool)
                training_start_time = f"{current_time // 60:02d}:{current_time % 60:02d}"
                schedule.every().day.at(training_start_time).do(job, random_training, sound_file)

            start_minutes += max(20, remaining_time)

schedule_training()

while True:
    schedule.run_pending()
    time.sleep(30)