import sys
import json
import spacy

# Încarcă modelul spacy
nlp = spacy.load("en_core_web_sm")

# Textul este furnizat ca argument de linie de comandă
text = sys.argv[1]

# Procesează textul
doc = nlp(text)

# Extrage entitățile
entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

# Returnează rezultatele ca JSON
print(json.dumps(entities))
