import os
import re
import shutil
import urllib.parse

# --- Configuration ---
VAULT_ROOT = "."
NOTES_DIR = os.path.join(VAULT_ROOT, "College", "HAM", "Gradient Boosting")
ATTACHMENTS_DIR = os.path.join(VAULT_ROOT, "Attachments")

OUTPUT_DIR = os.path.join(VAULT_ROOT, "Gradient_Boosting_Export")
OUTPUT_README = os.path.join(OUTPUT_DIR, "README.md")
OUTPUT_ASSETS = os.path.join(OUTPUT_DIR, "assets")
# ----------------------

os.makedirs(OUTPUT_ASSETS, exist_ok=True)

# Regex to match Obsidian embeds: ![[Pasted image ...png|400]] or ![[Pasted image ...png]]
OBSIDIAN_IMG_PATTERN = re.compile(r"!\[\[(.*?)\]\]")
# Regex to catch standard markdown embeds if present
MD_IMG_PATTERN = re.compile(r"!\[(.*?)\]\((.*?)\)")


def process_image(img_raw_name):
    # Strip any size parameters like "|400" or alt text
    img_clean = img_raw_name.split("|")[0].strip()
    filename = os.path.basename(img_clean)

    # Search in Vault Attachments folder, Notes folder, or Vault root
    candidates = [
        os.path.join(ATTACHMENTS_DIR, filename),
        os.path.join(NOTES_DIR, filename),
        os.path.join(VAULT_ROOT, filename),
    ]

    source_path = next((p for p in candidates if os.path.exists(p)), None)

    if source_path:
        dest_path = os.path.join(OUTPUT_ASSETS, filename)
        shutil.copy2(source_path, dest_path)
        print(f" Copied: {filename}")
    else:
        print(f" Image missing from disk: {filename}")

    # URL-encode spaces so GitHub & Markdown renderers parse the path properly
    encoded_filename = urllib.parse.quote(filename)
    return f"![{filename}](assets/{encoded_filename})"


# Grab all markdown files from the note directory
md_files = sorted(
    [
        os.path.join(NOTES_DIR, f)
        for f in os.listdir(NOTES_DIR)
        if f.endswith(".md") and not f.startswith(".")
    ]
)

combined_markdown = []

for filepath in md_files:
    print(f"\nProcessing: {os.path.basename(filepath)}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Convert ![[image.png]]
    content = OBSIDIAN_IMG_PATTERN.sub(
        lambda m: process_image(m.group(1)), content
    )

    # 2. Convert standard ![](...) if any existed
    content = MD_IMG_PATTERN.sub(lambda m: process_image(m.group(2)), content)

    combined_markdown.append(content.strip())

# Write out the combined README
with open(OUTPUT_README, "w", encoding="utf-8") as f:
    f.write("\n\n---\n\n".join(combined_markdown))

print(f"\n README.md generated successfully at: {OUTPUT_README}")
