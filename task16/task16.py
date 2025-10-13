import tkinter as tk


tasks = []
task_widgets = []



# =============================================================

# додавання нових завдань
def new_task():
    value = task_tekst.get()
    if value != "":
        # статус завдання
        task_status = tk.BooleanVar(value=False)
        tasks.append({"text": value,"completed": task_status})

        row = 5 + len(tasks)
        
        btn_dell = tk.Button(win, text="x", command=lambda i=len(tasks)-1: dell_task(i))
        btn_dell.grid(row=row, column=2, sticky="w")

        chek = tk.Checkbutton(win, text=value, variable=task_status)
        chek.grid(row=row, column=1, sticky="w")
       
        task_widgets.append((btn_dell, chek))
        task_tekst.delete(0, "end")

        
# видалення існуючих
def dell_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

        btn_dell, chek = task_widgets.pop(index)
        btn_dell.destroy()
        chek.destroy()

        new_widget(index)


# вивід нових полів
def new_widget(index):
    for i in range(index, len(task_widgets)):
        btn_dell, chek = task_widgets[i]
        row = 5 + i + 1
        chek.grid(row=row, column=1, sticky="w")
        btn_dell.config(command=lambda idx=i: dell_task(idx))
        btn_dell.grid(row=row, column=2, sticky="w")
    

# вивід всіх завдань
def print_task():
    info_win = tk.Toplevel(win)
    info_win.title("Список завдань")
    info_win.geometry("200x150")
    text_widget = tk.Text(info_win, width=40, height=20)
    text_widget.config(state='disabled')

    
    if len(tasks) == 0:
        label = tk.Label(info_win, text="Немає завдань")
        label.pack(padx=10, pady=10)
    else:
        task_list = []
        for i, task in enumerate(tasks, 1):
            status = "x" if task["completed"].get() else "o"
            task_list.append(f"{i}. {status} {task['text']}")
        
        label = tk.Label(info_win, text="\n".join(task_list), justify="left")
        label.pack(padx=10, pady=10)
    
    
# вивід не виконаних завдань
def print_uncompleted_task():
    info_win = tk.Toplevel(win)
    info_win.geometry("200x150")
    info_win.title("Не виконані завдання")
    text_widget = tk.Text(info_win, width=40, height=20)
    text_widget.config(state='disabled')

    uncompleted = [task["text"] for task in tasks if not task["completed"].get()]
    
    if len(uncompleted) == 0:
        label = tk.Label(info_win, text="Всі завдання виконані!")
        label.pack(padx=10, pady=10)
    else:
        task_list = "\n".join(f"{i}. {task}" for i, task in enumerate(uncompleted, 1))
        label = tk.Label(info_win, text=task_list, justify="left")
        label.pack(padx=10, pady=10)


def delete_entry():
     task_tekst.delete(0, "end")


# =======================================================

win = tk.Tk()
win.title("Список завдань")
win.geometry("500x400+300+200" )

label_task = tk.Label(win, text = "Введіть завдання: ")
label_task.grid(row=2, column=1)

task_tekst = tk.Entry(win, width=50)
task_tekst.grid(row=2, column= 2)


tk.Button(win, text="Додати завдання", command=new_task, width=20).grid(row=3, column=1, sticky="w")
tk.Button(win, text="Очистити поле", command=delete_entry, width=20).grid(row=3, column=2, sticky="w")
tk.Button(win, text="Список завдань", command=print_task, width=20).grid(row=4, column=1, sticky="w")
tk.Button(win, text="Не виконані завдання", command=print_uncompleted_task, width=20).grid(row=4, column=2, sticky="w")
win.grid_columnconfigure(0, minsize = 20)



win.mainloop()

