from time import sleep
from shutil import rmtree
from shutil import copytree
from os import mkdir
import os

loop = 1
while loop == 1:

    
    try:
      if os.path.exists('/home/messias/k8/'):#ao iniciar o programa verifica se tem a pasta
        
          print('tem pasta')
      else:#se não tiver a pasta ele cria uma nova pasta 
          print('não tem pasta')
          mkdir('/home/messias/k8')
          
    except OSError:
       print()
                
    
    try:
      if os.path.exists('/home/messias/k9/'):#ao iniciar o programa verifica se tem a pasta
        
          print('tem pasta')
      else:#se não tiver a pasta ele cria uma nova pasta   
          print('não tem pasta')
          mkdir('/home/messias/k9')
          
    except OSError:
       print()
    
    
    Pasta1 = 0#rebe o valor de todos os arquivos dentro da pata
    folderpath = "/home/messias/k8"#caminho da pasta para verificar o tamanho dos arquivos

    for path, dirs, files in os.walk(folderpath):#os.walk vai listar todos os arquivos,caminhos,diretorios o escolhido diretorio
        for f in files: #para arquivos dentro pasta listada por os.walk
            fp = os.path.join(path, f)#join pega a string de arquivos feita por os.walk e transforma em lista
            Pasta1 += os.path.getsize(fp)#aqui pega a lista de arquivos feita por join e soma seu valor + pasta1
    
    
    
    if Pasta1 > 43104879:#se a pasta1 tiver um valor maior quê o indicado
      print('hora de copiar a pasta')
      rmtree('/home/messias/k9/')#apaga a pasta antiga do backup anterior
      copytree('/home/messias/k8','/home/messias/k9')#copia toda a pasta para uma nova pasta
      rmtree('/home/messias/k8/')#apaga a pasta pois já foi feito um backup dela
      mkdir('/home/messias/k8') #cria uma nova pasta
      sleep(60)
    else:
       print('Hora de Dormir')
       sleep(60)
   
  
    
    