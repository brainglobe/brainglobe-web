from loguru import logger
from rich import print
from rich.table import Table
from mdutils.mdutils import MdUtils

import semanticscholar as sch


from myterial import pink, blue_light

'''
    Searches google scholar for papers using brainglobe's tools
'''

AUTHORS = (
    '34308754', # Federico Claudi
    '3853277', # Adam L. Tyson
    '8668066', # Luigi petrucco
)
KEYWORDS = ('brainglobe', 'brainrender', 'cellfinder', 'brainreg')

def fetch_citations():
    '''
        Fetches citations semantic scholar, for each author in the list
        get all publications and only keep the ones relevant for brainglobe.
        Then, use these publications to find papers citing them
    '''
    citations = []
    brainglobe_papers =  dict(
        id = [],
        year = [],
        title = [],
        authors = [],
        link=[],
    )
    citing_brainglobe =  dict(
        id = [],
        year = [],
        title = [],
        authors = [],
        link=[],
    )

    # loop over authors
    logger.info('Getting brainglobe papers')
    for author_n, author_id in enumerate(AUTHORS):
        logger.debug(f'Fetching for author {author_n+1}/{len(AUTHORS)}')
        author = sch.author(author_id)

        if not len(author.keys()):
            raise ValueError('Could not fetch author data, probably an API timeout error, wait a bit.')

        # loop over papers
        for paper in author['papers']:
            paper = sch.paper(paper['paperId'])
            if not paper or paper['abstract'] is None:
                continue

            matched_keywords = [kw for kw in KEYWORDS if kw in paper['abstract'].lower()]

            # add it to the list of brainglobe papers
            if matched_keywords:
                if paper['corpusId'] in brainglobe_papers['id']:
                    continue  # skip duplicates
                brainglobe_papers['id'].append(paper['corpusId'])
                brainglobe_papers['year'].append(str(paper['year']))
                brainglobe_papers['authors'].append([auth['name'] for auth in paper['authors']])
                brainglobe_papers['title'].append(paper['title'])
                brainglobe_papers['link'].append(paper['url'])

                citations.append(paper['citations'])
    logger.info(f'Found {len(brainglobe_papers["id"])} brainglobe papers')
    logger.info('Getting papers citing our work')

    for paper_citations in citations:
        for paper in paper_citations:
            if paper['paperId'] in citing_brainglobe['id']:
                continue  # avoid duplicates
            citing_brainglobe['id'].append(paper['paperId'])
            citing_brainglobe['year'].append(str(paper['year']))
            citing_brainglobe['title'].append(paper['title'])
            citing_brainglobe['authors'].append([auth['name'] for auth in paper['authors']])
            citing_brainglobe['link'].append(paper['url'])

    logger.info(f'Found {len(citing_brainglobe["id"])} papers citing brainglobe')            

    return {**brainglobe_papers, **citing_brainglobe}


def print_citations(citations):
    '''
        prints a list of citations as a rich tble
    '''
    tb = Table(box=None, header_style=f'bold {pink}')
    tb.add_column('Year', justify='right', style='dim')
    tb.add_column('Title', style=blue_light)
    tb.add_column('Authors')

    for n in range(len(citations['id'])):
        tb.add_row(
            citations['year'][n],
            citations['title'][n],
            ', '.join(citations['authors'][n]),
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
    mdFile.new_header(level=1, title='Papers citing BrainGlobe tools ')
    
    years = sorted(set(citations['year']))
    for adding_year in years:
        mdFile.new_header(level=2, title=adding_year)

        # add papers
        for n in range(len(citations['id'])):
            year = citations['year'][n]
            link = citations['link'][n]

            if year != adding_year:
                continue

            mdFile.new_header(level=3, title=
                mdFile.new_inline_link(link=link, text=citations['title'][n])
            )

    # add 'in the press'
    mdFile.write("""
# BrainGlobe reported in press/online
### [Why These Python Coders are Joining the napari Community](https://cziscience.medium.com/why-these-python-coders-are-joining-the-napari-community-c0af6bb6ee3a)

_Chan Zuckerberg Science Initiative (Medium), June 2021_

### [Using deep learning to aid 3D cell detection in whole brain microscopy images](https://www.sainsburywellcome.org/web/blog/using-deep-learning-aid-3d-cell-detection-whole-brain-microscopy-images)

_Sainsbury Wellcome Centre Blog, June 2021_

### [Brainrender: visualising brain data in 3D](https://www.sainsburywellcome.org/web/blog/brainrender-visualising-brain-data-3d)

_Sainsbury Wellcome Centre Blog, March 2021_

### [Cellfinder: Harnessing the power of deep learning to map the brain](https://www.sainsburywellcome.org/web/blog/cellfinder-harnessing-power-deep-learning-map-brain)

_Sainsbury Wellcome Centre Blog, April 2020_

### [The best neuroscience stories from April 2020](https://www.scientifica.uk.com/neurowire/the-best-neuroscience-stories-from-april-2020)

_NeuroWire (Scientifica), April 2020_
    """)

    # save
    mdFile.create_md_file()

    # remove extra empty lines at top of file
    with open('_pages/references.md', 'r') as fin:
        content = fin.read()
    with open('_pages/references.md', 'w') as fout:
        fout.write(content.replace('\n\n\n\n', ''))

if __name__ == '__main__':
    citations = fetch_citations()
    # print_citations(citations)
    make_citations_markdown(citations)