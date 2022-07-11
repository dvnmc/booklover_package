import numpy as np
import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test = BookLover('Devin', 'djm6cz@virginia.edu', 'Historical Fiction')
        book_added = test.add_book('The Odyssey', 4)
        expected = 'This book has been added to your book list!'
        self.assertEqual(book_added, expected)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test = BookLover('Devin', 'djm6cz@virginia.edu', 'Historical Fiction')
        book_added = test.add_book('East of Eden', 5)
        book_added_copy = test.add_book('East of Eden', 5)
        expected = 'This book is already in your book list.'
        self.assertEqual(book_added_copy, expected)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test = BookLover('Devin', 'djm6cz@virginia.edu', 'Historical Fiction')
        book_added = test.add_book('The Odyssey', 4)
        book_read = test.has_read('The Odyssey')
        expected = True
        self.assertEqual(book_read, expected)

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test = BookLover('Devin', 'djm6cz@virginia.edu', 'Historical Fiction')
        book_not_read = test.has_read('The Illiad')
        expected = True
        self.assertFalse(book_not_read, expected)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test = BookLover('Devin', 'djm6cz@virginia.edu', 'Historical Fiction')
        book_added_1 = test.add_book('The Hobbit', 4)
        book_added_2 = test.add_book('Before The Beginning', 3)
        book_added_3 = test.add_book("The Hitchhiker's Guide to the Galaxy", 4)
        num_books = test.num_books_read()
        expected = 3
        self.assertEqual(num_books, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test = BookLover('Devin', 'djm6cz@virginia.edu', 'Historical Fiction')
        book_added_1 = test.add_book('The Poisonwood Bible', 3)
        book_added_2 = test.add_book('The Mind of God', 4)
        
        fav_books = test.fav_books()
        expected = True
        ratings = np.all((fav_books['book_rating'] > 3))
        self.assertEqual(ratings, expected)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
    