df.isna().sum()

customerID          0
.
.
.
MonthlyCharges      0
TotalCharges        0
Churn               0
dtype: int64

plt.figure(figsize = (6,5))
sns.countplot(data=df,x='Churn')
plt.show()

plt.figure(figsize = (10,6))
sns.boxplot(data = df, x = "TotalCharges", y = "Contract", hue = "Churn")
plt.legend(loc = (1.01,.5))
plt.show()

corr = pd.get_dummies(df[['gender', 'SeniorCitizen', 'Partner', 'Dependents','PhoneService', 'MultipleLines',
                          'InternetService','OnlineSecurity', 'OnlineBackup','DeviceProtection', 'TechSupport',
                          'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod','Churn']]).corr()
                          
corr["Churn_Yes"].sort_values().iloc[1:-1]

plt.figure(figsize = (15,10), dpi = 200)
sns.barplot(x = corr["Churn_Yes"].sort_values().iloc[1:-1].index, y = corr["Churn_Yes"].sort_values().iloc[1:-1].values)
plt.title("Correlation to Churn_Yes")
plt.xticks(rotation = 90)
plt.show()
