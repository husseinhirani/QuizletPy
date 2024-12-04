import tkinter
import parse


index=0
termodef=True
def flipCard():
    global termodef
    global index
    if termodef:
        flashcard["text"] = definition[index]
        
    else:
        flashcard["text"]= terms[index]
    termodef= not termodef
def nextCard():
    global index
    global termodef
    if(index < len(terms)-1):
        index +=1
        flashcard["text"] = terms[index]
        termodef = True
def prevCard():
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



flashcard = tkinter.Button(text=terms[index], command=flipCard)
right = tkinter.Button(text=">", command = nextCard)
left = tkinter.Button(text="<", command = prevCard)


flashcard.pack()
right.pack()
left.pack()

root.mainloop()








