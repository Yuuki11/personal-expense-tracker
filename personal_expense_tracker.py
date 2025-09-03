

def main():
    print("=== Personal Expense Tracker ===")
    print("Welcome to your personal expense tracker!")

    expenses = []

    while True:
        print("\n --- Main Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View by category")
        print("4. Show summary")
        print("5. Exit")

        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            amount = float(input("Enter expense amount: "))
            category = str(input("Enter expense category: "))
            description = input("Enter expense description: ")

            expense = {
                "amount": amount,
                "category": category,
                "description": description
            }
            expenses.append(expense)
            print("Expense added successfully!")
            # for expense in expenses:
            #     print(expense)

            # break
        elif choice == 2:
            if len(expenses) == 0:
                print("No expenses recorded yet.")
            else:
                print(f"\n Your expenses ({len(expenses)} total):")
                for i, expense in enumerate(expenses, start=1):
                    print(
                        f"{i}. Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}")

            # break

        elif choice == 4:
            if len(expenses) == 0:
                print("No expenses recorded yet.")
            else:
                total = sum(expense['amount'] for expense in expenses)
                print(f"\n Total expenses: ${total:.2f}")
                print(f"\n number of expenses: {len(expenses)}")
                print(f"\n Average expense: ${total/len(expenses):.2f}")
        elif choice == 3:
            if len(expenses) == 0:
                print("No expenses recorded yet.")
            else:
                categories = list(set(expense['category']
                                  for expense in expenses))
                print(f"\n Available categories: {','.join(categories)}")
                filter_category = input("Enter category to filter by: ")
                filtered = [expense for expense in expenses if expense['category'].lower(
                ) == filter_category.lower()]
                print(filtered)
                if len(filtered) == 0:
                    print(
                        f"No expenses found in category '{filter_category}'.")
                else:
                    print(f"\n {filter_category} expenses")
                    for i, expense in enumerate(filtered, start=1):
                        print(
                            f"{i}. Amount: ${expense['amount']:.2f}, Description: {expense['description']}")

                    total = sum(expense['amount'] for expense in filtered)
                    print(f"\n Total {filter_category} expenses: ${total:.2f}")

        elif choice == 5:
            print("Exiting the Personal Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
