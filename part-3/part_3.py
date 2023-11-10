my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book2 = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2009,
    "rating": 4.12,
    "pages": 345
}
# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def parser(book):
    _string = f"Author, {book["author"]}, wrote the book {book["title"]}, in the year {book["year"]}. It is {book["pages"]} pages long and has a rating of {book["rating"]}."
    return _string

print(parser(my_book))
# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def title(book):
    ti = book["title"]
    return ti

def year(book):
    ye = book["year"]
    return ye

def author(book):
    au = book["author"]
    return au

def pages(book):
    pa = book["pages"]
    return pa

print(pages(my_book))
# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def compare_rating(book1, book2):
    if book1["rating"] > book2["rating"]:
        return "Book 1 has a higher rating"
    elif book1["rating"] < book2["rating"]:
        return "Book 2 has a higher rating"

print(compare_rating(my_book, my_book2))

def compare_length(book1, book2):
    if book1["pages"] > book2["pages"]:
        return "book 1 is longer"
    elif book1["pages"] < book2["pages"]:
        return "book 2 is longer"
    
def compare_dates(book1, book2):
    if book1["year"] > book2["year"]:
        return "book 1 is newer"
    elif book1["year"] < book2["year"]:
        return "book 2 is newer"
    
print(compare_length(my_book, my_book2))
print(compare_dates(my_book, my_book2))