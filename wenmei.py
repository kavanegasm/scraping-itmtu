import urllib.request
import os

def dl_jpe(url,number_jpe):
    for j in range (33,34):
            
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
                            #path 002/0032.jpg link http://img.itmtu.com/mm/w/wenmei/NO.0032.jpg
                            #                       http://img.itmtu.com/mm/w/wenmei/NO.008/0001.jpg
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

#dl_jpe('http://img.itmtu.com/mm/w/sandaodaomiido/NO.',1000)
dl_jpe('http://img.itmtu.com/mm/w/wenmei/NO.',200)
