from openai import OpenAI
from pathlib import Path
client = OpenAI(api_key = "sk-XngEOzdgqd1lND6NsIqcT3BlbkFJ9dWkuzc2aZkDd41tK")
# Import necessary libraries
from PIL import Image
import pytesseract


# Set the path to the Tesseract executable (adjust as needed)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Path to the image file (change the path accordingly)
image_path = '/content/image.png'

# Open the image using PIL (Python Imaging Library)
img = Image.open(image_path)

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print("Extracted Text:")
print(text)

speech_file_path =  "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=f"{text}"
)

response.stream_to_file(speech_file_path)
from IPython.display import Audio, display

audio_file_path = 'speech.mp3'

display(Audio(audio_file_path))

