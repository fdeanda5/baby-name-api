from repository import BabyNameRepository
from models import BabyNameRecord


def menu():
    print("""
=== Baby Name Database ===
1. Add a new name
2. Search for a name
3. Update a name record
4. Delete a name record
5. Exit
""")


def main():
    repo = BabyNameRepository()

    while True:
        menu()
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Name: ")
                year = int(input("Year: "))
                count = int(input("Count: "))
                repo.insert(BabyNameRecord(name, year, count))
                print("Record added.")

            elif choice == "2":
                name = input("Name to search: ")
                results = repo.find_by_name(name)
                for year, count in results:
                    print(year, count)

            elif choice == "3":
                name = input("Name: ")
                year = int(input("Year: "))
                count = int(input("New count: "))
                repo.update(name, year, count)
                print("Record updated.")

            elif choice == "4":
                name = input("Name: ")
                year = int(input("Year: "))
                repo.delete(name, year)
                print("Record deleted.")

            elif choice == "5":
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
