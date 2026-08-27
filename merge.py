import os
import re
import shutil

# --- Configuration ---
VAULT_ROOT = "."
NOTES_DIR = os.path.join(VAULT_ROOT, "College", "HAM", "Gradient Boosting")
ATTACHMENTS_DIR = os.path.join(VAULT_ROOT, "Attachments")

OUTPUT_DIR = os.path.join(VAULT_ROOT, "Gradient_Boosting_Export")
OUTPUT_README = os.path.join(OUTPUT_DIR, "README.md")
OUTPUT_ASSETS = os.path.join(OUTPUT_DIR, "assets")

# Set exact note order here (filenames without path)
NOTE_ORDER = [
    "Maths Behind Gradient Boosting Regression.md",
    "Gradient Boosting (Regression).md",
    "Maths Behind Gradient Boosting Classification.md",
    "Gradient Boosting (Classification).md",
    "Implementation.md",
]
# ----------------------

os.makedirs(OUTPUT_ASSETS, exist_ok=True)

# Matches ![[image.png]] or ![[image.png|400]] or standard markdown ![](...)
WIKILINK_IMG_REGEX = re.compile(r"!\[\[(.*?)(?:\|.*?)?\]\]")
STANDARD_IMG_REGEX = re.compile(r"!\[(.*?)\]\((.*?)\)")


def resolve_and_copy_image(img_filename):
    clean_filename = os.path.basename(img_filename.strip().split("|")[0])

    # Search in root Attachments folder, notes folder, or vault root
    search_paths = [
        os.path.join(ATTACHMENTS_DIR, clean_filename),
        os.path.join(NOTES_DIR, clean_filename),
        os.path.join(VAULT_ROOT, clean_filename),
    ]

    found_path = None
    for path in search_paths:
        if os.path.exists(path):
            found_path = path
            break

    if found_path:
        dest_path = os.path.join(OUTPUT_ASSETS, clean_filename)
        shutil.copy2(found_path, dest_path)
        return f"![{clean_filename}](assets/{clean_filename})"
    else:
        print(f"⚠️ Image not found: {clean_filename}")
        return f"![{clean_filename}](assets/{clean_filename})"


combined_markdown = []

# Fallback: if filenames in NOTE_ORDER differ slightly, scan the directory directly
files_to_process = []
if all(os.path.exists(os.path.join(NOTES_DIR, f)) for f in NOTE_ORDER):
    files_to_process = [os.path.join(NOTES_DIR, f) for f in NOTE_ORDER]
else:
    files_to_process = sorted(
        [
            os.path.join(NOTES_DIR, f)
            for f in os.listdir(NOTES_DIR)
            if f.endswith(".md")
        ]
    )

print(f"Processing {len(files_to_process)} notes...")

for filepath in files_to_process:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace Obsidian Wikilink image embeds: ![[image.png]]
    content = WIKILINK_IMG_REGEX.sub(
        lambda m: resolve_and_copy_image(m.group(1)), content
    )

    # 2. Replace standard Markdown image paths if any exist
    content = STANDARD_IMG_REGEX.sub(
        lambda m: resolve_and_copy_image(m.group(2)), content
    )

    combined_markdown.append(content.strip())

# Write combined output
with open(OUTPUT_README, "w", encoding="utf-8") as f:
    f.write("\n\n---\n\n".join(combined_markdown))

print(f"\n Export complete:")
print(f"- Combined File: {OUTPUT_README}")
print(f"- Copied Images: {OUTPUT_ASSETS}")
