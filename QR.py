import qrcode
import cv2
from pyzbar.pyzbar import decode

def createQR(string):
    qr = qrcode.QRCode(
    version=1,  #
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4 
    )
    qr.add_data(string)
    qr.make(fit=True)
    imagen_qr = qr.make_image(fill='black', back_color='white')
    imagen_qr.save("QR"+string+".png")
    return "QR"+string+".png"

def scanQR(root):
    imagen_qr = cv2.imread(root)
    decodificado = decode(imagen_qr)
    string = ""
    for obj in decodificado:
        string += obj.data.decode('utf-8')
    return string
