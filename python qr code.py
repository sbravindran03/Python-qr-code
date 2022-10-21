import  pyqrcode
url = 'https://www.linkedin.com/in/ravindran-s-b-51b54a243'
k = pyqrcode.create(url)
k.svg('Qr.svg,scale=10')