# 1. Extinderea funcționalităților NLP

## pipeline NLP pentru întrebări și răspunsuri (bazat pe modelul roberta-base-squad2).
Ce putem adăuga:
    # Îmbunătățirea pipeline-ului: Utilizarea unui set mai larg de date medicale pentru fine-tuning al modelului.
    # Clasificarea textului: Identificarea categoriilor de risc sau diagnosticare pe baza simptomelor descrise.
    # Entitate-recunoaștere (NER): Extracția entităților medicale (medicamente, boli, simptome) din text.

# 2. Dezvoltarea unui modul CNN pentru imagini medicale

## Clasificare (ex. detectarea tumorilor) sau segmentare de imagini medicale.

## Fluxul de lucru:
    # Antrenarea unui model CNN (cum ar fi ResNet sau EfficientNet) pentru clasificarea imaginilor medicale.
    # Integrarea modelului într-un API care primește imagini medicale și returnează rezultate (diagnostic probabil).

## Tehnologii recomandate:
    # Framework-uri: TensorFlow, PyTorch.
    # Dataset-uri publice: ChestX-ray14, ISIC (pentru detectarea melanomului) etc.

# 3. Integrarea funcționalităților AI în backend

## Crearea de API-uri dedicate pentru:
    # Procesarea textului: Endpoint pentru întrebări și răspunsuri.
    # Procesarea imaginilor: Endpoint pentru încărcarea și analiza imaginilor medicale.
## Testarea API-urilor cu seturi de date anonimizate.

# 4. Frontend pentru testarea AI

## Formulare web în templates/medical pentru:
    # Introducerea textului pentru sugestii NLP.
    # Încărcarea imaginilor medicale pentru diagnosticare CNN.
