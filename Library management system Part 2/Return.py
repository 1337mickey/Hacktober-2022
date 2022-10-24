import datetime


def lists():
    file = open("Books.txt", "r")
    listBooks = []
    dictionary = {}
    for each in file:
        line = each.replace("\n", "")
        listBooks.append(line.split(","))
        for i in range(1, len(listBooks)+1):
            each = i
            dictionary[each] = listBooks[i-1]
    file.close()
    return dictionary


def return_book():
    listsBooks = lists()
    name = input("Enter the name of the person who borrowed the book: ")
    ID = int(input("Enter the ID of the book you want to return: "))
    dt = datetime.datetime.now()
    t = dt.strftime("%H:%M:%S")
    d = dt.strftime("%d/%m/%Y")
    change_quantity(ID)
    book_list()
    number = int(input("Enter the number of days you borrow the book: "))
    if number > 10:
        number = number - 10
        fine = 2
        fine = number * fine
        price = (listsBooks[ID][3])
        p1 = float(price.strip("$"))
        total = round(fine + p1,2)
        print(str(fine)+ "$ is your fine. ")
        
        print("Total cost of the book is",str(total))
        bill(name, ID, t, d, fine, price, total)
        
    else:
        listsBooks = lists()
        price = (listsBooks[ID][3])
        print("The total price of the book is",str(price))
        bill(name, ID, t, d, fine, price, total)
        
    while(True):
        YesNo = input("Do you want to return more books. 'Y' for Yes and 'N' for No: ")
        if YesNo == "Y" or YesNo == "y":
            ID = int(input("Enter the ID of the book you want to return: "))
            change_quantity(ID)
            book_list()
            number = int(input("Enter the number of days you borrow the book: "))
            if number > 10:
                number = number - 10
                fine = 2
                fine = number * fine
                price = (listsBooks[ID][3])
                p1 = float(price.strip("$"))
                total = round(fine + p1,2)
                print(str(fine)+ "$ is your fine. ")
                
                print("Total cost of the book is ",str(total))
                bill(name, ID, t, d, fine, price, total)
                
            else:
                listsBooks = lists()
                price = (listsBooks[ID][3])
                print("The total price of the book is ",str(price))
                bill(name, ID, t, d, fine, price, total)
        else:
            
            break
            
        
    
    
    





def book_list():
    print("--------------------------------------------------------------------------------------")
    print("Book ID"+"      "+"Book Name"+"          "+" Author" +
          "                      "+"Quantity"+"    "+"Price")
    print("------------------------------------------------------------------------------------")
    listBooks = lists()
    for key, value in listBooks.items():
        print("  ", key, "       ",
              value[0], " ", value[1], "      ", value[2], "      ", value[3])
    print("------------------------------------------------------------------------------------")


def change_quantity(val):
    listBooks = lists()
    quantity = int(listBooks[val][2])+1
    listBooks[val][2] = str(quantity).zfill(2)
    file = open("Books.txt", "w")
    for key, value in listBooks.items():
        file.write(value[0]+","+value[1]+","+value[2]+","+value[3]+"\n")
    file.close()
    print("Books ID: "+str(val) + "has been successfully returned! Please Proceed to cost calculation")

def bill(name, ID, t, d, fine, price, total):
    listBooks = lists()
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    second = str(datetime.datetime.now().second)
    
    with open("Returned_By-"+name+""+year+""+month+""+day+""+second+".txt", "w+") as f:
        f.write("+++++++++++++++++++++++++++++++++++ \n")
        f.write("    Library Management System       \n")

        f.write("\n Book is return by: "+name+"\n")
        f.write("The time of return book is: "+t+"\n")
        f.write("The date of return book is : "+d+"\n")
        f.write("The return book is: "+listBooks[ID][0]+"\n")
        f.write("The fine is: $"+str(fine)+"\n")
        f.write("The price of the book is: "+price+"\n")
        f.write("The total price of the book is: "+str(total)+"\n")
        
        


