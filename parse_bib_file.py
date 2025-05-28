#!/usr/bin/python3
# Author: Nicolas Bohm Agostini
# Date: 2022-Dec-12
# Version: 1.1
# License: MIT

# Changelog:
# 1.1 - added alternative way of printing

# @brief: This script parses a bib file and prints it in a specific format
# @usage: python3 parse-bib-file.py <bibfile>
# if no bibfile is provided, the script will look for a file named "works.bib"

# Dependencies:
# create a virtual environment
# python3 -m venv venv
# source venv/bin/activate
# pip install pybtex

import os
import re
from pybtex.database.input import bibtex
import argparse

# Function to load the data from a bib file into a dictionary


def load_bib(bibfile):
    bib_data = bibtex.Parser().parse_file(bibfile)
    list_of_entries = bib_data.entries

    # BibliographyData(
    # entries=OrderedCaseInsensitiveDict([
    # ('agostini2022sodaopt', Entry('inproceedings',
    #   fields=[
    #     ('bo
    #     oktitle', 'IEEE/ACM International Conference on Computer-Aided Design'),
    #     ('series', "ICCAD'22"), ('title', '{An MLIR-based Compiler Flow for System-Level Design and Hardware Acceleration}'),
    #     ('year', '2022'),
    #     ('volume', ''),
    #     ('number', ''),
    #     ('pages', ''),
    #     ('publisher', 'IEEE'),
    #     ('address', 'San Diego, CA'),
    #     ('doi', '10.1145/3508352.3549424')],
    #   persons=OrderedCaseInsensitiveDict([('author', [Person('Bohm Agostini, Nicolas'), Person('Curzel, Serena'), Person('Amatya, Vinay'), Person('Tan, Cheng'), Person('Minutoli, Marco'), Person('Castellana, Vito Giovanni'), Person('Manzano, Joseph'), Person('Kaeli, David'), Person('Tumeo, Antonino')])])))]),
    #   preamble=[])
    # print(bib_data)

    # OrderedCaseInsensitiveDict([('agostini2022sodaopt', Entry('inproceedings',
    # fields=[
    #('booktitle', 'IEEE/ACM International Conference on Computer-Aided Design'),
    #('series', "ICCAD'22"), ('title', '{An MLIR-based Compiler Flow for System-Level Design and Hardware Acceleration}'),
    #('year', '2022'),
    #('volume', ''),
    #('number', ''),
    #('pages', ''),
    #('publisher', 'IEEE'),
    #('address', 'San Diego, CA'),
    # ('doi', '10.1145/3508352.3549424')],
    # persons=OrderedCaseInsensitiveDict([('author', [Person('Bohm Agostini, Nicolas'), Person('Curzel, Serena'), Person('Amatya, Vinay'), Person('Tan, Cheng'), Person('Minutoli, Marco'), Person('Castellana, Vito Giovanni'), Person('Manzano, Joseph'), Person('Kaeli, David'), Person('Tumeo, Antonino')])])))])
    # print(list_of_entries)
    return bib_data

# function find and remove braces from a string at any position
# and other special characters: \, {, }, '


def remove_braces(s):
    return re.sub(r'\{|\}|\\', '', s)

def remove_parenthesis(s):
    return re.sub(r'\(|\)', '', s)

# function to remove leading number and spaces from a string
def remove_leading_number(s):
    return re.sub(r'^\d+\s', '', s)

# function to remove trailing expression in parenthesis from a string
# input "something like this (with parenthesis)"
# output "something like this"
def remove_trailing_parenthesis(s):
    return re.sub(r'\s\(.+\)', '', s)

def process_title(s):
    s = remove_braces(s)
    s = remove_leading_number(s)
    s = remove_trailing_parenthesis(s)
    return s

# retrieve expression in parenthesis
# input: 2021 {IEEE}/{ACM} International Conference On Computer Aided Design ({ICCAD})
# input: a string (ICCAD)
# output: (ICCAD)
def get_expr_in_parenthesis(s):
    # if there is no parenthesis, return the string
    if not re.search(r'\(.+\)', s):
        return s
    else:
        return re.search(r'\(.+\)', s).group()
    
# function to format the journal name
# input: 2021 {IEEE}/{ACM} International Conference On Computer Aided Design ({ICCAD})
# output: (ICCAD)
def format_journal_name(journal):
    tmp = get_expr_in_parenthesis(journal)
    tmp = remove_braces(tmp)
    tmp = remove_parenthesis(tmp)
    return tmp

# function to transform a number into 1st, 2nd, 3rd, 4th, etc.
def ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, "th")

# function join the author name and fix the case. Only the first letter is capitalized
def full_name(author):
    tmp = ' '.join(author.first_names +
                   author.middle_names + author.last_names)
    return tmp.title()

def last_first_name(author):
    firstname_initials = ['{}. '.format(x[0]) for x in author.first_names]
    middle_initials = ['{}.'.format(x[0]) for x in author.middle_names]
    tmp = ' '.join(author.last_names+[',']+firstname_initials+middle_initials)
    tmp = re.sub(r'\s+', ' ', tmp)
    tmp = re.sub(r'\.\s', '.', tmp)
    tmp = re.sub(r'\s+,', ',', tmp)
    return tmp.title()

# function to get the position of an author in the list of authors
def get_author_position(author, authors):
    for i in range(len(authors)):
        if full_name(authors[i]) == author:
            return i
    return -1

# function to print entries of a specific type
# must print the following fields for @articles: title, author, year, journal
# must print the following fields for @inproceedings: title, author, year, booktitle
def print_entries_of_type(bib, entry_type):
    for entry in bib.entries.values():
        if entry.type == entry_type:
            # print on the same line:
            print(ordinal(get_author_position('Nicolas Bohm Agostini',
                  entry.persons['author'])+1), 
                  'author of', len(entry.persons['author']), 
                  'in: ', end='')
            print(remove_braces(entry.fields['title']), end='. ')
            for author in entry.persons['author']:
                author_name = full_name(author)
                author_name = remove_braces(author_name)
                if author_name == 'Nicolas Bohm Agostini':
                    # perform last print and break the loop
                    print(author_name, end=', et al. ')
                    break
                print(author_name, end=', ')
            print(entry.fields['year'], end='. ')
            if entry_type == 'article':
                print(process_title(entry.fields['journal']), end='.')
            elif entry_type == 'inproceedings':
                print(process_title(entry.fields['booktitle']), end='.')
            print()

# function to print entries of a specific type
# must print the following fields for @articles: title, author, year, journal
# must print the following fields for @inproceedings: title, author, year, booktitle
# this generates entries with the format:
# Paper in ICPE2021: Gutierrez, J., Shi, D., Agostini, N.B., and Kaeli, D., Performance Evaluation and Improvement of Computer Vision Applications on Heterogeneous Edge Computing Devices
def print_entries_of_type2(bib, entry_type):
    for entry in bib.entries.values():
        if entry.type == entry_type:
            # print on the same line:
            if entry_type == 'article':
                print('Article in', end=' ')
                print(format_journal_name(entry.fields['journal']), end='')
            elif entry_type == 'inproceedings':
                print('Paper in', end=' ')
                print(format_journal_name(entry.fields['booktitle']), end='')
            print(entry.fields['year'], end='. ')
            count = 0
            for author in entry.persons['author']:
                count += 1
                if count > 4:
                    print('et al.', end=', ')
                    break
                author_name = last_first_name(author)
                author_name = remove_braces(author_name)
                print(author_name, end=', ')
            print(remove_braces(entry.fields['title']), end='.')
            print()
                

# function to count the number of entries of a given type


def count_entries(bib, entry_type):
    count = 0
    for entry in bib.entries.values():
        if entry.type == entry_type:
            count += 1
    return count

# main function


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bibfile', nargs='?', default='works.bib')

    args = parser.parse_args()
    bibfile = args.bibfile

    # print full path to file
    bibfile_path = os.path.abspath(bibfile)
    print('Processing file:', bibfile_path, '\n')
    bib = load_bib(bibfile)

    # print count of journal entries
    print('Journals: ', count_entries(bib, 'article'))
    print_entries_of_type(bib, 'article')
    print()
    print('Proceedings: ', count_entries(bib, 'inproceedings'))
    print_entries_of_type(bib, 'inproceedings')

    # print('Journals: ', count_entries(bib, 'article'))
    # print_entries_of_type2(bib, 'article')
    # print()
    # print('Proceedings: ', count_entries(bib, 'inproceedings'))
    # print_entries_of_type2(bib, 'inproceedings')


if __name__ == '__main__':
    main()