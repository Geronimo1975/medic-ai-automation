import spacy

# Încarcă modelul
nlp = spacy.load("en_core_sci_sm")

# Testează modelul pe un text
doc = nlp("Ibuprofen is used to treat headaches.")
print([(ent.text, ent.label_) for ent in doc.ents])