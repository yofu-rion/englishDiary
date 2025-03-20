import whisper
import pyaudio
import numpy as np
import wave
import keyboard

key='space'

# Whisperモデルをロード
model_medium = whisper.load_model("medium")
custom_prompt = "Rion,Yofu"

# オーディオ設定
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # Whisperの推奨サンプリングレート
CHUNK = 1024  # バッファサイズ

# PyAudioの設定
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

def audio_medium():
    print(f"Press and hold '{key}' to start recording...")
    while not keyboard.is_pressed(key):
        pass
    # 音声を録音
    frames = []
    print("Recording started.")
    while keyboard.is_pressed(key):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Recording stopped.")
    # バイナリデータをnumpy配列に変換
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16).astype(np.float32) / 32768.0

    # 文字起こし
    result = model_medium.transcribe(audio_data, fp16=False,language="en",initial_prompt=custom_prompt)
    return result["text"]

if __name__ == "__main__":
    print(audio_medium())