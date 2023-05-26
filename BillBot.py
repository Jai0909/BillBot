import pyautogui
import mysql.connector
from j import *
from k import *
import datetime
now = datetime.datetime.now()
Total_Bill = 0
Binary_Order = 1
Order_Qty_1 = 0
Order_Qty_2 = 0
Order_Qty_3 = 0
Order_Qty_4 = 0
Order_Qty_5 = 0
Order_Qty_6 = 0
Order_Qty_7 = 0
Order_Qty_8 = 0
Order_Qty_9 = 0
Order_Qty_10 = 0
Primary_Action = input("Type 'n' for a new billing. Type 'x' to abort. ")
if Primary_Action == ("n"):  
    while Binary_Order == 1:
        Order_Item = (input("Type in the Menu Item Number : "))
        if now.hour>=8 and now.hour<11:
            demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
            democursor=demodb.cursor( )
            if Order_Item == ("1"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=1")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_1 = abs(int(input("How Many")))
                Total_Bill += e0* Order_Qty_1
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("2"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=2")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_2 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_2
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("3"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=3")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_3 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_3
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("4"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=4")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_4 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_4
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("5"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=5")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_5 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_5
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("6"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=6")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_6 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_6
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("7"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=7")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_7 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_7
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("8"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=8")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_8 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_8
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("9"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=9")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_9 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_9
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("10"):
                democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=10")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_10 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_10
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))         
            else:
                print("Error")
                Binary_Order = abs(int(input("""Do you want to retry your order, Type '1' if yes Type '0' if no""")))
        elif now.hour>=12 and now.hour<16:
            demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
            democursor=demodb.cursor( )
            if Order_Item == ("1"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=1")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_1 = abs(int(input("How Many")))
                Total_Bill += e0* Order_Qty_1
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("2"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=2")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_2 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_2
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("3"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=3")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_3 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_3
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("4"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=4")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_4 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_4
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("5"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=5")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_5 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_5
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("6"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=6")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_6 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_6
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("7"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=7")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_7 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_7
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("8"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=8")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_8 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_8
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("9"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=9")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_9 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_9
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("10"):
                democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=10")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_10 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_10
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))         
            else:
                print("Error")
                Binary_Order = abs(int(input("""Do you want to retry your order, Type '1' if yes Type '0' if no""")))
        elif now.hour>=17 and now.hour<19:
            if Order_Item == ("1"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=1")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_1 = abs(int(input("How Many")))
                Total_Bill += e0* Order_Qty_1
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("2"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=2")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_2 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_2
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("3"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=3")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_3 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_3
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("4"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=4")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_4 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_4
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("5"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=5")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_5 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_5
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("6"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=6")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_6 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_6
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("7"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=7")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_7 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_7
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("8"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=8")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_8 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_8
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("9"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=9")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_9 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_9
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("10"):
                democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=10")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_10 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_10
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))         
            else:
                print("Error")
                Binary_Order = abs(int(input("""Do you want to retry your order, Type '1' if yes Type '0' if no""")))
        elif now.hour>=20 and now.hour<23:
            demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
            democursor=demodb.cursor( )
            if Order_Item == ("1"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=1")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_1 = abs(int(input("How Many")))
                Total_Bill += e0* Order_Qty_1
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("2"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=2")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_2 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_2
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("3"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=3")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_3 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_3
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("4"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=4")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_4 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_4
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("5"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=5")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_5 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_5
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("6"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=6")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_6 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_6
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("7"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=7")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_7 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_7
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("8"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=8")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_8 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_8
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("9"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=9")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_9 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_9
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))
            elif Order_Item == ("10"):
                democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=10")
                for c in democursor:
                    d=c
                e=d[0]
                e0=d[1]
                Order_Qty_10 = abs(int(input("How Many")))
                Total_Bill += e0 * Order_Qty_10
                Binary_Order = abs(int(input("""Do you want to order more, Type '1' if yes Type '0' if no""")))         
            else:
                print("Error")
                Binary_Order = abs(int(input("""Do you want to retry your order, Type '1' if yes Type '0' if no""")))
        Y=150
    Tips = (abs(int(input("Any Tips, Enter Amount. If none Type '0'"))))
    if now.hour>=8 and now.hour<11:
        demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
        democursor=demodb.cursor( )
        if Order_Qty_1 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=1")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_1)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_1 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_2 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=2")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_2)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_2 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
        if Order_Qty_3 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=3")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_3)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_3 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
        if Order_Qty_4 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=4")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_4)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_4 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass   
        if Order_Qty_5 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=5")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_5)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_5 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass 
        if Order_Qty_6 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=6")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_6)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_6 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass   
        if Order_Qty_7 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=7")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_7)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_7 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass     
        if Order_Qty_8 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=8")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_8)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_8 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_9 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=9")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_9)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_9 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_10 > 0:
            democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=10")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_10)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_10 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
    elif now.hour>=12 and now.hour<16:
        demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
        democursor=demodb.cursor( )
        if Order_Qty_1 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=1")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_1)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_1 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_2 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=2")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_2)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_2 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
        if Order_Qty_3 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=3")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_3)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_3 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
        if Order_Qty_4 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=4")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_4)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_4 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass   
        if Order_Qty_5 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=5")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_5)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_5 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass 
        if Order_Qty_6 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=6")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_6)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_6 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass   
        if Order_Qty_7 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=7")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_7)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_7 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass     
        if Order_Qty_8 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=8")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_8)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_8 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_9 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=9")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_9)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_9 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_10 > 0:
            democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=10")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_10)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_10 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
    elif now.hour>=17 and now.hour<19:
        demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
        democursor=demodb.cursor( )
        if Order_Qty_1 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNAKSMENU WHERE SNO=1")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_1)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_1 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_2 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNAKSMENU WHERE SNO=2")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_2)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_2 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
        if Order_Qty_3 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNAKSMENU WHERE SNO=3")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_3)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_3 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
        if Order_Qty_4 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNAKSMENU WHERE SNO=4")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_4)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_4 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass   
        if Order_Qty_5 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNAKSMENU WHERE SNO=5")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_5)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_5 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass 
        if Order_Qty_6 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNAKSMENU WHERE SNO=6")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_6)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_6 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass   
        if Order_Qty_7 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNAKSMENU WHERE SNO=7")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_7)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_7 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass     
        if Order_Qty_8 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNAKSMENU WHERE SNO=8")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_8)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_8 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_9 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=9")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_9)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_9 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_10 > 0:
            democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=10")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_10)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_10 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
    elif now.hour>=20 and now.hour<23:
        demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
        democursor=demodb.cursor( )
        if Order_Qty_1 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=1")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_1)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_1 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_2 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=2")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_2)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_2 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
        if Order_Qty_3 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=3")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_3)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_3 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
        if Order_Qty_4 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=4")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_4)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_4 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass   
        if Order_Qty_5 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=5")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_5)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_5 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass 
        if Order_Qty_6 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=6")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_6)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_6 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass   
        if Order_Qty_7 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=7")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_7)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_7 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass     
        if Order_Qty_8 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=8")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_8)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_8 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_9 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=9")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_9)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_9 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass  
        if Order_Qty_10 > 0:
            democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=10")
            for c in democursor:
                d=c
            e=d[0]
            e0=d[1]
            f=Text(Point(100,Y),e)
            f.setTextColor(color_rgb(0,0,0))
            f.draw(a)
            g=Text(Point(200,Y),Order_Qty_10)
            g.setTextColor(color_rgb(0,0,0))
            g.draw(a)
            h=Text(Point(300,Y),e0)
            h.setTextColor(color_rgb(0,0,0))
            h.draw(a)
            i=Text(Point(400,Y),"Rs."+str(Order_Qty_10 * e0))
            i.setTextColor(color_rgb(0,0,0))
            i.draw(a)
            Y=Y+20
        else:
            pass
    j=Text(Point(400,360),"Rs."+str(Total_Bill))
    j.setTextColor(color_rgb(0,0,0))
    j.draw(a)
    k=Text(Point(400,385),"Rs."+str((Total_Bill * 2.5)/100))
    k.setTextColor(color_rgb(0,0,0))
    k.draw(a)
    m=Text(Point(400,410),"Rs."+str((Total_Bill * 2.5)/100))
    m.setTextColor(color_rgb(0,0,0))
    m.draw(a)
    n=Text(Point(400,435),"Rs."+str(Tips))
    n.setTextColor(color_rgb(0,0,0))
    n.draw(a)
    Total_Bill_1=Total_Bill + ((Total_Bill * 5)/100) + Tips
    o=Text(Point(400,475),"Rs."+str(Total_Bill_1))
    o.setTextColor(color_rgb(0,0,0))
    o.draw(a)
    p=int(input("ENTER BILL NUMBER AS BILL :"))
    q=(str(p)+'.png')
    r=(r'/Users/jai/Desktop/BILLBOT/'+q)
    z=pyautogui.screenshot()
    z.save(r)
elif Primary_Action == ("x"):
    print("Aborted")
else:
    print("Error")
