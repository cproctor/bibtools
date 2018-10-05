# BibTools

Tools for data analysis using bibtex bibliographies. For example, 
you could convert a directory of `.bib` files into a CSV like so:

    import bibtools
    reader = bibtools.reader.bib_dir_reader("bibliographies")
    dataframe = bibtools.utils.entries_to_df(reader)
    dataframe.to_csv("publications.csv")

## Installation

    git clone https://github.com/cproctor/bibtools.git
    pip install -r requirements.txt
