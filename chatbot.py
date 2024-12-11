import tkinter as tk
from tkinter import Scrollbar, END

# Predefined responses for the chatbot
responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm doing great! How about you?",
    "what is your name": "I'm your friend and i can do something good for you",
    "bye": "Goodbye! Have a great day!",
    "help": "I'm here to assist you with your queries. Just type something!",
    "hi":"Namaste dude",
     "hiii":"Namaste dude",
      "hii":"Namaste dude",
    "Hi":"Bhai namaste ",
    "play music":"Okay check it out",
}

# Function to process user input and generate a response
def get_response():
    user_input = user_entry.get().lower().strip()
    if user_input == "exit":
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(END, "Chatbot: Goodbye! Take care!\n", "bot")
        chat_window.config(state=tk.DISABLED)
        root.destroy()  # Close the application
        return

    # Fetch the response or default message
    response = responses.get(user_input, "I'm sorry, I didn't understand that.")
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(END, f"You: {user_input}\n", "user")
    chat_window.insert(END, f"Chatbot: {response}\n", "bot")
    chat_window.config(state=tk.DISABLED)
    user_entry.delete(0, END)  # Clear the entry field
    chat_window.see(END)  # Auto-scroll to the latest message

# GUI setup
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Header
header = tk.Label(root, text="AI Chatbot", bg="#6200ea", fg="white", font=("Helvetica", 16, "bold"), pady=10)
header.pack(fill=tk.X)

# Chat display frame
frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_window = tk.Text(frame, bd=0, bg="lightyellow", wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED)
chat_window.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

scrollbar = Scrollbar(frame, command=chat_window.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_window['yscrollcommand'] = scrollbar.set

# Tags for styling text
chat_window.tag_configure("user", foreground="#0000FF", font=("Arial", 12, "bold"))
chat_window.tag_configure("bot", foreground="#008000", font=("Arial", 12, "italic"))

# Input frame for user entry
entry_frame = tk.Frame(root, bg="#f0f0f0")
entry_frame.pack(fill=tk.X, padx=10, pady=10)

user_entry = tk.Entry(entry_frame, bg="white", font=("Arial", 14), width=35, relief=tk.SOLID)
user_entry.pack(side=tk.LEFT, padx=5, pady=5)

# Styled Send button
send_button = tk.Button(entry_frame, text="Send", command=get_response, bg="#6200ea", fg="white",
                        font=("Arial", 12, "bold"), width=8, relief=tk.RAISED)
send_button.pack(side=tk.LEFT, padx=5)

# Footer
footer = tk.Label(root, text="Type 'exit' to close the chatbot", bg="#f0f0f0", fg="gray", font=("Arial", 10, "italic"))
footer.pack(pady=10)

# Start the GUI event loop
root.mainloop()
