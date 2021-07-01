# importing pyttsx3 pythons speech api
import pyttsx3

# commands to set properties for speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 140
engine.setProperty('rate', newVoiceRate)
engine.setProperty('volume', 1)


# this function gives the audio output
def speak(audio):
    print(audio)
    engine.say(audio)
    engine
    engine.runAndWait()


speak("Write your name and I will predict your future! ")
# empty string to store the value
output = ""
# keeps the count of inputs
count = 0
# command to stop the program
end = "quit"
while True:
    # variable to store the name
    name = input("Write here: ").lower()
    # already defined dictionaries
    prediction = {
        "hrithik": '''Hrithik has many dreams, but he can't take right path and so being depressed he blames others.
    If he will talk less and will try to stay focused then i would say he can do miracles! 
    ''',
        "nisha": '''I think you are a pretty girl who always try to talk sweet but sometimes becomes so furious that you 
    don't even think whom you are talking right , this can be easily sorted if you try to stay calm and stay focused 
    don't let your brain do some hustle ''',
        "puja": '''You are a money maker and finds ways to be rich and successful instantly without sparing much time, 
    you can be rich one day but now you should try to do things which are important for you now and which will sure 
    have impact on your future. '''

    }
    # to check weather the input is present in the dictionary if present then speak the result
    if "hrithik" in name:
        if count == 0:
            output = prediction.get("hrithik")
            count += 1
        elif count > 0:
            output = "I already predicted your future!"
        speak(output)
    elif "puja" in name:
        if count < 2:
            output = prediction.get("puja")
            count += 1
        else:
            output = "I already predicted your future!"
        speak(output)
    elif "nisha" in name:
        if count < 3:
            output = prediction.get("nisha")
            count += 1
        else:
            output = "I already predicted your future!"
        speak(output)

    elif name == end:
        break
    else:
        output = prediction.get(name, "sorry i don't have enough data to predict your future!")
        speak(output)
