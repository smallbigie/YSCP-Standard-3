def collect_book_data():
    bookstore = {} # the primary dictionary named bookstore
    while True:
        genre = input("Enter a book genre (or type 'done' to finish): ").strip()
        if genre.lower() == 'done':
            break

        if genre not in bookstore:
            bookstore[genre] = {} # the secondary dictionary name genre

        while True:
            book_title = input(f"Enter a book title for genre '{genre}' (or type 'done' to finish): ").strip()
            if book_title.lower() == 'done':
                break

            price = float(input(f"Enter the price for the book '{book_title}': "))
            bookstore[genre][book_title] = price

    return bookstore

def display_bookstore(bookstore):
    print("\nBookstore Inventory:")
    for genre, books in bookstore.items():
        print(f"Genre: {genre}")
        for book, price in books.items():
            print(f"  - {book}: ${price:.2f}")

    print("\nHere is the bookstore dictionary: \n", bookstore)
    print("\nHere is the genre dictionary: \n", bookstore[genre])

# Collect book data from user
bookstore_inventory = collect_book_data()

# Display the collected book data
display_bookstore(bookstore_inventory)
