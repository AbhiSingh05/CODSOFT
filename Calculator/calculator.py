import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""

        # Create display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(root, textvariable=self.display_var, font=("Arial", 18))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create number buttons
        numbers = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            "0", ".", "="
        ]
        row = 1
        col = 0
        for number in numbers:
            tk.Button(root, text=number, command=lambda n=number: self.on_button_click(n)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Create operation buttons
        operations = ["+", "-", "*", "/"]
        row = 1
        col = 3
        for operation in operations:
            tk.Button(root, text=operation, command=lambda op=operation: self.on_button_click(op)).grid(row=row, column=col, padx=5, pady=5)
            row += 1

        # Create clear button
        tk.Button(root, text="C", command=self.clear_display).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result
            except:
                self.display_var.set("Error")
                self.expression = ""
        elif button_text == "C":
            self.clear_display()
        else:
            self.expression += button_text
            self.display_var.set(self.expression)

    def clear_display(self):
        self.expression = ""
        self.display_var.set("")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
