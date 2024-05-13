import pyttsx3
engine = pyttsx3.init()

print("Enter q to quit.")
while True:
    prompt = input("What do you want the pc to say? ")
    if prompt == 'q':
        break
    engine.say(prompt)
    engine.runAndWait()
