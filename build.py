#!/usr/bin/env python3
import datetime
import json
import os
import random
from rich import print, traceback
from app.monologue.generate import generate_monologue
from app.imagegen.generate import generate_artprompt_from_monologue
from app.speech.generate import generate_speech

import app.config as config


traceback.install(show_locals=True)

today = datetime.datetime.now().date()

year = today.year
mon = today.month
day = today.day

print(f"DATE:\n", f"{year}-{mon}-{day}")

with open("topics.json") as f:
    topics = json.load(f)

# pick a random topic

topic = random.choice(topics)

print(f"TOPIC:\n{topic}")

# ---

config.build_path = "."

if not config["skip_build_path"]:
    today_path = f"{year}/{mon}-{day}"
    config.build_path = f"output/{today_path}-{topic.replace(' ', '-')}"

    # if build path already exists, ask to overwrite

    if os.path.exists(config.build_path):
        print(f"Build path {config.build_path} already exists. Overwrite? (y/n)")
        response = input().lower()
        if response != "y":
            print("Exiting...")
            exit(0)

    os.makedirs(config.build_path, exist_ok=True)

print(f"BUILD PATH:\n{config.build_path}")

# ---

monologue = generate_monologue(topic)
print(f"MONOLOGUE:\n{monologue}")

# ---

artprompt = generate_artprompt_from_monologue(monologue)

print(f"ART PROMPT:\n{artprompt}")

# ---

if config.DEBUG["render_audio"]:
    print("Generating speech...")
    generate_speech(monologue, f"{config.build_path}/output.wav")
