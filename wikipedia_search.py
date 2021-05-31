from tkinter import *
import wikipedia as wiki

root=Tk()
root.title('Wikipedia')
root.geometry("700x675")


my_label_frame=LabelFrame(root,text="Search wiki")
my_label_frame.pack(pady=20)


#Create entry box
my_entry=Entry(my_label_frame,font=("Helvetica",18),width=47)
my_entry.pack(pady=20,padx=20)

#Create text box frame
my_frame=Frame(root)
my_frame.pack(pady=5)

#create vertical scrollbar
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#create horizontal scrollbar
hor_scroll=Scrollbar(my_frame,orient='horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)

#Create text box
my_text=Text(my_frame,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
my_text.pack(pady=5)

#Configure scrollbars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)


#clear
def clear():
    my_entry.delete(0,END)
    my_text.delete(0.0,END)

#search
def search():
    data=wiki.page(my_entry.get())
    #clear screen
    clear()
    #output wiki result
    my_text.insert(0.0,data.content)
    

#buttons frame
button_frame=Frame(root)
button_frame.pack(pady=10)


#buttons
search_button=Button(button_frame,text="Lookup",font=("Helvetica",20),command=search)
search_button.grid(row=0,column=0,padx=20)

clear_button=Button(button_frame,text="Celear",font=("Helvetica",20),command=clear)
clear_button.grid(row=0,column=1,padx=20)

root.mainloop()