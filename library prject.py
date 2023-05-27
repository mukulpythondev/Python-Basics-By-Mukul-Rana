class library:
    def __init__(self):
        self.books=[]
        self.nobooks=0
        
    def addbook(self, book):
        self.books.append(book)
        self.nobooks=len(self.books)      
    def showbooks(self):
        print(f"The library has {self.nobooks} books, The books are ")
        for book in self.books:
            print(book)

l1=library()
l1.addbook("Harry")
l1.addbook("Harry Potter 2")
l1.addbook(" Harry Potter 3")
l1.showbooks()