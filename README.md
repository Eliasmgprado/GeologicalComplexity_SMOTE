# Geological Complexity (Fractal Dimension) and SMOTE
Implementation and Data repository for
**Modeling of Cu-Au Prospectivity in the Carajás mineral province (Brazil) through Machine Learning: Dealing with Imbalanced Training Data**
## Authors
[Elias M. G. Prado](mailto:lukas.mosser15@imperial.ac.uk) [Twitter](https://twitter.com/porestar)<sup>1,2</sup>
[Carlos Roberto de Souza Filho](https://www.imperial.ac.uk/people/o.dubrule)<sup>2</sup>
[Emmanuel John M. Carranza](https://www.imperial.ac.uk/people/m.blunt)<sup>3</sup>
[João Gabriel Motta](https://www.imperial.ac.uk/people/m.blunt)<sup>2</sup>

<sup>1</sup>*Centre for Technological Development, Geological Survey of Brazil - CPRM*

<sup>2</sup>*Institute of Geosciences, University of Campinas - UNICAMP*

<sup>3</sup>*Department of Geology, University of KwaZulu-Natal*

## Results
### Geological Complexity
Geological Complexity Map of Carajás Mineral Province, Pará, Brazil.
![Beadpack Comparison](https://github.com/LukasMosser/PorousMediaGan/blob/master/paper/figures/beadpack_comparison.png)
### SMOTE


<img align="center" width="100%" height="100%" src="https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/imgs/Hodkiewicz.png"/>

## Methodology
### Geological Complexity
![Process Overview](https://github.com/Eliasmgprado/GeologicalComplexity/blob/master/imgs/Hodkiewicz.png)
#### References
- Ford, A., Blenkinsop, T.G., 2008. Evaluating geological complexity and complexity gradients as controls on copper mineralisation, Mt Isa Inlier. Aust. J. Earth Sci. 55, 13–23.
- Hodkiewicz, P., 2003, The Interplay Between Physical and Chemical Processes in the Formation of World-Class Orogenic Gold Deposits in the Eastern Goldfields Province , Western Australia.
### SMOTE
## Instructions
### Pre-requisites
- To run any of the `jupyter` notebooks follow instructions [here](http://jupyter.org/install.html) or install via pip.
```bash
pip install jupyter
```
- In addition we make use of following packages:

    - gdal                      2.3.3  
    - geopandas                 0.4.1  
    - pandas                    0.24.2  
    - matplotlib                3.0.3  
    - rasterio                  1.0.21  
    - numpy                     1.16.3  
    - scipy                     1.2.1  

- We recommend the use of [anaconda](https://www.continuum.io/downloads)
- After installing the packages Clone this repo
```bash
git clone https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE
cd PorousMediaGAN
```
- The codes with instructions and comments are in the `jupyter` notebooks inside the `GeologicalComplexity` and `SMOTE` folders

## Citation
If you use our code for your own research, we would be grateful if you cite our publication
```
@article{EliasPrado2020,
	title={Modeling of Cu-Au Prospectivity in the Carajás mineral province (Brazil) through Machine Learning: Dealing with Imbalanced Training Data},
	author={Prado, E.M.G. and Souza Filho, C.R. and Carranza, E.J.M. and Motta, J.G.},
	journal={Ore Geology Reviews},
	year={2020}
}
```

## Acknowledgement
The code used for Geological Complexity is based on the works [Ford and Blenkinsop (2008)](https://www.tandfonline.com/doi/full/10.1080/08120090701581364) and [Hodkiewicz (2003)](https://research-repository.uwa.edu.au/en/publications/the-interplay-between-physical-and-chemical-processes-in-the-form)
and the code used for SMOTE is based on the work [Chawla et al. (2002)](https://arxiv.org/pdf/1106.1813.pdf).
