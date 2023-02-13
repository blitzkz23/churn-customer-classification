﻿# Telco Churn Customer Classification
 <img src="https://images.unsplash.com/photo-1611599281058-94426d0618a7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="Telco Customer Churn" width="50%">
<figcaption>Photo by <a href="https://unsplash.com/@sigmund?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Sigmund</a> on <a href="https://unsplash.com/photos/r9PeXDCJyEw?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

 ## Bussiness Understanding
 Telecom Churn Classification is the process of predicting whether a telecom customer is likely to leave or stay with the service provider. This information is critical for the telecom industry as retaining existing customers is more cost-effective than acquiring new ones.

In this problem, the aim is to build a machine learning model that can predict whether a customer is likely to churn or not based on past customer behavior, demographic information, and other factors. This information can be used to target customers who are at a higher risk of leaving with retention offers and incentives.

A successful Telecom Churn Classification model can help the service provider identify and retain high-value customers, reduce customer churn, and increase customer lifetime value. By proactively addressing customer churn, the service provider can improve customer satisfaction and brand loyalty, leading to increased revenue and profits.

Overall, Telecom Churn Classification is a critical aspect of customer relationship management for the telecom industry, providing valuable insights into customer behavior and enabling service providers to take proactive measures to retain customers and improve their bottom line.

## Data Understanding
- CustomerID: A unique ID that identifies each customer.
- Gender: The customer’s gender: Male, Female
- Senior Citizen: Indicates if the customer is 65 or older: Yes, No
- Partner: Indicate if the customer has a partner: Yes, No
- Tenure: Indicates the total amount of months that the customer has been with the company by the end of the quarter specified above.
- Phone Service: Indicates if the customer subscribes to home phone service with the company: Yes, No
- Streaming TV: Indicates if the customer uses their Internet service to stream television programing from a third party provider: Yes, No. The company does not charge an additional fee for this service.
- Paperless Billing: Indicates if the customer has chosen paperless billing: Yes, No
- Monthly Charge: Indicates the customer’s current total monthly charge for all their services from the company.
- Total Charges: Indicates the customer’s total charges, calculated to the end of the quarter specified above.
- Churn Label: Yes = the customer left the company this quarter. No = the customer remained with the company. Directly related to Churn Value.

## Project Aim:
- Classify potential churn customer based on numerical and categorical features
- Solve binary classification problem with imbalanced dataset
