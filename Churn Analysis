df['Contract'].unique()

plt.figure(figsize = (10,7))
sns.histplot(data = df, x = "tenure", bins = 40)
plt.show()

noChurn = df.groupby(["Churn","tenure"]).count().transpose()["No"]
yesChurn = df.groupby(["Churn","tenure"]).count().transpose()["Yes"]

churnRate = yesChurn / (noChurn + yesChurn) * 100

churnRate.transpose()["customerID"]
tenure
1 61.990212
2 51.680672
...
70 9.243697
71 3.529412
72 1.657459
Name: customerID, Length: 72, dtype: float64

plt.figure(figsize = (10,5),dpi = 100)
churnRate.iloc[0].plot()
plt.ylabel("Churn Rate")
plt.show()

def cohorts(n): 
  if n < 13:
    return "0 to 12 Months"
  elif n < 25:
    return "12 to 24 Months"
  elif n < 49:
    return "24 to 48 Months"
  else:
    return "Over 48 Months"

df["Tenure Group"] = df["tenure"].apply(cohorts)

plt.figure(figsize = (10,5), dpi = 100)
sns.scatterplot(data = df, x = "MonthlyCharges",
                y = "TotalCharges", hue = "Tenure Group", alpha = .5)
plt.show()

plt.figure(figsize = (10,8), dpi = 100)
sns.catplot(data = df, x = "Tenure Group",
            hue = "Churn", col = "Contract", kind = "count")
plt.show()
