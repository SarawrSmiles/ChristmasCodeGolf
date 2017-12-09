def print_box(l, w, h):
    top = '.'
    for i in range (0, w):
        top += "."

    top += '+'
    for i in range (0, l):
        top += "-"
    top += '+'

    side = './'
    for i in range (0,l):
        side += "."
    side += '/|'

    bot = '+'
    for i in range (0, l):
        bot += "-"
    bot += '+ |'



    print top
    print side
    print bot

def print_box2(l, w, h):
    hor = '+'
    for i in range (0, l):
        hor += '-'
    hor += "+"

    push = 1 + w;

    for i in range (0, push):
        hor = "." + hor

    print hor

    for i in range (0, w):
        line = ""
        push -= 1
        for i in range (0, push):
            line += "."
        line += "/"
        for i in range(0,l):
            line+= "."
        line += "/"
        for i in range(0, w-push):
            line += "."
        line += "|"
        print line

    hor = hor.replace(".", "")
    for i in range (0,w):
        hor += "."
    hor += "+"
    print hor
   
    push = w - 1  
    for i in range (0, h):
        line = "|"
        for i in range(0,l):
            line+= "."
        line += "|"
        for i in range(0,push):
            line += "."
        push -= 1
        line += "/"
        print line

    hor = hor.replace(".", "") 
    print hor[:-1]

def print_box3(l, w, h):
    full_width = l + 3 + w
    full_height = h + 2 + w
    push = 1 + w;


    for i in range(0, full_height):
        line =''
        for j in range(0, full_width):
            if i == 0:
                if j < push:
                    line += "."
                elif (j == push) or (j == full_width-1):
                    line += "+"
                else:
                    line += "-"
            elif i == full_height - 1 :
                if j == 0 or j == l + 1:
                    line += "+"
                elif j > l + 1:
                    line += "."
                else:
                    line += "-"
            else:
                line += "."
        print line







print_box3(4, 1, 2)
print "\nnextbox\n"
print_box3(5, 3, 4)
print "\nnextbox\n"
print_box3(8, 3, 3)
print "\nnextbox\n"
print_box3(1, 3, 7)
