terms = []
definition=[]
with open("first.txt", 'r') as file:
    file_content = file.read()
    print(file_content)
    file_content = file_content.split('	')
    termodef= True
    for i in file_content:
        if termodef:
            terms.append(i)
        else:
            definition.append(i)
        termodef = not termodef



def term():
    return terms
def defs():
    return definition
