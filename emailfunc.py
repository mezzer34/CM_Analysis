import imaplib
import base64
import os
import email


def doGetMail():
    #Loginto burner email test account    
    email_user, email_password = doGetEmailFromFile()

    mail = imaplib.IMAP4_SSL("outlook.office365.com", 993)

    mail.login(email_user, email_password)

    mail.select("inbox")


    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()


    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
        
        
        #convert byte literal to string removing b''
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)# downloading attachments
        for part in email_message.walk():
            # this part comes from the snipped I don't understand yet... 
            if part.get_content_maintype() == 'multipart':
                continue
            
            if part.get('Content-Disposition') is None:
                continue
            
            fileName = part.get_filename()        
            
            if bool(fileName):
                filePath = os.path.join("./Emails/", fileName)
                if not os.path.isfile(filePath) :
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()            
                    subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                    if subject == "":
                        subject = "No Subject"
                print('Downloaded "{file}" from email titled'.format(file=fileName))
                
               
    #Return true when mail has been collected 
    return True



def doGetEmailFromFile():
    #Stores the email and password in a local text file that is added to the .gitignore
    #USE A BURNER ACCOUNT!!
    
    f = open("./UserInfo/email.txt", "r")
    email_user = f.readline().strip()
    email_password = f.readline().strip()   
    
    
    
    
    return email_user, email_password