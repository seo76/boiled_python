def makeCodebook():
	decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m',  '*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' ' }
	#암호화 딕셔너리	
	encbook = { } 
	for k in decbook:
		val = decbook[k] #decbook의 value값을 k로 읽어 val변수에 집어넣는다.
		encbook[val] = k #val에 들어간 decbook의 value값을 encbook의 key값으로 적용하고, decbook의 key값인 k는 encbook의 value값으로 적용한다.

	return encbook, decbook


def encrypt(msg, encbook):
	for c in msg:
		if c in encbook: #encbook의 key값 중 msg텍스트 중 일치하는 글자가 있다면
			msg = msg.replace(c, encbook[c]) #상응하는 encbook의 value값으로 변경한다.(=decbook딕셔너리의 key값)
			
	return  msg


def decrypt(msg, decbook):
	for c in msg:
		if c in decbook: #decbook의 key값 중 msg텍스트 중 일치하는 글자가 있다면
			msg = msg.replace(c, decbook[c]) #상응하는 decbook의 value값으로 변경한다.
			
	return msg


if __name__ == '__main__': 
	plaintext = 'I love you with all my heart' #메세지에 들어가는 텍스트
	
	encbook, decbook = makeCodebook() #makeCodebook함수에 encbook, decbook변수는 makeCodebook함수에서 적용가능
	ciphertext = encrypt(plaintext, encbook) #encrypt함수에 plaintext를 msg로, encbook은 makeCodebook함수에서 적용되는 방식으로  취급한다.
	print (ciphertext)

	deciphertext = decrypt(ciphertext, decbook)#decrypt함수에 plaintext를 msg로 decbook은 makeCodebook함수에서 적용되는 방식으로 취급한다.
	print (deciphertext)
