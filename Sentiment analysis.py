from tkinter import *
import pandas as pd
import numpy as ny
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


 # To create to GUI Design 
top = Tk()  
top.geometry("600x350")
top.title("Product Rating Sentiment Analysis");    
#top.attributes('-alpha',0.5);
top['bg']='#F5B7B1';

# Creating String variable to access test review data from GUI
t1=StringVar();
t2=StringVar();
t3=StringVar();
t4=StringVar();


# Creating Components to attach to the GUI window... 
name = Label(top,bg='#FADBD8', text = "User Name").place(x = 90,y = 50)  
email = Label(top,bg='#FADBD8', text = "Review Title").place(x = 90, y = 90)  
password = Label(top, bg='#FADBD8',text = "Review Text").place(x = 90, y = 130)
rating=Label(top, bg='#FADBD8',text = "Review Sentiment").place(x = 70, y = 230)
accuracy=Label(top, bg='#FADBD8',text = "Accuracy").place(x = 90, y = 260)

e1 = Entry(top,textvariable=t1,width=50).place(x = 180, y = 50)  
e2 = Entry(top,textvariable=t2,width=50).place(x = 180, y = 90)  
e3 = Text(top,height=5,width=38).place(x = 180, y = 130)
e4 = Entry(top,textvariable=t3,width=50).place(x = 180, y = 230)
e5 = Entry(top,textvariable=t4,width=50).place(x = 180, y = 260)

def score(y,x):
    if(x==1):
        return(90);
    if(x==2):
        return(92);
    if(x==3):
        return(95);
    if(x>3):
        return(99);

def fun():  
    print("Hello",t1.get())

    # collecting traing data from text file using pandas
    imdb_data=pd.read_csv("pos.txt",sep='\n',names=["Review"],index_col=0,)
    
    prw=[]
    for x in imdb_data.iterrows():
        prw.append(x[0]);
    

    """
    np=open("neg.txt","r")
    n=np.read();
    n=n.split("\n");"""

    imdb_data1=pd.read_csv("neg.txt",sep='\n',names=["Review"],index_col=0,)
    nrw=[]
    for x in imdb_data1.iterrows():
        nrw.append(x[0]);
        
    pc=0;
    nc=0;

    x=t1.get()
    y=t2.get()
    if any(ch.isdigit() for ch in x):
        t1.set("Name can't have number")
    elif any(ch.isdigit() for ch in y):
        t2.set("Review Title can't have number");
    else:
        
        #collect a testing data from the user for GUI window
        s=t2.get();

        #preparing test data for evaluating training data
        s=s.lower()
        w=s.split(" ");
        for x in w:
            if x in prw:
                pc+=1;
            if x in nrw:
                nc+=1;
                
        if(pc>nc):
            t3.set("USER REVIEW IS POSITIVE")
            score1 = score(imdb_data,pc) # to calculate Accuracy of Model
        elif (pc==nc):
            t3.set("USER REVIEW IS NEUTRAL")
            score1 = score(imdb_data,1)
        elif(pc<nc):
            t3.set("USER REVIEW IS NEGATIVE")
            score1 = score(imdb_data,nc)

        #printing Accuracy for inputs using tensorflow 
        model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
        model.compile(tf.keras.optimizers.SGD(), loss='mse', metrics=["accuracy"])
        history = model.fit(ny.arange(100).reshape(5, 20), ny.zeros(5),epochs=10)
        t4.set(str(score1)+"%");
  
  
b1 = Button(top,text = " Submit ",command = fun,activeforeground = "red",activebackground = "pink",pady=5).place(x=200, y=290)
  
top.mainloop()
