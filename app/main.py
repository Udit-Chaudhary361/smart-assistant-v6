from database import Database
from tools.joke_tool import get_joke


db = Database()
while True:
    print("\n=== Smart Assistant ===\n")
    print("1. Set Name")
    print("2. View Name")
    print()
    print("3. Add Note")
    print("4. View Notes")
    print("5. Delete Note")
    print()
    print("6. Add Task")
    print("7. Complete Task")
    print("8. Delete Task")
    print("9. View Tasks")
    print()
    print("10. Get Joke")
    print()
    print("11. View History")
    print()
    print("12. See Task Stats")
    print()
    print("13. Exit\n")

    try:
        choose = int(input("Choose - "))
        
        if choose == 1:
            user = input("Enter Name : ").strip()

            if not user:
                print("Name cannot be empty!")
            else:
                db.set_name(user)
                print("Name Updated Successfully!!")

        elif choose ==2:
            print(f"Name - {db.get_name()}")

        elif choose == 3:
            note = input("Enter Note : ").strip()

            if not note:
                print("Note cannot be empty!")
            else:
                db.add_note(note)
                print("Note Added Successfully!!")

        elif choose ==4:
            print("Notes :")
            print(f"{db.get_notes()}")

        elif choose == 5:
            try:
                note_num = int(input("Enter Note Number To Delete : "))
                if db.delete_note(note_num):
                    print("Note Deleted Successfully!!")
                else:
                    print("Note Id Not Found")
            except ValueError:
                print("Enter Only Numeric Value")

        elif choose ==6:
            try:
                task = input("Enter Task : ").strip()

                if not task:
                    print("Task cannot be empty!")
                else:
                    db.add_task(task)
                    print("Task Added Successfully!!")
            except ValueError:
                print("Enter Only Numeric Value")

        elif choose ==7:
            try:
                task = int(input("Enter Task Number : "))
                if db.complete_task(task):
                    print("Task Marked Completed!")
                else:
                        print("Task Id Not Found")
            except ValueError:
                print("Enter Only Numeric Value")

        elif choose == 8:
            try:
                task_num = int(input("Enter Task Number To Delete : "))
                if db.delete_task(task_num):
                    print("Task Deleted Successfully!")
                else:
                    print("Task ID Not Found!")
            except ValueError:
                print("Enter Only Numeric Value")

        elif choose == 9:
            print("-----Tasks-----")
            print(f"{db.get_tasks()}")

        elif choose == 10:
            print(get_joke())

        elif choose == 11:
            print(db.history_viewer())

        elif choose == 12:
            print(db.get_task_stats())
        elif choose == 13:
            db.close()
            print("GoodBye!")
            break
        else:
            print("Invalid Choice")
        
        print()
        input("Press Enter To Continue...")

    except ValueError:
        print()
        print("Enter Only Numeric Value")
        print()
        input("Press Enter To Continue...")