# def plot_feature_importances(model,X_train):
#     n_features = X_train.shape[1]
#     plt.figure(figsize=(8,8))
#     plt.barh(range(n_features), model.feature_importances_, align='center',color='#1c3290') 
#     plt.yticks(np.arange(n_features), X_train.columns.values) 
#     plt.xlabel('Feature importance', fontsize=20)
#     plt.ylabel('Feature',fontsize=20)
   

    
    
# def plot_confusion(y_test,y_pred_test):
#     from sklearn.metrics import confusion_matrix
#     c_matrix = confusion_matrix(y_test, y_pred_test)
    
#     f, ax = plt.subplots(figsize=(5,5))
#     sns.heatmap(c_matrix,fmt=".0f", annot=True,linewidths=0.2, linecolor="purple", ax=ax)
#     plt.xlabel("Prediction")
#     plt.ylabel("Actual")
#     plt.show()     
    
# def find_best_k(X_train, y_train, X_test, y_test, min_k=1, max_k=25):
#     best_k = 0
#     best_score = 0.0
#     for k in range(min_k, max_k+1, 2):
#         knn = KNeighborsClassifier(n_neighbors=k)
#         knn.fit(X_train, y_train)
#         preds = knn.predict(X_test)
#         f1 = f1_score(y_test, preds)
#         if f1 > best_score:
#             best_k = k
#             best_score = f1
    
#     print("Best Value for k: {}".format(best_k))
#     print("F1-Score: {}".format(best_score))    

# def results(names,performance):
#     size = len(names)
#     final = {}
    
#     for i in range(size):
#         final.update({names[i]: performance[i]})
        
#     sorted_d = sorted(final.items(), key=lambda x: (x[1],x[0]), reverse=True)
#     top = sorted_d[:1]
# #     print(top)
#     bottom = sorted_d[1:]
# #     print(bottom)

#     x1_val = [x[0] for x in top]
#     y1_val = [x[1] for x in top]
#     x2_val = [x[0] for x in bottom]
#     y2_val = [x[1] for x in bottom]

#     fig, ax = plt.subplots(figsize=(20,10))
#     #fig, ax = plt.subplots(figsize=(20,10))
#     plt.bar(x1_val,y1_val,color = '#1c3290', label="Top model")
#     plt.bar(x2_val,y2_val, color = "#907A1C", label="")
# #     plt.title("Top 10 US Zip Codes", fontsize = 35)
#     plt.xticks(rotation=45, fontsize=15)
#     plt.xlabel("Models", fontsize=20)
#     plt.ylabel("%", fontsize = 20)
#     plt.legend()
#     plt.show()