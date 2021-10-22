import argparse
import os
import os.path
import platform
from shutil import copy2


def has_translation(filepath, language_code):
    translated_path = filepath.replace('.md', f'.{language_code}.md')
    return os.path.exists(translated_path)


def add_missing_translation_warning(filepath: str):
    warning = """
    
{{% warning %}}
**Obs:** Detta innehåll finns inte tillgängligt på svenska. Därför ser du engelska versionen.
Om du tycker att denna sida borde översättas till svenska, kan du skriva till oss på [support.trafiklab.se](https://suport.trafiklab.se).

Om du vill se webbsidan på engelska, [klicka här](/en/).
{{% /warning %}}
    
    """
    # Read in the file
    with open(filepath, 'r', encoding='utf8') as file:
        content = file.read()

    # Replace the target string
    content = content.replace('---', '', 1)  # Remove the top --- marker
    # Add the warning
    content = content.replace('---', '---' + warning, 1)
    # Add the leading --- back, along with a property to indicate which page acted as the source
    # Remove the leading .../content/ part of the path
    content = '---\ngenerated_fallback_page_source: true"' + content

    # Write the file out again
    with open(filepath, 'w', encoding='utf8') as file:
        file.write(content)


def generate_fallback_page(source_file_path, language_code, dry_run=False):
    translation_path = source_file_path.replace('.md', f'.{language_code}.md')
    print(f"Creating fallback page for lang {language_code}, "
          + f"from {translation_path} to {source_file_path}")
    if not dry_run:
        copy2(source_file_path, translation_path)
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


def replace_ssh_submodules_with_http():
    # DigitalOcean apps platform cannot checkout SSH submodules at the moment
    # Read in the file
    with open(".gitmodules", 'r', encoding='utf8') as file:
        content = file.read()
    # Replace the target string
    content = content.replace('git@github.com:', 'https://github.com/')
    # Write the file out again
    with open(".gitmodules", 'w', encoding='utf8') as file:
        file.write(content)


def checkout_theme_submodule():
    cwd = os.getcwd()
    os.chdir('themes/trafiklab-2021')
    ssh_url = os.popen('git remote get-url origin').read()
    https_url = ssh_url.replace('git@github.com:', 'https://github.com/')
    print('Fetching theme submodule from ' + https_url, flush=True)
    os.system('git remote set-url origin ' + https_url)
    os.system('git checkout')
    os.chdir(cwd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.set_defaults(dry=False)
    parser.add_argument('--dry', dest='dry', action='store_true')
    parser.add_argument('--without-git-fix', dest='git_fix', action='store_false')
    args = parser.parse_args()
    generate_fallback_pages_if_needed(os.path.join(os.getcwd(), 'content/api'), dry_run=args.dry)
    generate_fallback_pages_if_needed(os.path.join(os.getcwd(), 'content/cases'), dry_run=args.dry)
    generate_fallback_pages_if_needed(os.path.join(os.getcwd(), 'content/docs'), dry_run=args.dry)
    generate_fallback_pages_if_needed(os.path.join(os.getcwd(), 'content/news'), dry_run=args.dry)
    # Continue build
    if args.git_fix:
        replace_ssh_submodules_with_http()
        checkout_theme_submodule()
    if os.path.exists("public"):
        os.removedirs("public")
    exitCode = os.system("hugo -d public --minify")
    if platform.system() != "Windows":
        exitCode = os.WEXITSTATUS(exitCode)
    print(f"Hugo build process exited with code {exitCode}")
    exit(exitCode)

