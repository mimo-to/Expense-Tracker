import matplotlib.pyplot as plt
import csv
from datetime import datetime


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open('expenses.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    self.expenses.append({
                        'date': row[0],
                        'category': row[1],
                        'amount': float(row[2])
                    })
        except FileNotFoundError:
            with open('expenses.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Category', 'Amount'])

    def save_expenses(self):
        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount'])
            for expense in self.expenses:
                writer.writerow([expense['date'], expense['category'], expense['amount']])

    def add_expense(self, category, amount):
        date = datetime.now().strftime('%Y-%m-%d')
        self.expenses.append({'date': date, 'category': category, 'amount': amount})
        self.save_expenses()

    def get_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def get_expenses_by_category(self):
        categories = {}
        for expense in self.expenses:
            if expense['category'] not in categories:
                categories[expense['category']] = 0
            categories[expense['category']] += expense['amount']
        return categories

    def display_expenses(self):
        print("\nExpenses:")
        for expense in self.expenses:
            print(f"{expense['date']} | {expense['category']} | rs{expense['amount']:.2f}")

    def generate_pie_chart(self):
        categories = self.get_expenses_by_category()
        labels = categories.keys()
        sizes = categories.values()

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Expense Distribution by Category')
        plt.axis('equal')
        plt.show()


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View total expenses")
        print("3. View expenses by category")
        print("4. View all expenses")
        print("5. View expense chart")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            category = input("Enter category (e.g., Food, Transport, etc.): ")
            amount = float(input("Enter amount: rs"))
            tracker.add_expense(category, amount)

        elif choice == '2':
            print(f"Total expenses: rs{tracker.get_total_expenses():.2f}")

        elif choice == '3':
            expenses_by_category = tracker.get_expenses_by_category()
            print("\nExpenses by Category:")
            for category, total in expenses_by_category.items():
                print(f"{category}: rs{total:.2f}")

        elif choice == '4':
            tracker.display_expenses()

        elif choice == '5':
            tracker.generate_pie_chart()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
