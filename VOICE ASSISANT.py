import speech_recognition as sr
import pyttsx3
import datetime
import requests
import smtplib
import imaplib
import json

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to convert speech to text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your audio.")
    except sr.RequestError:
        print("Speech recognition service is unavailable.")

# Function to send email
def send_email(to_email, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, to_email, message)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

# Function to get weather updates
def get_weather(city):
    api_key = 'your_openweathermap_api_key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()
        
        if data['cod'] == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            speak(f"The weather in {city} is {weather_description}. The temperature is {temperature} degrees Celsius.")
        else:
            print("Error fetching weather data.")
    except Exception as e:
        print(f"Error fetching weather data: {e}")

# Function to set reminders
def set_reminder(event_name, event_date):
    # Example using a local storage (you might want to integrate with Google Calendar API)
    reminders = []

    try:
        reminders_file = 'reminders.json'
        with open(reminders_file, 'r') as f:
            reminders = json.load(f)
    except FileNotFoundError:
        pass

    reminders.append({'event_name': event_name, 'event_date': event_date})

    with open(reminders_file, 'w') as f:
        json.dump(reminders, f, indent=2)

    print(f"Reminder set for {event_name} on {event_date}.")

# Main loop for voice assistant
def main():
    speak("Hello! How can I assist you today?")

    while True:
        command = recognize_speech()

        if "send email" in command:
            speak("Whom do you want to send the email to?")
            recipient = recognize_speech()
            speak("What is the subject of the email?")
            subject = recognize_speech()
            speak("What should the email say?")
            body = recognize_speech()
            send_email(recipient, subject, body)

        elif "weather update" in command:
            speak("Which city's weather would you like to know?")
            city = recognize_speech()
            get_weather(city)

        elif "set reminder" in command:
            speak("What is the name of the event?")
            event_name = recognize_speech()
            speak("When is the event? Please specify date and time.")
            event_date = recognize_speech()
            set_reminder(event_name, event_date)

        elif "exit" in command:
            speak("Exiting the voice assistant.")
            break

if __name__ == "__main__":
    main()
