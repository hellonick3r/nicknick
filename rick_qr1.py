import qrcode
data = 'https://youtu.be/xvFZjo5PgG0'
qr = qrcode.QRCode(version= 1 , box_size=10 , border= 2)
qr.add_data(data)
qr.make(fit = True)

pic = qr.make_image(fill_color = 'green', back_color = 'black' )
pic.save('rick.png')