import urllib.request
import os

def dl_jpe(url,number_jpe):
    for j in range (1,2):
            
            print('directorio '+dir(j))
            try:
                os.stat(dir(j))
            except:
                os.mkdir(dir(j))
            for i in range (1,number_jpe+1):
                number = str(linkes(i))
                full_path =  dir(j) + number 
                urli = url + dir(j) +  number 
                try:
                    urllib.request.urlretrieve(urli,full_path)
                    pass
                except :
                    i=number_jpe+1
                           
            
                print('path '+full_path+' link '+urli)


    

                
    
def linkes(number_i):
    i = str(number_i)
    if number_i<10:
        linkto =  '000' + i + '.jpg'
    elif number_i<100   :
        linkto =  '00' + i + '.jpg'
    else:
        linkto =  '0' + i + '.jpg'
    return(linkto)

def  dir(entrada):
    i = str(entrada)
    if entrada<10:
        lito =  '00' + i + '/'
    elif entrada<100:
        lito =  '0' + i + '/'
    else:
        lito = i
    return(lito)


dl_jpe('http://img.itmtu.com/mm/h/honghonghuohuodajiejie/NO..',200)
