#Check for overfitting and underfitting Achieved by evaluating the scores on training and test set
from sklearn import metrics
from sklearn.metrics import accuracy_score


model = 'model'
X_train, X_test, y_train, y_test, model_y_pred_train, model_y_pred_test = 0


print('Training-set accuracy score: {0:0.4f}'.format(accuracy_score(y_train, model_y_pred_train) ))
print('testing-set accuracy score: {0:0.4f}'.format(accuracy_score(y_test, model_y_pred_test) ))


print('Training set score: {:.4f}'.format(model.score(X_train, y_train) ))
print('Test set score: {:.4f}'.format(model.score(X_test, y_test) ))

difference=abs(model.score(X_test, y_test)-model.score(X_train, y_train))
print("\nDifference: ", difference)
