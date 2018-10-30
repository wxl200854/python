import qrcode
def makeQrCode(data):
	qr = qrcode.QRCode(
		version = 1,
		error_correction = qrcode.constants.ERROR_CORRECT_L,
		box_size = 10,
		border = 4,
	)
	qr.add_data(data)
	qr.make(fit=True)
	img = qr.make_image()
	img.save(r'E:\study\python\pythontest\python\test\123.png')

if __name__== "__main__":
	makeQrCode('http://www.baidu.com')