
mylist = [1,2,3]

print(len(mylist))#3

class Sample():
    pass


mysample= Sample()
print(mysample)#<__main__.Sample object at 0x000001870B891190>




class Book():

    def __init__(self,title,author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    # this method is for length
    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')

#before str method
b = Book('Python rocks', "Jose", 200)
#print(b)#<__main__.Sample object at 0x000002246DB31950>

#after creating str method in book class, it will print
print(b)#Python rocks by Jose

#after creating len method, we will be able to print pages
print(len(b))#200

#if we want to delete this book from the menory of the book. if the del method is not created in the class it will
#just delete it, but if you create del method there then call this delete function to delete the book
#it will print the line you inserted the del method
del b #A book object has been deleted
print(b)#NameError: name 'b' is not defined   => as we deleted there is no such thing
