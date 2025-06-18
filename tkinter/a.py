import tkinter as tk
import sys

class PrintRedirector:
  def __init__(self, widget):
    self.widget = widget

  def write(self, text):
    self.widget.insert(tk.END, text)

root = tk.Tk()
text_widget = tk.Text(root)
text_widget.pack()

    # Redirect standard output
sys.stdout = PrintRedirector(text_widget)

print("This will appear in the text widget.")

root.mainloop()