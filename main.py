import json
import os
from colorama import init, Fore, Style # type: ignore
from tabulate import tabulate # type: ignore
from openpyxl import Workbook  # type: ignore # ✅ For Excel export

# Initialize colorama for colored CLI
init(autoreset=True)

# Script and file locations
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE = os.path.join(SCRIPT_DIR, "todo_list.json")
EXPORT_FILE = os.path.join(SCRIPT_DIR, "exported_tasks.txt")
EXCEL_FILE = os.path.join(SCRIPT_DIR, "tasks.xlsx")

# Load tasks from JSON
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to JSON
def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Export tasks to text file using tabulate
def export_tasks_tabulated(tasks):
    if not tasks:
        print(Fore.RED + "⚠️ No tasks to export.")
        return

    table = []
    for idx, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Not Done"
        table.append([idx, task["title"], status])

    formatted = tabulate(table, headers=["No.", "Task", "Status"], tablefmt="grid")

    with open(EXPORT_FILE, "w", encoding="utf-8") as f:
        f.write(formatted)

    print(Fore.GREEN + f"📁 Tasks exported to:\n{EXPORT_FILE}")

# ✅ Export tasks to Excel file
def export_tasks_excel(tasks):
    if not tasks:
        print(Fore.RED + "⚠️ No tasks to export.")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "To-Do List"

    ws.append(["No.", "Task", "Status"])  # Header row

    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Done"
        ws.append([idx, task["title"], status])

    wb.save(EXCEL_FILE)

    print(Fore.GREEN + f"📊 Tasks exported to Excel:\n{EXCEL_FILE}")

# Print welcome banner
def show_banner():
    print(Fore.CYAN + Style.BRIGHT + "\n🎯 Welcome to Your Beautiful To-Do List App 🎯")
    print(Fore.MAGENTA + "=" * 45)

# Display menu
def show_menu():
    print(Fore.YELLOW + "\n📋 MENU")
    print("1️⃣  View tasks")
    print("2️⃣  Add a task")
    print("3️⃣  ✅ Mark task as complete")
    print("4️⃣  ❌ Delete a task")
    print("5️⃣  💾 Save & Exit")
    print("6️⃣  📤 Export tasks to tabulated .txt")
    print("7️⃣  📊 Export tasks to Excel (.xlsx)")

# Display tasks in tabulated CLI view
def display_tasks(tasks):
    print(Fore.CYAN + "\n🗂️  Your Tasks:")
    if not tasks:
        print(Fore.RED + "⚠️  No tasks in your list.")
        return

    table = []
    for idx, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Not Done"
        table.append([idx, task["title"], status])

    print(Fore.GREEN + tabulate(table, headers=["No.", "Task", "Status"], tablefmt="fancy_grid"))

# Add a new task
def add_task(tasks):
    title = input(Fore.BLUE + "📝 Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print(Fore.GREEN + "✅ Task added!")

# Mark a task as complete
def mark_task_complete(tasks):
    display_tasks(tasks)
    try:
        num = int(input(Fore.BLUE + "📌 Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print(Fore.GREEN + "🎉 Task marked as complete!")
        else:
            print(Fore.RED + "❌ Invalid task number.")
    except ValueError:
        print(Fore.RED + "⚠️ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        num = int(input(Fore.BLUE + "🗑️ Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(Fore.GREEN + f"🗑️ Deleted: {removed['title']}")
        else:
            print(Fore.RED + "❌ Invalid task number.")
    except ValueError:
        print(Fore.RED + "⚠️ Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()
    show_banner()
    while True:
        show_menu()
        choice = input(Fore.YELLOW + "\n👉 Choose an option (1-7): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print(Fore.GREEN + f"\n💾 Tasks saved to {TODO_FILE}\nGoodbye!")
            break
        elif choice == "6":
            export_tasks_tabulated(tasks)
        elif choice == "7":
            export_tasks_excel(tasks)
        else:
            print(Fore.RED + "❗ Invalid option. Choose between 1 and 7.")

if __name__ == "__main__":
    main()
