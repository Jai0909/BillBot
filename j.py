import mysql.connector
from graphics import *
import datetime
now = datetime.datetime.now()
a=GraphWin("MENU",500,390)
a.setBackground(color_rgb(255,255,255))
I=Text(Point(45,150),"DATE AND TIME:")
I.setTextColor(color_rgb(0,0,0))
I.draw(a)
J=Text(Point(140,150),now.strftime("%d-%m-%Y %H:%M"))
J.setTextColor(color_rgb(0,0,0))
J.draw(a)
b=Text(Point(250,10),"MENU")
b.setTextColor(color_rgb(0,0,0))
b.draw(a)
c=Text(Point(250,30),"BENNO FOODS")
c.setTextColor(color_rgb(0,0,0))
c.draw(a)
d=Text(Point(250,50),"K-220,NAR VIHAR-2,SECTOR-34,")
d.setTextColor(color_rgb(0,0,0))
d.draw(a)
e=Text(Point(250,70),"NOIDA,DISTRICT GATUM BUDH NAGAR,")
e.setTextColor(color_rgb(0,0,0))
e.draw(a)
f=Text(Point(250,90),"UTTAR PRADESH 201301")
f.setTextColor(color_rgb(0,0,0))
f.draw(a)
g=Text(Point(250,110),"PHONE NO.:+91-8368597428")
g.setTextColor(color_rgb(0,0,0))
g.draw(a)
h=Text(Point(250,130),"GST TIN NO.:29ABCDE1234F2Z5")
h.setTextColor(color_rgb(0,0,0))
h.draw(a)
i=Text(Point(50,170),"ITEMS")
i.setTextColor(color_rgb(0,0,0))
i.draw(a)
j=Text(Point(300,170),"RATE")
j.setTextColor(color_rgb(0,0,0))
j.draw(a)
if now.hour>=8 and now.hour<11:
    demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
    democursor=demodb.cursor( )
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=1")
    for k in democursor:
        l=k
    m=k[0]
    m1=k[1]
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=2")
    for n in democursor:
        o=n
    p=o[0]
    p1=o[1]
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=3")
    for q in democursor:
        r=q
    s=r[0]
    s1=r[1]
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=4")
    for t in democursor:
        u=t
    v=u[0]
    v1=u[1]
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=5")
    for w in democursor:
        x=w
    y=x[0]
    y1=x[1]
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=6")
    for z in democursor:
        A=z
    B=A[0]
    B1=A[1]
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=7")
    for C in democursor:
        D=C
    D1=C[0]
    D2=C[1]
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=8")
    for C1 in democursor:
        A1=C1
    D3=A1[0]
    D4=A1[1]
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=9")
    for C2 in democursor:
        A2=C2
    D5=A2[0]
    D6=A2[1]
    democursor.execute("SELECT ITEM,RATE FROM BREAKFASTMENU WHERE SNO=10")
    for C3 in democursor:
        A3=C3
    D7=A3[0]
    D8=A3[1]
    K=Text(Point(70,190),m)
    K.setTextColor(color_rgb(0,0,0))
    K.draw(a)
    K1=Text(Point(70,210),p)
    K1.setTextColor(color_rgb(0,0,0))
    K1.draw(a)
    K2=Text(Point(70,230),s)
    K2.setTextColor(color_rgb(0,0,0))
    K2.draw(a)
    K3=Text(Point(70,250),v)
    K3.setTextColor(color_rgb(0,0,0))
    K3.draw(a)
    K4=Text(Point(70,270),y)
    K4.setTextColor(color_rgb(0,0,0))
    K4.draw(a)
    K5=Text(Point(70,290),B)
    K5.setTextColor(color_rgb(0,0,0))
    K5.draw(a)
    K6=Text(Point(70,310),D1)
    K6.setTextColor(color_rgb(0,0,0))
    K6.draw(a)
    K7=Text(Point(70,330),D3)
    K7.setTextColor(color_rgb(0,0,0))
    K7.draw(a)
    K8=Text(Point(70,350),D5)
    K8.setTextColor(color_rgb(0,0,0))
    K8.draw(a)
    K9=Text(Point(70,370),D7)
    K9.setTextColor(color_rgb(0,0,0))
    K9.draw(a)
    K10=Text(Point(310,190),m1)
    K10.setTextColor(color_rgb(0,0,0))
    K10.draw(a)
    K11=Text(Point(310,210),p1)
    K11.setTextColor(color_rgb(0,0,0))
    K11.draw(a)
    K12=Text(Point(310,230),s1)
    K12.setTextColor(color_rgb(0,0,0))
    K12.draw(a)
    K13=Text(Point(310,250),v1)
    K13.setTextColor(color_rgb(0,0,0))
    K13.draw(a)
    K14=Text(Point(310,270),y1)
    K14.setTextColor(color_rgb(0,0,0))
    K14.draw(a)
    K15=Text(Point(310,290),B1)
    K15.setTextColor(color_rgb(0,0,0))
    K15.draw(a)
    K16=Text(Point(310,310),D2)
    K16.setTextColor(color_rgb(0,0,0))
    K16.draw(a)
    K17=Text(Point(310,330),D4)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
    K17=Text(Point(310,350),D6)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
    K17=Text(Point(310,370),D8)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
elif now.hour>=12 and now.hour<16:
    demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
    democursor=demodb.cursor( )
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=1")
    for k in democursor:
        l=k
    m=k[0]
    m1=k[1]
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=2")
    for n in democursor:
        o=n
    p=o[0]
    p1=o[1]
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=3")
    for q in democursor:
        r=q
    s=r[0]
    s1=r[1]
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=4")
    for t in democursor:
        u=t
    v=u[0]
    v1=u[1]
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=5")
    for w in democursor:
        x=w
    y=x[0]
    y1=x[1]
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=6")
    for z in democursor:
        A=z
    B=A[0]
    B1=A[1]
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=7")
    for C in democursor:
        D=C
    D1=C[0]
    D2=C[1]
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=8")
    for C1 in democursor:
        A1=C1
    D3=A1[0]
    D4=A1[1]
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=9")
    for C2 in democursor:
        A2=C2
    D5=A2[0]
    D6=A2[1]
    democursor.execute("SELECT ITEM,RATE FROM LUNCHMENU WHERE SNO=10")
    for C3 in democursor:
        A3=C3
    D7=A3[0]
    D8=A3[1]
    K=Text(Point(70,190),m)
    K.setTextColor(color_rgb(0,0,0))
    K.draw(a)
    K1=Text(Point(70,210),p)
    K1.setTextColor(color_rgb(0,0,0))
    K1.draw(a)
    K2=Text(Point(70,230),s)
    K2.setTextColor(color_rgb(0,0,0))
    K2.draw(a)
    K3=Text(Point(70,250),v)
    K3.setTextColor(color_rgb(0,0,0))
    K3.draw(a)
    K4=Text(Point(70,270),y)
    K4.setTextColor(color_rgb(0,0,0))
    K4.draw(a)
    K5=Text(Point(70,290),B)
    K5.setTextColor(color_rgb(0,0,0))
    K5.draw(a)
    K6=Text(Point(70,310),D1)
    K6.setTextColor(color_rgb(0,0,0))
    K6.draw(a)
    K7=Text(Point(70,330),D3)
    K7.setTextColor(color_rgb(0,0,0))
    K7.draw(a)
    K8=Text(Point(70,350),D5)
    K8.setTextColor(color_rgb(0,0,0))
    K8.draw(a)
    K9=Text(Point(70,370),D7)
    K9.setTextColor(color_rgb(0,0,0))
    K9.draw(a)
    K10=Text(Point(310,190),m1)
    K10.setTextColor(color_rgb(0,0,0))
    K10.draw(a)
    K11=Text(Point(310,210),p1)
    K11.setTextColor(color_rgb(0,0,0))
    K11.draw(a)
    K12=Text(Point(310,230),s1)
    K12.setTextColor(color_rgb(0,0,0))
    K12.draw(a)
    K13=Text(Point(310,250),v1)
    K13.setTextColor(color_rgb(0,0,0))
    K13.draw(a)
    K14=Text(Point(310,270),y1)
    K14.setTextColor(color_rgb(0,0,0))
    K14.draw(a)
    K15=Text(Point(310,290),B1)
    K15.setTextColor(color_rgb(0,0,0))
    K15.draw(a)
    K16=Text(Point(310,310),D2)
    K16.setTextColor(color_rgb(0,0,0))
    K16.draw(a)
    K17=Text(Point(310,330),D4)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
    K17=Text(Point(310,350),D6)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
    K17=Text(Point(310,370),D8)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
elif now.hour>=17 and now.hour<19:
    demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
    democursor=demodb.cursor( )
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=1")
    for k in democursor:
        l=k
    m=k[0]
    m1=k[1]
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=2")
    for n in democursor:
        o=n
    p=o[0]
    p1=o[1]
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=3")
    for q in democursor:
        r=q
    s=r[0]
    s1=r[1]
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=4")
    for t in democursor:
        u=t
    v=u[0]
    v1=u[1]
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=5")
    for w in democursor:
        x=w
    y=x[0]
    y1=x[1]
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=6")
    for z in democursor:
        A=z
    B=A[0]
    B1=A[1]
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=7")
    for C in democursor:
        D=C
    D1=C[0]
    D2=C[1]
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=8")
    for C1 in democursor:
        A1=C1
    D3=A1[0]
    D4=A1[1]
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=9")
    for C2 in democursor:
        A2=C2
    D5=A2[0]
    D6=A2[1]
    democursor.execute("SELECT ITEM,RATE FROM SNACKSMENU WHERE SNO=10")
    for C3 in democursor:
        A3=C3
    D7=A3[0]
    D8=A3[1]
    K=Text(Point(70,190),m)
    K.setTextColor(color_rgb(0,0,0))
    K.draw(a)
    K1=Text(Point(70,210),p)
    K1.setTextColor(color_rgb(0,0,0))
    K1.draw(a)
    K2=Text(Point(70,230),s)
    K2.setTextColor(color_rgb(0,0,0))
    K2.draw(a)
    K3=Text(Point(70,250),v)
    K3.setTextColor(color_rgb(0,0,0))
    K3.draw(a)
    K4=Text(Point(70,270),y)
    K4.setTextColor(color_rgb(0,0,0))
    K4.draw(a)
    K5=Text(Point(70,290),B)
    K5.setTextColor(color_rgb(0,0,0))
    K5.draw(a)
    K6=Text(Point(70,310),D1)
    K6.setTextColor(color_rgb(0,0,0))
    K6.draw(a)
    K7=Text(Point(70,330),D3)
    K7.setTextColor(color_rgb(0,0,0))
    K7.draw(a)
    K8=Text(Point(70,350),D5)
    K8.setTextColor(color_rgb(0,0,0))
    K8.draw(a)
    K9=Text(Point(70,370),D7)
    K9.setTextColor(color_rgb(0,0,0))
    K9.draw(a)
    K10=Text(Point(310,190),m1)
    K10.setTextColor(color_rgb(0,0,0))
    K10.draw(a)
    K11=Text(Point(310,210),p1)
    K11.setTextColor(color_rgb(0,0,0))
    K11.draw(a)
    K12=Text(Point(310,230),s1)
    K12.setTextColor(color_rgb(0,0,0))
    K12.draw(a)
    K13=Text(Point(310,250),v1)
    K13.setTextColor(color_rgb(0,0,0))
    K13.draw(a)
    K14=Text(Point(310,270),y1)
    K14.setTextColor(color_rgb(0,0,0))
    K14.draw(a)
    K15=Text(Point(310,290),B1)
    K15.setTextColor(color_rgb(0,0,0))
    K15.draw(a)
    K16=Text(Point(310,310),D2)
    K16.setTextColor(color_rgb(0,0,0))
    K16.draw(a)
    K17=Text(Point(310,330),D4)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
    K17=Text(Point(310,350),D6)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
    K17=Text(Point(310,370),D8)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
elif now.hour>=20 and now.hour<23:
    demodb = mysql.connector.connect(host="localhost", user="root",passwd="shreya2408", database="BILLBOT")
    democursor=demodb.cursor( )
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=1")
    for k in democursor:
        l=k
    m=k[0]
    m1=k[1]
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=2")
    for n in democursor:
        o=n
    p=o[0]
    p1=o[1]
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=3")
    for q in democursor:
        r=q
    s=r[0]
    s1=r[1]
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=4")
    for t in democursor:
        u=t
    v=u[0]
    v1=u[1]
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=5")
    for w in democursor:
        x=w
    y=x[0]
    y1=x[1]
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=6")
    for z in democursor:
        A=z
    B=A[0]
    B1=A[1]
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=7")
    for C in democursor:
        D=C
    D1=C[0]
    D2=C[1]
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=8")
    for C1 in democursor:
        A1=C1
    D3=A1[0]
    D4=A1[1]
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=9")
    for C2 in democursor:
        A2=C2
    D5=A2[0]
    D6=A2[1]
    democursor.execute("SELECT ITEM,RATE FROM DINNERMENU WHERE SNO=10")
    for C3 in democursor:
        A3=C3
    D7=A3[0]
    D8=A3[1]
    K=Text(Point(70,190),m)
    K.setTextColor(color_rgb(0,0,0))
    K.draw(a)
    K1=Text(Point(70,210),p)
    K1.setTextColor(color_rgb(0,0,0))
    K1.draw(a)
    K2=Text(Point(70,230),s)
    K2.setTextColor(color_rgb(0,0,0))
    K2.draw(a)
    K3=Text(Point(70,250),v)
    K3.setTextColor(color_rgb(0,0,0))
    K3.draw(a)
    K4=Text(Point(70,270),y)
    K4.setTextColor(color_rgb(0,0,0))
    K4.draw(a)
    K5=Text(Point(80,290),B)
    K5.setTextColor(color_rgb(0,0,0))
    K5.draw(a)
    K6=Text(Point(90,310),D1)
    K6.setTextColor(color_rgb(0,0,0))
    K6.draw(a)
    K7=Text(Point(70,330),D3)
    K7.setTextColor(color_rgb(0,0,0))
    K7.draw(a)
    K8=Text(Point(70,350),D5)
    K8.setTextColor(color_rgb(0,0,0))
    K8.draw(a)
    K9=Text(Point(70,370),D7)
    K9.setTextColor(color_rgb(0,0,0))
    K9.draw(a)
    K10=Text(Point(310,190),m1)
    K10.setTextColor(color_rgb(0,0,0))
    K10.draw(a)
    K11=Text(Point(310,210),p1)
    K11.setTextColor(color_rgb(0,0,0))
    K11.draw(a)
    K12=Text(Point(310,230),s1)
    K12.setTextColor(color_rgb(0,0,0))
    K12.draw(a)
    K13=Text(Point(310,250),v1)
    K13.setTextColor(color_rgb(0,0,0))
    K13.draw(a)
    K14=Text(Point(310,270),y1)
    K14.setTextColor(color_rgb(0,0,0))
    K14.draw(a)
    K15=Text(Point(310,290),B1)
    K15.setTextColor(color_rgb(0,0,0))
    K15.draw(a)
    K16=Text(Point(310,310),D2)
    K16.setTextColor(color_rgb(0,0,0))
    K16.draw(a)
    K17=Text(Point(310,330),D4)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
    K17=Text(Point(310,350),D6)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
    K17=Text(Point(310,370),D8)
    K17.setTextColor(color_rgb(0,0,0))
    K17.draw(a)
E=Line(Point(270,160),Point(270,380))
E.setOutline(color_rgb(0,0,0))
E.draw(a)
F=Line(Point(0,180),Point(500,180))
F.setOutline(color_rgb(0,0,0))
F.draw(a)
G=Line(Point(0,160),Point(500,160))
G.setOutline(color_rgb(0,0,0))
G.draw(a)
H=Line(Point(0,380),Point(500,380))
H.setOutline(color_rgb(0,0,0))
H.draw(a)
