import pyaudio
import wave
import keyboard

def record_while_key_held(key='space', output_file='output.wav'):
    """
    特定のキー(key)を押している間だけ録音し、
    録音が終了したら wave ファイル(output_file)として保存する。
    """
    chunk = 1024               # 一度に取得する音声バッファサイズ
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 44100               # サンプリングレート（44.1kHz）
    
    p = pyaudio.PyAudio()
    
    # 録音開始前にキーが押されるのを待つ
    print(f"Press and hold '{key}' to start recording...")
    while not keyboard.is_pressed(key):
        pass

    print(f"Recording started. Release '{key}' to stop.")
    
    # 録音用ストリームを開始
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    frames_per_buffer=chunk,
                    input=True)
    
    frames = []
    
    # 指定キーが押されている間だけ録音し続ける
    while keyboard.is_pressed(key):
        data = stream.read(chunk)
        frames.append(data)

    # キーが離されたら録音終了
    print("Recording stopped.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # waveファイルに書き出し
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    print(f"Recording saved to {output_file}")

if __name__ == "__main__":
    # スペースキーが押されている間だけ録音し、output.wav に保存する
    record_while_key_held(key='space', output_file='output.wav')