import re

def recognize_dialog_act(utterance):
    utterance = utterance.strip().lower()
    if re.search(r'\?$', utterance) or utterance.startswith(('what', 'why', 'how', 'when', 'where', 'who', 'is', 'are', 'can', 'could', 'do', 'does')):
        return 'Question'
    elif re.search(r'^(please|kindly|could you|can you)', utterance) or utterance.endswith('!') and 'please' in utterance:
        return 'Request'
    elif utterance in ('hi', 'hello', 'hey', 'good morning', 'good evening'):
        return 'Greeting'
    elif utterance in ('bye', 'goodbye', 'see you', 'take care'):
        return 'Farewell'
    elif re.search(r'^(thanks|thank you)', utterance):
        return 'Thanking'
    elif re.search(r'^(yes|yeah|sure|ok|okay|no|nope)', utterance):
        return 'Acknowledgement'
    else:
        return 'Statement'

conversation = [
    "Hello there!",
    "How are you doing today?",
    "Can you help me book a ticket?",
    "Yes, sure.",
    "Thank you so much.",
    "The weather is nice today.",
    "Goodbye!"
]

print("Dialog Act Recognition:")
for utterance in conversation:
    act = recognize_dialog_act(utterance)
    print(f"'{utterance}' -> {act}")
