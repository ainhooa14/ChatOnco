# Chat-OncoBot 💬

Asistente conversacional biomédico para apoyar a oncólogos en la consulta de efectos adversos de fármacos oncológicos, utilizando modelos de lenguaje y literatura científica.

## 🧪 Objetivo

Este prototipo permite al usuario introducir preguntas clínicas y recibir respuestas fundamentadas en artículos científicos (vía PubMed o PDFs). Está pensado como una herramienta de ayuda en la toma de decisiones médicas para reducir la descontinuación del tratamiento en oncología.

## ⚙️ Tecnologías utilizadas

- Python 3.11+
- Streamlit (interfaz)
- Transformers (BioGPT, PubMedBERT)
- PubMed Entrez API (Biopython)
- PyMuPDF (extracción de texto desde PDF)
- OpenAI API (opcional)
- GitHub (control de versiones)

## 📦 Instalación

```bash
git clone https://github.com/tu_usuario/chat-onco-bot.git
cd chat-onco-bot
pip install -r requirements.txt
