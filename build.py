#!/usr/bin/env python3
import json
import random
from rich import print, traceback
from app.monologue.generate import generate_monologue
from app.imagegen.generate import generate_artprompt_from_monologue

traceback.install(show_locals=True)

# import topics from topics.json

with open("topics.json") as f:
    topics = json.load(f)

# pick a random topic

topic = random.choice(topics)

print(f"TOPIC:\n{topic}")

monologue = generate_monologue(topic)
print(f"MONOLOGUE:\n{monologue}")


artprompt = generate_artprompt_from_monologue(monologue)

print(f"ART PROMPT:\n{artprompt}")
