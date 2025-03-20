from openai import OpenAI
 
def chat(text):
    client = OpenAI(api_key='')
    
    prompt = text
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": 
             """You are an English conversation assistant for Japanese.
                Basically, the conversation is about what user did today.
                You will be asked questions to get general answers and further information about what the user is saying.
                The reason the user is learning English is to get a TOIEC score. Therefore, use words and expressions that are commonly found on TOIEC.
                User Information: Gender - Male, Age - 19 (5th year college of technology student), Name - Rion Yofu, TOIEC: Current score 350, Target score 550, Not good at English
                The employer's statements given are those made now and those made in the past. Responses should be made to the current statement (Past conversations may not be available).
                The user's statements include current statements and past conversations with you. Responses should be made to current statements (past conversations may not exist).
             """
             },
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    text1 = "Hello"
    ans1 = chat("Current Statements:"+text1)
    print(ans1)
    text2 = "We played soccer today."
    print(chat("past conversations:User"+text1+"you:"+ans1+"\nCurrent Statements:"+text2))