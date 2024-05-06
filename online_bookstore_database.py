class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Book:
    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

class OnlineBookstore:
    def __init__(self):
        self.books = []
        self.users = []
        self.logged_in_user = None

    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_in_user = user
                return True
        return False

    def logout(self):
        self.logged_in_user = None

    def add_book(self, title, author, genre, price, quantity):
        if self.logged_in_user:
            book = Book(title, author, genre, price, quantity)
            self.books.append(book)
            return f"{title} added successfully."
        else:
            return "You need to be logged in as admin to add books."

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def add_review(self, title, review):
        book = self.search_book(title)
        if book:
            book.add_review(review)
            return "Review added successfully."
        else:
            return "Book not found in the store."

    def buy_book(self, title, quantity):
        book = self.search_book(title)
        if book:
            if book.quantity >= quantity:
                book.quantity -= quantity
                return f"Successfully purchased {quantity} copies of {book.title}."
            else:
                return f"Sorry, only {book.quantity} copies of {book.title} are available."
        else:
            return "Book not found in the store."

    def remove_book(self, title):
        if self.logged_in_user:
            book = self.search_book(title)
            if book:
                self.books.remove(book)
                return f"{title} removed successfully."
            else:
                return "Book not found in the store."
        else:
            return "You need to be logged in as admin to remove books."

# Example usage
if __name__ == "__main__":
    bookstore = OnlineBookstore()
    bookstore.register_user("admin", "admin123")
    bookstore.login("admin", "admin123")
    print(bookstore.add_book("Harry Potter", "J.K. Rowling", "Fantasy", 20.99, 50))
    print(bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 15.50, 30))
    print(bookstore.remove_book("The Great Gatsby"))
    print(bookstore.add_review("Harry Potter", "Fantastic book! Highly recommended."))
    print(bookstore.buy_book("Harry Potter", 2))
    bookstore.logout()
