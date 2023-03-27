import pikepdf
import os

def PdfEnc():
    nameEncrypt=str(input("파일 이름 입력ex)TestWr\n"))
    nameEncrypt+='.pdf'
    pwEncrypt = input("비밀번호설정")

    rPdf = pikepdf.Pdf.open(nameEncrypt)

    no_extracting = pikepdf.Permissions(extract=False)

    nameEncrypt = os.path.splitext(nameEncrypt)[0]
    nameEncrypt += '_enc.pdf'

    rPdf.save(nameEncrypt, encryption=pikepdf.Encryption(
        user = pwEncrypt, owner = pwEncrypt, allow = no_extracting))

PdfEnc()
