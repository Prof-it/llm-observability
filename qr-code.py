import qrcode

def main():
    # vCard formatted data
    vcard_data = """
    BEGIN:VCARD
    VERSION:3.0
    FN:Tianxiang Lu
    ORG:IU International University of Applied Sciences;IT & Technology
    TITLE:Professor Dr.rer.nat.
    ADR:;;Juri-Gagarin-Ring 152;Erfurt;;99084;Germany
    EMAIL:Tianxiang.lu@iu.org
    EMAIL:onyinye.suche@gmail.com
    URL:https://orcid.org/0009-0006-4462-1636
    URL:https://orcid.org/0009-0002-8027-7343
    URL:https://www.iu.de/hochschule/lehrende/lu-tianxiang/
    URL:https://www.researchgate.net/profile/Tianxiang-Lu-3
    URL:https://www.linkedin.com/in/dr-rer-nat-tianxiang-lu
    NOTE:First author Onyinye S. Uche acknowledged
    X-GITHUB-REPO:https://github.com/Prof-it/llm-observability
    END:VCARD
    """

    # Generate QR code
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    file_path = "./contact_vcard_qr.png"
    img.save(file_path)
    print(f"QR code saved to {file_path}")

if __name__ == "__main__":
    main()