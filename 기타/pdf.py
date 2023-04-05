from PyPDF2 import PdfMerger
import pikepdf
import os

def PdfEnc():
    nameEncrypt=list(input("(pdf암호화)파일 이름 입력\n").split())
    pwEncrypt = input("비밀번호설정")

    for e in nameEncrypt:
        e+='.pdf'
        rPdf = pikepdf.Pdf.open(e)
        
        no_extracting = pikepdf.Permissions(extract=False) #추출 못하게 막음

        e = os.path.splitext(e)[0] #확장자 빼고 분리
        e+= '_enc.pdf' #암호화파일 생성

        rPdf.save(e, encryption=pikepdf.Encryption(
            user = pwEncrypt, owner = pwEncrypt, allow = no_extracting))

#PdfEnc()

def PdfMerge():
    merger=PdfMerger()

    nameMerge=list(input("(pdf암호화)파일 이름 입력\n").split())
    
    for m in nameMerge:
        m+='.pdf'
        merger.append(m)#파일 병합

    m1 = nameMerge[0]
    m2 = nameMerge[-1]
    merger.write(m1+'~'+m2+'_merged.pdf') #병합파일 생성
    merger.close()
    
#PdfMerge()

hello=int(input("pdf암호화=1, pdf병합=2 입력\n"))

if hello==1:
    PdfEnc()
if hello==2:
    PdfMerge()




    
    
