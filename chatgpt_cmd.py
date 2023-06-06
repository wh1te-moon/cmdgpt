import openai
import csv
import os
import re

openai.api_key = os.environ.get("OPENAI_API_KEY")
chat_history_dir = os.environ.get("CHAT_HISTORY_DIR")


def get_response(chat):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=chat, temperature=0.2  # diy it
    )
    return response["choices"][0]["message"]["content"]


def save_chat(chat):
    chat.append(
        {
            "role": "user",
            "content": "summarize the entire conversation in under 4 words",
        }
    )
    with open(
        f"{chat_history_dir}/{get_response(chat[1:])}csv", mode="w", newline=""
    ) as file:
        writer = csv.DictWriter(file, fieldnames=["role", "content"])
        writer.writeheader()
        for row in chat[1:]:
            writer.writerow(row)


def reinput_line(history):
    target = int(history[-1]["content"][1:])
    if len(history) > 2 * target - 1:
        for i in range(2 * target - 1, len(history)):
            if history[i]["role"] == "user":
                history[i]["content"] = input(
                    "> reinput your " + str(target) + " line:"
                ).strip()
                print()
                break
        else:
            print(f"No user message found for line {target}")
    else:
        print("Input error\n")
    return history


def default_command(history):
    print("Invalid command")
    return inputProcess(input("\n:"),history)


def save_template(history):
    file_name = "./templates/" + input("Enter file name to load the chat history:")
    with open(file_name, "w") as f:
        for message in history:
            f.write(message["role"] + ": " + message["content"] + "\n")
    print("Chat history saved successfully\n")
    return history


def System():
    pass


def load_template(history):
    file_name = input("Enter file name to load the chat history: ")
    try:
        with open("./templates/"+file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() != "":
                    if line[0] == "u":
                        history.append({"role": "user", "content": line[2:].strip()})
                    elif line[0] == "a":
                        history.append({"role": "assistant", "content": line[2:].strip()})
                    else:
                        history.append({"role": "system", "content": line[2:].strip()})
            print("Chat history loaded successfully\n")
    except FileNotFoundError:
        print("File not found\n")
    return inputProcess(input("\n:"),history)


def inputProcess(user_input, history):
    global command_dict
    if user_input[0] == "/" or user_input[0] == ":" or user_input[0]=='\\':
        command = user_input[1:]
        if command in command_dict:
            result = command_dict[command](history)
            if result:
                return result
        else:
            result = command_dict["default"](history)  # 执行默认命令
            if result:
                return result
    else:
        history.append({"role": "user", "content": user_input})
        return history


def INPUT(history):
    print("input:")
    while True:
        line = input()
        if line:
            if line!="END":
                inputProcess(line, history)
            else:
                print("LONG INPUT END")
                break
        else:
            continue
    return history

command_dict = {
    "input":INPUT,
    "i":INPUT,
    "save": save_template,
    "load": load_template,
    "print": lambda history: (print(history), inputProcess(input("\n:"),history)),
    "quit": lambda history: (save_chat(history), exit()),
    "exit": lambda history: (save_chat(history), exit()),
    "q": lambda history: (save_chat(history), exit()),
    "q!": lambda history: exit(),
    "reinput": reinput_line,
    "default": default_command,  # 添加默认命令
}


def main():
    print(f"Welcome to the ChatGPT command line tool!\n")
    history = [{"role": "system", "content": f"You are a helpful assistant."}]
    i = 1
    
    while True:
        user_input = input(str(i) + " > Xhm: ").strip()
        print()
        if user_input:
            history = inputProcess(user_input, history)
        else:
            print("Input your content")
            continue
        rsp_content = get_response(history)
        print(f"> ChatGPT: {rsp_content}\n")
        history.append({"role": "assistant", "content": rsp_content})
        i += 1

if __name__ == "__main__":
    main()