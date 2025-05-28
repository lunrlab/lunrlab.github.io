import os
import argparse

from parse_bib_file import load_bib

def argument_parser():
    parser = argparse.ArgumentParser(description="Process a BibTeX file to extract entries.")
    parser.add_argument("--bibfile", required=True, type=str, help="Path to the BibTeX file")
    parser.add_argument("--output_file", required=True, type=str, help="Path to the processed, output BibTeX file")
    return parser

def main(args):
    raw_contents = load_bib(args.bibfile)

    sbu_start_year = 2016

    filtered_contents = []
    for entry in raw_contents.entries.values():
        try:
            if int(entry.fields['year']) < sbu_start_year:
                continue
        except:
            # in case year is not listed in the record
            continue
        filtered_contents.append(entry)
    filtered_contents.sort(key=lambda entry: int(entry.fields['year']), reverse=True)

    output_file = args.output_file
    count = 0
    with open(output_file, "w") as f:
        for entry in filtered_contents:
            count += 1
            f.write(entry.to_string("bibtex") + "\n\n")
    print(f"Filtered contents (n={count}) written to {output_file}")

if __name__ == "__main__":
    parser = argument_parser()
    args = parser.parse_args()

    main(args)