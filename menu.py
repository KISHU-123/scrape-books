from app import books
USER_CHOICE = '''ENTER ONE OF THE FOLLOWING
-'b' to look at 5-star books
-'c' to look at the cheapest books
-'n' to look at the next books in the catalogue
-'q' to quit

'''

def print_cheapest_book():
    best_books = sorted(books, key=lambda x: x.price)[:10]
    for book in best_books:
        print(book)


def print_best_books():
    best_ratings = sorted(books, key=lambda x: x.rating*-1)[:10]
    for ratings in best_ratings:
        print(ratings)


books_generator = (x for x in books)


def get_next_book():
    print(next(books_generator))


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'b':
            print_best_books()
        elif user_input == 'n':
            get_next_book()
        elif user_input == 'c':
            print_cheapest_book()
        else:
            print('INVALID')
        user_input = input(USER_CHOICE)

menu()