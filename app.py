import os
import sys
import time
import smtplib
from email.message import EmailMessage
from os import chdir 




# jpg count

while(1):
	while(1):
		files=os.listdir("./")
		count=0
		for file in files:
			if file.find("jpg")==-1:
				continue
			count=count+1
	
		if(count < 9):
			time.sleep(5)
			print("wait....")
			continue
		else:
			break
# CNN part
	chdir('/var/www/html/androidupload/uploads/ML/CNN/')
	os.system('python2.7 /var/www/html/androidupload/uploads/ML/CNN/convert.py')
	os.system('python2.7 /var/www/html/androidupload/uploads/ML/CNN/eval.py')

# checking precise
	chdir('/var/www/html/androidupload/uploads/ML/CNN/data/eval/smoker/')
	f=open("result.txt","r")
	precise=float(f.read())
	os.system('rm result.txt')
# if smoker
	if precise >= 50 :
		timestamp = str(time.time())
		os.system('mkdir ' + timestamp)
		os.system('mv ./*.jpg ' + timestamp)
		
		#send mail
		smtp_gmail = smtplib.SMTP('smtp.gmail.com',587)
		smtp_gmail.ehlo()
		smtp_gmail.starttls()
		smtp_gmail.login('ldj0635@gmail.com','Djfrnf08!@')

		msg=EmailMessage()
		msg['Subject']="smoker detected"
		msg.set_content("smoker!!! smoker!!!!")

		msg['From']='ldj0635@gmail.com'
		msg['To']='ldj0635@gmail.com'

		files=os.listdir("./"+timestamp)

		for file in files:
	
			fp=open("./"+timestamp+"/"+file,"rb")
			file_data=fp.read()
			msg.add_attachment(file_data,maintype='image',subtype='plain',filename=file)


		smtp_gmail.send_message(msg)
		print("a smoker is detected!, sended message to ldj0635@gmail.com")
		

	else:
		print("not a smoker")
		

	time.sleep(3)
	
	









