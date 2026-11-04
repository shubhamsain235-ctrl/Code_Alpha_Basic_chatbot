print("=====================================================")
print("           WELCOME TO PYTHON CHATBOT ")
print("=====================================================")
import random
bot_name="BlackZ"
print(f"Hello my name is {bot_name}")
user_name=input("Sir what is your name:")
print(f"nice to meet you,{user_name} lets start chating")
responses={
    "hi":["Hello how can i help you today?","hello how are you?"],
    "what is your name":["I am BlackZ chatbot","i am a chatbot "],
    "so according to you ai can replace human jobs in it sector":["Yes some jobs can be replaced by AI"],
    "can you give me some examples like which jobs can be replaced by ai":["it going to very controversial but jobs like frontend,backend,even full stack can be replaced by ai not fully but 90%"],
    "do you think that in future btech cse student can crack job i there any futre in btech cse":["yes definitetly but in specialization like ai&ds there is no future in CSE core because of ai"],
    "currently i am thinking to start python so can you give me roadmap for python":["yes you can go with code with harry 100 days of code"],
    "bye":["ok bye you need any other help?","byy see you later!"]

}

def get_response(message):
    message=message.lower().strip()
    if message in responses:
        return random.choice(responses[message])
    else:
        return "sorry, i dont understand that."


def chatbot():
    while True:
        user_message=input(f"{user_name}:")

        if user_message.lower().strip()=="bye":
            print(f"{bot_name}:goodbye {user_name}")
            
            break
        reply=get_response(user_message)
        print(f"{bot_name}:{reply}")



try:
    chatbot()
except Exception as e:
    print("something went wrong",e)