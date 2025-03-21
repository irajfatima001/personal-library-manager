
import os
import json

# 📂 File to store book data
FILE_NAME = "library.txt"

# 📚 Library Storage
library = []  

# 📂 Load library data from file (if exists)
def load_library():
    global library
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                library = json.load(file)
            except json.JSONDecodeError:
                library = []
    else:
        library = []

# 💾 Save library data to file
def save_library():
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)

# ➕ Add a Book
def add_book():
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
    library.append(book)
    print(f"📖 Book '{title}' added successfully!\n")
    save_library()  # Save changes

# ❌ Remove a Book
def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"🗑️ Book '{title}' removed successfully!\n")
            save_library()
            return
    print(f"⚠️ Book '{title}' not found!\n")

# 🔍 Search for a Book
def search_book():
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ").strip()
    search_term = input("Enter the title/author: ").strip().lower()
    
    results = [book for book in library if (search_term in book["title"].lower() or search_term in book["author"].lower())]
    
    if results:
        print("\n📚 Matching Books:")
        for idx, book in enumerate(results, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("⚠️ No matching books found!")
    print()

# 📜 Display All Books
def display_books():
    if not library:
        print("📂 Your library is empty!\n")
        return

    print("\n📚 Your Library:")
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    print()

# 📊 Display Statistics
def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("📊 No books in the library yet!\n")
        return
    
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100
    print(f"📊 Total books: {total_books}")
    print(f"📖 Percentage read: {percentage_read:.1f}%\n")

# 📌 Main Menu
def main_menu():
    load_library()  # Load library when program starts
    
    while True:
        print("\n📖 Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("💾 Library saved to file. Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1-6.\n")

# 🚀 Run the program
if __name__ == "__main__":
    main_menu()


