## ejemplo de como hacer una peticion a gemini
from openai import OpenAI
from google import genai
from dotenv import load_dotenv
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="dame tu opinion sobre "
)
print(response.text)

#ejemplo de como pedir usando groq
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Explain the importance of fast language models",
    model="openai/gpt-oss-20b",
)
print(response.output_text)



# --- CONFIGURACIÓN DE MODELOS SUJETOS  ---

# Modelos disponibles en Groq (Requieren GROQ_API_KEY)
GROQ_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "llama-3.2-3b-preview",
    "llama-3.2-1b-preview",
    "mixtral-8x7b-32768",
    "gemma2-9b-it"
]

# Modelos disponibles en Google (Requieren GOOGLE_API_KEY)
GEMINI_MODELS = [
    "gemini-1.5-pro",
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b",
    "gemini-2.0-flash-exp"
]

