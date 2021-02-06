# Surfs Up

For this analysis, we look at the climatic conditions for opening a surfing goods & ice cream store. Specifically, we want to know if this store will be viable year round. For instance, when it's raining for long stretches at a time, you might have a few hard-core surfers buying gear, but very few customers for ice cream. 

We also know that people buy ice cream when it's hot out. Hot out and *not raining*. Conversely, ideal surfing conditions (i.e big waves) are positively correlated with wind speed and wind speed is positively correlated with rainfall. So in essense, we are looking for the goldilocks happy-medium which will be conducive for both sides of the business. To summarize in bullet points, we are looking for this info: 

</br>

* **Monthly Temperature for June**
* **Monthly Temperature for December**
* **Monthly Rainfall in June (indicative of dry season)**
* **Monthly Rainfall in December (rainy of rainy season)**

</br>

All analysis and charts were created in jupyter notebook, using a combination of Python and SqLite. Source code found [here](https://github.com/carlosjennings1991/surfs_up/blob/main/SurfsUp_Challenge.ipynb)

</br>

<img src="https://github.com/carlosjennings1991/surfs_up/blob/main/surfer2.png" width="1099" height="486">

___

## Results Pt 1: June Temperature

Pretty self explanatory, we want to know what's the temperature in Oahu Hawaii in June. To do this, we import a SQLite file that contains the weather data for five weather stations on the island. These five stations have recorded the temperature everyday from 2010 to 2017. We simply need to query the file, filter it so that we only look at June's data and produce the summary statistics of that month. The output looks like this: 

<img src="https://github.com/carlosjennings1991/surfs_up/blob/main/june_temps.png" width="132" height="236">

## Results Pt 2: Decemember Temperature

Exactly the same as above, but for the month of December. 

<img src="https://github.com/carlosjennings1991/surfs_up/blob/main/dec_temps.png" width="132" height="236">

