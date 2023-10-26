import csv
def write(info):
    with open("data.txt","a") as csv_file:
        write=csv.writer(csv_file)
        write.writerow(info)

def read():
    with open("data.txt","r") as csv_file:
        read=csv.reader(csv_file)
        for rows in read:
            print(rows)

            

def main():
    while True:
        print("        WELLCOME ON OUR PLATFORM")
        print("Press 1 for booking tickets")
        print("Press 2 for checking previous records")
        print("Press 3 for exit")
        key=int(input("Enter a number of key : ")) 
        if (key==1):
            name=str(input("Enter your name : "))
            print("Enter lahore for visiting Lahore"),print("Enter karachi for visiting Karachi"),print("Enter quetta for visiting Quetta"),print("Enter peshawar for visiting peshawar")
            city=str(input("Select the city you want to visit from Rawalpindi :"))
            if (city=="lahore"):
              print("You have selected to visit Lahore")
              print("Enter executive class for Executive Class Bogie with price 1500 per person"),print("Enter lower class for Lower A/C Bogie with price 800 per person"),print("Enter economy class for Economy Class Bogie with price 1000 per person")       
              #These prices are without government tax but in total bill government tax will also be included according to a number of tickets.
              bogie_class=str(input("Select the bogie class : "))
              if (bogie_class=="executive class"):
                exec=1500
                print("You have selected an Executive Class Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((exec*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(exec*tickets)+tax
                print("Your total bill is : ",bill)
              elif (bogie_class=="lower class"):
                low=800
                print("You have selected an Lower A/C Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((low*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(low*tickets)+tax
                print("Your total bill is : ",bill)
              elif (bogie_class=="economy class"):
                econ=1000
                print("You have selected an Lower A/C Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((econ*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(econ*tickets)+tax
                print("Your total bill is : ",bill)
              else:
                ("Please select correct option.") 
            elif (city=="karachi"):
              print("You have selected to visit Karachi.")
              print("Enter executive class for Executive Class Bogie with price 8000 per person"),print("Enter lower class for Lower A/C Bogie with price 2000 per person"),print("Enter economy class for Economy Class Bogie with price 3000 per person"),print("Enter first class sleeper for First Class Sleeper bogie with price 4500 per person"),print("Enter economy sleeper for Economy Sleeper Bogie with price 6000 per person")       
              #These prices are without government tax but in total bill government tax will also be included according to number of tickets
              bogie_class=str(input("Select the bogie class : "))
              if (bogie_class=="executive class"):
                exec=8000
                print("You have selected an Executive Class Bogie.")
                tickets=input("Enter number of seats you want : ")
                tax=((exec*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(exec*tickets)+tax
                print("Your total bill is : ",bill)
              elif (bogie_class=="lower class"):
                low=2000
                print("You have selected an Lower A/C Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((low*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(low*tickets)+tax
                print("Your total bill is : ",bill)
              elif (bogie_class=="economy class"):
                econ=3000
                print("You have selected an Lower A/C Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((econ*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(econ*tickets)+tax
                print("Your total bill is : ",bill)
              elif (bogie_class=="first class sleeper"):
                f_class_sleeper=4500
                print("You have selected an First Class Sleeper Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((f_class_sleeper*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(f_class_sleeper*tickets)+tax
                print("Your total bill is : ",bill)
              elif (bogie_class=="economy sleeper"):
                econ_sleeper=6000
                print("You have selected an Economy Sleeper Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((econ_sleeper*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(econ_sleeper*tickets)+tax
                print("Your total bill is : ",bill)  
              else:
                ("Please select correct option.")
            elif (city=="quetta"):
              print("You have selected to visit Quetta.")
              print("Enter first class sleeper for First Class Sleeper bogie with price 2500 per person"),print("Enter economy sleeper for Economy Sleeper Bogie with price 4000 per person")       
              #These prices are without government tax but in total bill government tax will also be included according to number of tickets
              bogie_class=str(input("Select the bogie class : "))
              if (bogie_class=="first class sleeper"):
                f_class_sleeper=2500
                print("You have selected an First Class Sleeper Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((f_class_sleeper*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(f_class_sleeper*tickets)+tax
                print("Your total bill is : ",bill)
              elif (bogie_class=="economy sleeper"):
                econ_sleeper=4000
                print("You have selected an Economy Sleeper Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((econ_sleeper*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(econ_sleeper*tickets)+tax
                print("Your total bill is : ",bill)    
              else:
                ("Please select correct option.")
            elif (city=="peshawar"):
              print("You have selected to visit Peshawar")
              print("Enter executive class for Executive Class Bogie with price 2500 per person"),print("Enter lower class for Lower A/C Bogie with price 1200 per person"),print("Enter economy class for Economy Class Bogie with price 2000 per person")       
              #These prices are without government tax but in total bill government tax will also be included according to a number of tickets.
              bogie_class=str(input("Select the bogie class : "))
              if (bogie_class=="executive class"):
                exec=2500
                print("You have selected an Executive Class Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((exec*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(exec*tickets)+tax
                print("Your total bill is : ",bill)
              elif (bogie_class=="lower class"):
                low=1200
                print("You have selected an Lower A/C Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((low*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(low*tickets)+tax
                print("Your total bill is : ",bill)
              elif (bogie_class=="economy class"):
                econ=2000
                print("You have selected an Lower A/C Bogie.")
                tickets=int(input("Enter number of seats you want : "))
                tax=((econ*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(econ*tickets)+tax
                print("Your total bill is : ",bill)
              else:
                ("Please select correct option.")  
            else:
              ("Please enter the correct city.Thanks")      
            info=[name,city,bogie_class,tickets,bill]
            write(info)
        
        elif (key==2):
            read()
        elif (key==3):
            exit
        else:
            print("Invalid Selection!Please Select The Correct key.Thanks")
    
main()
