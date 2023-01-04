import tkinter as tk

window = tk.Tk()
window.title("Year fav")

label = tk.Label(text="¿Cuál es tu year fav?")
label.pack()


entry = tk.Entry()
entry.pack()


def send_answer():
    answer = entry.get()
    print("Tu year favorito es:", answer)

button = tk.Button(text="Enter", command=send_answer)
button.pack()

window.mainloop()
