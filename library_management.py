from datetime import date, datetime #import date class from the datetime module

def save_books():
    with open('books_StudentID.txt', 'w') as file:
        for book in books:
            file.write(','.join(book) + '\n')


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")

        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def valid_date(date_text):
    try:
        datetime.strptime(date_text, '%d-%m-%Y')
        return True
        
    except ValueError:
        return False

def get_menu_choice(prompt, min_choice, max_choice):
    while True:
        try:
            choice = int(input(prompt))

            if min_choice <= choice <= max_choice:
                return choice

            print(f"Please enter a number between {min_choice} and {max_choice}.")

        except ValueError:
            print("Invalid input. Please enter a number.")

def display_single_book(book):
    print("ISBN:", book[0])
    print("Author:", book[1])
    print("Title:", book[2])
    print("Publisher:", book[3])
    print("Genre:", book[4])
    print("Year Published:", book[5])
    print("Date Purchased:", book[6])
    print("Status:", book[7])

def checking(isbn, year_published, date_purchased, status):
    current_year = date.today().year #import today's year

    if not (isbn.isdigit() and len(isbn) == 13):
        return False

    if not year_published.isdigit():
        return False

    if int(year_published) > current_year:
        return False

    if not valid_date(date_purchased):
        return False

    if status not in ['read', 'to-read']:
        return False

    # All checks passed
    return True


def add_book_records():

    num_books = get_positive_integer("Enter the number of books you want to add: ")# ask the user for the number of books wanted to be added

    for x in range(num_books):
        print('Book', (x + 1), 'Details:')# print the index of the book
        #ask the user for the necessary information needed about the book that wanted to be added
        isbn = input("Enter the ISBN: ")

        #Check ISBN format
        if not (isbn.isdigit() and len(isbn) == 13):
            print("Invalid ISBN format. ISBN must be a 13-digit number.")
            continue

        #Check whether the ISBN already exists
        duplicate_isbn = False

        for book in books:
            if book[0] == isbn:
                duplicate_isbn = True
                break

        if duplicate_isbn:
            print('A book with this ISBN already exists.')
            continue

        #Ask for the remaining information only if ISBN is valid and unique
        author = input("Enter the author: ")
        title = input("Enter the title: ")
        publisher = input("Enter the publisher: ")
        genre = input("Enter the genre: ")
        year_published = input("Enter year published: ")
        date_purchased = input("Enter date purchased (dd-mm-yyyy): ").strip()
        status = input("Enter status (read/to-read): ").strip().lower()

        if not author or not title or not publisher or not genre:
            print('Author, title, publisher and genre cannot be empty.')
            continue

        #Insert the new book to the file if all the format are correct
        if checking(isbn, year_published, date_purchased, status):
            new_book = [isbn, author, title, publisher, genre, year_published, date_purchased, status]

            books.append(new_book)
            save_books()

            print(f"Book {x + 1} added successfully.")
        else:
            print(f"Invalid data for Book {x + 1}. Book not added.")


def delete_book_record():
    global books

    delete_books = get_positive_integer("Enter the number of books you want to delete: ")

    for number in range(delete_books):
        print(f"\nBook {number + 1}")
        isbn = input("Enter the ISBN of the book to delete: ").strip()

        if not (isbn.isdigit() and len(isbn) == 13):
            print("Invalid ISBN format. ISBN must be a 13-digit number.")
            continue

        book_found = False

        for index in range(len(books)):
            if books[index][0] == isbn:
                del books[index]
                book_found = True
                print("Book deleted successfully.")
                break

        if not book_found:
            print("Book not found.")

    save_books()


def edit_book_record():
    global books

    books_to_edit = get_positive_integer(
        "How many books do you want to edit? "
    )

    for x in range(books_to_edit):
        print(f"\nEditing book {x + 1}")
        print("Edit Book Menu")
        print("1. Edit by ISBN")
        print("2. Edit by Author and Title")

        choice = get_menu_choice(
            "Enter a choice: ",
            1,
            2
        )

        book = None

        # Search using ISBN
        if choice == 1:
            isbn = input("Enter ISBN: ").strip()

            if not (isbn.isdigit() and len(isbn) == 13):
                print("ISBN must contain exactly 13 digits.")
                continue

            for existing_book in books:
                if existing_book[0] == isbn:
                    book = existing_book
                    break

            if book is None:
                print(f"Book with ISBN {isbn} was not found.")
                continue

            print("\nBook found!")
            display_single_book(book)

            field_to_edit = get_menu_choice(
                "\nWhich field do you want to edit?\n"
                "1. Author\n"
                "2. Title\n"
                "3. Publisher\n"
                "4. Genre\n"
                "5. Year Published\n"
                "6. Date Purchased\n"
                "7. Status\n"
                "Enter choice: ",
                1,
                7
            )

            if field_to_edit == 1:
                new_author = input(
                    "Enter new author name: "
                ).strip()

                if not new_author:
                    print("Author name cannot be empty.")
                    continue

                book[1] = new_author
                print("Author updated successfully!")

            elif field_to_edit == 2:
                new_title = input(
                    "Enter new title: "
                ).strip()

                if not new_title:
                    print("Title cannot be empty.")
                    continue

                book[2] = new_title
                print("Title updated successfully!")

            elif field_to_edit == 3:
                new_publisher = input(
                    "Enter new publisher: "
                ).strip()

                if not new_publisher:
                    print("Publisher cannot be empty.")
                    continue

                book[3] = new_publisher
                print("Publisher updated successfully!")

            elif field_to_edit == 4:
                new_genre = input(
                    "Enter new genre: "
                ).strip()

                if not new_genre:
                    print("Genre cannot be empty.")
                    continue

                book[4] = new_genre
                print("Genre updated successfully!")

            elif field_to_edit == 5:
                current_year = date.today().year
                new_year = input(
                    "Enter new published year: "
                ).strip()

                if not new_year.isdigit():
                    print("Published year must contain numbers only.")
                    continue

                if int(new_year) > current_year:
                    print("Published year cannot be in the future.")
                    continue

                book[5] = new_year
                print("Published year updated successfully!")

            elif field_to_edit == 6:
                new_date = input(
                    "Enter new date purchased (dd-mm-yyyy): "
                ).strip()

                if not valid_date(new_date):
                    print("Date purchased is not valid.")
                    continue

                book[6] = new_date
                print("Date purchased updated successfully!")

            elif field_to_edit == 7:
                new_status = input(
                    "Enter new status (read/to-read): "
                ).strip().lower()

                if new_status not in ("read", "to-read"):
                    print("Status must be read or to-read.")
                    continue

                book[7] = new_status
                print("Status updated successfully!")

        # Search using author and title
        elif choice == 2:
            author = input("Enter author name: ").strip()
            title = input("Enter book title: ").strip()

            if not author or not title:
                print("Author and title cannot be empty.")
                continue

            for existing_book in books:
                if (
                    existing_book[1].strip().lower() == author.lower()
                    and existing_book[2].strip().lower() == title.lower()
                ):
                    book = existing_book
                    break

            if book is None:
                print(
                    f'Book with author "{author}" and '
                    f'title "{title}" was not found.'
                )
                continue

            print("\nBook found!")
            display_single_book(book)

            field_to_edit = get_menu_choice(
                "\nWhich field do you want to edit?\n"
                "1. ISBN\n"
                "2. Publisher\n"
                "3. Genre\n"
                "4. Year Published\n"
                "5. Date Purchased\n"
                "6. Status\n"
                "Enter choice: ",
                1,
                6
            )

            if field_to_edit == 1:
                new_isbn = input("Enter new ISBN: ").strip()

                if not (
                    new_isbn.isdigit()
                    and len(new_isbn) == 13
                ):
                    print("New ISBN must contain exactly 13 digits.")
                    continue

                duplicate_isbn = any(
                    existing_book is not book
                    and existing_book[0] == new_isbn
                    for existing_book in books
                )

                if duplicate_isbn:
                    print("Another book already uses this ISBN.")
                    continue

                book[0] = new_isbn
                print("ISBN updated successfully!")

            elif field_to_edit == 2:
                new_publisher = input(
                    "Enter new publisher: "
                ).strip()

                if not new_publisher:
                    print("Publisher cannot be empty.")
                    continue

                book[3] = new_publisher
                print("Publisher updated successfully!")

            elif field_to_edit == 3:
                new_genre = input(
                    "Enter new genre: "
                ).strip()

                if not new_genre:
                    print("Genre cannot be empty.")
                    continue

                book[4] = new_genre
                print("Genre updated successfully!")

            elif field_to_edit == 4:
                current_year = date.today().year
                new_year = input(
                    "Enter new published year: "
                ).strip()

                if not new_year.isdigit():
                    print("Published year must contain numbers only.")
                    continue

                if int(new_year) > current_year:
                    print("Published year cannot be in the future.")
                    continue

                book[5] = new_year
                print("Published year updated successfully!")

            elif field_to_edit == 5:
                new_date = input(
                    "Enter new date purchased (dd-mm-yyyy): "
                ).strip()

                if not valid_date(new_date):
                    print("Date purchased is not valid.")
                    continue

                book[6] = new_date
                print("Date purchased updated successfully!")

            elif field_to_edit == 6:
                new_status = input(
                    "Enter new status (read/to-read): "
                ).strip().lower()

                if new_status not in ("read", "to-read"):
                    print("Status must be read or to-read.")
                    continue

                book[7] = new_status
                print("Status updated successfully!")

        save_books()

    print("\nFinished editing book records.")



def display():

    if not books:
        print("No books to display.")
        return

    headers = ['ISBN', 'Author', 'Title', 'Publisher', 'Genre', 'Year Published', 'Date Purchased', 'Status']

    #finding the maximum width needed for each column
    max_widths = []
    for header in headers:
        max_widths.append(len(header))

    for book in books:
        for i in range(len(headers)):
            max_widths[i] = max(max_widths[i], len(str(book[i])))

    #print headers
    for i in range(len(headers)):
        print(f"{headers[i]:<{max_widths[i]}}", end=" | ")

    total_width = 0
    #print the line that seperates headers from info
    for width in max_widths:
        total_width += width

    print()
    #print the seperator line for formatting
    print('-' * (total_width + 23))


    for book in books:
        for i in range(len(headers)):
            #print every book info individually+
            print(f"{str(book[i]):<{max_widths[i]}}", end=' | ')
        #print to go to next line
        print('')


def search_book_record():

    #ask the user for the necessary information needed for searching the book
    isbn = input("Enter the ISBN: ").strip()

    if not (isbn.isdigit() and len(isbn) == 13):
        print("Invalid ISBN.")
        return

    author = input("Enter author name: ").strip()
    title = input("Enter the title: ").strip()

    book_found = False

    for z in range(len(books)):
        #if the wanted isbn, author, and title matches the one in the file
        if books[z][0].strip() == isbn and books[z][1].strip().lower() == author and books[z][2].strip().lower() == title:
            book_found = True
            #print all the information according to the file
            print(' ISBN: ', books[z][0], '\n', 'Author: ', books[z][1], '\n', 'Title: ', books[z][2], '\n', 'publisher: ', books[z][3], '\n', 'genre: ', books[z][4], '\n', 'year published: ', books[z][5], '\n', 'date purchased: ', books[z][6], '\n', 'status: ', books[z][7], '\n')
            break

    if not book_found:
        #if book is not found on the file, will return book is not found
        print('book is not found')


#all books stored
books = []

try:

    with open("books_StudentID.txt", 'r') as file:
        # Read all lines and store them in books
        lines= file.readlines()

    # Remove newline characters from each line and split into lists
    for line in lines:
        record = [
            field.strip()
            for field in line.strip().split(',')
        ]

        if len(record) == 8:  # Ensure that the record has exactly 8 fields
            books.append(record)
        else:
            print('Warning: An invalid book record was skipped')

except FileNotFoundError:
    print(
        'books_StudentID.txt was not found. '
        'A new file will be created.'
    )





while True:
    # Display the main menu
    print("\nMain Menu:")
    print("1. Add Book Record(s)")
    print("2. Delete Book Record(s)")
    print("3. Update/Edit Book Record(s) ")
    print("4. Display")
    print("5. Search for Books")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")# Ask the user for their choices

    if choice == '1':
        add_book_records() #operate the function add_book_records()
    elif choice == '2':
        delete_book_record() #operate the function delete_book_record()
    elif choice == '3':
        edit_book_record() #operate the function edit_book_record()
    elif choice == '4':
        display() #operate the function display()
    elif choice == '5':
        search_book_record() #operate the function search_book_record()
    elif choice == '6':
        save_books()
        print("Successfully exit the program") # exit the program
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5 or 6.") # will as user again if the entered choice is not 1, 2, 3, 4, 5, or 6


    

