---
permalink: /cellfinder
author_profile: true
title: "cellfinder"
---
### *Automated 3D cell detection and registration of whole-brain images*
## [GitHub](https://github.com/brainglobe/cellfinder)

cellfinder is software from the [Margrie Lab](https://www.sainsburywellcome.org/web/groups/margrie-lab) at the
[Sainsbury Wellcome Centre](https://www.sainsburywellcome.org/web/), [UCL](https://www.ucl.ac.uk/) for automated 3D cell detection and registration
of whole-brain images (e.g. serial two-photon or lightsheet imaging).

<img src='https://brainglobe.info/images/cells.png' width="800">

cellfinder can:
* Detect labelled cells in 3D in whole-brain images (many hundreds of GB)
* Register the image to an atlas (such as the [Allen Mouse Brain Atlas](https://atlas.brain-map.org/atlas?atlas=602630314))
* Segment the brain based on the reference atlas
* Calculate the volume of each brain area, and the number of labelled cells within it
* Transform everything into standard space for analysis and visualisation



### Introduction
cellfinder takes a stitched, but otherwise raw whole-brain dataset with at least
two channels:
* Background channel (i.e. autofluorescence)
* Signal channel, the one with the cells to be detected:

![raw](https://raw.githubusercontent.com/brainglobe/cellfinder/master/resources/raw.png)
**Raw coronal serial two-photon mouse brain image showing labelled cells**


### Cell candidate detection
Classical image analysis (e.g. filters, thresholding) is used to find
cell-like objects (with false positives):

![raw](https://raw.githubusercontent.com/brainglobe/cellfinder/master/resources/detect.png)
**Candidate cells (including many artefacts)**


### Cell candidate classification
A deep-learning network (ResNet) is used to classify cell candidates as true
cells or artefacts:

![raw](https://raw.githubusercontent.com/brainglobe/cellfinder/master/resources/classify.png)
**Cassified cell candidates. Yellow - cells, Blue - artefacts**

### Registration and segmentation (brainreg)
Using [brainreg](https://github.com/brainglobe/brainreg),
cellfinder aligns a template brain and atlas annotations (e.g.
the Allen Reference Atlas, ARA) to the sample allowing detected cells to be assigned
a brain region.

This transformation can be inverted, allowing detected cells to be
transformed to a standard anatomical space.


![raw](https://raw.githubusercontent.com/brainglobe/cellfinder/master/resources/register.png)
**ARA overlaid on sample image**

### Analysis of cell positions in a common anatomical space
Registration to a template allows for powerful group-level analysis of cellular
disributions. *(Example to come)*


### Installation
`pip install cellfinder`

For more detailed instructions, see the
[documentation](https://docs.brainglobe.info/cellfinder/) or
[ask a question](https://forum.image.sc/tag/brainglobe)

### Contributing

We're interested in supporting as many applications as possible. If you have ideas, or want to contribute please
[get in touch](https://forum.image.sc/tag/brainglobe) or raise an issue on the
[GitHub repository](https://github.com/brainglobe/cellfinder)
