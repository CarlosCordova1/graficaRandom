"""def recur_sum(n):
   #Function to return the sum
   #of natural numbers using recursion
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = int (input("insertar num - >>> "))

# uncomment to take input from the user
#num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
   
   
   """
#https://datatofish.com/how-to-create-a-gui-in-python/

import tkinter as tk
from random import randrange,  uniform

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def limitSize(*args):
    value = entryText.get()
    if len(entryText.get()) > 6: entryText.set(value[:6])



root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=300)
canvas1.pack()
root.title("carloscordova9003@gmail.com")
label1 = tk.Label(root, text='Grafica con tkinter y matplotlib')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)

label1entry = tk.Label(root, text='Label 1')
label1entry.config(font=('Arial', 12))
canvas1.create_window(300, 100, window=label1entry)

#entry1 = tk.Entry(root)
entryText = tk.StringVar()
entryText.trace('w', limitSize)
entry1 = tk.Entry( root, textvariable=entryText )
entryText.set( "5" )


canvas1.create_window(400, 100, window=entry1)

label2entry = tk.Label(root, text='Label 2')
label2entry.config(font=('Arial', 12))
canvas1.create_window(300, 120, window=label2entry)
#ntry2 = tk.Entry(root)
entryText2 = tk.StringVar()
entry2 = tk.Entry( root, textvariable=entryText2 )
entryText2.set( "10" )
canvas1.create_window(400, 120, window=entry2)

label3entry = tk.Label(root, text='Label 3')
label3entry.config(font=('Arial', 12))
canvas1.create_window(300, 140, window=label3entry)
#entry3 = tk.Entry(root)
entryText3 = tk.StringVar()
entry3 = tk.Entry( root, textvariable=entryText3 )
entryText3.set( "30" )
canvas1.create_window(400, 140, window=entry3)


def create_charts():
    global x1
    global x2
    global x3
    global bar1
    global pie2

    try:
        bar1
    except NameError:
        print("well, it WASN'T defined after all!")
    else:
        print("sure, it was defined.")
        bar1.get_tk_widget().pack_forget()
        pie2.get_tk_widget().pack_forget()




    x1 = float(entry1.get())
    x2 = float(entry2.get())
    x3 = float(entry3.get())

    figure1 = Figure(figsize=(4, 3), dpi=100)
    subplot1 = figure1.add_subplot(111)
    xAxis = [float(x1), float(x2), float(x3)]
    yAxis = [float(x1), float(x2), float(x3)]
    subplot1.bar(xAxis, yAxis, color='lightsteelblue')
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

    figure2 = Figure(figsize=(4, 3), dpi=100)
    subplot2 = figure2.add_subplot(111)
    labels2 = 'Label1 ' +str(x1), 'Label2 '+str(x2), 'Label3 '+str(x3)
    pieSizes = [float(x1), float(x2), float(x3)]
    my_colors2 = ['lightblue', 'lightsteelblue', 'silver']
    explode2 = (0, 0.1, 0)
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True,
                 startangle=90)
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().pack()


def clear_charts():
    #bar1.get_tk_widget().pack_forget()
    #pie2.get_tk_widget().pack_forget()
    entryText.set(str(round(uniform(0, 100), 2)))
    entryText2.set(str(round(uniform(0, 100), 2)))
    entryText3.set(str(round(uniform(0, 100), 2)))
    #entryText2.set(randrange(0, 101, 2))
    #entryText3.set(randrange(0, 101, 2))



button1 = tk.Button(root, text=' Crear Charts ', command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold'))
canvas1.create_window(270, 180, window=button1)

button2 = tk.Button(root, text='  Random', command=clear_charts, bg='lightskyblue2', font=('Arial', 11, 'bold'))


canvas1.create_window(400, 180, window=button2)

button3 = tk.Button(root, text='Salir', command=root.destroy, bg='lightsteelblue2',
                    font=('Arial', 11, 'bold'))
canvas1.create_window(500, 180, window=button3)

root.mainloop()