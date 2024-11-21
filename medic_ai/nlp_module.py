from transformers import pipeline
import spacy

# 1. Clasificare - Inițializare model de clasificare text
classification_pipeline = pipeline(
    "text-classification", 
    model="bert-base-uncased", 
    return_all_scores=True
)

# 2. NER - Inițializare spaCy pentru extragerea entităților medicale
nlp = spacy.load("en_core_web_sm")

def classify_text(text):
    """
    Clasifică textul medical în funcție de categoria identificată.
    
    Args:
        text (str): Textul medical de analizat.
    Returns:
        list: Lista de scoruri pentru fiecare categorie.
    """
    predictions = classification_pipeline(text)
    return predictions

def extract_entities(text):
    """
    Extrage entități medicale din text.
    
    Args:
        text (str): Textul medical de analizat.
    Returns:
        list: Entitățile extrase (nume și tipuri).
    """
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return entities

# Exempel de utilizare
if __name__ == "__main__":
    input_text = "Patient exhibits symptoms of fever and fatigue. Possible diagnosis is flu."
    
    # Clasificare
    classification_result = classify_text(input_text)
    print("Classification Results:")
    print(classification_result)
    
    # Extragere entități
    ner_result = extract_entities(input_text)
    print("\nNamed Entity Recognition (NER) Results:")
    print(ner_result)
