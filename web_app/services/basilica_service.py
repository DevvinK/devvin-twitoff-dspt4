import basilica
import os
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection)) #> <class 'basilica.Connection'>


if __name__ == "__main__":
      
   embedding = connection.embed_sentences("Hey this is a cool tweet!", model="twitter") # > a list of 768 numbers
   print(embedding)

   tweets = ["Hello World", "artificail intelligence", "another tweet here #cool"]
   embeddings = connection.embed_sentences(tweets, model="twitter")
   for embed in embeddings:
      print("-----")
      print(len(embed))