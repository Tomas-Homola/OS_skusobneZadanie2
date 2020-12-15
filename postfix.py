
def eval_expr(s, d = {}):
    
    temp = []
    s = s.split() # rozdelenie na list

    for item in s:
        
        if (item.isnumeric()): # ak je to cislo
            temp.append(item)

        elif (item in d): # ak je to premenna, tak potom prida do temp jej hodnotu zo slovnika
            temp.append(d[item])
        
        else: # ak je znamienko, tak pocita
            druhe = int(temp.pop())
            prve = int(temp.pop())
            
            # potom podla toho, ze ake je znamienko, sa vyhodnoti vysledok
            if (item == "+"):
                temp.append(prve + druhe)
            
            elif (item == "-"):
                temp.append(prve - druhe)
            
            elif (item == "*"):
                temp.append(prve * druhe)
            
            elif (item == "/"):
                temp.append(prve // druhe)


    return temp[0]

def to_infix(s):

    temp = []
    s = s.split()

    for item in s:

        if (item.isnumeric()): # znovu, ak je to cislo, tak ho da do tempu
            temp.append(item)

        else: # ak je to znamienko
            druhe = temp.pop()
            prve = temp.pop()

            if (item == "+"):
                temp.append('( ' + prve + ' + ' + druhe + ' )')
            
            elif (item == "-"):
                temp.append('( ' + prve + ' - ' + druhe + ' )')

            elif (item == "*"):
                temp.append('( ' + prve + ' * ' + druhe + ' )')

            elif (item == "/"):
                temp.append('( ' + prve + ' / ' + druhe + ' )')

    return temp[0]
