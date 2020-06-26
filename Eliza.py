import random
def respond(message):
    if message.endswith("?"):
        return random.choice(responses["question"])
    return random.choice(responses["statement"])
print(respond("hello"))

