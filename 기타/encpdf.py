from PyPDF2 import PdfMerger
import pikepdf
import os

def PdfEnc():
    nameEncrypt=str(input("(pdf암호화)파일 이름 입력\n"))
    nameEncrypt+='.pdf'
    pwEncrypt = input("비밀번호설정")

    rPdf = pikepdf.Pdf.open(nameEncrypt)

    no_extracting = pikepdf.Permissions(extract=False)

    nameEncrypt = os.path.splitext(nameEncrypt)[0]
    nameEncrypt += '_enc.pdf'

    rPdf.save(nameEncrypt, encryption=pikepdf.Encryption(
        user = pwEncrypt, owner = pwEncrypt+'123', allow = no_extracting))

#PdfEnc()

def PdfMerge():
    merger=PdfMerger()

    nameMerge=list(input("(pdf암호화)파일 이름 입력\n").split())
    
    for m in nameMerge:
        m+='.pdf'
        merger.append(m)

    merger.write('merged.pdf')
    merger.close()
    
#PdfMerge()

hello=int(input("pdf암호화=1, pdf병합=2 입력\n"))

if hello==1:
    PdfEnc()
if hello==2:
    PdfMerge()




    
    
