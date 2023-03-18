import tkinter as tk
window=tk.Tk()

window.title('Testing Window')
window.geometry("900x500")

frame = tk.Frame(window)
frame.configure(width=200, height=1000)
frame.pack()

button = tk.Button(frame, text="click me!")
button.pack()
button2 = tk.Button(frame, text="click me!")
button2.pack(padx=50, pady=10)

window.mainloop()
