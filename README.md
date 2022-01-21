
# QR Code Generator

Um gerador de QR Code, escrito em python utilizando a biblioteca [qrcode](https://pypi.org/project/qrcode/)


## Funcionalidades

- [X]  Gerar um QR Code que redireciona o usuário para um link
- [X]  Gerar um QR Code que mostra um texto para o usuário
- [X]  Gerar um     QR Code que redireciona o usuário para o aplicativo do whatsapp, com o objetivo de adicionar um novo contato.
- [X]  Adicionar icones aos QR Code gerados (ainda falta no QR Code do link)
- [ ]  Manipulamento dos arquivos gerados
- [ ]  QR Code com cores e logos personalizadas para compartilhamento de redes sociais
- [ ]  Implementar o gerador ao meu bot do discord
- [ ]  Fazer uma interface gráfica do gerador com a biblioteca Tkinter


## Uso/Exemplos

Quando o programa for executado ele vai gerar o seguinte menu:

```
---------------------------
     QR CODE GENERATOR
---------------------------
[ 1 ] QR CODE => LINK
[ 2 ] QR CODE => TEXT
[ 3 ] QR CODE => WHATSAPP PHONE NUMBER
[ 4 ] EXIT
Select an option:
```
A partir disso o usuário vai selecionar uma opção, e supondo que ele selecione a opção 1 (QR CODE => LINK) o programa vai limpar o terminal e gerar um segundo menu:
```
-------------------------
     QR CODE => LINK     
-------------------------
OBS: Don't forget the 'http://' or 'https://' in the URL.
Paste the link here:
```
E então o usuário vai digitar ou colar o link no input e o programa vai gerar o QR Code
[![QRcode-Link.png](https://i.postimg.cc/JnBVmq6V/QRcode-Link.png)](https://postimg.cc/jwKk4zYZ)


