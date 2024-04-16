
from openai import OpenAI
import dotenv

dotenv.load_dotenv()
client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)


