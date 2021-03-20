import pyttsx3
import speech_recognition as sr
from datetime import datetime
import winsound
from playsound import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Sorry! didn't get that,Please repeat...")  
        return "None"
    return query


def reminder():
    now = datetime.now()

    c = float(now.strftime("%H.%M"))
    print("Current Time = ", c)

    if c > 8.0 and c < 8.30:
        duration = 2000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
    
        speak("Dude, time to take Breakfast, refer your diet Plan")
        print(" Time to take breakfast.")
        speak("say 'OK' if u are there.")

        query = takeCommand().lower()

        if 'ok' in query:
            speak("Fine..")
            speak("Take your Medicines after breakfast...")


    if c > 11.0 and c < 11.30:
        duration = 2000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        speak("Dude, time to take Mid-Meal, refer your diet Plan")
        print(" Time to take Mid-Meal.")
        speak("say 'OK' if u are there.")

        query = takeCommand().lower()

        if 'ok' in query:
            speak("Fine..")



    if c > 14.0 and c < 14.30:
        duration = 2000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        speak("Dude, time to take Lunch,  refer your diet Plan")
        print(" Time to take Lunch.")
        speak("say 'OK' if u are there.")

        query = takeCommand().lower()

        if 'ok' in query:
            speak("Fine..")
            speak("Take your Medicines after Lunch...")


    if c > 16.0 and c < 16.30:
        duration = 2000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        speak("Dude, time to take Evening Snack, refer your diet Plan")
        print(" Time to take Evening Snack.")
        speak("say 'OK' if u are there.")

        query = takeCommand().lower()

        if 'ok' in query:
            speak("Fine..")


    if c > 20.0 and c < 20.30:
        duration = 2000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        speak("Dude, time to take Evening Snack, refer your diet Plan")
        print(" Time to take Evening Snack.")
        speak("say 'OK' if u are there.")

        query = takeCommand().lower()

        if 'ok' in query:
            speak("Fine..")
            speak("Take your Medicines after if any after Evening snack...")


def underWeight():
    print("\nUnderweight")
    speak("\nHey Dude, you are Underweight")
    print("A  BMI of less than 18.5 indicates that you are underweight, so you may need to put on some weight. ")
    speak("A  BMI of less than 18.5 indicates that you are underweight, so you may need to put on some weight. ")
    speak("being your Health Coach It is my responsibility to keep you fit.")
    speak("To get your Diet say 'Diet' or 'No' to Exit.")

    query = takeCommand().lower()

    if 'diet' in query:
        f = open('underweight.txt')
        a = f.read()
        print(a)
        print("\n\nPlease Note Down and Follow this diet Carefully and Sincerely to Stay Fit and Healthy.....")
        speak("\n\nPlease Note Down and Follow this diet Carefully and Sincerely to Stay Fit and Healthy.....")
        speak("I can Remind you out to Drink Water , Take your Medicines on Time And also Help you to Do some Exercise.")
        speak("If you Want this then Please Let me know.")
        speak("Say 'Help me out' for reminders from me or you can say 'I can Do that' to Exit.")
            
        query = takeCommand().lower()

        if 'help me out' in query:
            speak("Done, Now I will Inform You for Your Meals Accroding to your Diet.")
            reminder()
        elif 'i can do that' in query:
            speak("Thank You Stay Fit and Healthy")
            print("Thank You Stay Fit and Healthy")
            exit()

    elif 'no' in query:
        speak("Thank You Stay Fit and Healthy")
        print("Thank You Stay Fit and Healthy")
        exit()


def healthy():
    print("\nHealthy")
    speak("\nHey Dude, you are Healthy")
    print("A BMI of 18.5–24.9 indicates that you are at a healthy weight for your height. By maintaining a healthy weight, you lower your risk of developing serious health problems.")
    speak("A BMI of 18.5–24.9 indicates that you are at a healthy weight for your height. By maintaining a healthy weight, you lower your risk of developing serious health problems.")
    speak("I can Remind you out to Drink Water , Take your Medicines on Time And also Help you to Do some Exercise.")
    speak("If you Want this then Please Let me know.")
    speak("Say 'Help me out' for reminders from me or you can say 'I can Do that' to Exit.")
        
    query = takeCommand().lower()

    if 'help me out' in query:
        speak("Done, Now I will Inform You for Your Meals Accroding to your Diet.")
        reminder()

    elif 'i can do that' in query:
        speak("Thank You Stay Fit and Healthy")
        print("Thank You Stay Fit and Healthy")
        exit()


def overWeight():
    print("\nOverweight")
    speak("\nHey Dude, you are Overweight")
    print("A BMI of 25–29.9 indicates that you are slightly overweight. You may be advised to lose some weight for health reasons.")
    speak("A BMI of 25–29.9 indicates that you are slightly overweight. You may be advised to lose some weight for health reasons.")
    speak("Being your Health Coach It is my responsibility to keep you fit.")
    speak("To get your Diet say 'Diet' or 'No' to Exit.")
    print("Being your Health Coach It is my responsibility to keep you fit.")
    print("To get your Diet say 'Diet' or 'No' to Exit.")
        
    query = takeCommand().lower()
        
    if 'diet' in query:
        f = open('overweight.txt')
        a = f.read()
        print(a)
        print("\n\nPlease Note Down and Follow this diet Carefully and Sincerely to Stay Fit and Healthy.....")
        speak("\n\nPlease Note Down and Follow this diet Carefully and Sincerely to Stay Fit and Healthy.....")
        speak("I can Remind you out to Drink Water , Take your Medicines on Time And also Help you to Do some Exercise.")
        speak("If you Want this then Please Let me know.")
        speak("Say 'Help me out' for reminders from me or you can say 'I can Do that' to Exit.")
            
        query = takeCommand().lower()

        if 'help me out' in query:
            speak("Done, Now I will Inform You for Your Meals Accroding to your Diet.")
            reminder()

        elif 'i can do that' in query:
            speak("Thank You Stay Fit and Healthy")
            print("Thank You Stay Fit and Healthy")
            exit()

    elif 'no' in query:
        speak("Thank You Stay Fit and Healthy")
        print("Thank You Stay Fit and Healthy")
        exit()


def obese():
    print("\nObese")
    speak("\nHey Dude, you are Obese")
    print("A BMI of over 30 indicates that you are heavily overweight. Your health may be at risk if you do not lose weight.")
    speak("A BMI of over 30 indicates that you are heavily overweight. Your health may be at risk if you do not lose weight.")
    speak("Being your Health Coach It is my responsibility to keep you fit.")
    print("Being your Health Coach It is my responsibility to keep you fit.")
    print("To get your Diet say 'Diet' or 'No' to Exit.")
    speak("To get your Diet say 'Diet' or 'No' to Exit.")
        
    query = takeCommand().lower()
        
    if 'diet' in query:
        f = open('obese.txt')
        a = f.read()
        print(a)
        print("\n\nPlease Note Down and Follow this diet Carefully and Sincerely to Stay Fit and Healthy.....")
        speak("\n\nPlease Note Down and Follow this diet Carefully and Sincerely to Stay Fit and Healthy.....")
        speak("I can Remind you out to Drink Water , Take your Medicines on Time And also Help you to Do some Exercise.")
        speak("If you Want this then Please Let me know.")
        speak("Say 'Help me out' for reminders from me or you can say 'I can Do that' to Exit.")
            
        query = takeCommand().lower()

        if 'help me out' in query:
            speak("Done, Now I will Inform You for Your Meals Accroding to your Diet.")
            reminder()
        elif 'i can do that' in query:
            speak("Thank You Stay Fit and Healthy")
            print("Thank You Stay Fit and Healthy")
            exit()

    elif 'no' in query:
        speak("Thank You Stay Fit and Healthy")
        print("Thank You Stay Fit and Healthy")
        exit()


class patientDetails:
    formType = 'patientDetails'
    def printData(self):
        with  open('user.txt', 'w') as f:
            a = f.write(f"\t\t\tName: {self.name}\n\t\t\tAge: {self.age}\n\t\t\tGender: {self.gender}\n\t\t\tHeight: {self.height}\n\t\t\tWeight: {self.weight}\n\t\t\tBlood Group: {self.blood}\n\t\t\tContact: {self.number}\n\t\t\tPlace: {self.place}\n\t\t\tMail ID: {self.mid}")
            # print(a)
user = patientDetails()


speak("\n\t\t\t***** WELCOME TO VIRTUAL HEALTH ASSISTANT *****\n")
print("\n\t\t\t***** WELCOME TO VIRTUAL HEALTH ASSISTANT *****\n")

speak("I am Louis,Your Personal Health Coach\n Let me First collect some of Your Basic Details.")
print("\t\t\tI am Louis,Your Personal Health Coach\n\t\t\t Let me First collect some of Your Basic Details.")
speak("\nPlease fill the below Details Carefully and Correctly.\n")
print("\n\nPlease fill the below Details Carefully and Correctly.\n\n")

name = input("Enter your Name: ")
age = input("Enter your Age: ")
gender = input("Enter your Gender (M | F | O): ")
blood = input("Enter your Blood Group: ")
number = int(input("Enter Your Phone Number: "))
place = input(("Enter your Place of Residence:  "))
weight = int(input("Enter your Weight in Kg: "))
height = float(input("Enter your Height in M : "))
mid = input("Your Mail ID: ")

user.name = name
user.age = age
user.mid = mid
user.gender =gender
user.blood = blood
user.number = number 
user.place = place
user.weight = weight
user.height = height    

user.printData()    

speak("Well Done, Your Details are safe with us  and we will help  you in the best possible way.")
print("Well Done, Your Details are safe with us \n we will help  you in the best possible way.")

print("\nNow I will Calculate your B.M.I and will Tell you Your prescribed DIET.")
speak("Now I will Calculate your B M I and will Tell you Your prescribed DIET.")
print("\nSay 'CONTINUE' for B.M.I or 'STOP' to Quit.")
speak("Say 'CONTINUE' for B M I or 'STOP' to Quit.")

query = takeCommand().lower()

if 'continue' in query:

    speak("Your Height in CentiMeters")
    h = int(input("Enter Your Height in C.M: "))
    speak("Your Weight in KG")
    w = int(input("Enter Your Weight in KG: "))
    h1 = (h/100)
    b = w/(h1*h1)
    print("Calculating BMI.......")
    speak("Calculating BMI.......")
    print(".\n.\n.\n.")
    print(f"Your B.M.I is: {b}")
    if 18.5>b:
        underWeight()

    elif 18.5<b or 24.9>b:
        healthy()

    elif 25<b or 29.9>b:
        overWeight()

    else:
      obese()

elif 'stop' in query:
    speak("Thank You")
    exit()

