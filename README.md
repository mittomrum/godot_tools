# cicd_compress_send

## Game Deployment Script

This Python script automates the compression and upload of game files to itch.io using Butler.

### Overview

The `cicd_compress_send` script simplifies the process of deploying games to itch.io by automating key tasks such as file compression and upload. It is designed to be used as a submodule in game projects, providing a seamless integration with Python and Butler.

**Key Processes:**

1. 📦 **Compression:**
   - The script compresses game files into a ZIP archive, optimizing them for distribution.

2. 🚀 **Upload to itch.io:**
   - Utilizing Butler, the script facilitates the automatic upload of the compressed game to itch.io, streamlining the deployment workflow.

### Requirements

- Python
- [Butler](https://github.com/itchio/butler)

### Configuration

- Set the `itchio_user` variable to your itch.io username.
  
### Usage

1. 🛠 **Configure Project:**
   - Ensure that you have a folder structure like this: 
     `GameRoot/Export/Web`

3. 🚀 **Export to itch.io:**
   - Build the game as normal using godot engine
   - Run the script to export your game to itch.io.
   - A file named `GameRoot/Export/GAMENAME_EXPORTPRESET.Zip` will be generated, it automaticly gets updated each time you run the script, no need to delete.

   ```bash
   python cicd_compress_send.py
