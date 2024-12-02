#library management
class Libirary:
    def __init__(self):
        self.book=[]
        
    def add_book(self):
        
        rang=int(input("enter how many book you want to add:"))
        for i in range (rang):
                 title=input("ener book title:")
                 self.book.append(title)
        print("\n added to the library")
    def remove_book(self):
        title=input("enter the book title to return:")
        if title not in self.book:
            self.book.append(title)
            print(f"\n{title} returned successffully")
        else:
            print(f"\n{title} already returned ")
    def borrow_book(self):
        title=input("enter book title to borrow:")
        if title in self.book:
            self.book.remove(title)
            print(f"{title} borrowed successfully")
        else:
            print("book not returnned")
    def display_book(self):

        print(self.book)

def main():
    library=Libirary()
    while True:
        
        print("\n\n\t\t\tLibrary Management\n\n\n")
        print("1.add book")
        print("2.display book")
        print("3.borrow book")
        print("4.Return book")
        print("5.exit")
        choice=int(input("\n\nenter your choice:"))
        if choice==1:
            library.add_book()
        elif choice==2:
            library.display_book()
        elif choice==3:
            library.borrow_book()
        elif choice==4:
            library.remove_book()
        elif choice==5:
            print("exiting...")
            break
        else:
            print("invalid input")
if __name__=="__main__":
    main()
