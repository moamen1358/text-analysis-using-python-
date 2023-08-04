from textblob import TextBlob
from tkinter import *
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as my_file:
            text = my_file.read()
            Text_entry.delete(1.0, END) 
            Text_entry.insert(END, text) 

def analyze_sentiment(event=None):
    text = Text_entry.get("1.0", END).strip()  
    if text:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity * 100 
        result_label.config(text=f"Polarity: {sentiment:.2f}")
    else:
        result_label.config(text="Polarity: N/A")

window = Tk()
window.title("Sentiment Analysis")
window.config(padx=20, pady=20, bg="#e6f2ff")  
canvas = Canvas(height=200, width=400, bg="#e6f2ff") 
logo_img = PhotoImage(file="logo.png")
canvas.create_image(200, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2)

Text_label = Label(text="Text:", bg="#e6f2ff") 
Text_label.grid(row=1, column=0, sticky="e")

Text_entry = Text(height=10, width=40)
Text_entry.grid(row=1, column=1, columnspan=2, pady=5, padx=5)
Text_entry.focus()

browse_button = Button(text="Browse", command=browse_file, bg="#cce0ff") 
browse_button.grid(row=3, column=0)

Text_entry.bind("<KeyRelease>", analyze_sentiment)

result_label = Label(text="Polarity: N/A", bg="#e6f2ff") 
result_label.grid(row=2, column=1, columnspan=2, pady=5)

window.mainloop()

