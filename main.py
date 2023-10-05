import os
import sys
from dotenv import load_dotenv

load_dotenv()
print("OpenAI key: ", os.getenv('OPENAI_API'))
print(os.path.dirname(sys.executable))


print("Agora foi!!")
