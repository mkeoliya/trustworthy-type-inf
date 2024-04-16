
from openai import OpenAI
import dotenv
import json

from utils import annotate_gts

dotenv.load_dotenv()

annotate_gts(folders=['benchmarks/type-eval-py/analysis_sensitivities', 'benchmarks/type-eval-py/python_features'])

# client = OpenAI()
# completion = get_response(client, p)
# for choice in completion.choices:
#     print(choice.message['content'])


