import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns; sns.set()
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectFromModel
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import glob
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report
from sklearn.metrics import cohen_kappa_score
from imblearn.over_sampling import BorderlineSMOTE
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import RepeatedStratifiedKFold
from imblearn.over_sampling import RandomOverSampler
from collections import Counter
from sklearn.model_selection import cross_validate
import tensorflow as tf
from featurewiz import featurewiz
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

os.chdir('G:\material')
path = 'G:\material'
val = os.path.join(path,os.listdir(path)[1])
train = os.path.join(path,os.listdir(path)[2])
features = os.listdir(val) #0 for en, 1 for ins, 2 for mean, 3 for SD
networks = os.listdir(os.path.join(val,features[2])) # 0 for DMN, 1 for ECN, 2 for HIPPO, 3 for SAL
#ins = os.listdir(os.path.join(val,features[1])) #0 for inam, 1 for inf, 2 for inp
#innetwork = os.listdir(os.path.join(val,features[1],ins[0]))
#f_n = os.path.join(features[1],ins[0],innetwork[0]) 
f_n = os.path.join(features[2],networks[0]) 
val_f_n = os.path.join(val,f_n)
train_f_n = os.path.join(train,f_n)

for u in range(7): #each group with 7 SD data

            #prepare materials
            train_names = glob.glob(os.path.join(train_f_n,'*'))
            val_names = glob.glob(os.path.join(val_f_n,'*'))
            df_results = pd.DataFrame(columns=['File Name', 'Model','train_acc','train_F1','train_loss','train_roc_auc','test_acc','test_F1','test_loss','test_roc_auc','val_acc','val_F1','val_loss','val_kappa','val_roc_auc'])
            train_data = pd.read_excel(train_names[u], header=None)
            val_data = pd.read_excel(val_names[u], header=None)
            file_name = train_names[u].strip(train_f_n)

            a = train_data.iloc[-4, :] != 0
            b = pd.DataFrame([])
            for n in range(len(a)):
                if a[n] == False:
                    c = pd.DataFrame([0])    
                else:
                    c = pd.DataFrame([1])
                b = pd.concat([b,c])
            train_Y = pd.DataFrame(b.iloc[:,0].values)            
            train_X = pd.DataFrame(train_data.iloc[:-4, :].T.values.astype('float32'))
            train_Y.rename(columns={0:'H'},inplace=True)
            train_for_fw = pd.DataFrame()
            train_for_fw = pd.concat([train_X,train_Y],axis=1)
            for  i in range(len(train_for_fw.T)-1):
                train_for_fw.rename(columns={train_for_fw.columns[i]: 'voxels'+str([i])},inplace=True)

            features, train_data_fw = featurewiz(dataname = train_for_fw, target='H' , corr_limit=0.7, verbose=2, sep=",",
            header=0,test_data="", feature_engg="", category_encoders="")
            train_X = train_data_fw.iloc[:,:-1]
            train_Y = train_data_fw.iloc[:,-1]
            train_X =  StandardScaler().fit_transform(train_X)

            d = val_data.iloc[-4, :] != 0
            e = pd.DataFrame([])
            for n in range(len(d)):
                if d[n] == False:
                    f = pd.DataFrame([0])    
                else:
                    f = pd.DataFrame([1])
                e = pd.concat([e,f])
                val_Y = e.iloc[:,0].values
            val_Y = pd.DataFrame(e.iloc[:,0].values)
            val_X = pd.DataFrame(val_data.iloc[:-4, :].T.values.astype('float32'))
            val_Y.rename(columns={0:'H'},inplace=True)
            val_for_fw = pd.DataFrame()
            val_for_fw = pd.concat([val_X,val_Y],axis=1)
            for  i in range(len(val_for_fw.T)-1):
                val_for_fw.rename(columns={val_for_fw.columns[i]: 'voxels'+str([i])},inplace=True)
            dif = val_for_fw.columns.difference(train_data_fw.columns)
            val_for_fw.drop(columns = dif,axis=1,inplace=True)
            val_X = val_for_fw.iloc[:,:-1]
            val_Y = val_for_fw.iloc[:,-1]
            val_X =  StandardScaler().fit_transform(val_X)

            # 準備模型
            models = [('LinearDiscriminantAnalysis_svd', LinearDiscriminantAnalysis()), 
            ('LinearDiscriminantAnalysis_lsqr', LinearDiscriminantAnalysis(solver='lsqr',shrinkage =0.2)), 
            ('KNN', KNeighborsClassifier()), 
            ('NaiveBayes', GaussianNB()), 
            ('SVM_rbf', SVC(C=0.5,kernel='rbf')),
            ('SVM_sigmoid', SVC(C=0.5,kernel='sigmoid')),
            ('Tree', DecisionTreeClassifier()),
            ('RandomForest',RandomForestClassifier()),
            ('Logistic',LogisticRegression(penalty='elasticnet', solver='saga', l1_ratio=0.5, random_state=0))]

            # about to train
            for model_name, model in models:
                #this step for changing non-zero values in y into one.

                # adress nan
                train_accuracy_sum = 0
                test_accuracy_sum = 0
                loss_sum = 0
                imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
                regressor = Pipeline(steps=[('imputer', imp_mean), ('regressor', model)])
                imp_mean1 = imp_mean.fit(train_X)
                train_X = imp_mean.transform(train_X)
                imp_mean2 = imp_mean.fit(val_X)
                val_X = imp_mean.transform(val_X)
                #BorderlineSMOTE for below, or try X,y = RandomOverSampler(sampling_strategy='all').fit_resample(X,y)
                train_X, train_Y =  BorderlineSMOTE(sampling_strategy='all',random_state = 42, k_neighbors = 2).fit_resample(train_X,train_Y)
                val_X, val_Y =  BorderlineSMOTE(sampling_strategy='all',random_state = 42, k_neighbors = 2).fit_resample(val_X,val_Y)
                #X, y =  SMOTE(sampling_strategy='all',random_state = 42, k_neighbors = 2).fit_resample(X,y)
                # Cross Validation * 1000 times
                #s = cross_val_score(models[0][1], X=X, y=y, cv=10, n_jobs=1)
                #print('Cross Validation accuracy: %.3f +/- %.3f' % (np.mean(s),np.std(s)))

                for r in range(1000): 
                    val_acc = []
                    val_f1 = []
                    val_loss = []
                    val_kappa = []
                    val_roc_auc = []
                    CV_results = cross_validate(model, train_X, train_Y, cv = 10,scoring = ('accuracy','f1','roc_auc','neg_brier_score'), return_train_score = True ,return_estimator = True) #cv here is (Stratified)KFold
                    train_acc_M= CV_results['train_accuracy'].mean()
                    #train_acc_SD.append(CV_results['train_score'].std())
                    train_f1_M=CV_results['train_f1'].mean()
                    #train_f1_SD.append(CV_results['train_f1'].std())
                    train_loss_M=CV_results['train_neg_brier_score'].mean()
                    #train_loss_SD.append(CV_results['train_neg_brier_score'].SD())
                    train_roc_auc_M=CV_results['train_roc_auc'].mean()
                    CV_acc_M=CV_results['test_accuracy'].mean()
                    #CV_acc_SD.append(CV_results['test_score'].std())
                    CV_f1_M= CV_results['test_f1'].mean()
                    #CV_f1_SD.append(CV_results['test_f1'].std())
                    CV_loss_M=CV_results['test_neg_brier_score'].mean()
                    #CV_loss_SD.append(CV_results['test_neg_brier_score'].SD())
                    CV_roc_auc_M=CV_results['test_roc_auc'].mean()

                    val_score=[]
                    val_predict = []

                    for i in range(len(CV_results['estimator'])):
                        val_score.append(CV_results['estimator'][i].score(val_X,val_Y)) 
                        val_predict.append(CV_results['estimator'][i].predict(val_X))


                    for ii in range(len(CV_results['estimator'])):  
                        val_acc.append(accuracy_score(val_Y, val_predict[ii]))
                        val_loss.append(tf.keras.losses.BinaryCrossentropy(from_logits=True)(np.float32(val_Y), np.float32(val_predict[ii])).numpy())
                        val_f1.append(f1_score(val_Y, val_predict[ii], average = 'weighted'))
                        #PRF = precision_recall_fscore_support( val_Y, val_predict[ii], average = 'weighted')
                        val_kappa.append(cohen_kappa_score(val_Y, val_predict[ii]))
                        try:
                            val_roc_auc.append(roc_auc_score( val_Y, val_predict[ii], average = 'weighted'))
                        except ValueError:
                            pass
                    val_acc_M=np.array(val_acc).mean()
                    val_loss_M = np.array(val_loss).mean()
                    val_f1_M = np.array(val_f1).mean()
                    val_kappa_M = np.array(val_kappa).mean()
                    val_roc_auc_M = np.array(val_roc_auc).mean()




                #output
                #print('File: {}, Model: {}, Cross Validation Loss: {:.4f}, Training Accuracy: {:.4f}, Testing Accuracy: {:.4f}'.format(f, model_name, loss, train_accuracy, test_accuracy))
                    df_results = df_results.append({'File Name': file_name,
                                        'Model': model_name, 
                                        'train_acc': train_acc_M,
                                        'train_F1':train_f1_M,
                                        'train_loss':train_loss_M,
                                        'train_roc_auc':train_roc_auc_M,
                                        'test_acc': CV_acc_M,
                                        'test_F1':CV_f1_M,
                                        'test_loss':CV_loss_M,
                                        'test_roc_auc':CV_roc_auc_M, 
                                        'val_acc': val_acc_M,
                                        'val_F1':val_f1_M,
                                        'val_loss':val_loss_M,
                                        'val_kappa':val_kappa_M,
                                        'val_roc_auc':val_roc_auc_M},
                                        ignore_index=True)
                   # print(df_results,train_index,test_index)


                #save results
                result1000 = df_results.groupby(['File Name','Model']).mean()

                # 將結果寫入 Excel 檔案
                #df = pd.DataFrame([[f, model_name, loss, train_accuracy, test_accuracy]], columns=['File Name', 'Model', 'Cross Validation Loss', 'Training Accuracy', 'Testing Accuracy'])
                result1000.to_excel('G:\\material\\reslut\\meanFre\DMN\\P'+file_name, index=True, header=True)
