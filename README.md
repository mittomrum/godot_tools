# cicd_compress_send.py (Game Deployment Script)

This Python script automates the compression and upload of game files to itch.io using Butler.

## Overview

I use this script as a submodule in my game projects to streamline the deployment process. It leverages Python and Butler for compressing files into a ZIP archive and pushing the game to itch.io, respectively.

### Key Processes

1. **Compression:**
   - The script compresses game files into a ZIP archive, optimizing them for distribution.

2. **Upload to itch.io:**
   - Utilizing Butler, the script facilitates the automatic upload of the compressed game to itch.io, streamlining the deployment workflow.

## Requirements

- Python
- [Butler](https://github.com/itchio/butler)

## Configuration

- Set the `itchio_user` variable to your itch.io username.

## Usage

1. **Configure Project:**
   - Ensure that you have a folder structure like this: 
     `GameRoot/Export/Web/index.html`

3. **Export to itch.io:**
   Run the script to export your game to itch.io.

   ```bash
   python cicd_compress_send.py

