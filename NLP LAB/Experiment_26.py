from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_to_french(text):
    batch = tokenizer([text], return_tensors="pt", padding=True)
    generated = model.generate(**batch)
    translated = tokenizer.batch_decode(generated, skip_special_tokens=True)
    return translated[0]

sentences = [
    "Natural language processing is a fascinating field.",
    "How are you today?",
    "I love learning new languages."
]

for sentence in sentences:
    translation = translate_to_french(sentence)
    print("English:", sentence)
    print("French:", translation)
    print("-" * 50)
