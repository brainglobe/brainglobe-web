from loguru import logger
from scholarly import scholarly
from rich import print
from rich.table import Table
from mdutils.mdutils import MdUtils



from myterial import pink, blue_light

'''
    Searches google scholar for papers using brainglobe's tools
'''

def fetch_citations():
    '''
        Fetches citations from Google Scholar to identify papers using/citing
        brainglobe's tools
    '''
    QUERY = '"brainglobe"'
    logger.debug(f'Searching for citations with query string: {QUERY}')
    citations = list(scholarly.search_pubs(QUERY, year_low=2018, sort_by='relevance'))
    logger.debug(f'Found {len(citations)} publications with query: {QUERY}')
    return citations


def print_citations(citations):
    '''
        prints a list of citations as a rich tble
    '''
    tb = Table(box=None, header_style=f'bold {pink}')
    tb.add_column('Year', justify='right', style='dim')
    tb.add_column('Title', style=blue_light)
    tb.add_column('Authors')

    for entry in citations:
        tb.add_row(
            entry['bib']['pub_year'],
            entry['bib']['title'],
            ' '.join(entry['bib']['author'])
        )

    print(tb)

def make_citations_markdown(citations):
    '''
        Replaces ./_pages/references.md to update with the most recent 
        citations of papers using/citing brainglobe
    '''
    logger.debug('Updating markdown file')

    # create markdown file
    mdFile = MdUtils(file_name='_pages/references.md')
    

    # add metadata & header
    mdFile.write(text="""
---
permalink: /references
author_profile: true
title: "References"
---
    """)
    mdFile.new_header(level=1, title='Papers citing cellfinder ')
    
    years = sorted(set([paper['bib']['pub_year'] for paper in citations]))
    for year in years:
        mdFile.new_header(level=2, title=year)

        # add papers
        for paper in citations:
            if paper['bib']['pub_year'] != year:
                continue

            if 'eprint_url' not in paper.keys():
                link = paper['url_scholarbib']
            else:
                link = paper['eprint_url']
            mdFile.new_header(level=3, title=
                mdFile.new_inline_link(link=link, text=paper['bib']['title'])
            )

    # add 'in the press'
    mdFile.write("""
# cellfinder reported in press/online


### [Cellfinder: Harnessing the power of deep learning to map the brain](https://www.sainsburywellcome.org/web/blog/cellfinder-harnessing-power-deep-learning-map-brain)

_Sainsbury Wellcome Centre Blog, April 2020_

### [The best neuroscience stories from April 2020](https://www.scientifica.uk.com/neurowire/the-best-neuroscience-stories-from-april-2020)

_NeuroWire (Scientifica), April 2020_
    """)
    mdFile.create_md_file()

if __name__ == '__main__':
    citations = fetch_citations()
    print_citations(citations)
    make_citations_markdown(citations)