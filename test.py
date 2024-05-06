import unittest
from online_bookstore_database import OnlineBookstore

class TestOnlineBookstore(unittest.TestCase):
    def setUp(self):
        self.bookstore = OnlineBookstore()
        self.bookstore.register_user("admin", "admin123")
        self.bookstore.login("admin", "admin123")
        self.bookstore.add_book("Harry Potter", "J.K. Rowling", "Fantasy", 20.99, 50)
        self.bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 15.50, 30)

    def test_buy_book_available(self):
        result = self.bookstore.buy_book("Harry Potter", 2)
        self.assertEqual(result, "Successfully purchased 2 copies of Harry Potter.")

    def test_buy_book_not_available(self):
        result = self.bookstore.buy_book("The Great Gatsby", 40)
        self.assertEqual(result, "Sorry, only 30 copies of The Great Gatsby are available.")

    def test_buy_book_not_found(self):
        result = self.bookstore.buy_book("Lord of the Rings", 1)
        self.assertEqual(result, "Book not found in the store.")

    def test_add_review(self):
        result = self.bookstore.add_review("Harry Potter", "Fantastic book! Highly recommended.")
        self.assertEqual(result, "Review added successfully.")

    def test_add_book_admin(self):
        result = self.bookstore.add_book("The Catcher in the Rye", "J.D. Salinger", "Fiction", 18.99, 20)
        self.assertEqual(result, "The Catcher in the Rye added successfully.")

    def test_remove_book_admin(self):
        result = self.bookstore.remove_book("The Great Gatsby")
        self.assertEqual(result, "The Great Gatsby removed successfully.")

    def test_add_book_user(self):
        self.bookstore.logout()
        self.bookstore.register_user("user", "password")
        self.bookstore.login("user", "password")
        result = self.bookstore.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction", 16.99, 25)
        self.assertEqual(result, "To Kill a Mockingbird added successfully.")

    
if __name__ == "__main__":
    unittest.main()
