import pandas as pd
dataset = pd.read_csv('Placement_Data_Full_Class.csv')

gender = dataset['gender']
ssc_b = dataset['ssc_b']
hsc_b = dataset['hsc_b']
hsc_s = dataset['hsc_s']
degree_t = dataset['degree_t']
workex = dataset['workex']
specialisation = dataset['specialisation']
status = dataset['status']

#changing into dummy variable
gender = pd.get_dummies(gender, drop_first=True )
ssc_b = pd.get_dummies(ssc_b, drop_first=True )
hsc_b = pd.get_dummies(hsc_b, drop_first=True )
hsc_s = pd.get_dummies(hsc_s, drop_first=True)
degree_t = pd.get_dummies(degree_t, drop_first=True)
workex = pd.get_dummies(workex, drop_first=True )
specialisation = pd.get_dummies(specialisation, drop_first=True)
status = pd.get_dummies(status, drop_first=True)

X = dataset[['ssc_p', 'hsc_p','degree_p', 'etest_p', 'mba_p']]
X = pd.concat([X, gender, ssc_b, hsc_b, hsc_s, degree_t, workex, specialisation], axis=1)

y = status['Placed']

from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = Sequential()
model.add(Dense(units=20, input_dim=14, activation='relu'))
model.add(Dense(units=15, activation='relu'))
model.add(Dense(units=10, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer=Adam(learning_rate=0.00001), loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train,epochs= 500)

pred = model.predict(X_test)

model.fit(X_train, y_train,epochs= 500, verbose=0)

print(y_test)

for i in range(len(pred)):
    if pred[i]>=0.5:
        pred[i]=1
    else:
        pred[i]=0