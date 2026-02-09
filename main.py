import tkinter as tk
from tkinter import messagebox, simpledialog

class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee, quantity=1):
        for _ in range(quantity):
            self.items.append(coffee)

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            return "Your order is empty."
        summary = "Order Summary:\n"
        for item in self.items:
            summary += f"- {item.name}: ${item.price:.2f}\n"
        summary += f"Total: ${self.total():.2f}"
        return summary

# Indian Coffee Menu
coffees = [
    Coffee("South Indian Filter Coffee", 2.50),
    Coffee("Mysore Coffee", 3.00),
    Coffee("Chikmagalur Coffee", 3.50),
    Coffee("Coorg Coffee", 4.00),
    Coffee("Karnataka Coffee", 2.75),
]

class CoffeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("India Coffee App")
        self.root.geometry("400x500")
        self.order = Order()

        # Menu Label
        self.menu_label = tk.Label(root, text="Indian Coffee Menu", font=("Arial", 16))
        self.menu_label.pack(pady=10)

        # Menu List
        self.menu_text = tk.Text(root, height=10, width=50)
        self.menu_text.pack()
        self.display_menu()

        # Buttons
        self.add_button = tk.Button(root, text="Add to Order", command=self.add_to_order)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Order", command=self.view_order)
        self.view_button.pack(pady=5)

        self.checkout_button = tk.Button(root, text="Checkout", command=self.checkout)
        self.checkout_button.pack(pady=5)

    def display_menu(self):
        self.menu_text.delete(1.0, tk.END)
        for i, coffee in enumerate(coffees, 1):
            self.menu_text.insert(tk.END, f"{i}. {coffee.name} - ${coffee.price:.2f}\n")

    def add_to_order(self):
        coffee_num = simpledialog.askinteger("Add Coffee", "Enter coffee number:")
        if coffee_num is None:
            return
        coffee_num -= 1
        if 0 <= coffee_num < len(coffees):
            quantity = simpledialog.askinteger("Quantity", "Enter quantity:", minvalue=1)
            if quantity:
                self.order.add_item(coffees[coffee_num], quantity)
                messagebox.showinfo("Added", f"Added {quantity} {coffees[coffee_num].name}(s) to order.")
        else:
            messagebox.showerror("Error", "Invalid coffee number.")

    def view_order(self):
        summary = self.order.show_order()
        messagebox.showinfo("Order", summary)

    def checkout(self):
        summary = self.order.show_order()
        messagebox.showinfo("Checkout", summary + "\nThank you for your order!")
        self.order = Order()  # Reset order

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeApp(root)
    root.mainloop()
