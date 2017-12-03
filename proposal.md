# Proposal

**Team**: hw3-p2-ou-yu-li-1
**Members**: Aaron Ou, Julien Yu, Brian Lin

### i) Why we choose the dataset
The dataset we intend to work on is named `adult.csv`, which consists of demographic information about adults such as age, work class, education, race, sex, etc. and also whether or not the adult makes more than \$50 thousand dollars per year. 

We chose this dataset because while many papers have cited this data set, they have been mostly been done in a machine learning context of attempting to increase the classification accuracy of whether an individual makes more than $50 thousand dollars per year. There has been no study done to actually look into **the relationship between different explanatory variables**. For example, does one's gender affect how many years of education they obtain? What about one's race? These questions are essential to understanding society today.

### ii) Validity that the dataset is openly and freely available for you to use
All data are from the UC Irvine Machine Learning Repository. 
In the `About` page of the website, the website states with pride: 
>The UCI Machine Learning Repository is a collection of databases, domain theories, and data generators that are used by the machine learning community for the empirical analysis of machine learning algorithms. The archive was created as an ftp archive in 1987 by David Aha and fellow graduate students at UC Irvine. Since that time, it has been widely used by students, educators, and researchers all over the world as a primary source of machine learning data sets. As an indication of the impact of the archive, it has been cited over 1000 times, making it one of the top 100 most cited "papers" in all of computer science.
As such, the dataset is available for us to use, and the citation policy is in the following html file: http://archive.ics.uci.edu/ml/citation_policy.html

### iii) The url of where we download the dataset
The csv file can be downloaded from `http://archive.ics.uci.edu/ml/datasets/Adult`

### iv) The main properties of the dataset

File format: | csv
--- | ---
Rough total size: | 32561 rows and 15 columns, 4009 KB
Source of Origin: | 1994 Census database
Scientific Area: | Social Science
Donor: | Ronny Kohavi and Barry Becker, Silicon Graphics
Intention: | To see if it is possible to achieve high classification accuracy of whether an individual makes more than $50 thosuand dollars per year through demographic information. 
Attributes (15 in total): | `age`,`workclass`,`fnlwgt`,`education`,`education num`,`marital status`,`occupation`,`relationship`,`race`,`sex`,`capital gain`,`capital loss`,`hours per week`,`native country`,`income (>50k/year or <=50k/year)`

### v) The questions we intend to answer
Our potential tasks involve but are not limited to: 
1. (main objective) Explore the pairwise relationships between different categorical variables such as sex, occupation and education level. Find causal relationships if there is any. Do different races and sexes pursuit a different level of education? Likewise, do different races and sexes pursuit different kinds of occupation? Do different races have a different distribution of martial status? The demographic questions we can explore are endless. 
2. Perform possible regression analysis on quantitative variables such as working hours per week, capital loss, etc. Find the extent to which these variables affect the annual income number.
3. Implement the analysis with different types of graphs including boxplots, violinplots, dotplots, etc. 
