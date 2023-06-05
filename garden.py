import spacy #This statement should work if you have spaCy installed 

nlp = spacy.load('en_core_web_sm')

sentence_1 = "The old man the boat."
sentence_2 = "The florist sent the flowers was pleased."

gardenpathSentences = [sentence_1, sentence_2]

gardenpathSentences.append("Mary gave the child a Band-Aid.")
gardenpathSentences.append("That Jill is never here hurts.")
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi.")

# Tokenise each sentence and Named entity recognition:
for i in gardenpathSentences:
    doc = nlp(i)
    print([token.orth_ for token in doc])
    print([(w, w.label_) for w in doc.ents])

# Tokenise and Entity recognition:
for i in gardenpathSentences:
    doc = nlp(i)
    print([token.orth_ for token in doc])
    for word in doc:
        if word.is_title == True:
            print(word)

# Entity explanation:
print(spacy.explain("PERSON"))

# PERSON: People, including fictional. Correct, this was given to the names Mary and Jill.

# GPE: Countries, cities, states. Correct, this was given to the place Mississippi.