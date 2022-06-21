Tweak the pipeline in the tutorial, by applying PCA to reduce the dimensionality of features (feature selection). 


Implement cross-validation, but this time changing to leave-one-out.

What are the features we are using in this model? What are the numbers representing the shape of the time series (168, 64), and the shape of the connectivity matrix (64 x 64), (155 x 200?

**Response** 168 are the number of time points/mesures and 64 is the amount of ROIs. The matrix is 64*64 because we have a connectivity measure (edges) for each pair of ROIs (nodes). We end up with a matrix 155 *2016. We have 155 subjects with 2016 connectivity measures. 

Using the performance of the different polynomial fit (MSE) for train and test error, try to explain why increasing complexity of models does not necessarily lead to a better model.
**Response** Increasing the complexity of models can lead to overfitting on the training set. We go from high bias to low bias, and from low variance to high variance, as we add more complexity.  

Remember we talked about regularization in the introduction to machine learning? Variance of model estimation increases when there are more features than samples. This especially relevant when we have > 2000 features ! Apply a penalty to the SVR model. Refer to the documentation https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html. 
