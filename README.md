# LUNR Lab Website

## Files

- `index.html`: The HTML file for the main page of the website.
- `index.css`: The CSS file for styling the website.
- `people.html`: The HTML file for the people page of the website.
- `publications.html`: The HTML file for the publications page of the website.
- `bibtex_js.js`: The JavaScript file to render information from the bib files in the Publications page.
- `site.js`: Publication search, result counts, and year navigation, initialized after the bibliography renders.
- `images/`: Directory containing images used in the website.
- `parse_bib_file.py`: Python script to parse `.bib` files into structured data
- `process_bib_file.py`: Python script that uses `parse_bib_file.py`, performs filtering and creates a processed `.bib` file to be rendered in the Publications page.

## Local preview

The website is static and does not require a build step. From the repository root:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/` and use the navigation to review all three pages.
Use HTTP rather than opening `publications.html` with `file://`, which can block
the bibliography request. Hard refresh with `Cmd+Shift+R` if styles appear stale.
Bootstrap and bibliography dependencies load from CDNs and require network access.

Shared colors, typography, and responsive layouts are in `index.css`. Keep the
layout compact, with readable body text and page links in the main navigation.
Publication search matches titles, authors, and venues;
year navigation is generated from the rendered bibliography.

**Keep edits local until publication is explicitly approved.** See `AGENTS.md`
for editing and publishing instructions.

## Bibliography tool installation

```
conda create -n lunr_lab_website python=3.10
conda activate lunr_lab_website
pip install -r requirements.txt
```

## Script Usage

The publications page lists Google Scholar records from 2020 onward, newest first,
and links to the full Scholar profile for earlier work. `nb_scholar.bib` was updated
from Niranjan Balasubramanian's profile on October 16, 2026. Duplicate records for
the same 2024 workshop paper were consolidated, and the DIAMONDs title retains
the corrected text. Publication titles link to their Scholar records. The optional
`sortdate` field (`YYYYMMDD`, using `00` for unknown months or days) orders entries
within each year; retain it when refreshing the bibliography.

First, use Google Scholar's export all citations button as part of the "Cite" menu to download a `.bib` file of all publications. Save this file as `raw_nb_scholar.bib`.

Then, run the following command to process the `.bib` file:

```bash
python process_bib_file.py --bibfile raw_nb_scholar.bib --output_file nb_scholar.bib
```

If there are bib-related errors (such as duplicate entries), they will be pointed out one by one on this script run and need to be fixed in the original bibfile, before the output file can be generated.
Make sure to check the output bib file and remove any LaTeX/Markdown formatting (e.g., see @ghosh2025texttt entry).
