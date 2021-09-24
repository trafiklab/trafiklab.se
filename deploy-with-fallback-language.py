import argparse
import os
import os.path
from shutil import copy2


def has_translation(filepath, language_code):
    translated_path = filepath.replace('.md', f'.{language_code}.md')
    return os.path.exists(translated_path)


def generate_fallback_page(filepath, language_code, dry_run=False):
    if dry_run:
        print(f"copy2({filepath}, {filepath.replace('.md', f'.{language_code}.md')})")
    else:
        copy2(filepath, filepath.replace('.md', f'.{language_code}.md'))


def generate_fallback_pages_if_needed(dir: str, dry_run=False):
    for root, dirs, files in os.walk(dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            if filepath.endswith(".md") \
                    and not filepath.endswith(".sv.md") \
                    and not filepath.endswith(".en.md"):
                # This is a content file which isn't language specific
                if not has_translation(filepath, 'sv'):
                    generate_fallback_page(filepath, 'sv', dry_run)
        for dirname in dirs:
            generate_fallback_pages_if_needed(os.path.join(root, dirname))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry', dest='dry', action='store_true')
    parser.set_defaults(dry=False)
    args = parser.parse_args()
    generate_fallback_pages_if_needed(os.path.join(os.getcwd(), 'content'), dry_run=args.dry)
    # Continue build
    exec("hugo -d public")