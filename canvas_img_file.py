import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import json

class mainWindow(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        menu = tk.Menu(self.master)
        master.config(menu=menu)

        file_menu = tk.Menu(menu,tearoff = 0)
        file_menu.add_command(label="Open", command = self.openFile)
        file_menu.add_command(label="Save", command = self.saveLabel)
        file_menu.add_command(label="Exit", command = self.onExit)
        
        
        menu.add_cascade(label="File", menu=file_menu)
        
        effect_menu = tk.Menu(menu,tearoff = 0)
        effect_menu.add_command(label="Gray")
        
        menu.add_cascade(label="Effect", menu=effect_menu)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.image = None # none yet

    #Where I open my file
    def openFile(self):
        
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=[("png files","*.png"),("jpeg files","*.jpg")])
        
        if not filename:
            return # user cancelled; stop this method
        
        self.imagepath = filename
        load = Image.open(filename)
        w, h = load.size
        self.render = ImageTk.PhotoImage(load) #must keep a reference to this

        if self.image is not None: # if an image was already loaded
            self.canvas.delete(self.image) # remove the previous image

        #if self.i:
         #   self.canvas.delete(slef.i) # remove the previous image
            
        self.image = self.canvas.create_image((w / 2, h / 2), image = self.render)
        
        root.geometry("%dx%d" % (w, h))
        
        self.canvas.bind("<ButtonPress-1>", self.drawFirstCorner)
        self.canvas.bind("<B1-Motion>", self.drawRectangle)
        self.canvas.bind("<ButtonRelease-1>", self.drawLastCorner)
    
    def onExit(self):
        self.canvas.delete("all")
        self.quit()
        
    def drawFirstCorner(self,event):
    
        global ix,iy,drawing
        # Left Mouse Button Down Pressed
        
        print(event, "event") 
        self.spt_x = event.x
        self.spt_y = event.y
        print("{} and {}".format(self.spt_x,self.spt_y)) 
        
        
    
    def drawRectangle(self,event):
        
        drawing = False
        ix = event.x
        iy = event.y
        print(event, "event")
        
        print("{} and {}".format(ix,iy))
        i = self.canvas.create_rectangle(self.spt_x, self.spt_y, ix, iy, outline="#D0FFC0", fill='')
        print(i)
        if(i>1):
            j = i-1
            print(j)
            self.canvas.delete(j) # remove        
       
            
    def drawLastCorner(self,event):
        
        print(event, "event")
        print("{} and {}".format(event.x,event.y))
        self.canvas.create_rectangle(self.spt_x, self.spt_y, event.x, event.y, outline="#D0FFC0", fill='')    
        self.lpt_x = event.x
        self.lpt_y = event.y
        
    def saveLabel(self):
    
        #if self.image is not None: # if an image was already loaded
         #   return 
        print(self.imagepath)
        basefile = os.path.basename(self.imagepath)
        print(basefile)
        filestem = os.path.splitext(basefile)[0]
        fileext = os.path.splitext(basefile)[1]
        print(filestem)
        print(fileext)
        dirpath = os.path.dirname(os.path.realpath(self.imagepath))
        print(dirpath)
        
        f = open('data.json',"w+")   
        f.write("This is line")
        f.close()

root = tk.Tk()
root.geometry("%dx%d" % (600, 600))
root.title("MakeupImage")
app = mainWindow(root)
app.pack(fill=tk.BOTH, expand=1)
root.mainloop()