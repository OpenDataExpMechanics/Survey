# Script for sending the second mail 
#
# Configuration
# - config.yaml.example for the smtp connection
# - text.dat.example for the e-mail's text
#   The tags inside < > are replaced with the values
#   of the corresponding attributes in the bibtex
#   file
#
# @author Open Data in Experimental Mechanics

# Packages
import csv
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import yaml, codecs
import sys  
import bibtexparser
####

# Activate utf8 encoding
reload(sys)  
sys.setdefaultencoding('utf8')

# Open the template text of the e-mail
file = open("text.dat.example",'r')
plainText = file.read()

# Configuraton of the smtp connection
username= ""
server= ""
password= ""
port = -1
address = ""
subject = ""

print "Starting e-mail sending script"

# Loading the configuration from the yaml file
with open("config.yaml.example",'r') as f:
    doc = yaml.load(f)
    username = doc["Mail"]["user"]
    server = doc["Mail"]["server"]
    password = doc["Mail"]["pw"]
    port = int(doc["Mail"]["port"])
    address = doc["Mail"]["address"]
    subject = doc["Mail"]["subject"]
    print "Loading config data for", username, server, port

# Start the connection to the server    
server = smtplib.SMTP(server, port)
server.starttls()
server.login(username, password)

# Send mails
with open('second.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
        if len(row[3]) == 0 or len(row[4]) == 0:
        
        	name = ""
        	with open("../data/"+row[0]+".bib") as bibtex_file:
        		bibtex_str = bibtex_file.read()
        		bib_database = bibtexparser.loads(bibtex_str)
        		for k, entry in enumerate(bib_database.entries):
        			if entry['author-email'] == row[1]:
        				name = entry['author-name']
        	
                customText = plainText.replace("<author>",name.encode("utf8"))
                customText = customText.replace("<title>",row[2].encode("utf8"))
                customText = customText.replace("<year>",row[0].encode("utf8"))
		customSubject = subject.replace("<year>",row[0].encode("utf8"))
		customSubject = customSubject.replace("<title>",row[2].encode("utf8"))
	    
		print customText
		to = row[1]
		cc = ""
		bcc = "patrick.diehl@polymtl.ca"
		rcpt = cc.split(",") + bcc.split(",") + [to]
                msg = MIMEMultipart("alternative")
                msg['From'] = address
                msg['To'] = to
                msg['Subject'] = customSubject
		msg['Bcc'] = bcc

                msg.attach(MIMEText(customText.encode("utf-8"), 'plain', "utf8"))
             
                text = msg.as_string()
		
		server.sendmail(address, rcpt, text)
		print "E-mail sent to " , to
		
            
# Close the connection
server.quit()


