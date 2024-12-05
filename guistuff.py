import tkinter
import parse
import tkinter.font as tkFont

index=0
termodef=True

#functions
def flipCard(event=None):
    global termodef
    global index
    if termodef:
        flashcard["text"] = definition[index]
        
    else:
        flashcard["text"]= terms[index]
    termodef= not termodef
def nextCard(event=None):
    global index
    global termodef
    if(index < len(terms)-1):
        index +=1
        flashcard["text"] = terms[index]
        termodef = True
def prevCard(event=None):
    
    global index
    global termodef
    if(index !=0 ):
        index -=1
        flashcard["text"] = terms[index]
        termodef = True
#load lists
terms = parse.term()
definition = parse.defs()
root = tkinter.Tk()
normal_font = tkFont.Font(family="Arial", size=20, weight=tkFont.NORMAL)

#defining UI elements
flashcard = tkinter.Button(text=terms[index], command=flipCard, font=normal_font)
right = tkinter.Button(text=">", command = nextCard)
left = tkinter.Button(text="<", command = prevCard)


#Keyboard Controls
root.bind("<Left>", prevCard)
root.bind("<Right>", nextCard)
root.bind("<space>", flipCard)



#pack
flashcard.pack()
right.pack()
left.pack()

root.mainloop()








