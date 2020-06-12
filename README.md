# Geological Complexity (Fractal Dimension) and SMOTE
Code repository for
**Modeling of Cu-Au Prospectivity in the Carajás mineral province (Brazil) through Machine Learning: Dealing with Imbalanced Training Data**
with implementation of Geological complexity and SMOTE algorithms.
```
[Link to article](https://www.sciencedirect.com/science/article/pii/S0169136819308819)
[DOI - https://doi.org/10.1016/j.oregeorev.2020.103611](https://doi.org/10.1016/j.oregeorev.2020.103611)
```

## Authors
[Elias M. G. Prado](mailto:elias.prado@cprm.gov.br), [ResearchGate](https://www.researchgate.net/profile/Elias_Prado3)<sup>1,2</sup>  
[Carlos Roberto de Souza Filho](https://portal.ige.unicamp.br/en/faculty/carlos-roberto-de-souza-filho)<sup>2</sup>  
[Emmanuel John M. Carranza](https://www.ukzn.ac.za/inaugural-lectures/inauglec-2018/emmanuel-john-m-carranza/)<sup>3</sup>  
[João Gabriel Motta](https://www.researchgate.net/profile/Joao_Motta)<sup>2</sup>  
<sup>1</sup>*Centre for Technological Development, Geological Survey of Brazil - CPRM*  
<sup>2</sup>*Institute of Geosciences, University of Campinas - UNICAMP*  
<sup>3</sup>*Department of Geology, University of KwaZulu-Natal*  

# Geological Complexity
## Results
Geological Complexity Map of Carajás Mineral Province (CMP), Pará, Brazil. (a) Map of faults/fractures was produced by interpretation of shaded-relief images derived from the 30 m resolution Shuttle Radar Topographic Mission (SRTM) (b) Geological Complexity map of CMP.
![Geological Complexity Results](https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/GeologicalComplexity/imgs/GeoComplex_Result.png "Geological Complexity Results")    

## Methodology
The algorithm used for calculating geological complexity was written in Python 3 by Elias Martins Guerra Prado. The algorithm is based on the program developed by Stephan Gardoll, published in Hodkiewicz (2003), to compute fractal dimension, which is based on the box-counting methodology of Hirata (1989). The advantage of this implementation compared to others is that the box-counting calculus is done using matrices (rasters) instead of spatial vectors, considerably reducing the time to compute the fractal dimension for each pixel.

![Geological Complexity Methodology](https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/GeologicalComplexity/imgs/Hodkiewicz.png)

A brief description of the input parameters is given below:
1.	Polygon shapefile with work area boundaries. This polygon defines the limits of the geological complexity map.
2.	Grid spacing. Distance between the points of the fractal dimension grid. The location of each point of the grid defines the center of a fractal box. In this study, there is a 5 km spacing between grid points.
3.	Polyline shapefile with geological contacts and/or faults/fractures. These linear features are sampled by the box-counting method to measure the fractal dimension. In this study, both geological contacts and faults/fractures were used.
4.	Initial box size around each grid point. The initial pixel size used to rasterize the input line features. In this study, a 5 km initial box size was used.
5.	Number of box count levels calculated. The number of times the initial pixel size will be halved. In this study, a five-level box count was used, resulting in box sizes of 5 km, 2.5 km, 1.25 km and 0.625 km

The program output is a raster produced by the interpolation of the fractal dimension for each grid point. The interpolation is done using a two-dimensional minimum curvature spline technique (the resulting surface passes precisely through the input points). 
To compute the geological complexity the algorithm uses the following procedure:
1.	First, the work area shapefile (input #1) is transformed into a raster with a pixel size equal to the grid spacing (input #2).
2.	The work area raster is then converted to a point shapefile, where each point is placed in the center of each pixel. This shapefile is used as the grid for computing the fractal dimensions.
3.	Then, the input line features (input parameter #3) is transformed into a binary raster, where pixels with value 1 indicate the presence of a feature. One raster is created for each box count level (input #5). The pixel size of the first raster is equal to the initial box size parameter (input #4). The pixel size of the other raster files is calculated by halving the initial pixel size N-1 times, where N is the number of box count levels (input #5). 
4.	The fractal dimension for each point of the grid is then determined by computing the sum of the pixels inside a square window, with side equal to two times the initial box size (input #4), centered at the grid point. 
5.	To determine the fractal dimension at each pixel, the slope of the line on a log-log plot of box size (pixel size) and box count result (sum of pixels for each pixel size). The value of the fractal dimension is then assigned to the corresponding grid point.
6.	Finally, the fractal dimension grid is interpolated using a spline function. 

### References
- Ford, A., Blenkinsop, T.G., 2008. Evaluating geological complexity and complexity gradients as controls on copper mineralisation, Mt Isa Inlier. Aust. J. Earth Sci. 55, 13–23.
- Hodkiewicz, P., 2003, The Interplay Between Physical and Chemical Processes in the Formation of World-Class Orogenic Gold Deposits in the Eastern Goldfields Province, Western Australia.

## Instructions
> This algorithm was implemented using `jupyter notebook`
### Pre-requisites
- To run the `jupyter` notebooks follow instructions [here](http://jupyter.org/install.html) or install via pip.
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
cd GeologicalComplexity_SMOTE
```
- The codes with instructions and comments are in the `jupyter` notebooks inside the `GeologicalComplexity` and `SMOTE` folders


# SMOTE
## Results
Mineral Prospectivity Model Flowchart
![Model Flowchart](https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/SMOTE/imgs/Fig4_flowchart.jpg "Model Flowchart")    
    
    
Training F1 scores of SVM models. The scores are arranged by over-sampling/under-sampling rates used to generate the training data points. Models with tendency to over-fit and under-fit are highlighted inside dashed contours. Models trained with same number of mineralized and non-mineralized samples are highlighted in purple.
<p align="center">
<img align="center" src="https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/SMOTE/imgs/Fig5_SVM_heatmaps_f1_train.jpg" width="800" /></p>    


Testing F1 scores of SVM models. The scores are arranged by over-sampling/under-sampling rates used to generate the training data points. Models with tendency to over-fit and under-fit are highlighted inside dashed contours. Models trained with same number of mineralized and non-mineralized samples are highlighted in purple.
<p align="center">
<img src="https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/SMOTE/imgs/Fig6_SVM_heatmaps_f1_test.jpg" width="800" /></p>    


Success-rate curves of SVM-based prospectivity models derived using training data (a) with fixed under-sampling rate of 5% for non-mineralized samples and variable over-sampling rates for mineralized samples ranging from 100-2000%, (b) with fixed over-sampling rate of 100% for mineralized samples and variable under-sampling rates for non-mineralized samples ranging from 5%-100%, and (c) with same number of mineralized and non-mineralized samples. The rate between mineralized and non-mineralized locations for each model is shown in the legend in brackets.
<p align="center">
<img align="center" src="https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/SMOTE/imgs/Fig7_Models_CAPPs.jpg" width="600" /></p>    


Success-rate and prediction-rate curves of CMP Cu-Au prospectivity models. (a) SVM model trained with 2000% over-sampling rate of mineralized class and 100% under-sampling rate of non-mineralized class (balanced class distribution). (b) SVM model trained without over-sampling of mineralized class (100% over-sampling rate) and without under-sampling non-mineralized class (100% under-sampling rate). (c) SVM model trained without over-sampling of mineralized class (100% over-sampling rate) and 5% under-sampling rate of non-mineralized class (balanced class distribution). (d) WofE model trained with the same input features of the SVM models and the original training mineralized locations. Vertical lines highlight which proportion of Carajás area predicted as prospective for Cu-Au deposits covers 100% of training/test (success-rate/prediction-rate) Cu-Au mineralized locations.
![CAPPS](https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/SMOTE/imgs/Fig8_capp.jpg "CAPPS")    


(a) Predictive map for Cu-Au prospectivity obtained by a SVM model trained with 2000% over-sampling rate and 100% under-sampling rate of mineralized and non-mineralized samples, respectively. The map is colored according to the hyperplane distance (distance from the feature vector to the surface computed by the SVM model that defines the boundaries between classes), which is directly proportional to the predicted likelihood of finding a Cu-Au deposit. Dashed polygons in red highlight zones that could be prioritized for Cu-Au exploration according to the interpretation of the prospectivity map. (b) The same predictive map with the target variables used to train and test the model plotted.
![Prospectivity Map](https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/SMOTE/imgs/Fig9_Final%20Model.jpg "Prospectivity Map")    

## Methodology
Check work of [Chawla et al. (2002)](https://doi.org/10.1613/jair.953) for detail on methodology, and the [imbalanced-learn](https://imbalanced-learn.readthedocs.io/en/stable/user_guide.html)<sup>1</sup> page for details on SMOTE algorithm implementation    

<sup>1</sup>*Chawla, N., Bowyer, K.W., Hall, L.O., Kegelmeyer, W.P., 2002. SMOTE: Synthetic minority over-sampling technique. J. Artif. Intell. Res. 16, 321–357. https://doi.org/10.1613/jair.953*

## Instructions
> This is an implamentation of the SMOTE algorithm provided in [imbalanced-learn](https://imbalanced-learn.readthedocs.io/)<sup>1</sup> for ArcGis as a `toolbox`.    
    
<sup>1</sup> *Lemaître, G., Nogueira, F., Aridas, C.K., 2017. Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning. J. Mach. Learn. Res. 18, 1–5.*

### Pre-requisites

- We make use of following packages:

    - imbalanced-learn     0.4.3

- To install the packages in ArcGis 10:
    1. Start Windows command prompt and change your directory to your Arcgis desktop python installation (containing python.exe). Typically something like c:\python27xx\arcgis10.x\
    2.  In the commandprompt type `python -m pip install -I scikit-learn`
    3. Restart ArcMap

- To install the packages in ArcGis Pro:
    1. Close out of ArcGIS Pro
    2. Navigate to the `Start Menu > All Programs > ArcGIS > ArcGIS Pro > right-click and run Python Command Prompt as Administrator`
    3. If using Windows 10, simply type in `Python Command Prompt > right click> Open File Location> right-click and run Python Command Prompt as Administrator`
    6. install the packages by typing in `pip install -U imbalanced-learn`
    7. Once this is done installing, close out of the command prompt and open ArcGIS Pro

- After installing the packages Clone this repo
```bash
git clone https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE
cd GeologicalComplexity_SMOTE
```
- The `toolbox` is inside the `SMOTE` folders

- To add the toolbox to ArcMap 10>:
    1.  Open ArcMap, open `ArcToolbox` and right click in the white space and go to Add Toolbox:
    ![](https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE/blob/master/SMOTE/imgs/tuto_1-1.png)
    2. Browse to and click the toolbox inside the `SMOTE` folder.
    3. The toolbox appears in the `Arctoolbox` pane.

- To add the toolbox to ArcGis Pro:
    1. Open ArcGis Pro, Open the `catalog view` and click `Project` or `Toolboxes` in the `Contents` pane. On the `Catalog` tab on the ribbon, in the `Create` group, click the `Add` drop-down arrow and click `Add Toolbox`.
    2. On the `Insert` tab, in the `Project` group, click the `Toolbox` drop-down arrow Toolbox and click `Add Toolbox`.
    3. Browse to and click the toolbox inside the `SMOTE` folder.
    4. The toolbox appears in the `Catalog` pane and catalog view in the Toolboxes category `Toolbox` folder.





## Citation
If you use our code for your own research, we would be grateful if you cite our publication
```
@article{MARTINSGUERRAPRADO2020103611,
title = "Modeling of Cu-Au Prospectivity in the Carajás mineral province (Brazil) through Machine Learning: Dealing with Imbalanced Training Data",
journal = "Ore Geology Reviews",
pages = "103611",
year = "2020",
issn = "0169-1368",
doi = "https://doi.org/10.1016/j.oregeorev.2020.103611",
url = "http://www.sciencedirect.com/science/article/pii/S0169136819308819",
author = "Elias [Martins Guerra Prado] and Carlos [Roberto de Souza Filho] and Emmanuel [John M. Carranza] and João [Gabriel Motta]",
abstract = "Machine learning (ML) is becoming an appealing tool in various fields of Earth Sciences, especially in mineral prospectivity mapping (MPM) to support mineral exploration. ML algorithms are designed to assume a relatively balanced amount of training data for the estimation of the decision boundaries between the classes of interest (i.e., in MPM: mineralized- and non-mineralized locations). However, in MPM the numbers of mineralized and non-mineralized locations are naturally imbalanced, as the number of known mineral deposit occurrences (as a proxy of mineralized or positive class) are naturally much smaller than the number of non-mineralized locations (the negative class). The use of imbalanced data leads to difficulties in the training of ML models for MPM, due to the learning bias towards the features of the predominant (i.e., negative) class. In the present study, using support vector machine for Cu-Au prospectivity modeling in the Carajás mineral province (Brazil), we evaluated the effects of Synthetic Minority Over-sampling Technique (SMOTE), which addresses the issue of imbalanced training data on the performance of MPM. The original training data for the positive (i.e., minority) class was modified by over-sampling the mineralized locations using SMOTE and by randomly under-sampling the non-mineralized locations at different proportions, producing 400 training datasets with proportions of mineralized-to-non-mineralized samples ranging from 600:30 to 30:600. Each of these individual training datasets was used to evaluate the performance of MPM under different proportions of mineralized-to-non-mineralized samples. The performance of each prospectivity model was objectively evaluated using the F1 score and the success-rate curve. The results show that SMOTE can significantly increase the performance and the spatial efficiency of MPM. The main differences between the performances of the derived prospectivity models illustrate the sensitivity of MPM to the number of samples and distribution of classes in the training data. According to the results, better performance is achieved using SMOTE when the prospectivity models are trained with an equal number of mineralized and non-mineralized samples. The best prospectivity model trained with a modified dataset with 600:600 proportion of mineralized to non-mineralized samples resulted in 100% classification of the training mineralized locations and almost 80% of the testing mineralized locations, and outlined only 7% of the study area as prospective."
}
```

## Acknowledgement
The code used for Geological Complexity is based on the works [Ford and Blenkinsop (2008)](https://www.tandfonline.com/doi/full/10.1080/08120090701581364) and [Hodkiewicz (2003)](https://research-repository.uwa.edu.au/en/publications/the-interplay-between-physical-and-chemical-processes-in-the-form)    
and the code used for SMOTE is based on the work [imbalanced-learn](https://imbalanced-learn.readthedocs.io/).
