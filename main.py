
from openai import OpenAI
import dotenv

dotenv.load_dotenv()
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
)

print(completion.choices[0].message)


