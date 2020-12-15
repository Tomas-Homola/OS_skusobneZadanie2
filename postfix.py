

def eval_expr(s):
    
    temp = []
    s = s.split() # rozdelenie na list

    for item in s:
        
        if (item.isnumeric()): # ak to je cislo, tak sa prida do temp zoznamu
            temp.append(item)
        else: # ak to nie je cislo, tak uz sa predpoklada, ze v temp zozname su uz 2 cisla, tie sa vyberu a daju do "a" a "b"
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
