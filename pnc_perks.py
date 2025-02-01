import tkinter as tk
from tkinter import Label, Canvas, Button

def show_first_page():
    clear_window()
    root.configure(bg="#E6611F")
    
    canvas = Canvas(root, width=800, height=450, bg="#E6611F", highlightthickness=0)
    canvas.pack()
    
    def create_rounded_rectangle(x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1, x2, y1 + radius,
            x2, y2 - radius,
            x2, y2, x2 - radius, y2,
            x1 + radius, y2,
            x1, y2, x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)
    
    create_rounded_rectangle(50, 100, 350, 280, 20, fill="#F6C7A0", outline="")
    canvas.create_text(130, 150, text="My PNC Perks", font=("Arial", 18, "bold"), anchor="w")
    canvas.create_text(130, 180, text="Get rewarded for reaching\nfinancial goals!", font=("Arial", 12), anchor="w")
    
    button = Button(root, text="Get started...", font=("Arial", 12, "bold"), bg="#434A52", fg="white", relief="flat", command=show_second_page)
    canvas.create_window(160, 230, window=button, width=120, height=30)
    
    canvas.create_rectangle(450, 100, 650, 300, fill="#434A52", outline="")
    canvas.create_text(550, 200, text="image of product", font=("Arial", 12, "bold"), fill="white")

def show_second_page():
    clear_window()
    root.configure(bg="white")
    
    question_label = Label(root, text="What's\n your goal?", font=("Arial", 24, "bold"), fg="black", bg="white")
    question_label.place(x=50, y=80)
    
    canvas = Canvas(root, width=400, height=300, bg="white", highlightthickness=0)
    canvas.place(x=200, y=50)
    
    def create_circle_button(canvas, x, y, text):
        canvas.create_oval(x-50, y-50, x+50, y+50, fill="#434A52", outline="")
        canvas.create_text(x, y, text=text, fill="white", font=("Arial", 12, "bold"))
    
    create_circle_button(canvas, 100, 100, "Spend less")
    create_circle_button(canvas, 250, 50, "Learn more")
    
    canvas.create_oval(220, 170, 320, 270, fill="#434A52", outline="")
    canvas.create_text(270, 220, text="Save better", fill="white", font=("Arial", 12, "bold"))
    
    back_button = Button(root, text="Back", font=("Arial", 12, "bold"), bg="#434A52", fg="white", relief="flat", command=show_first_page)
    back_button.place(x=50, y=20)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("PNC Perks")
root.geometry("800x450")
show_first_page()
root.mainloop()
