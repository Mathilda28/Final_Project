# Final_Project
Authors: Mathilda Hosiana Tambun
# Overview
The overall goal is to create machine learning models that can forecast consumer deposits reliably based on historical data.
# Success Criteria
The following metrics will be used to assess the project's success:
1. Our analytics capabilities give banks with actionable client deposit insights.
2. Ensure at least 90% accuracy in determining whether consumers are deposit customers or not.
# Data Description
## Penjelasan Dataset

**Fitur**

- age (numeric)
- job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar","self-employed","retired","technician","services")
- marital : marital status (categorical: "married","divorced","single"; note: "divorced" meansdivorced or widowed)
- education (categorical: "unknown","secondary","primary","tertiary")
- default: has credit in default? (binary: "yes","no")
- balance: average yearly balance, in euros (numeric)
- housing: has housing loan? (binary: "yes","no")
- loan: has personal loan? (binary: "yes","no")
- contact: contact communication type (categorical: "unknown","telephone","cellular")
- day: last contact day of the month (numeric)
- month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
- duration: last contact duration, in seconds (numeric)
- campaign: number of contacts performed during this campaign and for this client (numeric,includes last contact)
- pdays: number of days that passed by after the client was last contacted from a previouscampaign (numeric, -1 means client was not previously contacted)
- previous: number of contacts performed before this campaign and for this client (numeric)
- poutcome: outcome of the previous marketing campaign
(categorical:"unknown","other","failure","success")

**Target**
- Deposit

  Yes, the consumer is now a deposit customer.

  no = the consumer rejects the deposit
# Modelling
Gaussian Naive Bayes, Gradient Boosting, DecisionTree, Random Forest, and KNeighbors are the models that were used. The best model is then chosen based on a cross-validation evaluation of model performance. Gradient Boosting, which was generated using hyperparameter tuning and had a 100% train set accuracy and an 86% test set, is the best model that could be found.
# Project Conclusion
1. Based on Exploratory Data Analysis (EDA) :
- The majority of consumers are stable financially and between the ages of 38 and 42.
- The stability, analytical skills, and simplicity of management, engineering, and administrative jobs all affect deposit choices.
- Education has an impact; whereas higher education prefers complexity, secondary education prefers simplicity.
- Promotions only apply during specific months and holidays.
- Prediction models, in particular Gradient Boosting, successfully pinpoint potential clients.
  The majority hasn't used deposits yet; more education is needed.
- Special incentives and educational programs raise interest and awareness.
2. Business Insights :
- The most common occupational backgrounds are management, technicians, and administration. This suggests possibilities for developing targeted marketing tactics for each demographic.
- Job type influences time deposit preferences. Management demands consistency, technicians are analytical, and administration seeks convenience. A tailored marketing plan can boost attractiveness to each demographic.
- Offering particular incentives to specific client groups, such as higher interest rates on term deposits, can encourage interest and promote participation. This strategy can also concentrate on certain moments that are important to the demands of the customer.
- According to data, the vast majority of clients have not used time deposits. This could be an opportunity to create related items or versions that better meet the needs and preferences of customers.




  
