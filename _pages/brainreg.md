---
permalink: /brainreg
author_profile: true
title: "brainreg"
---
## Automated 3D brain registration with support for multiple species and atlases.

### For full details see the [GitHub repository.](https://github.com/brainglobe/brainreg)



brainreg is an update to
[amap](https://github.com/SainsburyWellcomeCentre/amap_python) (itself a port
of the [original Java software](https://www.nature.com/articles/ncomms11879))
to include multiple registration backends, and to support the many atlases
provided by the [BrainGlobe Atlas API](https://brainglobe.info/atlas-api).

The aim of brainreg is to register the template brain
(e.g. from the [Allen Reference Atlas](https://mouse.brain-map.org/static/atlas))
to the sample image. Once this is complete, any other image in the template
space can be aligned with the sample (such as region annotations, for
segmentation of the sample image). The template to sample transformation
can also be inverted, allowing sample images to be aligned in a common
coordinate space.

To do this, the template and sample images are filtered, and then registered in
a three step process (reorientation, affine registration, and freeform
registration.) The resulting transform from template to standard space is then
applied to the atlas.

Full details of the process are in the
[original aMAP paper](https://www.nature.com/articles/ncomms11879).
![reg_process](https://user-images.githubusercontent.com/13147259/143553945-a046e918-7614-4211-814c-fc840bb0159d.png)


### Installation
`pip install brainreg`

For more detailed instructions, see the
[documentation](https://docs.brainglobe.info/brainreg/) or
[ask a question](https://forum.image.sc/tag/brainglobe).


## brainreg-segment
#### Segmentation of 1/2/3D brain structures in a common anatomical space

`brainreg-segment` is a companion to [`brainreg`](https://github.com/brainglobe/brainreg) allowing manual segmentation of regions/objects within the brain (e.g. injection sites, probes etc.) allowing for automated analysis of brain region distribution, and visualisation (e.g. in [brainrender](https://github.com/BrancoLab/brainrender)).

### Installation

brainreg-segment comes bundled with [`brainreg`](https://github.com/brainglobe/brainreg), so see the [brainreg installation instructions](https://docs.brainglobe.info/brainreg/installation).

brainreg-segment can be installed on it's own (`pip install brainreg-segment`), but you will need to register your data with brainreg first.

### Contributing

We're interested in supporting as many applications as possible. If you have ideas, or want to contribute please
[get in touch](https://forum.image.sc/tag/brainglobe) or raise an issue on the
[GitHub repository](https://github.com/brainglobe/brainreg)
