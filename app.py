import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for
from gemini_service import generate_curiosity_text, get_random_topic

# Configura il logging
logging.basicConfig(level=logging.DEBUG)

# Crea l'app Flask
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "chiave_segreta_sviluppo")

@app.route("/", methods=["GET", "POST"])
def index():
    generated_text = None
    selected_topic = None
    error_message = None
    
    if request.method == "POST":
        # Ottieni il tema dal form o usa un tema casuale
        topic = request.form.get("topic", "").strip()
        
        if not topic:
            topic = get_random_topic()
            selected_topic = topic
        else:
            selected_topic = topic
        
        try:
            generated_text = generate_curiosity_text(topic)
            flash(f"Testo generato con successo per il tema: {selected_topic}", "success")
        except Exception as e:
            error_message = f"Errore nella generazione del testo: {str(e)}"
            flash(error_message, "error")
            logging.error(f"Errore nella generazione del testo: {e}")
    
    return render_template("index.html", 
                         generated_text=generated_text, 
                         selected_topic=selected_topic,
                         error_message=error_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
