#! /usr/bin/env python3

import requests, sys, datetime, smtplib, os, getpass
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep

now = datetime.datetime.now()

##############################################################################

# To extract content from a URL
def extract_content(url):
    page = requests.get(url)
    new_page = ''
    new_page += ('<b> HackerNews Top 30 Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    content = BeautifulSoup(page.content, 'html.parser')
    soup = content.find_all('td',attrs={'class':'title', 'valign':''})
    for i,tag in enumerate(soup):
        if tag.text != "More":
            new_page += (str(i+1) + ". " + tag.text + "\n" + "<br>")
    return(new_page)

##############################################################################

# Sending an email via gmail SMTP
def send_email():
    smtp_server = 'smtp.gmail.com' # Using gmail's services
    port = 587 # Port number for email (TLS)
    sender_email = input("\nEnter the following email information\nFrom: ")
    receiver_email = input("To: ")
    password = getpass.getpass(prompt = "Enter your email password: ")

    # To create a message
    message = MIMEMultipart()
    message['Subject'] = 'Top 30 News Stories from Hacker News [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
    message['From'] = sender_email
    message['To'] = receiver_email
    message.attach(MIMEText(extract_content(url), 'html'))

    print('Sending email...')

    # Configuring and starting server

    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

    print('Email has been sent successfully...')

    server.quit
    
##############################################################################

# Writing content onto a file
def writing_file(url):
    with open('URLContent.txt', 'w') as file:
        file.write(str(extract_content(url)))

##############################################################################

# Program starts and keeps running until user quits
while True:
    print("============================================\nWelcome to URL scraper\n============================================ \n1) Extract content and send to email\n2) Extract content and save to file.\n\nChoose 1 or 2 (Press enter to quit)")
    user = input()
    # User picks to extract content to send to email
    if user == "1":
        url = input('Enter the URL you would like to extract:\n')
        print("Extracting URL's content...")  
        extract_content(url)
        send_email()
        sys.exit()
    # User picks to extract content to save to local file
    elif user == "2":
        url = input("Enter the URL you would like to extract:\n")
        # Validates that the URL is an actual URL
        if ("http" or "https" or "www") not in url:
            print("\nIncorrect URL link. Try again\n")
            continue
        else:
            print("\nExtracting URL's content and saving to file...")
            extract_content(url)
            writing_file(url)
            sleep(1)
            print(f'File is saved in {os.getcwd()}\n')
            print("Would you like to view the content? Y/N")
            view_input = input()
            view_input = view_input.lower()
            if view_input == "y":
                with open('URLContent.txt', 'r') as file:
                    print(file.read(), "\n")
            elif view_input == "n":
                print()
                continue
    else:
        print("Exiting...")
        sys.exit()

#############################################################################
