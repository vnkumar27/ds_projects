# Foreign Revenue	

### Goal   
The goals of this project were:     
* Webscraping (using Beautiful Soup)  
* Probability  
* Linear Regression  
* Train & Test  
* Naive Bayes  
* Visualization with Matplotlib  

### Overview
For this project I practiced webscraping using Beautiful Soup. I noticed that most American movies only received 
a portion of their gross revenue from domestic sales, and the rest were from foreign sales. As such, I sought to create
a linear regression model that would predict the percent of total gross that an American movie would
receive from foreign sales.

### Data Cleaning and Analytics

I scraped BoxOfficeMojo.com for the top 100 total grossing American movies from the years 2000 to 2016. 
I had a total list of 1700 movies. After removing null values, my final data set had 1300 entries. 
I scraped information for the following features: movie distributor, production budget, title, date of release,
 genre, MPAA rating, total gross, foreign gross, domestic gross, runtime. 

After some playing around, I determined the following features were the most impactful for my 
dependent variable (foreign revenue percent):    
* *Distributor*  
	- Fox  
	- Paramount    
	- Disney (aka Buena Vista)  
	- Lions Gate  
	- Sony  
	- Warner Bros  
* *Rating*  
	- G  
	- PG  
	- PG-13  
	- R  
* *Runtime*  
* *Genre*  
	- Adventure  
	- Horror  
	- Animation  
	- Comedy  
	- Drama  
	- Romance  
* *Season*  
* *Release Year*  

I initially had also included production budget but many of the movies did not have that value, 
so I had to eventually drop it. 

### Discussion  

After running linear regression with the above features, I found that a few features were more 
correlated than others (as expected). Interestingly none of the distributors had a high correlation 
with foreign gross. One possible explanation is that American movie distributors may outsource to 
different distributors that are located locally in foreign countries. Another interesting finding was 
that comedy movies had a negative correlation. This may simply be due to cultural differences and 
inability for foreign countries to relate to American humor. 

### Conclusion  
Next time I would like to run the same model with a larger training set. I would also incorporate 
feature selection methods like Lasso to better parse out relevant variables. BoxOfficeMojo also has 
foreign gross data broken down by country, so it would be interesting to look at which countries 
contribute the most to total gross, and if there are any correlations between the country’s gross 
and genre or other features. This information would be great for movie producers who want to capture a 
larger audience outside of the United States.   

I have also included my notebooks and slides if you would like to look at my project in more detail. 