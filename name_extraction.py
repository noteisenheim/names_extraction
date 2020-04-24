import spacy

# loading the model for english language
nlp = spacy.load("en_core_web_sm")


print('enter the text: ')
# reading input, removing the apostrophes
inp = input().replace("'s ", ' ').replace("' ", ' ')
# feeding the input to the model
doc = nlp(inp)

# extracting the names
names_list = []
for ent in doc.ents:
    if ent.label_ == 'PERSON':
        names_list.append(ent.text)

print(names_list)