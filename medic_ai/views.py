from django.http import JsonResponse
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from django.http import JsonResponse
from .nlp_module import classify_text, extract_entities
import spacy
import subprocess
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class NERView(View):
    def post(self, request):
        # Obține textul din cererea POST
        text = request.POST.get('text', '')
        if not text:
            return JsonResponse({'error': 'Textul nu a fost furnizat.'}, status=400)
        
        # Rulează scriptul NER
        try:
            entities = self.run_ner(text)
            return JsonResponse({'entities': entities})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def run_ner(self, text):
        # Rulează scriptul din mediul NER folosind subprocess
        command = f'source ner_env/bin/activate && python ner_script.py "{text}"'
        process = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )
        # Verifică dacă scriptul a returnat erori
        if process.returncode != 0:
            raise Exception(process.stderr)
        
        # Returnează rezultatele în JSON
        return json.loads(process.stdout)


nlp = spacy.load("en_core_sci_sm")

def ner_view(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        if not text:
            return JsonResponse({"error": "Text not provided"}, status=400)

        # Procesarea textului cu modelul NER
        doc = nlp(text)
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

        return JsonResponse({"entities": entities})

    return JsonResponse({"error": "Invalid request method"}, status=405)


# Inițializăm modelul și tokenizer-ul DialoGPT
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Inițializăm istoricul conversației
chat_history_ids = None  # Inițializăm istoricul conversației

def chat_response(request):
    global chat_history_ids
    if request.method == "POST":
        user_input = request.POST.get("message")
        if user_input:
            # Encodăm input-ul utilizatorului și actualizăm istoricul conversației
            new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids
            
            # Generăm răspunsul folosind modelul DialoGPT
            chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
            bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

            return JsonResponse({"response": bot_response})
        else:
            return JsonResponse({"error": "No message provided."})

# Funcția care generează răspunsul botului
def chat_with_bot(user_input, chat_history_ids=None):
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids

    # Generează răspunsul botului
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return bot_response, chat_history_ids


@csrf_exempt
def classify_view(request):
    if request.method == "POST":
        user_text = request.POST.get("text", "")
        if not user_text:
            return JsonResponse({"error": "No text provided"}, status=400)
        predictions = classify_text(user_text)
        return JsonResponse({"predictions": predictions})

@csrf_exempt
def ner_view(request):
    if request.method == "POST":
        user_text = request.POST.get("text", "")
        if not user_text:
            return JsonResponse({"error": "No text provided"}, status=400)
        entities = extract_entities(user_text)
        return JsonResponse({"entities": entities})