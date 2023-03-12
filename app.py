import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an expert at absolutely everything."}]


def custom_chat_gpt(user_input):
    messages.append({"role": "user", "content": user_input})
    repsonse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )
    reply = repsonse["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

demo = gradio.Interface(fn=custom_chat_gpt, inputs="text", outputs="text", title="PyChat", theme="dark")
demo.launch()