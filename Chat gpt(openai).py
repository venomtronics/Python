import openai
import re

# Set your API key
openai.api_key = "YOUR_API_KEY"

# Set the model and prompt
model_engine = "text-davinci-002"
prompt = "What is the capital of India?"

# Generate text
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
message = re.sub('[^0-9a-zA-Z\n\.\?,!]+', ' ', message).strip()
print(message)
