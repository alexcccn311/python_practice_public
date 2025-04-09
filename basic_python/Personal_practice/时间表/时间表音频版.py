import schedule
import time
import tkinter as tk
from tkinter import font
from threading import Thread
import random
import pygame

pygame.mixer.init()

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
    position_y = (screen_height // 2) - (window_height // 2)
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

def job(message, sound_file, end_sound_file=None):
    Thread(target=show_popup, args=(message, sound_file)).start()
    if end_sound_file:
        schedule.every().day.at(time.strftime("%H:%M", time.localtime(time.time() + 60))).do(play_end_sound, end_sound_file)

def play_sound(sound_file, loop=False):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1 if loop else 0)

def play_end_sound(sound_file):
    play_sound(sound_file)

def schedule_training():
    training_duration_minutes = random.randint(120, 360)  # 修改为生成整数
    print(training_duration_minutes)

    leisure_times = [
        ("08:00", "09:30", "休闲娱乐", "leisure_alarm.mp3"),
        ("09:30", "10:00", "休闲娱乐", "leisure_alarm.mp3"),
        ("12:40", "13:10", "休闲娱乐", "leisure_alarm.mp3"),
        ("14:30", "15:00", "休闲娱乐", "leisure_alarm.mp3"),
        ("17:30", "18:00", "休闲娱乐", "leisure_alarm.mp3"),
        ("19:00", "19:30", "休闲娱乐", "leisure_alarm.mp3"),
        ("23:00", "23:59", "休闲娱乐", "leisure_alarm.mp3")
    ]

    selected_times = []
    total_minutes = 0

    while total_minutes < training_duration_minutes and leisure_times:
        start_time_str, end_time_str, original_activity, original_sound_file = leisure_times.pop(random.randint(0, len(leisure_times) - 1))

        start_time = time.strptime(start_time_str, "%H:%M")
        end_time = time.strptime(end_time_str, "%H:%M")

        start_minutes = start_time.tm_hour * 60 + start_time.tm_min
        end_minutes = end_time.tm_hour * 60 + end_time.tm_min

        duration = end_minutes - start_minutes
        if total_minutes + duration > training_duration_minutes:
            duration = training_duration_minutes - total_minutes

        selected_times.append((start_minutes, start_minutes + duration, original_activity, original_sound_file))
        total_minutes += duration

    training_types = [
        ("贱奴，快爬过来舔我的鸡吧！", r"D:\Python\pythonProject2\个人实践\语音支持\贱奴，快爬过来舔我的鸡吧！.wav"),
        ("贱狗，快趴下翘起屁股，让我肏死你这个贱货。", r"D:\Python\pythonProject2\个人实践\语音支持\贱狗，快趴下翘起屁股，让我肏死你这个贱货。.wav"),
        ("快跪下舔干净我的高跟鞋！你这个下贱的狗奴！", r"D:\Python\pythonProject2\个人实践\语音支持\快跪下舔干净我的高跟鞋！你这个下贱的狗奴！.wav")
    ]

    for start, end, original_activity, original_sound_file in selected_times:
        while start < end:
            remaining_time = end - start
            if remaining_time < 20:
                break

            training_duration = random.randint(20, remaining_time)

            max_switch_count = (remaining_time // 20) - 1
            switch_count = random.randint(0, max(0, min(2, max_switch_count)))

            intervals = sorted([start + random.randint(1, training_duration - 1) for _ in range(switch_count)])

            current_time = start
            for interval in intervals:
                if interval >= end or (interval - current_time) < 20:
                    continue
                random_training, sound_file = random.choice(training_types)
                training_start_time = f"{current_time // 60:02d}:{current_time % 60:02d}"
                schedule.every().day.at(training_start_time).do(job, random_training, sound_file, original_sound_file)
                print(f"Scheduled {random_training} at {training_start_time} for {interval - current_time} minutes")
                current_time = interval

            if current_time < end:
                random_training, sound_file = random.choice(training_types)
                training_start_time = f"{current_time // 60:02d}:{current_time % 60:02d}"
                schedule.every().day.at(training_start_time).do(job, random_training, sound_file, original_sound_file)
                print(f"Scheduled {random_training} at {training_start_time} for {end - current_time} minutes")

            start += training_duration

schedule_training()

schedule.every().day.at("07:30").do(job, "起床和个人准备", r"D:\Python\pythonProject2\个人实践\语音支持\贱狗，睡那么死。.wav")
schedule.every().day.at("08:30").do(job, "点餐（早餐）", "breakfast_alarm.mp3")
schedule.every().day.at("09:10").do(job, "吃早餐", "breakfast_alarm.mp3")
schedule.every().day.at("10:00").do(job, "处理业务", "work_alarm.mp3")
schedule.every().day.at("12:00").do(job, "形体训练", "exercise_alarm.mp3")
schedule.every().day.at("12:30").do(job, "点餐（午餐）", "lunch_alarm.mp3")
schedule.every().day.at("13:10").do(job, "吃午餐", "lunch_alarm.mp3")
schedule.every().day.at("13:30").do(job, "学习", "study_alarm.mp3")
schedule.every().day.at("15:00").do(job, "处理业务", "work_alarm.mp3")
schedule.every().day.at("17:00").do(job, "体能训练", "exercise_alarm.mp3")
schedule.every().day.at("18:00").do(job, "点餐（晚餐）", "dinner_alarm.mp3")
schedule.every().day.at("18:40").do(job, "吃晚餐", "dinner_alarm.mp3")
schedule.every().day.at("19:30").do(job, "学习", "study_alarm.mp3")
schedule.every().day.at("20:30").do(job, "形体训练", "exercise_alarm.mp3")
schedule.every().day.at("21:00").do(job, "处理业务", "work_alarm.mp3")

while True:
    schedule.run_pending()
    time.sleep(10)