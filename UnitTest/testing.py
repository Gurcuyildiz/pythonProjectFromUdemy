

#unittest is a built in function, we are importing it to here to use
import unittest
#this is the file we are going to test here
import Cap
#we will inherit the testcase class from unittest
class TestCap(unittest.TestCase):

#this is how we do testing of unit

    def test_one_word(self):# this is test method name
        text = 'python'
        result = Cap.cap_text(text)# call the function we have written in the Cap file
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        test = 'monty python'
        result = Cap.cap_text(test)
        self.assertEqual(result,'Monty Python')


if __name__ == '__main__':
    #we will the unittesthere
    unittest.main()

