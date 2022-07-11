import os
import time
File = str(input("'.FJ' files\t"))
if os.path.splitext(File)[1] != '.FJ':
    print("File could not be opened or does not exist.")
    pass
else:
    if os.path.exists(File):
        time.sleep(0.5)
    else:
        print("File could not be opened or does not exist.")
        exit()
    f = open(File,"r")
    sf = f.readlines()
    final = []
    for line in sf:
        s = line.split()
        final.append(s)
    f.close()
    del(f)
    newfile = os.path.splitext(File)[0]
    pyf = newfile + ".py"
    nf = open(pyf,'w')
    nf.write("")
    nf.close()
    nf = open(pyf,'a')
    for i in final:
        for I in i:
            
            #add new syntax here        
            if I == 'out':
                nf.write('print ')
            elif I == 'equals':
                nf.write(' = ')
            elif I == ';':
                nf.write('\n')
            elif I == 'compare':
                nf.write('if ')
            elif I == 'NCompare':
                nf.write('elif ')
            elif I == 'FCompare':
                nf.write('else')
            elif I == 'skip':
                nf.write('pass')
            elif I == '~':
                nf.write('\t')
            elif I == '//':
                nf.write('#')
            else:
                nf.write(I+' ')
                
    
    nf.close()
    os.system('python3 ' + pyf)
    os.system('rm ' + pyf)
exit()
