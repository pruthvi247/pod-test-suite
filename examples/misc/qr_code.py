import qrcode
import qrcode.image.svg
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=25,
    border=4,
)
data = 'Peppermint. Uses: indigestion, nausea. Steep time: 5-10 mins.'
qr.add_data("https://play.google.com/store/apps/details?id=com.hoopinc.Hoop")
qr.make(fit=True)
factory = qrcode.image.svg.SvgImage

# img = qr.make_image(fill_color="black", back_color="white")
img = qr.make_image(fill_color="blue", back_color="white",image_factory=factory)
img.save('/Users/pruthvikumar/Documents/workspace/a1m/pod-test-suite/examples/misc/playstore_1.svg')