# Manga Recap (ShareCaptioner + Tortoise TTS)

## Project Overview

This project generates summaries of manga volumes by analyzing images extracted from PDF files. It now uses the open-source ShareCaptioner model for image understanding instead of GPT‑4 Vision, and Tortoise TTS for narration instead of ElevenLabs. The pipeline extracts images from PDFs, scales and base64‑encodes them, prompts ShareCaptioner to produce story‑style summaries, then synthesizes narration with Tortoise and combines narration with relevant panels to produce a recap video.

Join the Discord: https://discord.gg/MMqcuDe2WZ

https://github.com/pashpashpash/manga-reader/assets/20898225/debb0c15-3579-477c-813d-2ed878b0e6ea

## Features

- PDF processing to extract manga pages, plus panel extraction.
- Image scaling and base64 encoding for model input.
- Summarization via ShareCaptioner (local, open-source vision model).
- Narration via Tortoise TTS (local, neural TTS).
- Video creation combining narration and relevant panels/pages.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.9+ (recommended)
- pip (Python package manager)
- Virtual environment (recommended)
- A machine with sufficient CPU/GPU and disk space (Tortoise and ShareCaptioner are heavy and may download model weights on first run)

## Installation Steps

1. Create a virtual environment to manage your project's dependencies separately.

```
python -m venv venv
```

2. Activate the virtual environment

On Windows PowerShell:
```
venv\Scripts\Activate.ps1
```

On macOS/Linux:
```
source venv/bin/activate
```

3. Install Required Python Packages

```
pip install -r requirements.txt
```

4. Environment Variables

No API keys are required for ShareCaptioner or Tortoise TTS. A `.env` file is optional and currently unused.

5. Prepare Your Manga PDFs

Place your manga volume PDF files in a directory structure as expected by the script, for example, `naruto/v10/v10.pdf`. Additionally include `chapter-reference.pdf` and `profile-reference.pdf` in each manga directory (e.g. `naruto/chapter-reference.pdf`, `naruto/profile-reference.pdf`) to help identify chapter starts and character profiles for downstream processing.

## Running the Project

To run the project, execute the `app.py` script from the root directory of your project:

```
python3 app.py --manga naruto --volume-number 10
```

This script processes the specified PDF files, extracts and scales images, encodes them in base64, and passes them to ShareCaptioner for analysis. The generated summaries are printed to the console. Tortoise TTS synthesizes narration locally, and narration plus relevant panels are combined into a recap video saved at `naruto/v10/recap.mp4`.

## Optional/Recommended running instructions

I personally recommend running this in a Jupiter notebook ([anime_recap.ipynb](anime_recap.ipynb)), as it allows you run the script one cell at a time, which is useful for debugging and understanding the process.
