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

## Results Pt 3: June Rainfall

Here we see the precipitation info for June, keep in mind this is for the individual days of june. 

<img src="https://github.com/carlosjennings1991/surfs_up/blob/main/june_rain.png" width="132" height="236">

## Results Pt 4: December Rainfall

Like the above chart but for the December rainfall. Hawaii is on the northern edge of the tropics, so this would align with the rainy season, albeit less intensely than other place closer to the equator. 

<img src="https://github.com/carlosjennings1991/surfs_up/blob/main/dec_rain.png" width="132" height="236">

___

## Summary

After analyzing the data, we come across a few key takeaways: 

* **Summer is oddly cool**
* **Winter is oddly warm**

<img src="https://github.com/carlosjennings1991/surfs_up/blob/main/double_box_plot.png" width="417" height="296">

Of course, small changes from winter to summer temperatures are a feature of tropical climates, what's notable about Hawaii is it's moderate summer temperatures. There are summer climates in the Northeast with hotter summers than Oahu Hawaii. This can partly be explained by the moderating effects of the ocean and it's cooling breezes, but it's still quite shocking to see the hard data. 

As for how this portends to the business - it's pretty good. While winter is cooler, it's a barely perceptible cooling, and not too cold to preclude anyone from buying ice cream. 
