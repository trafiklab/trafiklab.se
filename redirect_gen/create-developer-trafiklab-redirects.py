import os.path
import requests


def create_redirect(path: str):
    content = \
        f"""<!doctype html>
<html>
  <head>
  <meta http-equiv="refresh" content="0; url=https://developer.trafiklab.se{path}" />
  </head>
  <body>
    This page has moved. You will be redirected shortly. If the page doesn't redirect automatically, click here: 
    <a href="https://developer.trafiklab.se{path}">https://developer.trafiklab.se{path}</a>
  </body>
</html>
"""
    # Write the file
    dir = os.path.dirname(f"./static{path}")
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(f"./static{path}/index.html", 'w+', encoding='utf8') as file:
        file.write(content)


if __name__ == "__main__":
    print("Creating meta-redirects")
    redirects = requests.get(os.getenv('TLAB_MIGRATE_REDIRECTS')).text
    i = 0
    for path in redirects.splitlines():
        create_redirect(path.strip())
        i += 1
    print(f"Created {i} meta-redirects")
