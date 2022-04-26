# Trafiklab.se

This project contains the Trafiklab.se website, based on the Hugo framework. Both the layout/theme and content are
stored in this repository.

Continuous deployment is used to

- automatically deploy the **main** branch to https://trafiklab.se.
- automatically deploy the **development** branch to https://staging.trafiklab.se.

## Rendering the website

The website can be rendered locally. In order to do so, follow the following steps:

- Ensure Hugo is installed and in your PATH. You should be able to run the "hugo" command in the terminal of your
  choice. If you do not have Hugo on your computer, grab the latest **extended release**
  from https://github.com/gohugoio/hugo/releases.
- Run `hugo serve` from the project root to render all pages, making them accessible at port 1313 (by default).
- You can now alter the source, the development server will update all changed pages on the fly.

_Note:_ A python script is used to automatically create Swedish pages from English content when no Swedish content is
available. Since this script isn't run when running the development server, some pages will be missing from the Swedish
development instance.

## Editing content

Every page is stored as a markdown file. Each file contains so-called "front-matter" at the top, containing metadata
such as the title and publish date, as well as which layout which should be used in case one wants to deviate from the
default layout for a section. Below the front-matter all page content is written as markdown.

When creating a folder, which also should have its own page (for example, if both `/api` and `/api/gtfs-regional` need
to be pages with content in the `api` folder), the "index" file should be called `_index.md`.
