import matplotlib.pyplot as plot
import geopandas as gpd
import json
from shapely.geometry import Point, shape

def readshapefile(choosenshpfile):  
    shapefile = gpd.read_file(choosenshpfile) 
    fig, ax = plot.subplots() 
    shapefile.plot(edgecolor="black", categorical = True,
                         legend = True, figsize = (10, 10),
                         markersize = 45,cmap = "Set2", ax = ax)
    #ax.set_title("please click on the figure " , fontsize = 14)



    def onclick(event): 
        global pointofclick 
        ix = float(event.xdata) 
        iy = float(event.ydata)
        pointofclick = Point(ix , iy)
        print(pointofclick)
        click(pointofclick)

    cid = fig.canvas.mpl_connect('button_press_event', onclick)

   

    def click(mypoint): 
        global liner , poly
        for liner in range(0 , len(geomeryofgeo)):
            poly = shape(geomeryofgeo.get(liner))
            checker(poly, mypoint)

   

    def checker(myobject, pointofcheck):
        if pointofcheck.within(myobject):
            print(liner)
          
            onclick
            readtable(liner)
            newtkinter(pointofcheck)
        else:
            onclick

   

    listofheader = []
    listofattrib = []

    def readtable(countertable):

        for g in geo:
            if g!= "geometry":
                geodict = geo.get(g)
                listofheader.append(g)
                print(g)
                print(geodict.get(countertable))
                atrrib = geodict.get(countertable)
                listofattrib.append(atrrib) 
        onclick 

  

    def newtkinter(ourpoint): 
        dictofobject = [list(x) for x in zip(listofheader, listofattrib)] 
        listofattrib.clear() 
        listofheader.clear() 
        import tkinter as tk 
        import tksheet
        top = tk.Tk()
        top.title("%s" % ourpoint) 
        sheet = tksheet.Sheet(top) 
        sheet.grid()
        sheet.set_sheet_data(dictofobject)
        sheet.enable_bindings(("single_select","row_select","column_width_resize","arrowkeys","right_click_popup_menu","rc_select","rc_insert_row","rc_delete_row", "copy","cut","paste","delete","undo","edit_cell"))
        sheet.highlight_columns([1], bg="light blue", fg="black")
        sheet.highlight_columns([0], bg="light green", fg="blue")
        sheet.clipboard_clear()
        top.mainloop()

    

geo = []
def dbfread(dbffile): 
    global geo , geomeryofgeo 
    dbfmainfile = gpd.GeoDataFrame.from_file(dbffile)
    geo = gpd.GeoDataFrame.to_dict(dbfmainfile) 
    for g in geo:
        if g=="geometry" or "Geometry" or "GEOMETRY":
            geomeryofgeo = geo.get(g) 


from tkinter import *
from tkinter import filedialog
import numpy as np
window=Tk()
window.title("ShapefileReader") 
window.geometry("500x125") 
color="gray" 
label = Label(window, text = "This program is designed to read shapefiles", bg = "green", bd = 10, fg = "white", font = "Castellar")
label.pack()
def getmainfile():
    global fname
    fname=filedialog.askopenfile(mode="r" )
    print(fname.name)
    readshapefile(fname.name)
firstbutton=Button(window, height=1, width=60, bg="green", fg = "white",text="click on your .shp file", command=getmainfile)

firstbutton.pack()
def getdbffile():
    global dbffname
    dbfname=filedialog.askopenfile(mode="r")
    print(dbfname.name)
    dbfread(dbfname.name)
secondbutton=Button(window, height=1, width=50, bg="green",fg = "white", text="click on your .dbf file", command=getdbffile)
secondbutton.pack()
def showgraph(): 
    plot.show()
thirdbutton=Button(window, height=1, width=40, bg="green", fg = "white",text='file figure', command=showgraph)
thirdbutton.pack()
window.mainloop()