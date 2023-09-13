import openai
import os
openai.api_key = os.environ.get("OPENAI_API_KEY")
def storyboard(story):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", messages=[{"role": "system", "content": f"You are a helpful assistant."},{"role": "assistant", "content": "将下面这段文字分割为数个画面精密，逻辑连续，描写清楚的画面。"+story}], temperature=0.0  # diy it
    )["choices"][0]["message"]["content"]