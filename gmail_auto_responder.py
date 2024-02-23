import base64
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
import time
from email.mime.text import MIMEText
import ai_assistant

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def gmail_authenticate():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(r'C:\Users\smaye\OneDrive\Serge\python\Byob AI email responder\client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def create_message(sender, to, subject, received_message):
    # AI generated response
    message_text = ai_assistant.generate_response(received_message)
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(f'An error occurred: {error}')

def check_emails(service):
    # Check the inbox
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
    messages = results.get('messages', [])

    if not messages:
        print("No new emails found.")
    else:
        print("New emails found. Sending responses...")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
            sender = ""
            for header in msg['payload']['headers']:
                if header['name'] == "From":
                    sender = header['value']

            # Extracting and decoding the message body
            try:
                message_body = msg['payload']['parts'][0]['body']['data']
                decoded_body = base64.urlsafe_b64decode(message_body).decode('utf-8')
            except Exception as e:
                print(f"Error decoding message: {e}")
                decoded_body = "[Message body could not be decoded]"

            print(f"From: {sender}")
            print(f"Message: {decoded_body}\n")

            if sender:
                response_message = create_message("me", sender, "Re: Automated Response", decoded_body)
                send_message(service, 'me', response_message)
                service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()

def main():
    service = gmail_authenticate()
    while True:
        check_emails(service)
        print(f"Checked emails at {datetime.datetime.now()}. Waiting for next check...")
        time.sleep(600)  # Wait for 10 minutes

if __name__ == '__main__':
    main()
