import argparse
import os
import os.path
from shutil import copy2


def has_translation(filepath, language_code):
    translated_path = filepath.replace('.md', f'.{language_code}.md')
    return os.path.exists(translated_path)


def add_missing_translation_warning(filepath):
    warning = """
    
{{% warning %}}
**Obs:** Denna innehåll finns inte tillgängligt på Svenska. Därför ser du Engelska versionen.

Om du tycker att denna sida borde översättas till Svenska, kan du skriva till oss på 
[support.trafiklab.se](https://suport.trafiklab.se).

Om du vill se webbsidan på Engelska, [klicka här](/en/).
{{% /warning %}}
    
    """
    # Read in the file
    with open(filepath, 'r', encoding='utf8') as file:
        content = file.read()

    # Replace the target string
    content = content.replace('---', '', 1)  # Remove the top --- marker
    content = '---' + content.replace('---', '---' + warning)  # Replace the bottom --- marker, add the top marker back

    # Write the file out again
    with open(filepath, 'w', encoding='utf8') as file:
        file.write(content)


def generate_fallback_page(filepath, language_code, dry_run=False):
    translation_path = filepath.replace('.md', f'.{language_code}.md')
    print(f"Creating fallback page for lang {language_code}, "
          + f"from {translation_path} to {filepath}")
    if not dry_run:
        copy2(filepath, translation_path)
        add_missing_translation_warning(translation_path)


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
            generate_fallback_pages_if_needed(os.path.join(root, dirname), dry_run=dry_run)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.set_defaults(dry=False)
    parser.add_argument('--dry', dest='dry', action='store_true')
    args = parser.parse_args()
    generate_fallback_pages_if_needed(os.path.join(os.getcwd(), 'content/api'), dry_run=args.dry)
    generate_fallback_pages_if_needed(os.path.join(os.getcwd(), 'content/cases'), dry_run=args.dry)
    generate_fallback_pages_if_needed(os.path.join(os.getcwd(), 'content/docs'), dry_run=args.dry)
    generate_fallback_pages_if_needed(os.path.join(os.getcwd(), 'content/news'), dry_run=args.dry)
    # Continue build
    os.removedirs("public")
    os.system("hugo -d public")
