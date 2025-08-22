import os
import random
import logging
from google import genai

# Inizializza il client Gemini
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY", "chiave_api_predefinita"))

# Lista di temi casuali per i testi di curiosità
RANDOM_TOPICS = [
    "scienza",
    "storia antica",
    "animali strani e curiosi",
    "tecnologia del futuro",
    "misteri irrisolti",
    "cibi strani dal mondo",
    "fenomeni naturali incredibili",
    "scoperte archeologiche",
    "spazio e astronomia",
    "invenzioni bizzarre",
    "tradizioni culturali uniche",
    "record mondiali assurdi",
    "leggende urbane",
    "curiosità geografiche",
    "psicologia umana"
]

def get_random_topic():
    """Ottieni un tema casuale dalla lista predefinita."""
    return random.choice(RANDOM_TOPICS)

def generate_curiosity_text(topic):
    """
    Genera un testo di curiosità usando Gemini AI basato sul tema fornito.
    
    Args:
        topic (str): Il tema per cui generare il testo di curiosità
        
    Returns:
        str: Testo di curiosità generato
        
    Raises:
        Exception: Se c'è un errore con la chiamata API
    """
    
    # Prompt ultra-ottimizzato per velocità
    prompt = f"Scrivi 120 parole su una curiosità di {topic}. Stile: scorrevole, intrigante, per video YouTube. Inizia forte, finisci con stupore."
    
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        
        # Prova diversi modi per accedere al testo della risposta
        text_content = None
        
        # Metodo 1: response.text (diretto)
        if hasattr(response, 'text') and response.text:
            text_content = response.text.strip()
        
        # Metodo 2: attraverso candidates
        elif hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'content') and candidate.content:
                if hasattr(candidate.content, 'parts') and candidate.content.parts:
                    part = candidate.content.parts[0]
                    if hasattr(part, 'text') and part.text:
                        text_content = part.text.strip()
        
        if text_content:
            return text_content
        else:
            raise Exception("Impossibile estrarre il testo dalla risposta di Gemini")
            
    except Exception as e:
        logging.error(f"Errore nella chiamata all'API Gemini: {e}")
        raise Exception(f"Errore nella chiamata all'API: {str(e)}")
