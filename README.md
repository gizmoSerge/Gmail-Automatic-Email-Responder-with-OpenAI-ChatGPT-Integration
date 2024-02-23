
# Gmail Automatic Email Responder with OpenAI ChatGPT Integration

## Description
This project integrates the latest OpenAI Assistant, currently in beta, with Gmail, enabling automated, intelligent email responses. It comprises two key components:

1. **AI Assistant (`ai_assistant.py`)**: This script interacts with the beta version of OpenAI's new assistant to generate contextually relevant responses based on email content. It facilitates communication with OpenAI's service for advanced response generation.

2. **Gmail Auto Responder (`gmail_auto_responder.py`)**: This script connects with the Gmail API to monitor incoming emails and uses the AI Assistant to create responses. It manages all email-related activities, including reading and responding to emails.

## Key Features
- **Integration with OpenAI's Latest Assistant (Beta)**: Utilizes the new assistant feature from OpenAI, offering cutting-edge language model capabilities for email responses.
- **Gmail API Compatibility**: Seamlessly works with Gmail for receiving and responding to emails.
- **Customization Options**: Allows modification of response logic for specific needs.
- **Secure Gmail Access**: Employs OAuth for protected access to Gmail accounts.

## Setup and Configuration
- **OpenAI Assistant Creation**: You need to create an assistant in OpenAI and obtain its ID, which is currently a beta feature.
- **OpenAI API Key**: An API key from OpenAI is required to access their services.
- **Gmail API Setup**: Involves authorizing the application for Gmail access using Google's OAuth 2.0.

## Usage Instructions
1. Create an assistant in OpenAI and note its ID.
2. Configure the OpenAI and Gmail API credentials in the provided config file.
3. Execute `gmail_auto_responder.py` to start the email monitoring process.
4. The script will use `ai_assistant.py` to generate responses to new emails and send them automatically.

## Disclaimer
This project is primarily for educational purposes. Users should consider privacy and ethical implications when automating email responses. Be mindful of the beta nature of OpenAI's new assistant and potential changes or limitations in its functionality.
