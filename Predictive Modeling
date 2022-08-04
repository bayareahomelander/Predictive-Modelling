X = df.drop(["Churn", "customerID"], axis = 1)
X = pd.get_dummies(X, drop_first = True)
y = df["Churn"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .1, random_state = 101)

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth = 6)

tree.fit(X_train, y_train)

prediction = tree.predict(X_test)

from sklearn.metrics import accuracy_score, plot_confusion_matrix, classification_report

print(classification_report(y_test, prediction))

plot_confusion_matrix(tree,X_test,y_test)
plt.show()

features = pd.DataFrame(data=dt.feature_importances_,index=X.columns,columns=['Feature Importance']).sort_values("Feature Importance")

plt.figure(figsize = (15,8),dpi=150)
sns.barplot(data = features.sort_values('Feature Importance'), x=features.sort_values('Feature Importance').index, y='Feature Importance')
plt.xticks(rotation=90)
plt.title("Feature Importance DecisionTree")
plt.show()

from sklearn.tree import plot_tree

plt.figure(figsize = (10,8))
plot_tree(tree, filled = True, feature_names = X.columns)

from sklearn.ensemble import RandomForestClassifier

random = RandomForestClassifier(n_estimators = 100, max_depth = 6)

random.fit(X_train, y_train)

predictions = random.predict(X_test)

print(classification_report(y_test,predictions))

plot_confusion_matrix(random,X_test,y_test)
plt.show()

from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier

ada = AdaBoostClassifier()

ada.fit(X_train, y_train)

adaPreds = ada.predict(X_test)

gboost = GradientBoostingClassifier()

gboost.fit(X_train, y_train)

gboostPreds = gboost.predict(X_test)

print(classification_report(y_test, adaPreds))

print(classification_report(y_test, gboostPreds))

plot_confusion_matrix(ada, X_test, y_test)
plt.show()
