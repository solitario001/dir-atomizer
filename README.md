# dir-atomizer

Pequeno escript quê  vai mover a pasta de origem escolhida quando chegar a x tamanho para a pasta de destino, quando a pasta atingir novamente o x tamanho o script vai apagar a pasta movida antiga é mover a nova pasta de origem novamente.,
eu criei esse programa com o intuito de mover os vidéos gravados da camera de vigilancia para um novo local quando chegasse a tamnho x e quando chegasse novamente ao tamnho ele iria apagar os videos antigos pra mim, o tempo de apagar os videos antigos
é o tempo de chegar a x tamnho novamente , então se eu coloquei para mover os arquivos com 10GB quando a pasta atinger novamente os 10GB vai apagar os arquivos antigos automaticamente ^^


Requesitos:

python3.8.10 +

Install Pillow with pip Linux:

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade Pillow

Install Pillow with pip Windows:

    py -m pip install --upgrade pip
    py -m pip install --upgrade Pillow




![Captura de tela de 2023-08-17 17-41-38](https://github.com/solitario001/dir-atomizer/assets/36905390/2e069f79-9e48-4389-99d9-d299171e7dc1)



o script trabalha lendo 3 arquivos .txt src,dst,memory.

![Captura de tela de 2023-08-18 18-29-22](https://github.com/solitario001/dir-atomizer/assets/36905390/267fa9bd-4f9e-414d-b712-ba3465c2442f)

src.txt é onde fica salvo o caminho da pasta de origem quê vc quer mover.
![Captura de tela de 2023-08-17 17-47-11](https://github.com/solitario001/dir-atomizer/assets/36905390/72b2d87e-771e-4c20-9e8a-0c76231164a6)
![Captura de tela de 2023-08-18 18-40-33](https://github.com/solitario001/dir-atomizer/assets/36905390/c72fcb46-89b1-421a-af36-1ace7c7f7b0f)

dst.txt é para onde vai os arquivos movidos da pasta de origem do caminho src.txt.
![Captura de tela de 2023-08-17 17-48-51](https://github.com/solitario001/dir-atomizer/assets/36905390/2f82114b-f9d4-4926-b39d-55a5cfeb9892)
![Captura de tela de 2023-08-18 19-07-37](https://github.com/solitario001/dir-atomizer/assets/36905390/021081dc-88fc-45f5-b829-e3fe130754e4)

memory.txt aqui você salva a quantidade x de dados quê você quer mover a pasta, exemplo: se eu colocar 60gb toda vez que atingir 60gb vai mover a pasta., Atenção o programa funciona lendo a memoria em bytes não em Megabytes ou Gigabytes, então se eu quero quê ele move quando tiver 60gb eu preciso de colocar o dobro quê é 120gb e converter para 120000000000 Bytes 

![Captura de tela de 2023-08-17 17-43-26](https://github.com/solitario001/dir-atomizer/assets/36905390/7bf5e19c-000d-453e-a859-1ba556d9d8c3)
![Captura de tela de 2023-08-18 19-33-07](https://github.com/solitario001/dir-atomizer/assets/36905390/1469b164-86ba-4d6d-8021-cf9a4046b034)


o gui e totalmente opcional, serve apena para criar os caminhos e memoria .txt você mesmo pode criar esse arquivos com suas configurações,.

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


