import qrcode

# qr = qrcode.make('Hello world');

# qr.save('myQr.png')

def inputToGetQrCode():
    stringInput = input("Input here 11 character: ")
    stringLength = len(stringInput)
    if(stringLength != 11):
        stringInput = input("Input here exact 11 character: ")
    qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=0)
    qr.add_data(stringInput)
    qr.make(fit=True)
    output = qr.make_image(fill_color ="black", back_color = "white")
    outputPng = f"{stringInput}.png"
    output.save(outputPng)
inputToGetQrCode()