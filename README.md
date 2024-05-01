# Stray Thought

Who knows?

## Workflow

- Get topic
- Generate monologue
- Generate prompt from monologue
- Generate audio from monologue
- Create generated video backdrop from prompt using audio length as guideline (full length, or just loop short clip?)
- Generate subtitles with timecodes (whisper)

- Merge together:
  - generated video
  - generated audio
  - overlay subtitles using time codes
  - public domain music? (later, generated)


# Requirements

## Ollama
- Running [Ollama](https://ollama.com/) server, with the desired model installed.

## XTTS speech

Borrows a bunch from here: https://github.com/daswer123/xtts-api-server

The xtts_models directory is not included since it's over a gig in size. Here's
the missing files:

```
─── xtts_api_server
    └── xtts_models
        └── v2.0.2
            ├── config.json
            ├── model.pth
            ├── speakers_xtts.pth
            └── vocab.json
```