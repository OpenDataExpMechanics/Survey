# Script for reading the bibtex entries, replacing the
# tags in the template text, and sending the mails to
# the author
#
# Configuration
# - config.yaml.example for the smtp connection
# - text.dat.example for the e-mail's text
#   The tags inside < > are replaced with the values
#   of the corresponding attributes in the bibtex
#   file 
#
# @author Open Data in Experimental Mechanics

# packages
import bibtexparser
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import yaml, codecs
import sys  
####

# Activate the utf8 encoding 
reload(sys)  
sys.setdefaultencoding('utf8')

# read the template text for the mail's content
file = open("text.dat",'r')
plainText = file.read()

# Setting for the smtp connection
username= ""
server= ""
password= ""
port = -1
address = ""
subject = ""

print "Starting e-mail sending script"

# Read the yaml file with the configuration
# for the connection to the smtp server
with open("config.yaml",'r') as f:
    doc = yaml.load(f)
    username = doc["Mail"]["user"]
    server = doc["Mail"]["server"]
    password = doc["Mail"]["pw"]
    port = int(doc["Mail"]["port"])
    address = doc["Mail"]["address"]
    subject = doc["Mail"]["subject"]
    print "Loading config data for", username, server, port
    
# Connect to the mail server
server = smtplib.SMTP(server, port)
server.starttls()
server.login(username, password)

# read the data from the bibtex file, replace the values in the
# template text and send e-mail to the author
data = []
key = ["author","year", "title","author-email","author-name", "data"]
values = []
for i in range(2013,2014):
    print i
    with open("../data/"+"extra"+".bib") as bibtex_file:
    #with open("../data/"+str(i)+".bib") as bibtex_file:
    #with open("./"+str(i)+"_test"+".bib") as bibtex_file:
	print "Opened file", "./"+str(i)+"_test"+".bib"
        bibtex_str = bibtex_file.read()

        bib_database = bibtexparser.loads(bibtex_str)
        #k = 0
        for k, entry in enumerate(bib_database.entries):
	    print "Loading entry", k
            if k >= 11:
                # Skip all entries scanned if we have
                # already processed 10 entries as only
                # the first ten entries are used for this work
                continue
            values.append(entry['author'])
            values.append(entry['year'])
            values.append(entry['title'])
            if 'author-email' in entry.keys():
                values.append(entry['author-email'])
                if entry[ 'author-email' ] == "N/A":	
		    print "Author email not found."
		    data.append([])
                    continue
            else:
                values.append("None")
            if 'author-name' in entry.keys():
		print entry['author-name']
                values.append(entry['author-name'])
            else:
                values.append("None")
                
            if 'data' in entry.keys():
                values.append(entry['data'])
            else:
                values.append("None")

            data.append(dict( zip( key, values)))
            values = []
	    
            if data[k][ 'author-name' ] == 'None':
                continue
            else:
		print "Found author-name tag"
                customText = plainText.replace("<author>",data[k]['author-name'].encode("utf8"))
                customText = customText.replace("<title>",data[k]['title'].encode("utf8"))
                customText = customText.replace("<year>",data[k]['year'].encode("utf8"))
		customSubject = subject.replace("<year>",data[k]['year'].encode("utf8"))
		customSubject = customSubject.replace("<title>",data[k]['title'].encode("utf8"))
	    
		to = data[k]['author-email']
		cc = ""
		bcc = ""

		rcpt = cc.split(",") + bcc.split(",") + [to]
                msg = MIMEMultipart("alternative")
                msg['From'] = address
                msg['To'] = to
                msg['Subject'] = customSubject
		msg['Bcc'] = bcc

                msg.attach(MIMEText(customText.encode("utf-8"), 'plain', "utf8"))
                print data[k]['author-email']
		print customSubject
		#print customText
                text = msg.as_string()
		if data[k]['author-email'] == "N/A":
		    print "Ignoring this entry, no author-email tag"
		    pass
		else:
		    print "Loading config data for", address, data[k]['author-email']
		    server.sendmail(address, rcpt, text)
		    print "E-mail sent"
		    print
            
# Close the connection
server.quit()


