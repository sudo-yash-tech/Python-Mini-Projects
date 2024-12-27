import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by YASH RAIKWAR")
    engine = pyttsx3.init()
    while True:
        # Initialize the text-to-speech engine
        
        user_input = input("Enter what you want me to say: ").lower()
        if user_input in ["q", "quit"]:
            engine.say("Thank you for talking") #break the program
            engine.runAndWait()
            break
        engine.say(user_input)
        engine.runAndWait()

