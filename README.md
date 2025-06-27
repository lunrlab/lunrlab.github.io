# LUNR Lab Website

## Files

- `index.html`: The HTML file for the main page of the website.
- `index.css`: The CSS file for styling the website.
- `people.html`: The HTML file for the people page of the website.
- `publications.html`: The HTML file for the publications page of the website.
- `bibtex_js.js`: The JavaScript file to render information from the bib files in the Publications page.
- `images/`: Directory containing images used in the website.
- `parse_bib_file.py`: Python script to parse `.bib` files into structured data
- `process_bib_file.py`: Python script that uses `parse_bib_file.py`, performs filtering and creates a processed `.bib` file to be rendered in the Publications page.

## Installation

```
conda create -n lunr_lab_website python=3.10
conda activate lunr_lab_website
pip install -r requirements.txt
```

## Script Usage

First, use Google Scholar's export all citations button as part of the "Cite" menu to download a `.bib` file of all publications. Save this file as `raw_nb_scholar.bib`.

Then, run the following command to process the `.bib` file:

```bash
python process_bib_file.py --bibfile raw_nb_scholar.bib --output_file nb_scholar.bib
```

If there are bib-related errors (such as duplicate entries), they will be pointed out one by one on this script run and need to be fixed in the original bibfile, before the output file can be generated.