import asyncio
import smtplib

async def send_mail(subject, body, to):
    content = "Hello world ..."
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender = "sender@gamil.com"
    recipient = "recipient@gmail.com"
    mail.login("sender@gmail.com", 'nsncdnc')
    header = "To: "+ recipient + '\n' + "From: " + sender + '\n' + 'subject: testmail\n'
    content = header + content
    mail.sendmail(sender, recipient, content)
    mail.close()

async def main():
    asyncio.create_task(send_mail("Test mail", "This is a test mail", "vinayakkanchan03@gamil.com"))
    
    print("doing other task")
    
    
asyncio.run(main())