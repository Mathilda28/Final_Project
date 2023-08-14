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
