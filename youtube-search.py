from tkinter import * 
from PIL import ImageTk, Image
from urllib.request import urlopen 
from io import BytesIO
from youtubesearchpython import VideosSearch


root=Tk()
root.title("Youtube Search")
root.geometry("1280x720")
root.configure(bg='#0f0e0e')


#heading
heading=Label(text="Youtube",font=("Helvetica",30),bg='#0f0e0e',fg="white")
heading.pack(pady=20)

#buttons frame
button_frame=Frame(root,bg='#0f0e0e')
button_frame.pack()

#Create search box
my_entry=Entry(button_frame,font=("Helvetica",18),width=47)
my_entry.pack(padx=10,side=LEFT)


#search
def search():
    data = VideosSearch(my_entry.get())
    for i in range(6):
        # print(data.result()['result'][i]['thumbnails'][0]["url"])
        URL=data.result()['result'][i]['thumbnails'][0]["url"]
        u = urlopen(URL)
        raw_data = u.read()
        u.close()

        myimg = Image.open(BytesIO(raw_data))
        myimg = myimg.resize((200, 200))
        photo = ImageTk.PhotoImage(myimg)
        img=Label(image=photo)
        img.image=photo
        img.pack()

        

#buttons
search_button=Button(button_frame,text="search",font=("Helvetica",13),bg='#0f0e0e',fg="white",command=search)
search_button.pack(side=RIGHT)







root.mainloop()