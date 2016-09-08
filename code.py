#bijoria,shivam
#1001359394
#2016-03-02
#Assignment_02
import threading
import time
import math
import tkinter as tk
from tkinter import filedialog
import os
global XRotation
global YRotation
global ZRotation
global XScale
global YSCale
global ZScale
global axis
#axis= StringVar()
    
#button function definitions
def openfiledialogbox():
    canvas.delete("all")
    global file_path 
    file_path= filedialog.askopenfilename()
    #print (file_path)
    global filename
    filename=os.path.basename(file_path)
    #print(filename)
def loadfile():
       canvas.delete("all") 
       
       mainloop()
    

def eoccur(event):
    canvas.delete("all")
    global winw
    winw=root.winfo_width()
    global winh
    winh=root.winfo_height()
    #mainloop()

	
def Rotation():	
    global degreetorotate
    degreetorotate=int(Degreeentry.get())
    global steps
    steps=int(stepentry.get())
    global axisselected
    axisselected=axis.get()
    w = threading.Thread(name='worker', target=worker)
    #t = threading.Thread(name='my_service', target=my_service)
    if(axisselected=='Z'):
       
        w.start()
        
        
         
         
        
def worker():
    for i in range (1,steps+1):
       ZRotation(math.radians(degreetorotate)*-1/steps)
       time.sleep(0.25)


    
    
            
def ZRotation(degree_in_each_step):
    
    canvas.delete("all")
    degreetoRadZ=degree_in_each_step
    
     #temporary vertexarray
    global VertexRotationtemp
    VertexRotationtemp = [[0 for x in range(3)]]
    VertexRotationtemp[0][0]=0
    VertexRotationtemp[0][0]=0
    VertexRotationtemp[0][0]=0
    loop1=1
    for loop1 in range (1,vertexcount):
       #VertexRotation[loop1][0]=Vertex[loop1][0]
       #VertexRotation[loop1][1]=(Vertex[loop1][1]*math.cos(degreetoRadX) + Vertex[loop1][2]*math.sin(degreetoRadX))
       #VertexRotation[loop1][2]=(Vertex[loop1][1]*math.sin(degreetoRadX)*-1 + Vertex[loop1][2]*math.cos(degreetoRadX))
       VertexRotationtemp.insert(loop1,[VertexRotation[loop1][0],VertexRotation[loop1][1],VertexRotation[loop1][2]])
	
	
	
    VertexRotation[0][0]=0
    VertexRotation[0][0]=0
    VertexRotation[0][0]=0
    loop1=1
    for loop1 in range (1,vertexcount):
       #VertexRotation[loop1][0]=Vertex[loop1][0]
       #VertexRotation[loop1][1]=(Vertex[loop1][1]*math.cos(degreetoRadX) + Vertex[loop1][2]*math.sin(degreetoRadX))
       #VertexRotation[loop1][2]=(Vertex[loop1][1]*math.sin(degreetoRadX)*-1 + Vertex[loop1][2]*math.cos(degreetoRadX))
       VertexRotation.insert(loop1,[VertexRotationtemp[loop1][0]*math.cos(degreetoRadZ)+VertexRotationtemp[loop1][1]*math.sin(degreetoRadZ),VertexRotationtemp[loop1][0]*math.sin(degreetoRadZ)*-1+VertexRotationtemp[loop1][1]*math.cos(degreetoRadZ),VertexRotationtemp[loop1][2]])

	
	
	#calcuting scale factor
    scalefactorX=(vxmax-vxmin)/(wxmax-wxmin)
    ##print ('scalefactorX ',scalefactorX)
    scalefactorY=(vymax-vymin)/(wymax-wymin)
    ##print ('scalefactorY ',scalefactorY)
    
	#rendering the polygons
    
    totalnumberfaces=len(Face)
    for facenumber in range (0,totalnumberfaces-1):
    
        vertex1=Face[facenumber][0]
        vertex2=Face[facenumber][1]
        vertex3=Face[facenumber][2]
        
        #drawing and calculating the right coordinates at the same time
        id=canvas.create_line(
	    round((((VertexRotation[vertex1][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((VertexRotation[vertex1][1]-wymin)*scalefactorY)+vymin)*winh),
	    round((((VertexRotation[vertex2][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((VertexRotation[vertex2][1]-wymin)*scalefactorY)+vymin)*winh),
	    round((((VertexRotation[vertex3][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((VertexRotation[vertex3][1]-wymin)*scalefactorY)+vymin)*winh),
	    round((((VertexRotation[vertex1][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((VertexRotation[vertex1][1]-wymin)*scalefactorY)+vymin)*winh)
	    )
     
    id1=canvas.create_line(round(vxmin*winw),round(winh-vymin*winh),
	round(vxmax*winw),round(winh-vymin*winh),
	round(vxmax*winw),round(winh-vymax*winh),
	round(vxmin*winw),round(winh-vymax*winh),
	round(vxmin*winw),round(winh-vymin*winh))
	
	 
    



def XRotation():
    canvas.delete("all")
    degreetoRadX=math.radians(-10)
    global VertexRotation
    VertexRotation = [[0 for x in range(3)]]
    VertexRotation[0][0]=0
    VertexRotation[0][0]=0
    VertexRotation[0][0]=0
    loop1=1
    for loop1 in range (1,vertexcount):
       #VertexRotation[loop1][0]=Vertex[loop1][0]
       #VertexRotation[loop1][1]=(Vertex[loop1][1]*math.cos(degreetoRadX) + Vertex[loop1][2]*math.sin(degreetoRadX))
       #VertexRotation[loop1][2]=(Vertex[loop1][1]*math.sin(degreetoRadX)*-1 + Vertex[loop1][2]*math.cos(degreetoRadX))
       VertexRotation.insert(loop1,[Vertex[loop1][0],Vertex[loop1][1]*math.cos(degreetoRadX) + Vertex[loop1][2]*math.sin(degreetoRadX),Vertex[loop1][1]*math.sin(degreetoRadX)*-1 + Vertex[loop1][2]*math.cos(degreetoRadX)])
    #calcuting scale factor
    scalefactorX=(vxmax-vxmin)/(wxmax-wxmin)
    #print ('scalefactorX ',scalefactorX)
    scalefactorY=(vymax-vymin)/(wymax-wymin)
    #print ('scalefactorY ',scalefactorY)
    #rendering the polygons
    
    totalnumberfaces=len(Face)
    for facenumber in range (0,totalnumberfaces-1):
    
        vertex1=Face[facenumber][0]
        vertex2=Face[facenumber][1]
        vertex3=Face[facenumber][2]
        
        #drawing and calculating the right coordinates at the same time
        id=canvas.create_line(
	    round((((VertexRotation[vertex1][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((VertexRotation[vertex1][1]-wymin)*scalefactorY)+vymin)*winh),
	    round((((VertexRotation[vertex2][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((VertexRotation[vertex2][1]-wymin)*scalefactorY)+vymin)*winh),
	    round((((VertexRotation[vertex3][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((VertexRotation[vertex3][1]-wymin)*scalefactorY)+vymin)*winh),
	    round((((VertexRotation[vertex1][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((VertexRotation[vertex1][1]-wymin)*scalefactorY)+vymin)*winh)
	    )
     
    id1=canvas.create_line(round(vxmin*winw),round(winh-vymin*winh),
	round(vxmax*winw),round(winh-vymin*winh),
	round(vxmax*winw),round(winh-vymax*winh),
	round(vxmin*winw),round(winh-vymax*winh),
	round(vxmin*winw),round(winh-vymin*winh))
    
   
#window creation
root = tk.Tk() #Tkinter's 'main window'

root.title('Assignment 01 ')
root.geometry('1000x700') # Size winw,winh
canvas = tk.Canvas( width=1000, height=700,bg='yellow')

#button creation
selectfile = tk.Button(text="Select file",command=openfiledialogbox)
loadfile = tk.Button(text="load file",command=loadfile)
Rotate = tk.Button(text="Rotate",command=Rotation)
Rotationaxis=tk.Label(text='Rotation axis:')
global axis
axis= tk.StringVar()

X= tk.Radiobutton(root, text ='X' ,variable=axis,  value='X')
Y= tk.Radiobutton(root, text ='Y',variable=axis , value='Y')
Z= tk.Radiobutton(root, text ='Z',variable=axis, value='Z')
Line_AB=tk.Label(text='Line AB ')
Point_A=tk.Label(text='A')
AXentry=tk.Entry(root,width=5)
AYentry=tk.Entry(root,width=5)
AZentry=tk.Entry(root,width=5)
Point_B=tk.Label(text='B')
BXentry=tk.Entry(root,width=5)
BYentry=tk.Entry(root,width=5)
BZentry=tk.Entry(root,width=5)
Degrees=tk.Label(text='Degree:')
Degreeentry=tk.Entry(root,width=5)
steps=tk.Label(text='Steps:')
stepentry=tk.Entry(root,width=5)
stepentry.insert(0, '1')
canvas.bind("<Configure>", eoccur)
Scalelabel=tk.Label(text='Scale')
ALL= tk.Radiobutton(root, text ='ALL' ,  value='ALL')
ALLentry=tk.Entry(root,width=5)
SXSYSZ= tk.Radiobutton(root, text ='[SxSySz]',  value='[SxSySz]')
SXentry=tk.Entry(root,width=5)
SYentry=tk.Entry(root,width=5)
SZentry=tk.Entry(root,width=5)
ScaleAboutPointA=tk.Label(text='A')
ScaleAXentry=tk.Entry(root,width=5)
ScaleAYentry=tk.Entry(root,width=5)
ScaleAZentry=tk.Entry(root,width=5)
stepsbottom=tk.Label(text='Steps:')
stepentrybottom=tk.Entry(root,width=5)
ScaleButton = tk.Button(text="Scale")


selectfile.grid(column=0, row=0,sticky='W')
loadfile.grid(column=1, row=0,sticky='W')

Rotationaxis.grid(column=0,row=1,sticky='W')
X.grid(column=1, row=1,sticky='W')
Y.grid(column=2, row=1,sticky='W')
Z.grid(column=3, row=1,sticky='W')

Line_AB.grid(column=4, row=1,sticky='W')
Point_A.grid(column=5, row=1,sticky='W')
AXentry.grid(column=6, row=1,sticky='W')
AYentry.grid(column=7, row=1,sticky='W')
AZentry.grid(column=8, row=1,sticky='W')

Point_B.grid(column=9, row=1,sticky='W')
BXentry.grid(column=10, row=1,sticky='W')
BYentry.grid(column=11, row=1,sticky='W')
BZentry.grid(column=12, row=1,sticky='W')

Degrees.grid(column=13, row=1,sticky='W')
Degreeentry.grid(column=14, row=1,sticky='W')
steps.grid(column=15, row=1,sticky='W')
stepentry.grid(column=16, row=1,sticky='W')
Rotate.grid(column=17, row=1,sticky='W')

canvas.grid(column=0,row=3,columnspan=100)

Scalelabel.grid(column=0, row=2,sticky='W')
ALL.grid(column=1, row=2,sticky='W')
ALLentry.grid(column=2, row=2,sticky='W')
SXSYSZ.grid(column=3, row=2,sticky='W')
SXentry.grid(column=4, row=2,sticky='W')
SYentry.grid(column=5, row=2,sticky='W')
SZentry.grid(column=6, row=2,sticky='W')
ScaleAboutPointA.grid(column=7, row=2,sticky='W')
ScaleAXentry.grid(column=8, row=2,sticky='W')
ScaleAYentry.grid(column=9, row=2,sticky='W')
ScaleAZentry.grid(column=10, row=2,sticky='W')
stepsbottom.grid(column=11, row=2,sticky='W')
stepentrybottom.grid(column=12, row=2,sticky='W')
ScaleButton.grid(column=13, row=2,sticky='W')

def mainloop():
    #declaration
    
    global vertexcount #it starts from 1 because in file vertex is indexed from 1 for drawing faces
    global degreetoRadX
    global Vertex
    global scalefactorX
    global vxmax 
    global vxmin
    global wxmax
    global wxmin
    global vymax
    global vymin
    global wymax
    global wymin
    global scalefactorY
    global totalnumberfaces
    global Face 
    global vertex1
    global vertex2
    global vertex3
    global winh
    global winw  
	#YRotation
#    ZRotation
 #   XScale
  #  YSCale
   # ZScale
    Vertex = [[0 for x in range(3)]]
    vertexcount=1
    Face = [[]]
    Facecount=0
    XRotation=45
    #file line counting and opening
    f1=open(file_path, 'r')
    filesize=len(f1.readlines())
    
    f1.close()
    f=open(file_path, 'r')




    #parsing and storing file
    for i in range (0,filesize):
        readingline=f.readline()
        if(readingline[0]=='v'):
      
            readinglinewithoutv=readingline[1:]
            vertexfloats = [float(x) for x in readinglinewithoutv.split()]
            #Vertex[vertexcount][0]=vertexfloats[0]
            #Vertex[vertexcount][1]=vertexfloats[1]
            #Vertex[vertexcount][2]=vertexfloats[2]
            Vertex.insert(vertexcount,[vertexfloats[0],vertexfloats[1],vertexfloats[2]])
            
            vertexcount=vertexcount+1
        if(readingline[0]=='f'):
      
            readinglinewithoutf=readingline[1:]
            faceintegers = [int(x) for x in readinglinewithoutf.split()]
            #Face[Facecount][0]=faceintegers[0]
            #Face[Facecount][1]=faceintegers[1]
            #Face[Facecount][2]=faceintegers[2]
            Face.insert(Facecount,[faceintegers[0],faceintegers[1],faceintegers[2]])
            
            Facecount=Facecount+1
        if(readingline[0]=='w'):
            readinglinewithoutw=readingline[1:]
            wfloats = [float(x) for x in readinglinewithoutw.split()]
            wxmin=wfloats[0]
            wymin=wfloats[1]
            wxmax=wfloats[2]
            wymax=wfloats[3]
            #print ('wymax is %d',wymax)
        if(readingline[0]=='s'):  
            readinglinewithouts=readingline[1:]
            vfloats = [float(x) for x in readinglinewithouts.split()]
            vxmin=vfloats[0]
            vymin=vfloats[1]
            vxmax=vfloats[2]
            vymax=vfloats[3]
            #print ('vymax is %d',vymax)
	  
	 	
	  
    #calcuting scale factor
    scalefactorX=(vxmax-vxmin)/(wxmax-wxmin)
    #print ('scalefactorX ',scalefactorX)
    scalefactorY=(vymax-vymin)/(wymax-wymin)
    #print ('scalefactorY ',scalefactorY)
    #rendering the polygons
    
    totalnumberfaces=len(Face)
    for facenumber in range (0,totalnumberfaces-1):
    
        vertex1=Face[facenumber][0]
        vertex2=Face[facenumber][1]
        vertex3=Face[facenumber][2]
        
        #drawing and calculating the right coordinates at the same time
        id=canvas.create_line(
	    round((((Vertex[vertex1][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((Vertex[vertex1][1]-wymin)*scalefactorY)+vymin)*winh),
	    round((((Vertex[vertex2][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((Vertex[vertex2][1]-wymin)*scalefactorY)+vymin)*winh),
	    round((((Vertex[vertex3][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((Vertex[vertex3][1]-wymin)*scalefactorY)+vymin)*winh),
	    round((((Vertex[vertex1][0]-wxmin)*scalefactorX)+vxmin)*winw),winh-round((((Vertex[vertex1][1]-wymin)*scalefactorY)+vymin)*winh)
	    )
     
    id1=canvas.create_line(round(vxmin*winw),round(winh-vymin*winh),
	round(vxmax*winw),round(winh-vymin*winh),
	round(vxmax*winw),round(winh-vymax*winh),
	round(vxmin*winw),round(winh-vymax*winh),
	round(vxmin*winw),round(winh-vymin*winh))
    
    f.close()
    global VertexRotation
    VertexRotation = [[0 for x in range(3)]]
    VertexRotation[0][0]=0
    VertexRotation[0][0]=0
    VertexRotation[0][0]=0
    loop1=1
    for loop1 in range (1,vertexcount):
       #VertexRotation[loop1][0]=Vertex[loop1][0]
       #VertexRotation[loop1][1]=(Vertex[loop1][1]*math.cos(degreetoRadX) + Vertex[loop1][2]*math.sin(degreetoRadX))
       #VertexRotation[loop1][2]=(Vertex[loop1][1]*math.sin(degreetoRadX)*-1 + Vertex[loop1][2]*math.cos(degreetoRadX))
       VertexRotation.insert(loop1,[Vertex[loop1][0],Vertex[loop1][1],Vertex[loop1][2]])
    #loop1=0
    #for loop1 in range (0,vertexcount):
       ##print(VertexRotation[loop1][0])
       ##print(VertexRotation[loop1][1])
       ##print(VertexRotation[loop1][2])
       
     

root.mainloop()