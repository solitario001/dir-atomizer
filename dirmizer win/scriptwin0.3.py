from time import sleep
from shutil import rmtree
from os import mkdir
from shutil import move
import os
import os.path







loop = 1
while loop == 1:
    
    store = []
    Pasta1 = 0#rebe o valor de todos os arquivos dentro da pata
    
    if os.path.isfile('src.txt'):
        with open ('src.txt','r') as origin:
          src = origin.readline()
          if os.path.isdir(src): 
             for path, dirs, files in os.walk(src):#os.walk vai listar todos os arquivos,caminhos,diretorios o escolhido diretorio
                for f in files: #para arquivos dentro pasta listada por os.walk
                   fp = os.path.join(path, f)#join pega a string de arquivos feita por os.walk e transforma em lista
                   Pasta1 += os.path.getsize(fp)#aqui pega a lista de arquivos feita por join e soma seu valor + pasta1
    else:
       sleep(1)
    
    
    
    if os.path.isfile('dst.txt'):
       with open ('dst.txt','r') as destiny:
        dst = destiny.readline()
    else:
       sleep(1)
   
    
    
    if os.path.exists('memory.txt'):
         if os.stat('memory.txt').st_size > 0:
            if os.path.exists('src.txt'):
               if os.stat('src.txt').st_size > 0:
                  for path, dirs, files in os.walk(src):#os.walk vai listar todos os arquivos,caminhos,diretorios o escolhido diretorio
                      for f in files: #para arquivos dentro pasta listada por os.walk
                        fp = os.path.join(path, f)#join pega a string de arquivos feita por os.walk e transforma em lista
                        Pasta1 += os.path.getsize(fp)#aqui pega a lista de arquivos feita por join e soma seu valor + pasta1
                  else:
                   sleep(1)
         
    
  
    if os.path.exists('memory.txt'):     
        if os.path.exists('src.txt'):
            if os.stat('src.txt').st_size > 0: 
               if os.path.exists('dst.txt'):
                  if os.stat('dst.txt').st_size > 0: 
                     if os.stat('memory.txt').st_size > 0:  
                      with open ('memory.txt') as memory:
                       folder = memory.readlines()
                       store.append(folder[0])
                      if Pasta1 > int(folder[0]):#se a pasta1 tiver um valor maior quê o indicado
                           rmtree(dst)
                           move(src,dst)
                           mkdir(src)
                           sleep(1)
                      else:
                         sleep(1)
    
    
    
      
      

    
      

                         
   
      
