from tkinter import *
import numpy as np

def knapsack_solver(max_weight, weight_vector, value_vector):
    n_elements = len(value_vector)
    
    matrix = [[0 for x in range(W+1)] for x in range(n+1)] 

    for line in range(n_elements + 1):
        for column in range(max_weight + 1):
            if line == 0 or column == 0:
                matrix[line][column] = 0
            elif weight_vector[line -1] <= column:
                w = column - weight_vector[line -1]
                v = value_vector[line - 1] + matrix[line-1][w]
                matrix[line][column] = max(v, matrix[line-1][column])  
            else:
                matrix[line][column] = matrix[line-1][column]
    
    return matrix[n_elements][max_weight]
            

def set_entry(parent, label_text, width=None, **options):
    entry_widget = Frame(master=parent, bg='black')
    entry_widget.pack(fill=X, ipady= 10, padx=10)
    Label(entry_widget, text=label_text, bg='black', fg='white').pack(side=LEFT)
    entry = Entry(entry_widget, **options, bg='black', fg='white',
                insertbackground='white')
    if width:
        entry.config(width=width)
    entry.pack(side=RIGHT)
    return entry


def add_values():
    try:
        n_elem = int(num_elements.get()) 
    except:
        print('tá errado')

    v_weight = []
    v_values = []
    
    for i in range(n_elem):
        Label(back, text = 'Element' + str(i+1) , bg='black', fg='white').pack()
        v_values.append(set_entry(back, 'Valor:', 30))
        v_weight.append(set_entry(back, 'Peso:', 30))
        
        if i < n_elem -1 :
            button_widget = Frame(master=back, bg='black')
            button_widget.pack(fill=X, pady=20, padx=10)
            next = Button(button_widget, text='Preencher valores e pesos',pady=5, width=100,
                          command=save, bg='white', fg='black')
            next.pack()
        
     
    button_widget = Frame(master=back, bg='black')
    button_widget.pack(fill=X, pady=20, padx=10)
    go = Button(button_widget, text='Preencher valores e pesos',pady=5, width=100,
                command=calc, bg='white', fg='black')
    go.pack()
    
def calc():
    print('oi')

if __name__ == '__main__':
    app = Tk()
#    val = [60, 100, 120] 
#    wt = [10, 20, 30] 
#    W = 50
#    n = len(val) 
#    print(knapsack_solver(W, wt, val)) 

    app.title('Knapsack problem')
    app.geometry('500x500')
    app.resizable(0,0)
    
    back1 = Frame(master=app, bg='black')
    back1.pack_propagate(0)
    back1.pack(fill=BOTH, expand=1)

    back=Canvas(back1,bg='black',width=300,height=300,scrollregion=(0,0,500,800))
    vbar=Scrollbar(back1,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=back.yview)
    back.config(width=300,height=300)
    back.config(yscrollcommand=vbar.set)
    back.pack(side=LEFT,expand=True,fill=BOTH)
    back.create_rectangle((200,300,300,600))
    
    title =  Label(back, text = 'The Knapsack Problem Solver', bg='black',
                   fg='white')
    title['font'] = ('URW Gothic','14','bold')
    title.pack(fill=X, ipady=10)

    knapsack_weight = set_entry(back, 'Peso maximo da mochila:', 30)  
    num_elements = set_entry(back, 'Numero de elementos:', 30)

    button_widget = Frame(master=back, bg='black')
    button_widget.pack(fill=X, pady=20, padx=10)
    fill = Button(button_widget, text='Preencher valores e pesos',pady=5, width=100,
                command=add_values, bg='white', fg='black')
    fill.pack()
    
    scrollable_body = Scrollable(body, width=32)
  
    app.mainloop()
