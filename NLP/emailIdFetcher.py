# Email ID fetcher using spacy library
import spacy

# load the blank spacy model
nlp = spacy.blank("en")

# text to be processed
# change the text as per your requirements
text = "My email is : akashboro111@gmail.com. And my friends email is : mpratim32@gmail.com.\
    And another friends email is : prakash@gmail.com"
doc = nlp(text)

# list to store email ids
emails = []
for token in doc :
    if token.like_email : 
        emails.append(token.text)

print(emails)
