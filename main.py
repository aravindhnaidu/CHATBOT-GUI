import tkinter as tk
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI GPT-3 API key
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

def get_chatbot_response(user_input):
    try:
        # Adjust temperature and max_tokens as needed
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            temperature=0.5,  # Experiment with different values
            max_tokens=100    # Experiment with different values
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def send_message():
    user_input = entry.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.config(state=tk.DISABLED)

    bot_response = get_chatbot_response(user_input)

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Chatbot: " + bot_response + "\n")
    chat_log.config(state=tk.DISABLED)

    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("OpenAI Chatbot")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

chat_log = tk.Text(frame, height=20, width=50, state=tk.DISABLED)
scrollbar = tk.Scrollbar(frame, command=chat_log.yview)
chat_log.config(yscrollcommand=scrollbar.set)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()

