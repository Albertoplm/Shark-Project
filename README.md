# Shark-Project

![shark](https://github.com/Albertoplm/Shark-Project/blob/main/images/shark.jpg)


My first project in Iron Hack:
- In this project we have to analyse the Global Shark Attacks dataset (https://www.kaggle.com/teajay/global-shark-attacks) and come up with some hypotheses and check if they are true.
- The process to carry out the project was as follows:
   1. First I have made a brief study of the database.
   2. Once I had a clear idea of what data was in the database, I created my hypotheses.
   3. I start the cleaning to keep only the data I need to test my hypotheses.
   4. Once I have the database clean I create a new file with that database.
   5. I download the new file into another document and start my analysis, creating graphs for the visualisation of the conclusions. 

To carry out this research I have used different libraries:
   - pandas 
   - seaborn
   - matplotlib.pyplot 
   - numpy 
   - re

Note: In the repo you will find two different Jupiters, one with the cleaning process and the other one with the Visualization process. Also you can find the data (.csv) and the images.

In order to clean the database I really fin very usefull regex

The final version of the database is composed of (with a total sample of 6302 cases):
   - COUNTRY: (6252)
   - YEAR: (6172)
   - MONTHLY: (5750)
   - N_TIME: (2366)
   - SEX: (5733)
   - AGE: (3408)
   - N_ACTIVITY: (4321)
   - N_SPECIES: (1436)
   - FATAL_Y_N: (5689)
   - N_INJURY: (2321)

## Hypotheses

1. **Sharks attacks men more often**
2. **The probability of been a fatal Shark attack, is higher on women**
3. **Have been reported more shark attacks with people between the ages of 15 and 35.**
4. **The most common injury was to the leg**
5. **The most common shark attacks reported were by white sharks**
6. **They are more Sharks attacks during summer**
7. **Sharks more frequently attack people that are sufing**
8. **The percentage of deaths is higher in people that is diving than in people who practice surfing**

## Conclusions

### **H1 - Sharks attacks men more often**

![Gender](https://github.com/Albertoplm/Shark-Project/blob/main/images/GENDER.svg)

We appreciate in the chart, that the number of attacks on males are significantly higher than on females, almost 90% of the reported attacks were on males. 

### **H2 - The probability of been a fatal Shark attack, is higher on women**

![GendervsFatal](https://github.com/Albertoplm/Shark-Project/blob/main/images/GENDER_vs_Mortal.svg)

In this graph we can notice that there is not a significant variance between gender respect to the probability of been a Fatal Attack

### **H3 - Have been reported more shark attacks with people between the ages of 15 and 35.**

![AGE](https://github.com/Albertoplm/Shark-Project/blob/main/images/AGE.svg)

Here we can see that the volume is highest in the age range between 15 and 30 and the mean of the age is around 25

### **H4 - The most common injury was to the leg**

![TYPE_OF_INJURY1](https://github.com/Albertoplm/Shark-Project/blob/main/images/TYPE_OF_INJURY1.svg)
![TYPE_OF_INJURY2](https://github.com/Albertoplm/Shark-Project/blob/main/images/TYPE_OF_INJURY2.svg)

We notice that half of the cases reported were injuries in legs or foots

### **H5 - The most common shark attacks reported were by white sharks**

![TYPE_OF_SHARK1](https://github.com/Albertoplm/Shark-Project/blob/main/images/TYPE_OF_SHARK1.svg)
![TYPE_OF_SHARK2](https://github.com/Albertoplm/Shark-Project/blob/main/images/TYPE_OF_SHARK2.svg)

As we can see in the graph the White shark has a bigger rate in the case attacks reported, almost 50% of the attacks where done by White Sharks

### **H6 - They are more Sharks attacks during summer (I just realized that the same day of the year in one place could be summer and in another winter...because it depends on the hemisphere... )**

![MONTLHY](https://github.com/Albertoplm/Shark-Project/blob/main/images/MONTLHY.svg)

If I have time i will try to check the hemispheres....

### **H7 - Sharks attacks more often to people that are surfing**

![TYPE_OF_ACTIVITY1](https://github.com/Albertoplm/Shark-Project/blob/main/images/TYPE_OF_ACTIVITY1.svg)
![TYPE_OF_ACTIVITY2](https://github.com/Albertoplm/Shark-Project/blob/main/images/TYPE_OF_ACTIVITY2.svg)

We notice that the attacks where done to people surfing and swimming in the same amount. 

### **H8 - The percentage of deaths is higher in people that is diving than in people who practice surfing**

![ACTIVITYvsFATAL](https://github.com/Albertoplm/Shark-Project/blob/main/images/ACTIVITYvsFATAL.svg)

In the graph we see that they were more fatal attacks in people that was diving than surfing, but also we notice that swiming has the highest fatal rate.

### **H9 - They are more sharks attacks reported during no lights hours**

![WORST_TIME_TO_WATER](https://github.com/Albertoplm/Shark-Project/blob/main/images/WORST_TIME_TO_WATER.svg)

We notice that they were more cases reported during day light... almost 50% of the cases were reported between 11 to 16.