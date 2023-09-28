
import rsa 
pub_key=int(input("Write the PublicKey: "))
text=input("\n[*] Write the text:\n\n[text] >> ")
message=text.encode("utf8")
crypt=rsa.encrypt(message,rsa.PublicKey(pub_key,65537))
with open("text_crypt.txt","wb") as w:
	w.write(crypt)
	print("\n[*] Crypt-text:\n\n"+str(crypt)+"\n\n[+] File: 'text_crypt.txt' successfully saved!\n")
