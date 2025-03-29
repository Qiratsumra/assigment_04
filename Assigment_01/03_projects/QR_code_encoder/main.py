import qrcode

qr_img= qrcode.make('https://github.com/panaversity')
qr_img.save('panaversity.png')