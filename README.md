# COMP3850 PACE project/internship with CSIRO. Pulsar Emission Study

Created by PACE Group 15.

## **Mandatory Python Dependencies needed**.
This environment has been created in Jupyter Notebooks via the Anaconda suite. Using **Python 3.9.7**, the minimum python dependencies required to be in the anaconda environment are as follows to run the notebooks.

- Pandas (native to anaconda)
- Numpy (native to anaconda)
- Seaborn (https://pypi.org/project/seaborn/)
- Matplotlib (https://pypi.org/project/matplotlib/)
- sklearn (native to anaconda)
- datetime (In Python (Unsure))
- scipy (https://pypi.org/project/scipy/)
- Keras (https://pypi.org/project/keras/)
- Tensorflow (https://pypi.org/project/tensorflow/)
- Statsmodels (https://pypi.org/project/statsmodels/)
- Randtest (https://pypi.org/project/randtest/)

Most of these dependencies should be native to anaconda. The ones known to not be native are Keras, Tesorflow and Randtest.

Installation commands for Randtest is currently (as it is not on conda):

````
pip install randtest

or

git clone https://github.com/sudo-rushil/randtest
cd randtest
python setup.py install
````

Errors such as:

````
ImportError: Missing required dependencies ['numpy']

ImportError: No module named pandas
````

can be resolved through solutions such as

````
pip install numpy
pip install pandas

conda install numpy
conda install pandas
````

This is done through the anaconda terminal or properly directed command prompt. Any other errors are currently unknown or not encountered. Best solution for these edgecases is google and stackoverflow of the error(s).

## Testing Suite Software

We obtained the use of a NIST suite software created in python from this Github Repository
https://github.com/stevenang/randomness_testsuite By the author Steven Kho Ang

## Project: Evaluation of pulsar randomness.

***Project Brief By Sponsor***: Pulsars are amongst the most extreme objects known in the universe. They spin so fast that their surface is moving close to the speed of light, their density is so great that their interiors may contain free quarks and their magnetic fields are the highest known in the universe. The majority of known pulsars have been discovered by the CSIRO Parkes radio telescope or with CSIRO instrumentation sold overseas, and pulsar research within Australia is internationally renowned. Pulsar research has, so far, led to two Nobel Prizes and represents key-science at the majority of current and planning radio telescopes (including the Square Kilometre Array).


Our project is to use pulsar observations for practical (and potentially commercial and/or defence) use. The Pioneer and Voyager spacecraft included a plaque indicating where the spacecraft came from using pulsars as markers. Numerous groups are interested in navigation, positioning and timing applications that do not rely on the global positioning system satellites (GNSS). This has clear defence applications (denying/ensuring GNSS will be key in future warfare), but also scientific use for deep-space navigation and positioning for terrestrial-based applications as well, such as triangulating location under rainforest canopies and in polar regions.


Pulsars have also (theoretically) been shown to be useful for time synchronisation (in particular in terms of synchronising power stations on continental baselines) and for producing publicly-verifiable random number sequences of interest for cryptography, scientific trials, electoral audits and international treaties.

Here we wish to determine which pulsars can be used as random number sources. In order to do this we need to note that individual pulses from pulsars vary in brightness, but, at least in some cases, adjacent pulses may be correlated.  We wish to determine:

The correlation time-scale for pulse-to-pulse correlations for different pulsars


The primary project deliverables will be (Ticked off by Group Members):
- [x] a table listing the correlation time-scale for different pulsars
- [x] a description of the analysis method used
- [x] an analysis of how random the pulse intensities actually are (after accounting for the correlation time scale)
- [x] Recommendations for further work.

## Delivered Result

The final result file will be provided in both the report.ipynb and report.pdf files.

## Group Members of Group 15

Member | Student ID | Git Names
--- | --- | --- |
Max Grant | 44910118 | mgrant223
Matthew Oxley | 44991738 | dougnutgod
Afeef Ahmed | 45833814 | Syed-Afeef
Tajkinur Rahman | 46124225 | Tajkinur Rahman
Alexandra Ellison | 45888949 | Alexandra

## Pulsar Datasets

Data was retrieved from the Parkes Telescope by the CSIRO (https://www.parkes.atnf.csiro.au)


CSIRO Catalogue used to get datasets (https://www.atnf.csiro.au/research/pulsar/psrcat/)

ID | Pulsar | Date | Number of Pulses | Filename
--- | --- | --- | --- | --- |
#1 | J0437-4715 | 24-06-2022 | 27000 | J0437-4715.pulses
#2 | J0953+0755 | 05-03-2016 | 14329 | J0953+0755.pulses
#3 | J0835-4510 | 19-07-2022 | 1331 | J0835-4510.pulses
#4 | J1243-6423 | 19-07-2022 | 1819 | J1243-6423.pulses
#5 | J1456-6843 | 25/06/2022 | 1219 | J1456-6843.pulses
#6 | J1644-4559 | 26/05/2022 | 698 | J1644-4559.pulses

## Jupyter Notebook Exploratory Data Analysis Explanation and Study Analysis

The team has decided to take an EDA approach to dealing with visualizing, processing and studying the datasets mentioned above. This will be done in 7 discrete notebooks using Jupyter via anaconda. The seven notebooks are as follows:

Notebook ID | Name | Pulsar(s)
--- | --- | --- |
#1 | Pulsar1.ipynb | Pulsar 1 
#2 | Pulsar2.ipynb | Pulsar 2 
#3 | Pulsar3.ipynb | Pulsar 3 
#4 | Pulsar4.ipynb | Pulsar 4 
#5 | Pulsar5.ipynb | Pulsar 5 
#6 | Pulsar6.ipynb | Pulsar 6
#7 | MasterNotebook.ipynb | Pulsars 1-6
#8 | Report.ipynb | Report Notebook of Results


The purpose of the seventh notebook is to collate and condense all the relevent pulsar analysis into 1 spot for easy transfer of work and data processing. This can also aid in presentation through exportation into a PDF document for easier accessibility of work.

The frame-work follows for each notebook in this format.

- Import of libraries
- Import data or make data readable for importation
- Visualise data and ensure the integrity, correctness and completeness of the dataset.
- Basic ML analysis and predicting any and all effects that Uncertainty has on the evaluation of the current method used. ML methods currently used are Bi-directional LSTM and Logistic Regression.
- Transforming data using Autocorrelation and other methods to find more usable data for final testing.
- Exportation of data into proper datasets to be tested using external programs or scripts in binary format.
- Reimportation of test results and evaluation

## Sub File Contents Explanation

Folder | Contents 
--- | --- | 
Data | Contains the Pulsar raw data 
Master Notebook Outputs | All outputs Generated from the Master Notebook, Edgecase protection against errors in collation. 
PulsarBinaryData | Binary data in TXT format ready for NIST suite 
PulsarBinaryDataResulsts | The Results of all data from the NIST Suite 
PulsarBinaryDataResulstsCSV | Contains all the results transcribed into CSV format for import 
redundancy notebooks | This contains the original 2 notebooks from week 2 before segregation