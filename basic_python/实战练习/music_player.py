import fluidsynth
import time
import threading

class MusicPlayer:

    def __init__(self, soundfont, instrument=0):
        self.fs = fluidsynth.Synth()  # 初始化 FluidSynth
        self.fs.start()  # 启动合成器
        self.sfid = self.fs.sfload(soundfont)  # 加载 SoundFont
        self.instrument = instrument  # 记录乐器音色编号

    def play_note(self, midi_note, velocity=100, duration=1):
        self.fs.program_select(0, self.sfid, 0, self.instrument)
        self.fs.noteon(0, midi_note, velocity)
        time.sleep(duration * 0.8)  # 播放时提前结束一点，创建连奏效果
        self.fs.noteoff(0, midi_note)
        time.sleep(duration * 0.2)  # 模拟自然的音符过渡

    def stop(self):
        self.fs.delete()


class Piano(MusicPlayer):
    def __init__(self, soundfont):
        super().__init__(soundfont, instrument=0)  # 钢琴


class Violin(MusicPlayer):
    def __init__(self, soundfont):
        super().__init__(soundfont, instrument=40)  # 小提琴


class Flute(MusicPlayer):
    def __init__(self, soundfont):
        super().__init__(soundfont, instrument=73)  # 长笛


class Bass(MusicPlayer):
    def __init__(self, soundfont):
        super().__init__(soundfont, instrument=32)  # 贝斯


def play_instrument(instrument, notes):
    """在单独线程中演奏乐器的音符序列"""
    for note, duration in notes:
        if note != -1:  # 排除休止符
            instrument.play_note(note, duration=duration)


if __name__ == "__main__":
    NOTE_TO_MIDI = {
        "0": None,  # 休止符
        "1": 60,  # C4
        "2": 62,  # D4
        "3": 64,  # E4
        "4": 65,  # F4
        "5": 67,  # G4
        "6": 69,  # A4
        "7": 71  # B4
    }


    def convert_note(note, octave=0):
        """将简谱音符转换为 MIDI 音符编号"""
        if note == "0":  # 如果是休止符，返回 None
            return -1
        base_midi = NOTE_TO_MIDI.get(note.strip("#b"))  # 去掉升降号部分
        if base_midi is None:
            raise ValueError(f"未找到音符 {note} 的 MIDI 编号")

        # 处理升降号
        if "#" in note:
            base_midi += 1  # 升半音
        elif "b" in note:
            base_midi -= 1  # 降半音

        # 根据八度调整音高
        return base_midi + (octave * 12)


    def convert_score_to_midi(score):
        """将简谱乐谱转换为 MIDI 乐谱"""
        midi_score = []
        for item in score:
            midi_note = convert_note(item["note"], item["octave"])
            duration = item["duration"]
            if midi_note == -1:
                continue
            midi_score.append((midi_note, duration * 0.625))  # 将时值转换为合适的播放时间
        return midi_score


    simple_score = [
        {"note": "0", "octave":  0, "duration": 0.5},
        {"note": "3", "octave": -1, "duration": 0.5},
        {"note": "3", "octave": -1, "duration": 0.5},
        {"note": "3", "octave": -1, "duration": 0.5},
        {"note": "3", "octave": -1, "duration": 0.5},
        {"note": "2", "octave": -1, "duration": 0.5},
        {"note": "2", "octave": -1, "duration": 1.5},
        {"note": "3", "octave": -1, "duration": 0.5},
        {"note": "4", "octave": -1, "duration": 0.5},
        {"note": "5", "octave": -1, "duration": 0.5},
        {"note": "5", "octave": -1, "duration": 0.5},
        {"note": "2", "octave": -1, "duration": 1.5},
        {"note": "0", "octave":  0, "duration": 0.5},
    ]

    # 将简谱转换为 MIDI
    midi_score = {"Piano": convert_score_to_midi(simple_score)}

    soundfont = r"D:\git\gitstorege\data\music\GeneralUser_GS_v2.0.1--doc_r3\GeneralUser-GS\GeneralUser-GS.sf2"

    # 创建乐器对象
    piano = Piano(soundfont)
    violin = Violin(soundfont)
    flute = Flute(soundfont)
    bass = Bass(soundfont)

    # 定义乐谱：每种乐器的音符序列
    score = midi_score

    # 创建线程列表
    threads = []

    # 为每个乐器分配一个线程
    for instrument_name, notes in score.items():
        if instrument_name == "Piano":
            t = threading.Thread(target=play_instrument, args=(piano, notes))
        elif instrument_name == "Violin":
            t = threading.Thread(target=play_instrument, args=(violin, notes))
        elif instrument_name == "Flute":
            t = threading.Thread(target=play_instrument, args=(flute, notes))
        elif instrument_name == "Bass":
            t = threading.Thread(target=play_instrument, args=(bass, notes))
        threads.append(t)

    # 启动所有线程
    for thread in threads:
        thread.start()

    # 等待所有线程结束
    for thread in threads:
        thread.join()

    # 停止所有乐器
    piano.stop()
    violin.stop()
    flute.stop()
    bass.stop()
