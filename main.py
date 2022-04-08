from tkinter import *
from tkinter import filedialog
import pandas as pd
from sklearn.linear_model import LogisticRegression
import tkinter.messagebox as tmsg
root=Tk()
root.geometry('400x640')
root.title('Classifier')
root.wm_iconbitmap('C:\\Users\\TITAS\\Downloads\\Grafikartes-Flat-Retro-Modern-Time-machine.ico')
read_file=0
#A=[]
def import_data():
    global  A
    global read_file
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv (import_file_path)
    print(read_file)
    A=list(read_file.columns)
    print(A)
Button(root, text="Quit",bg='red', command=root.destroy).pack(anchor=NE)
Button(root, text="Import Dataset",bg='green', font='lucida 10 bold',command=import_data,padx=100,pady=10).place(x=67,y=50)


def type_of_clf():
    print ("value is:" + variable.get())
variable=StringVar(root)
variable.set('select classifier type')
option=['Naive Bayes','Decision Tree','Logistic Regression','K-Nearest Neighbor','Support Vector Machine']
OptionMenu(root,variable,*option).place(x=20,y=120)
Button(root, text="Add", command=type_of_clf).place(x=200,y=120)


'''def Log_reg():
    global read_file
    global variable_tg
    global clf
    y=data[variable_tg.get()]
    x=data.drop([variable_tg.get()],axis=1)
    print(10)
    clf = LogisticRegression(random_state=0).fit(x, y)'''

def submit_test_case():
    global scval
    global L
    global top
    global clf
    L=scval.get().split()
    M=[]
    for x in L:
        M.append(eval(x))
    print('case:',M)
    P=StringVar()
    Q=StringVar()
    tmsg.showinfo('confarmed','you successfully submit test case')
    p=clf.predict([M])
    d=clf.predict_proba([M])
    P.set(p[0])
    Q.set(round(max(d[0])*100,2))
    Label(top,text='Result').place(x=5,y=80)
    Label(top,text='Probablity').place(x=5,y=100)
    Entry(top,textvar=P).place(x=70,y=80)
    Entry(top,textvar=Q).place(x=70,y=100)
    Button(top, text="Exit",bg='red', command=top.destroy).place(x=20,y=120)
    
    
    
def test_case():
    #print(n)
    global scval
    global top
    top=Toplevel()
    top.title('Test case')
    top.geometry('360x240')
    top.iconbitmap('C:\\Users\\TITAS\\Downloads\\ml.ico')
    scval=StringVar()
    scval.set('')
    screen=Entry(top,textvar=scval)
    screen.pack(fill=X,ipadx=100,padx=10,pady=10)
    Button(top, text="submit",fg='blue', command=submit_test_case).place(x=280,y=50)
    

def set_target():
    global variable_tg
    global read_file
    global clf
    print ("value is:" + variable_tg.get())
    print(10)
    s=variable_tg.get()
    print(type(s))
    if variable.get()=='Logistic Regression':
         print(12)
         print(read_file)
         y=read_file[s]
         x=read_file.drop([s],axis=1)
         print(x)
         print(y)
         clf = LogisticRegression(random_state=0).fit(x, y)
         test_case()
         
    else:
        pass
        
    
#m=50
def get_target():
    global A
    global variable_tg
    m=variable_tg
    variable_tg=StringVar(root)
    variable_tg.set('select')
    OptionMenu(root,variable_tg,*A).place(x=20,y=180)
    Button(root, text="set Target & build model",fg='blue',command=set_target).place(x=200,y=180)
    
Button(root, text="Add Target",fg='blue', command=get_target).place(x=20,y=150)
#Button(root, text="Test Case",fg='blue', command=lambda:test_case(m)).place(x=20,y=230)


Label(root,text='© MOLLA SAROAYR HOSSAIN',fg='red').place(y=600)
root.mainloop()


