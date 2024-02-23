from openai import OpenAI
import config
import time

client = OpenAI(api_key=config.ai_token)
assist_id = config.ai_assist_id

email_message = 'Tell me please the pricing'


def generate_response(message_body):

    # Create thread
    thread = client.beta.threads.create()
    thread_id = thread.id

    # Add message to thread
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message_body,
    )

    # Run the assistant and get the new message
    new_message = run_assistant(thread)
    # print(f"To {name}:", new_message)
    return new_message



def run_assistant(thread):
    # Retrieve the Assistant
    assistant = client.beta.assistants.retrieve(assist_id)

    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    # Wait for completion
    while run.status != "completed":
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    # Retrieve the Messages
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    new_message = messages.data[0].content[0].text.value
    # print(f"Generated message: {new_message}")
    print('Message generated')
    return new_message



