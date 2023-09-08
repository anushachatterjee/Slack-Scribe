import openai


def gpt4_call(system_prompt, user_prompt, input_file):

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    file_path = input_file
    with open(file_path, "a") as file:
        file.write(response['choices'][0]['message']['content'] + "\n\n")


def deadline_model(source, input_file):

    openai.api_key = "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"  # api key

    # read file from 
    system_prompt = "You are the Slack Scribe assistant, designed to help users manage events and deadlines. Your current task is to extract event details from the provided message and create a structured format for event data to be passed into the Google Calendar API. Please process the message and generate the necessary event information, including the event name, date, time, duration, location, and any additional details. Ensure the output is in a clear and organized format that can be readily used for creating calendar events. Once you've generated the event data, please present it as follows:\n\nEvent Name: [Event Name]\nDate: [Event Date]\nTime: [Start Time]\nLength: [Event Length (if available)]\nLocation: [Event Location (if available)]\nDescription: [Event Description (if available)]\n\nPlease make sure the output is comprehensive and user-friendly. If any details are missing or unclear in the original message, you can make reasonable assumptions or request clarification from the user. Thank you!\n"  # model updates -> should add remote update feature maybe using cloud api feature

    # read messages from txt_file
    file_path = source

    messages = []

    with open(file_path, "r") as file:
        messages = file.read().strip().split("\n\n")

    for message in messages:
        gpt4_call(system_prompt, message, input_file)



