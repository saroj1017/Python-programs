fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
    


make_pie(4)











# Tests
import unittest
from unittest.mock import patch
from io import StringIO

class MyTest(unittest.TestCase):

    def test_1(self):
      with patch('sys.stdout', new = StringIO()) as fake_out:
        expected_print = "Fruit pie\n"
        make_pie(4)
        self.assertEqual(fake_out.getvalue(), expected_print) 

    def test_2(self):
      with patch('sys.stdout', new = StringIO()) as fake_out:
        expected_print = "Pear pie\n"
        make_pie(1)
        self.assertEqual(fake_out.getvalue(), expected_print) 

    def test_3(self):
      with patch('sys.stdout', new = StringIO()) as fake_out:
        expected_print = "Orange pie\n"
        make_pie(2)
        self.assertEqual(fake_out.getvalue(), expected_print) 

    def test_4(self):
      with patch('sys.stdout', new = StringIO()) as fake_out:
        expected_print = "Pear pie\n"
        make_pie(-2)
        self.assertEqual(fake_out.getvalue(), expected_print) 

print("\n\n\n\n.\n.\n.")
print('Remember, your code should print "Fruit pie" if the index is out of range.')
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)
