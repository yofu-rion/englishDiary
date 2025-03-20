import pyttsx3

def voice(text):
    # エンジンの初期化
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    # テキストを読み上げる
    engine.say(text)

    # 読み上げを実行
    engine.runAndWait()

if __name__ == "__main__":
    # textに読み上げたいテキストを入力する。
    text = "Hello, this is a test of pyttsx3."
    voice(text)