import time
books_avail=[{'name':'Mahabharata','author':'Maha author'},
             {'name':'Ramayana','author':'Rama author'},
             {'name':'Secret Seven','author':'Enid Blyton'}]

class Library:

    def __init__(self,alistbook,alibname):
        self.listbook=alistbook
        self.libname=alibname

    def disp_book(self):
            disp_in=input("\nWhat do you want to display ? a) Available books b) Books lended to you c) Return File d) Lend File e) Exit ")
            if disp_in == "a":
                print("\nDisplaying Available Books .. ")
                print(books_avail)
            elif disp_in == "b":
                print("\nBooks Lended to you are: ")
                print(self.listbook)
            elif disp_in == "c":
                f=open("Return_Book.txt","rt")
                for line in f:
                    print(line)
            elif disp_in == "d":
                f = open("Lend_Book.txt", "rt")
                for line in f:
                    print(line)
            elif disp_in == "e":
                return None
            else:
                print("Input is incorrect ! Please check your input and try again.")


    def lend_book(self):
        print("Choose among these books...\n")
        print(books_avail)

        try:
            book_name = input("\nEnter name of a book you want to issue or 'e' to Exit : ")
            if book_name != 'e':
                for i in range(len(books_avail)):
                    if books_avail[i]['name'] == book_name:
                        lend_bk=(books_avail[i]).copy()
                        (self.listbook).append(lend_bk)
                        del books_avail[i]
                        f=open("Lend_book.txt","a")
                        f.write(f"{lend_bk} : lended to {self.libname} : {time.ctime()}\n")
                        f.close()
                        print("Book Lended !")
                        break
                else:
                    f2 = open("lend_Book.txt", "rt")
                    for lines in f2:
                        if len(book_name) > 2 and book_name != 'name' and book_name != 'author':
                            result = lines.find(book_name)
                            if result != -1:
                                print(f"\nBook is not available, its lended to {self.libname}")
                                break
                            else:
                                print("Book is not found")
                                break
                        else:
                            print("Check your input !")
                            break
            else:
                return 0
        except Exception as e:
            print("Book is not found")


    def donate_book(self):
        book_nm=input("\nEnter Book name to donate or 'e' to Exit : ")
        if book_nm != 'e':
            book_au=input("Enter Book author name: ")
            books_avail.append({book_nm:book_au})
            print("Thank you")
        else:
            return 0

    def return_book(self):
        book_nm = input("\nEnter Book name to return or 'e' to Exit : ")
        if book_nm != 'e':
            book_au = input("Enter Book author name: ")

            for i in range(len(self.listbook)):
                if self.listbook[i]['name'] == book_nm:
                    return_bk=(self.listbook[i]).copy()
                    books_avail.append({book_nm: book_au})
                    del self.listbook[i]
                    f1=open("Return_Book.txt","a")
                    f1.write(f"{return_bk} : returned by {self.libname} : {time.ctime()}\n")
                    f1.close()
                    break
            print("Thank you for returning")
        else:
            return 0

if __name__ == '__main__':
    print("**** Welcome To Library Management System ****")
    print("\n Hello Prakriti, Your Library name : Prakriti_Lib")
    p_book_names = [{'name': 'maze', 'author': 'maze author'}]
    prakriti = Library(p_book_names, 'Prakriti_Lib')

    while True:
        try:
            choice = int(input("\n * What are you upto ? 1) Display Books 2) Lend Book 3) Return Book 4) Donate Book : 5) Exit : "))
            if choice == 1:
                prakriti.disp_book()
            elif choice == 2:
                prakriti.lend_book()
            elif choice == 3:
                prakriti.return_book()
            elif choice == 4:
                prakriti.donate_book()
            elif choice == 5:
                print("   Bye - Bye")
                exit()
            else:
                print("Input is incorrect ! Please check your input and try again.")
        except Exception as e:
            print("Input is incorrect ! Please check your input and try again.")

