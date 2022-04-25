import qrcode
img = qrcode.make("https://github.com/shashacode")
img.save("GithubQR.jpg")

#to detect the information in the qrcode
import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("GithubQR.jpg"))
print("Decoded information is:", val)