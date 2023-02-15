import os
from webexteamssdk import WebexTeamsAPI, Webhook, Message, CardAction, Form, FormAction, FormField

# Initialize the API object
api = WebexTeamsAPI(access_token='your_bot_access_token')

# Get the current user details
me = api.people.me()

# Define the form fields
form_fields = [
    FormField(key="name", label="Name", type="text"),
    FormField(key="email", label="Email", type="text"),
    FormField(key="message", label="Message", type="text"),
]

# Define the form action
form_action = FormAction(
    type="submit",
    url="your_backend_endpoint_url",
    method="post",
    payload={"form": "contact"},
)

# Define the form
form = Form(
    title="Contact Us",
    header="Please provide your contact information",
    submit_label="Submit",
    fields=form_fields,
    actions=[form_action],
)

# Define the card action
card_action = CardAction(
    type="submit",
    form=form,
)

# Define the message with the card
message = Message(
    text="Please fill out the form below to contact us",
    markdown="Please fill out the form below to contact us",
    attachments=[card_action],
)

# Listen for messages
while True:
    # Get all messages
    messages = api.messages.list()
    for message in messages:
        # Check if the message was sent to a room
        if message.roomId:
            # Check if the message was sent by someone other than the bot
            if message.personId != me.id:
                # Send the message with the card
                api.messages.create(roomId=message.roomId, markdown=message.markdown, attachments=message.attachments)



###import os
import requests
import json
from adaptivecard import AdaptiveCard, ActionSubmit, ColumnSet, Column, Container, FormField, TextInput, DateInput, ChoiceSetInput

# Define the adaptive card
card = AdaptiveCard(
    type="AdaptiveCard",
    version="1.0",
    body=[
        Container(
            type="Container",
            items=[
                ColumnSet(
                    type="ColumnSet",
                    columns=[
                        Column(
                            type="Column",
                            items=[
                                FormField(
                                    type="TextInput",
                                    id="ami_id",
                                    title="AMI ID",
                                ),
                                FormField(
                                    type="DateInput",
                                    id="bio_screening_date",
                                    title="BIO Screening Date",
                                ),
                                FormField(
                                    type="TextInput",
                                    id="incident_number",
                                    title="Incident Number",
                                ),
                                FormField(
                                    type="ChoiceSetInput",
                                    id="incident_type",
                                    title="Select Incident Type",
                                    style="expanded",
                                    is_multi_select=True,
                                    choices=[
                                        {
                                            "title": "Option 1",
                                            "value": "option_1"
                                        },
                                        {
                                            "title": "Option 2",
                                            "value": "option_2"
                                        },
                                        {
                                            "title": "Option 3",
                                            "value": "option_3"
                                        },
                                        {
                                            "title": "Option 4",
                                            "value": "option_4"
                                        },
                                        {
                                            "title": "Option 5",
                                            "value": "option_5"
                                        },
                                        {
                                            "title": "Option 6",
                                            "value": "option_6"
                                        },
                                        {
                                            "title": "Option 7",
                                            "value": "option_7"
                                        },
                                        {
                                            "title": "Option 8",
                                            "value": "option_8"
                                        },
                                        {
                                            "title": "Option 9",
                                            "value": "option_9"
                                        }
                                    ]
                                ),
                            ],
                            width="auto",
                        ),
                    ],
                ),
            ],
        ),
    ],
    actions=[
        ActionSubmit(
            type="Action.Submit",
            title="Submit",
            data={"endpoint": "your_endpoint_url"},
        ),
    ],
)

# Get the JSON representation of the card
card_json = card.to_json(transparent=True)

# Define the message to be sent to the chat room
text = "Please fill out the form below"
message = {
    "markdown": text,
    "attachments": [{"contentType": "application/vnd

###
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_card():
    # Extract the JSON payload from the request body
    payload = request.get_json()

    # Extract the submitted form data from the payload
    ami_id = payload["data"]["ami_id"]
    bio_screening_date = payload["data"]["bio_screening_date"]
    incident_number = payload["data"]["incident_number"]
    incident_type = payload["data"]["incident_type"]

    # You can now use the extracted data as needed
    # ...

    return "Success"

if __name__ == '__main__':
    app.run()

##################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import EdgeService, EdgeOptions

# Create the EdgeOptions object and set the path to the Edge executable
options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Create the EdgeService object and start the driver service
service = EdgeService(executable_path=r"C:\Path\to\msedgedriver.exe")
service.start()

# Create the webdriver object and pass in the EdgeOptions and EdgeService objects
driver = webdriver.Edge(options=options, service=service)

# Navigate to the login page
driver.get("https://www.example.com/login")

# Find the email and password fields on the login page and enter the required information
email_field = driver.find_element_by_name("email")
email_field.send_keys("example@email.com")

password_field = driver.find_element_by_name("password")
password_field.send_keys("mypassword")

password_field.submit()

# Wait for the page to load before clicking on tabs
driver.implicitly_wait(10)

# Click on the first tab and verify if it has been clicked successfully
try:
    tab1 = driver.find_element_by_xpath("//div[@id='tabs']/ul/li[1]")
    tab1.click()
    print("PASS: Tab 1 clicked successfully.")
except:
    print("FAIL: Tab 1 not clicked.")

# Click on the second tab and verify if it has been clicked successfully
try:
    tab2 = driver.find_element_by_xpath("//div[@id='tabs']/ul/li[2]")
    tab2.click()
    print("PASS: Tab 2 clicked successfully.")
except:
    print("FAIL: Tab 2 not clicked.")

# Close the browser window and stop the driver service
driver.quit()
service.stop()

