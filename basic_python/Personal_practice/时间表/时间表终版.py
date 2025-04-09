import requests
import pyaudio
import time
import schedule
from openai import OpenAI
client = OpenAI(
    base_url="https://api.gptsapi.net/v1",
    api_key="sk-bPxb047a5bb6a60addce27af79928dc4be069203924Rfkrf"
)

def text_to_speech(text):
    # 流式传输音频的URL
    stream_url = f'http://127.0.0.1:5000/tts?text={text}&stream=true'

    # 初始化pyaudio
    p = pyaudio.PyAudio()

    # 打开音频流
    stream = p.open(format=p.get_format_from_width(2),
                    channels=1,
                    rate=32000,
                    output=True)

    # 使用requests获取音频流
    response = requests.get(stream_url, stream=True)

    # 读取数据块并播放
    for data in response.iter_content(chunk_size=1024):
        stream.write(data)

    # 停止和关闭流
    stream.stop_stream()
    stream.close()

    # 终止pyaudio
    p.terminate()

