### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def create_new_book(text_file):
    title = input("\nWhat is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please type a number? - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = int(input("Please type a number? - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Please type a number? - "))


    with open(text_file, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")
# create_new_book("library.txt")
# tested functions to make sure they work properly
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def view_books_original(book_source):

    print("\nHere are all your books...\n")

    with open(book_source, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

view_books_original("library.txt")
### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def get_books_as_dictionaries(book_source):
    books_list = []
    with open(book_source, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

def get_book_printed(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")

def view_books(book_source):
    print("\nHere are all your books...\n")
    for book in get_books_as_dictionaries(book_source):
        get_book_printed(book)

def average_rating(book_source):
    list = get_books_as_dictionaries(book_source)
    summed = sum([x['rating'] for x in list])
    y = 0
    for x in list:
        y = y + 1
    print(f"\nYour books have an average rating of {summed / y}!\n")

def newest(book_source):
    list = get_books_as_dictionaries(book_source)
    return max(list, key=lambda x: int(x["year"]))

def oldest(book_source):
    list = get_books_as_dictionaries(book_source)
    return min(list, key=lambda x: int(x["year"]))

def main_menu(book_source):

    active = True

    while active:
        choice = input("""
Choose 1 to add a book...
Choose 2 to see all your books...
Choose 3 to see a count of your books...
Choose 4 to see a count of the pages of your books...
Choose 5 to get the average rating of all books...
Choose 6 to get the newest book...
Choose 7 to get the oldest book...
Choose 0 to exit.
Type here: """)

        if choice == "1":
            create_new_book(book_source)
        elif choice == "2":
            view_books(book_source)
        elif choice == "3":
            print(f"\nYou have a total of {len(get_books_as_dictionaries(book_source))} books.\n")
        elif choice == "4":
            print(f"\nYour books have a total of {sum([x['pages'] for x in get_books_as_dictionaries(book_source)])} pages!\n")
        elif choice == "5":
            average_rating(book_source)
        elif choice == "6":
            print("\nHere is your newest book...\n")
            get_book_printed(newest(book_source))
        elif choice == "7":
            print("\nHere is your oldest book...\n")
            get_book_printed(oldest(book_source))
        elif choice == "0":
            print("\nGoodbye")
            active = False
        else:
            print("\nSorry, please type a number for one of the options.\n")

if __name__ == "__main__":
    main_menu("library.txt")