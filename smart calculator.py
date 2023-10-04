from tkinter import *
from tkinter import messagebox
def add(a,b,text):
    if("even" in text or "Even" in text):
        h=evensum(a,b,text)
        return h
    elif("odd" in text or "Odd" in text):
        h=oddsum(a,b,text)
        return h
    else:
        return a + b
def sub(a,b,text):
    return a - b
def mul(a,b,text):
    return a * b
def div(a,b,text):
    return a / b
def mod(a,b,text):
    return a % b
def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1
def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1
def cube(a,b):
    if(b==0):
        rahul=[]
        b=3
        f=a*a*a
        rahul.append(a)
        rahul.append("=")
        rahul.append(f)
        list.delete(0,END)
        list.insert(END,rahul)
    else:
        rahul=[]
        while(a<=b):
            f=a*a*a
            rahul.append(a)
            rahul.append("=")
            rahul.append(f)
            rahul.append(",")
            a=a+1
        list.delete(0,END)
        list.insert(END,rahul)
def evensum(a,b,text):
    rahul=[]
    if("between" in text or "b/w" in text):
        a=a+1
        while(a<b):
            if(a%2==0):
                rahul.append(a)
            a=a+1
        s=sum(rahul)
        return s
    else:
        while(a<=b):
            if(a%2==0):
                rahul.append(a)
            a=a+1
        s=sum(rahul)
        return s
def oddsum(a,b,text):
    rahul=[]
    if("between" in text or "b/w" in text):
        a=a+1
        while(a<b):
            if(a%2!=0):
                rahul.append(a)
            a=a+1
        s=sum(rahul)
        return s
    else:
        while(a<=b):
            if(a%2!=0):
                rahul.append(a)
            a=a+1
        s=sum(rahul)
        return s
def square(a,b):
    if(b==0):
        rahul=[]
        b=2
        f=a*a
        rahul.append(a)
        rahul.append("=")
        rahul.append(f)
        list.delete(0,END)
        list.insert(END,rahul)
    else:
        rahul=[]
        while(a<=b):
            f=a*a
            rahul.append(a)
            rahul.append("=")
            rahul.append(f)
            rahul.append(",")
            a=a+1
        list.delete(0,END)
        list.insert(END,rahul)
def root(a,text):
    import math
    rahul=[]
    shanu=[]
    if("between" in text or "b/w" in text or "Between" in text):
        q=a[0]+1
        i=q
        w=a[1]
        d=w
        rohit=[]
        sona=[]
        while(q<w):
            e=math.sqrt(q)
            rohit.append(e)
            q=q+1
        v=0
        while(i<d):
            sona.append(i)
            sona.append("=")
            sona.append(rohit[v])
            sona.append(",")
            v=v+1
            i=i+1
        list.delete(0,END)
        list.insert(END,sona)
    elif("and" in text):
        for i in range(len(a)):
            e=math.sqrt(a[i])
            rahul.append(e)
        for j in range(len(a)):
            shanu.append(a[j])
            shanu.append("=")
            shanu.append(rahul[j])
            shanu.append(",")
        list.delete(0,END)
        list.insert(END,shanu)
    elif("from" in text or "to" in text):
        q=a[0]
        i=q
        w=a[1]
        d=w
        rohit=[]
        sona=[]
        while(q<=w):
            e=math.sqrt(q)
            rohit.append(e)
            q=q+1
        v=0
        while(i<=d):
            sona.append(i)
            sona.append("=")
            sona.append(rohit[v])
            sona.append(",")
            v=v+1
            i=i+1
        list.delete(0,END)
        list.insert(END,sona)
    else:
        for i in range(len(a)):
            e=math.sqrt(a[i])
            rahul.append(e)
        for j in range(len(a)):
            shanu.append(a[j])
            shanu.append("=")
            shanu.append(rahul[j])
            shanu.append(",")
        list.delete(0,END)
        list.insert(END,shanu)
def perfect(a,b,text):
    if(b==0):
        s=0
        j=a
        i=1
        while(a>1):
            if(j%i==0):
                g=i
                s=s+g
                a=a-1
                i=i+1
            else:
                a=a-1
                i=i+1
        if(s==j):
            list.delete(0,END)
            list.insert(END,[str(j) + " " + " is a perfect number"])
        else:
            list.delete(0,END)
            list.insert(END,[str(j) + " " + " is not a perfect number"])
    else:
        k=a
        rahul=[]
        while(k<=b):
            j=k
            i=1
            s=0
            while(j>1):
                if(k%i==0):
                    g=i
                    s=s+g
                    i=i+1
                    j=j-1
                else:
                    j=j-1
                    i=i+1
            if(s==k):
                rahul.append(s)
            else:
                pass
            k=k+1
        if(len(rahul)==0):
            list.delete(0,END)
            list.insert(END," ALL ARE NOT A PERFECT NUMBER ")
        else:
                list.delete(0,END)
                list.insert(END,[str(rahul) + " = " + "PERFECT NUMBER " ])
def factorial(a,b,text):
    if(b==0):
        rahul=[]
        import math
        h=math.factorial(int(a))
        rahul.append(a)
        rahul.append("=")
        rahul.append(h)
        list.delete(0,END)
        list.insert(END,rahul)
    else:
        import math
        rahul=[]
        while(a<=b):
            h=math.factorial(int(a))
            rahul.append(a)
            rahul.append("=")
            rahul.append(h)
            rahul.append(",")
            a=a+1
        list.delete(0,END)
        list.insert(END,rahul)
def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l
def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                if(operations[word.upper()]==cube):
                    if(len(l)==1):
                        l.append(0)
                        cube(l[0],l[1])
                        break
                    cube(l[0],l[1])
                    break
                elif(operations[word.upper()]==square):
                    if(len(l)==1):
                        l.append(0)
                        square(l[0],l[1])
                        break
                    square(l[0],l[1])
                    break
                elif(operations[word.upper()]==root):
                    root(l,text)
                    break
                elif(operations[word.upper()]==perfect):
                    if(len(l)==1):
                        l.append(0)
                        perfect(l[0],l[1],text)
                        break
                    perfect(l[0],l[1],text)
                    break
                elif(operations[word.upper()]==factorial):
                    if(len(l)==1):
                        l.append(0)
                        factorial(l[0],l[1],text)
                        break
                    factorial(l[0],l[1],text)
                    break
                elif(operations[word.upper()]==evensum):
                    evensum(l[0],l[1],text)
                    break
                elif(operations[word.upper()]==oddsum):
                    oddsum(l[0],l[1],text)
                    break
                else:
                    r = operations[word.upper()](l[0] , l[1],text)
                    list.delete(0,END)
                    list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong please enter again')
            finally:
                    break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')
operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
'REMANDER':mod , 'MODULUS':mod ,'CUBE':cube ,'SQUARE':square
,'EVEN':evensum ,'ODD':oddsum ,'ROOT':root,'PERFECT':perfect,'FACTORIAL':factorial}
win = Tk()
win.geometry('500x500')
win.title('Smart Calculator')
win.configure(bg='lightskyblue')
l1 = Label(win , text='I am a smart calculator',width=20 , padx=3)
l1.place(x=250,y=10)
l2 = Label(win , text='PROJECT HOLDERS NAME RAHUL KUMAR' , padx=3)
l2.place(x=200,y=40)
l4=Label(win,text="Functions that a smart calculator can perform",padx=3)
l4.place(x=200,y=90)
scroll=Scrollbar(win,bg="lightskyblue")
scroll.pack(side=RIGHT,fill=Y)
lis =Listbox(win,yscrollcommand=scroll.set,xscrollcommand=scroll.set,fg="red",width=30)
lis.insert(END,"ADDITION OF NUMBER")
lis.insert(END,"SUBTRACTION OF NUMBER")
lis.insert(END,"MULTIPLICATION OF NUMBER")
lis.insert(END,"DIVISION OF NUMBER")
lis.insert(END,"MODULUS OF NUMBER")
lis.insert(END,"CUBE OF NUMBER ")
lis.insert(END,"SQUARE OF NUMBER")
lis.insert(END,"FACTORIAL OF NUMBER ")
lis.insert(END,"SUM OF EVEN NUMBER")
lis.insert(END,"SUM OF ODD NUMBER")
lis.insert(END,"ROOT OF NUMBER")
lis.insert(END,"LCM OF A NUMBER")
lis.insert(END,"HCF OF A NUMBER")
lis.place(x=230,y=130)
l3 = Label(win , text='What can i help you' , padx=3)
l3.place(x=250,y=330)
textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin)
e1.place(x=230,y=365)
b1 = Button(win , text='Just this',command=calculate)
b1.place(x=265,y=410)
b2=Button(win,text='Exit',command=win.destroy)
b2.place(x=350,y=410)
list = Listbox(win,width=100,height=12)
list.place(x=50,y=450)
win.mainloop()
