
**Climate Risk In Marginalized Communities**

Team Members: 
Bailey Forster \n
Zoe Kearney \n
Reeya Kumbhojkar \n
Viraj Meruliya \n
Braeden Reinoso \n

Five minute presentation: 

**Project description**

Project Overview: The Environmental Protection Agency (EPA) monitors concentrations of air toxins in the US, including particulate matter smaller than 2.5 micrometers (pm2.5). These fine particles are able to enter the lungs and bloodstream, posing a significant health risk. There is also evidence that people of color in the US are at increased risk for adverse health effects due climate change and pollution (see review article: Berberian et al. 2022). Our goal is to create a model that uses 2021 ACS 5-Year Estimates Data Profiles and EPA data to identify tracts likely to be at risk of high pm2.5 levels.

Stakeholders: climate and health researchers, policy makers, state and national-level government.
KPI:
Precision: % of predicted positives that are true positives
Recall: % of true positives that are predicted as positive
f-beta: calculated from precision and recall. Beta>1 indicates greater weight on recall, while beta<1 indicates greater weight on precision.

Our model is optimized by maximizing f2 (f-beta with beta=2). Since the goal of this model is to identify high-risk tracts for further study, we have decided to place a greater emphasis on recall over precision.

Approach: We have developed a binary classification model that predicts whether a census tract is high-risk for pm2.5 levels. We consider pm2.5> 9 µg/m3 high risk as supported by a recent EPA proposal.
Many rural tracts had insufficient environmental or demographic data, so we applied an urban cutoff of population density > 500/km².

Training: 68% of the data was used to train 5 different model types: logistic regression, decision tree, random forest, AdaBoost, and XGBoost. GridSearchCV was used for hyperparameter tuning and cross validation on each model separately.
Validation: 12% of the data was used to compare 5 model candidates (one of each type)
Testing: We reserved the remaining 20% of the data to perform a final test on the best model

19 features are considered:

Environmental:
- Ozone concentration [annual mean of the 10 highest MDA8 O3 concentrations, PPM]
- Diesel particulate matter [micrograms per cubic meter (μg/m3)]
- Superfund cite proximity [within 5 km of the average resident in a block group, divided by distance, calculated as the population-weighted average of blocks in each block group.]
- RMP facility proximity [total count of active RMP facilities in each block group within 5 km of the average resident in a block group, divided by distance, calculated as the population- weighted average of blocks in each block group.]
- Underground storage tanks [Count of Leaking Underground storage tanks (LUSTs)  (multiplied by a factor of 7.7) and the number of Underground storage tanks (USTs) within a 1,500- foot buffered block group]
- Wastewater discharge [toxicity-weighted concentrations in streams within 500m, weighted by distance and population]
- Hazardous waste proximity [total count of hazardous waste facilities in each block group within 5 km of the average resident in a block group, divided by distance, calculated as the population-weighted average of blocks in each block group.]

Demographic:
- Median Income via the Theil Index
- Primary Industry share [%]
- Secondary Industry Share [%]
- Traffic Proximity [annual average daily traffic volume over year / distance]
- White Population [%]
- Black only Population [%]
- Asian only Population [%]
- Hispanic only Population [%]
- Population Density [persons / land area]
- Health Insurance [%]
- Poverty
- Houses Built Before 1960

  Note: All racial groups as defined in the US Census

Results: XGBoost model with all 19 features achieved 93% accuracy and 89% f2-score. Feature importance gives new insights into causes and distribution of PM2.5 risk. Ozone and Diesel PM are among the top contributors, thus these other air toxins are good indicators of high pm2.5.  Without Ozone and Diesel PM the model still provides a reasonable prediction of risk with 84% accuracy and 78% f2-score. 

![Model Pipeline](https://github.com/zkearney7730/EJ-Erdos-Project/assets/77342133/7935b35f-bf84-4904-82b8-c4713ad15d11)


Future Work: 
Multinomial model - low, medium, high risk based on WHO, EPA, US standards
Separate classification models for target groups and use feature importance to identify the most significant pm2.5 sources or health risks affecting minority groups. 
E.g. control for areas with high hispanic/latino populations

Allow policy makers and state legislators to create targeted solutions and implement Evidence Based Policy, particularly around regulation. 
NOTE: Additional CDC health data with current tract boundaries is expected to become available in the next couple of years. The inclusion of this data in the model 
will allow for better understanding of the impact of envrionmental and economic factors on health.


**Dependencies**

<pre><code> Scikit-Learn, Pandas, Numpy, Matplotlib
</code></pre>

**Data Access**


**Included scripts and models**

**License?** 



