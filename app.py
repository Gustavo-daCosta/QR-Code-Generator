'''
O código no geral está pronto, só tenho que arrumar uma maneira de mover os arquivos gerados para dentro de uma pasta
'''

from os import system, replace
from PIL import Image
import qrcode
import validators

def Menu(msg):
    tamanhomsg = len(msg) + 10
    print('-' * tamanhomsg)
    print(msg.center(tamanhomsg))
    print('-' * tamanhomsg)

counterLink = counterText = counterPhone = 0
while True:
    Menu('QR CODE GENERATOR')
    print('''[ 1 ] QR CODE => LINK
[ 2 ] QR CODE => TEXT
[ 3 ] QR CODE => WHATSAPP PHONE NUMBER
[ 4 ] EXIT''')
# [ 5 ] SELECT FILE TYPE
    while True:
        try:
            option = int(input('Select an option: '))
        except ValueError:
            print('ERROR! Try again.')
        finally:
            if 0 < option <= 5:
                system('cls')
                break
            else:
                print('ERROR! Invalid option, try again!')
    if option == 1:
        Menu('QR CODE => LINK')
        print("OBS: Don't forget the 'http://' or 'https://' in the URL.")
        while True:
            link = str(input('Paste the link here: '))
            if validators.url(link) is True:
                img = qrcode.make(link)
                if counterLink == 0:
                    file_name = "QRcodeLink.jpg"
                    img.save(file_name)
                break
            else:
                print('Invalid link! Try again.')
                input('Press ENTER to continue...')
                system('cls')
    elif option == 2:
        Menu('QR CODE => TEXT')
        while True:
            try:
                text = str(input('Type or paste the text: '))
                break
            except:
                print('ERROR! Please try again.')
        img = qrcode.make(text.strip())
        logo_display = Image.open('images\logo_text.png')
        logo_display.thumbnail((60, 60))
        logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
        img.paste(logo_display, logo_pos)
        file_name = "QRcodeText.jpg"
        img.save(file_name)
        #replace(src = file_name, dst = f'\QRcodeFiles\{file_name}')

    elif option == 3:
        Menu('QR CODE => WHATSAPP PHONE NUMBER')
        print("OBS: Type only numbers and don't forget about the country code!")
        while True:
            try:
                phoneNumber = int(input('Type or paste the phone number: '))
            except ValueError:
                print('ERROR! Invalid phone number, please try again.')
            finally:
                if 9 < len(str(phoneNumber)) <= 13:
                    img = qrcode.make(f"https://wa.me/+{phoneNumber}")
                    logo_display = Image.open('images\logo_whatsapp.png')
                    logo_display.thumbnail((60, 60))
                    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
                    img.paste(logo_display, logo_pos)
                    img.save("QRcodeWhatsApp.jpg")
                    break
                else:
                    print('Invalid Phone Number! Try again.')
                    input('Press ENTER to continue...')
                    system('cls')

    else:
        Menu("EXIT QR CODE GENERATOR")
        while True:
            option = str(input('Do you really want exit the program? [y/n]: '))
            if option.lower().strip() in "yesno":
                exit()
            else:
                pass