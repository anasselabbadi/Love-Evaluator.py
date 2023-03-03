import tkinter as tk
from tkinter import messagebox

class LoveEvaluator:
    def __init__(self, master):
        self.master = master
        master.title("Love Evaluator")

        # Create entry field and button for entering person's name
        self.name_label = tk.Label(master, text="Enter the name of the person you are evaluating:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()
        self.evaluate_button = tk.Button(master, text="Evaluate", command=self.evaluate_love)
        self.evaluate_button.pack()

    def evaluate_love(self):
        # Retrieve name from entry field
        name = self.name_entry.get()

        # Calculate love score based on name length
        love_score = len(name) ** 2 % 101

        # Determine whether or not love score is high enough to indicate love
        if love_score >= 50:
            messagebox.showinfo("Love Evaluator", f"You love {name} ({love_score}%).")
        else:
            messagebox.showinfo("Love Evaluator", f"You don't love {name} ({love_score}%).")

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    evaluator = LoveEvaluator(root)
    evaluator.run()
