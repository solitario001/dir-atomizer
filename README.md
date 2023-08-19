# dir-atomizer

Small script that will move the chosen source folder when it reaches x size to the destination folder, when the folder reaches x size again the script will delete the old moved folder and move the new source folder again.,
I created this program in order to move the recorded videos from the surveillance camera to a new location when it reached size x and when it reached size again it would delete the old videos for me. the time to delete the old videos it 's time to reach x size again , so if I move the files with 10GB when the folder reaches 10GB again , it will delete the old files automatically


Requirements:

python3.8.10 +

Install Pillow with pip Linux:

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade Pillow

Install Pillow with pip Windows:

    py -m pip install --upgrade pip
    py -m pip install --upgrade Pillow




![Captura de tela de 2023-08-17 17-41-38](https://github.com/solitario001/dir-atomizer/assets/36905390/2e069f79-9e48-4389-99d9-d299171e7dc1)



the script works by reading 3 .txt files src,dst,memory.

![Captura de tela de 2023-08-18 18-29-22](https://github.com/solitario001/dir-atomizer/assets/36905390/267fa9bd-4f9e-414d-b712-ba3465c2442f)

src.txt is where the path of the source folder you want to move is saved.
![Captura de tela de 2023-08-17 17-47-11](https://github.com/solitario001/dir-atomizer/assets/36905390/72b2d87e-771e-4c20-9e8a-0c76231164a6)
![Captura de tela de 2023-08-18 18-40-33](https://github.com/solitario001/dir-atomizer/assets/36905390/c72fcb46-89b1-421a-af36-1ace7c7f7b0f)

dst.txt is where files moved from the src.txt path's source folder go.
![Captura de tela de 2023-08-17 17-48-51](https://github.com/solitario001/dir-atomizer/assets/36905390/2f82114b-f9d4-4926-b39d-55a5cfeb9892)
![Captura de tela de 2023-08-18 19-07-37](https://github.com/solitario001/dir-atomizer/assets/36905390/021081dc-88fc-45f5-b829-e3fe130754e4)

memory.txt here you save the x amount of data you want to move the folder, example: if I put 60gb every time I reach 60gb it will move the folder. Attention the program works by reading the memory in bytes not in Megabytes or Gigabytes, so if I want it to move when it reach 60gb I need to put twice as much which is 120gb and convert it to 120000000000 Bytes
![Captura de tela de 2023-08-17 17-43-26](https://github.com/solitario001/dir-atomizer/assets/36905390/7bf5e19c-000d-453e-a859-1ba556d9d8c3)
![Captura de tela de 2023-08-18 19-33-07](https://github.com/solitario001/dir-atomizer/assets/36905390/1469b164-86ba-4d6d-8021-cf9a4046b034)


the gui is completely optional, it only serves to create the paths and memory .txt you can create these files yourself with your settings,.

o gui vai variar os botões conforme a versão do windows, preciso criar uma versão separada para cada versão de sistema operacional para evitar discrepância no layout do gui.

o script vai rodar em modo furtivo, você só vai conseguir visualizar ele no gerenciador de tarefas,se ele dar erro vai fechar silenciosamente não vai ter nenhum avizo sonoro ou visual de funcionamento, porquê eu não queria quê ele ficasse a vista de olhos curiosos enquanto esta em execução e também não incomodar o usuario final pois ele não minimiza para o tray .

![Sem título](https://github.com/solitario001/dir-atomizer/assets/36905390/11504856-15d4-4745-8ac7-4c90d92d859f)


Atenção> Usuarios Windows:

o script não vai mover a pasta ou apagar se tiver um arquivo aberto dentro da pasta.... ele vai dar erro "WinError 5" pois o windows não permite apagar ou mover arquivos enquanto eles estão abertos

![Captura de tela de 2023-08-09 15-12-58](https://github.com/solitario001/dir-atomizer/assets/36905390/3a08922a-b5b0-4464-8a21-e496c5d64232)
![Opera Snapshot_2023-08-09_160538_stackoverflow com](https://github.com/solitario001/dir-atomizer/assets/36905390/0a52695c-967b-4c03-9e1b-df8fbbddf2f3)

não inicie o script antes de configurar os caminhos e memoria ou ele vai dar erro "WinError 3"fazendo isso com ele aberto... isso não acontece no Linux, esse erro acontece no windows quando você configura primeiro a memoria antes dos caminhos de origem e destino... preciso de mais pesquisa para concertar isso.

![WinError 3](https://github.com/solitario001/dir-atomizer/assets/36905390/f19a8ec8-9261-44a9-a03f-2edcafb13c4d)


Demonstração de Funcionamento

aqui quero quê move a pasta toda vez quê atingir 60gb então se eu quero quê ele move quando tiver 60gb eu preciso de colocar o dobro quê é 120gb e converter para 120000000000 Bytes porquê o script só faz leitura de memoria como bytes, 120000000000 Bytes para o script é 60gb., video abaixo monstrando o funcionamento do script. 

[![Watch the video](https://img.youtube.com/vi/NltIs4245Gg/maxresdefault.jpg)](https://youtu.be/NltIs4245Gg)


