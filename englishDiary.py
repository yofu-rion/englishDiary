import diaryWhisper
import diaryGPT
import pyttsxVoice

pastConversations = ""

while True:
    try:
        statement = diaryWhisper.audio_medium()
        print("Me：",statement)
        ans = diaryGPT.chat("Past Conversations:"+pastConversations+"\nCurrent Statements:"+statement)
        print("Assistant："+ ans)
        pyttsxVoice.voice(ans)

        pastConversations += "User-"+ statement + "You-" + ans + "\n"

    except KeyboardInterrupt:
        print("会話内容:\n")
        print("\n終了します。")
        break