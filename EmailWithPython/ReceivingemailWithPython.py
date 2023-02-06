
'''
Overview of Received Emails
Now that we understand how to send emails progammatically with Python,
let's explore how we can read and search recieved emails.
To do we will use the built-in imaplib library.
We will also use the built in email library for parsing through the recieved emails.
'''
import imaplib
#make connection to your imap gmail account
M = imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
user = input("Enter your email: ")
# Remember , you may need an app password if you are a gmail user
#
password = getpass.getpass("Enter your password: ")
#Enter your password: ········
M.login(user,password)
M.list()# wil give list of things to check
# ('OK',
#  [b'(\\HasNoChildren) "/" "INBOX"',
#   b'(\\HasNoChildren) "/" "Personal"',
#   b'(\\HasNoChildren) "/" "Receipts"',
#   b'(\\HasNoChildren) "/" "Sent"',
#   b'(\\HasNoChildren) "/" "Trash"',
#   b'(\\HasNoChildren) "/" "Travel"',
#   b'(\\HasNoChildren) "/" "Work"',
#   b'(\\HasChildren \\Noselect) "/" "[Gmail]"',
#   b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"',
#   b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"',
#   b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"',
#   b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"',
#   b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"',
#   b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"',
#   b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Trash"'])

# Connect to your inbox
M.select("inbox")



'''
Searching Mail
Now that we have connected to our mail, we should be able to search for it using the specialized syntax of IMAP.
 Here are the different search keys you can use:

<tr>
    <td>'BEFORE date'</td>
    <td>
    Returns all messages before the date. Date must be formatted as 01-Nov-2000.
    </td>
</tr>

 <tr>
    <td>'ON date'</td>
    <td>
    Returns all messages on the date. Date must be formatted as 01-Nov-2000.
    </td>
</tr>

 <tr>
    <td>'SINCE date'</td>
    <td>
    Returns all messages after the date. Date must be formatted as 01-Nov-2000.
    </td>
</tr>

<tr>
    <td>'FROM some_string '</td>
    <td>
    Returns all from the sender in the string. String can be an email, for example 
    'FROM               user@example.com' or just a string that may appear in the email, "FROM example"
    </td>
</tr>

<tr>
    <td>'TO some_string'</td>
    <td>
    Returns all outgoing email to the email in the string. String can be an email, 
    for example 'FROM user@example.com' or just a string that may appear in the email, "FROM example"
    </td>
</tr>

<tr>
    <td>'CC some_string' and/or 'BCC some_string'</td>
    <td>
    Returns all messages in your email folder. Often there are size limits from imaplib.
    To change these use imaplib._MAXLINE = 100 , where 100 is whatever you want the limit to be.
    </td>
</tr>

<tr>
    <td>'SUBJECT string','BODY string','TEXT "string with spaces"'</td>
    <td>
    Returns all messages with the subject string or the string in the body of the email.
     If the string you are searching for has spaces in it, wrap it in double quotes.
    </td>
</tr>

<tr>
    <td>'SEEN', 'UNSEEN'</td>
    <td>
    Returns all messages that have been seen or unseen. (Also known as read or unread)
    </td>
</tr>


    <tr>
    <td>'ANSWERED', 'UNANSWERED'</td>
    <td>
    Returns all messages that have been replied to or unreplied to. 
    </td>
</tr>


    <tr>
    <td>'DELETED', 'UNDELETED'</td>
    <td>
    Returns all messages that have been deleted or that have not been deleted.
    </td>
</tr>


Keyword	Definition
'ALL'	Returns all messages in your email folder. Often there are size limits from imaplib.
To change these use imaplib._MAXLINE = 100 , where 100 is whatever you want the limit to be.
You can also use the logical operators AND and OR to combine the above statements. 
Check out the full list of search keys here: http://www.4d.com/docs/CMU/CMU88864.HTM.

Please note that some IMAP server providers for different email services will have slightly different syntax.
 You may need to experiment to get the results you want.

Now we can search our mail for any term we want.
'''
# Use if you get an error saying limit was reached
imaplib._MAXLINE = 10000000

# Send yourself a test email with the subject line:
# this is a test email for python
# Or some other uniquely identifying string.
# We will now need to reconnect to our imap server.
# You will probably need to restart your kernel for this step if you are using jupyter notebook.

# Restart your kernel and run the following:
import imaplib
import getpass
M = imaplib.IMAP4_SSL('imap.gmail.com')
user = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
M.login(user,password)

# Connect to your inbox
M.select("inbox")

#Let's now search and confirm if it is there:# search by subject
typ ,data = M.search(None,'SUBJECT "this is a test email for python"')
#We can now save what it has returned:
typ #ok
#if there is more  than a list then it means it found more than one result
#data is the unique id of the list of data
data # [b'28493']
#The data will be a list of unique ids.

# typ, data = M.fetch(data[0],"(RFC822)")
result, email_data = M.fetch(data[0],"(RFC822)")
#
raw_email = email_data[0][1]
#we need to decode to utf-8 if there are some special symbol that make python not able to read
raw_email_string = raw_email.decode('utf-8')
#We can use the built in email library to help parse this raw string.

import email
email_message = email.message_from_string(raw_email_string)
#for every part of email in email.walk
for part in email_message.walk():
    #if part content is equal to plain text  blabla
    if part.get_content_type() == "text/plain":
        #decode it and
        body = part.get_payload(decode=True)
        #print it
        print(body)

#b'This is a test to see if the python search worked.\r\n'