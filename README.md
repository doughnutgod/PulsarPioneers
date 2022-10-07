# COMP3850 PACE project/internship with CSIRO. Pulsar Emission Study
## Project: Evaluation of pulsar randomness.

Project Brief By Sponsor: Pulsars are amongst the most extreme objects known in the universe. They spin so fast that their surface is moving close to the speed of light, their density is so great that their interiors may contain free quarks and their magnetic fields are the highest known in the universe. The majority of known pulsars have been discovered by the CSIRO Parkes radio telescope or with CSIRO instrumentation sold overseas, and pulsar research within Australia is internationally renowned. Pulsar research has, so far, led to two Nobel Prizes and represents key-science at the majority of current and planning radio telescopes (including the Square Kilometre Array).


Our project is to use pulsar observations for practical (and potentially commercial and/or defence) use. The Pioneer and Voyager spacecraft included a plaque indicating where the spacecraft came from using pulsars as markers. Numerous groups are interested in navigation, positioning and timing applications that do not rely on the global positioning system satellites (GNSS). This has clear defence applications (denying/ensuring GNSS will be key in future warfare), but also scientific use for deep-space navigation and positioning for terrestrial-based applications as well, such as triangulating location under rainforest canopies and in polar regions.


Pulsars have also (theoretically) been shown to be useful for time synchronisation (in particular in terms of synchronising power stations on continental baselines) and for producing publicly-verifiable random number sequences of interest for cryptography, scientific trials, electoral audits and international treaties.

Here we wish to determine which pulsars can be used as random number sources. In order to do this we need to note that individual pulses from pulsars vary in brightness, but, at least in some cases, adjacent pulses may be correlated.  We wish to determine:

The correlation time-scale for pulse-to-pulse correlations for different pulsars


The primary project deliverables will be:
- [ ] a table listing the correlation time-scale for different pulsars
- [ ] a description of the analysis method used
- [ ] an analysis of how random the pulse intensities actually are (after accounting for the correlation time scale)
- [ ] Recommendations for further work.

## Group Members of Group 15

Member | Student ID |
--- | --- | 
Matthew Oxley | 44991738
Max Grant | 44910118
Afeef Ahmed | 45833814
Tajkinur Rahman | 46124225
Alexandra Ellison | 45888949

## Pulsar Datasets

Data was retrieved from the Parkes Telescope by the CSIRO (https://www.parkes.atnf.csiro.au)


CSIRO Catalogue used to get datasets: https://www.atnf.csiro.au/research/pulsar/psrcat/

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

The purpose of the seventh notebook is to collate and condense all the relevent pulsar analysis into 1 spot for easy transfer of work and data processing. This can also aid in presentation through exportation into a PDF document for easier accessibility of work.

The frame-work follows for each notebook in this format.

- Import of libraries
- Import data or make data readable for importation
- Visualise data and ensure the integrity, correctness and completeness of the dataset.
- Basic ML analysis and predicting any and all effects that Uncertainty has on the evaluation of the current method used. ML methods currently used are Bi-directional LSTM and Logistic Regression.
- Transforming data using Autocorrelation and other methods to find more usable data for final testing.
- Exportation of data into proper datasets to be tested using external programs or scripts in binary format.