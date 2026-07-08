import qrcode

phone_number = "tel:+917671066717"

img = qrcode.make(phone_number)

img.save("mobile_qr.png")

print("✅ Mobile Number QR Code Generated Successfully!")