Pratica 6 Sistemas Embarcados

Vitor Marques Delmondes (10820949) e André Vinicius (12547681)

Introdução às interfaces de visão computacional, sistemas de versionamento de arquivos e controle de acesso via tags.

Nesta prática utilizou-se o sistemas de versionamento git para implementar aplicações básicas envolvendo o leitor de tag RFID
e a camera da RaspberryPi. 

Para a tag RFID, escreveu-se dois scripts python distintos. O primeiro, "rfid.py", tem o propósito de testar a escrita de texto na tag
e também obter a sua ID. Com a ID em mãos, criou-se o script "controle_acesso.py" para simular um possível controle de acesso via tag:
aquelas que tiverem as ID cadastradas têm acesso liberado, enquanto as outras têm o seu acesso negado. Além de imprimir na tela as mensagens
de acesso concedido e negado, utilizou-se pinos da GPIO para acionar ou um led verde quando o acesso era permitido ou um led vermelho
caso contrário. O dispositivo de leitura da tag funciona através de comunicação SPI e foi conectada de acordo com as instruções da prática.
A montagem e o funcionamento do circuito podem ser vistas nas imagens ao fim deste arquivo.

Já para a parte da câmera, o hardware se mostrou um grande impecilho. A maioria das câmeras disponíveis não eram identificadas pela
RaspberryPi e as poucas que estavam funcionando não eram suficientes para atender toda a turma. Dito isso, ainda foi possível testar
o equipamento de outro grupo que conseguiu fazer a câmera funcionar. A prática consiste em implementar o algoritmo de machine learning Haar
Cascade para detectar faces de pessoas na imagem obtida através da câmera da RaspberryPi. Uma vez detectada a face, o script salva a imagem
da face reconhecida em um diretório especificado. O código pode ser visto no arquivo "camera.py" e as imagens são exibidas abaixo.


<img src="/imgs/circuit.jpg">

<img src="/imgs/controle_acesso.jpg">

<img src="/imgs/camera.jpg">
