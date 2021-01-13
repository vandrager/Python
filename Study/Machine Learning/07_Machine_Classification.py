import pandas as pd
import seaborn as sns
import numpy as np
'''
[Step 1] 데이터 준비 - Seaborn에서 제공하는 titanic 데이터셋 가져오기
'''

# load_dataset 함수를 사용하여 데이터프레임으로 변환
df = sns.load_dataset('titanic')

#  IPython 디스플레이 설정 - 출력할 열의 개수 한도 늘리기
pd.set_option('display.max_columns', 15)

'''
[Step 2] 데이터 탐색
'''

# 데이터 자료형 확인
print(df.info())  
print('\n')

# NaN값이 많은 deck 열을 삭제, embarked와 내용이 겹치는 embark_town 열을 삭제
rdf = df.drop(['deck', 'embark_town'], axis=1)  
print(rdf.columns.values)
print('\n')

# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)
rdf = rdf.dropna(subset=['age'], how='any', axis=0)  
# print(len(rdf)) 714
print('\n')

# embarked 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()   
# print(most_freq) S
print('\n')

print(rdf.describe(include='all'))
print('\n')

rdf['embarked'].fillna(most_freq, inplace=True)



'''
[Step 3] 분석에 사용할 속성을 선택
'''

# 분석에 활용할 열(속성)을 선택 
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head())   
print('\n')
#    survived  pclass     sex   age  sibsp  parch embarked
# 0         0       3    male  22.0      1      0        S
# 1         1       1  female  38.0      1      0        C
# 2         1       3  female  26.0      0      0        S
# 3         1       1  female  35.0      1      0        S
# 4         0       3    male  35.0      0      0        S
# 원핫인코딩 - 범주형 데이터를 모형이 인식할 수 있도록 숫자형으로 변환
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town') # prefix='town'사용해서 열 이름에 접두어 'town'을 붙인다.
ndf = pd.concat([ndf, onehot_embarked], axis=1)

ndf.drop(['sex', 'embarked'], axis=1, inplace=True)
print(ndf.head())   
print('\n')
#    survived  pclass   age  sibsp  parch  female  male  town_C  town_Q  town_S
# 0         0       3  22.0      1      0       0     1       0       0       1
# 1         1       1  38.0      1      0       1     0       1       0       0
# 2         1       3  26.0      0      0       1     0       0       0       1
# 3         1       1  35.0      1      0       1     0       0       0       1
# 4         0       3  35.0      0      0       0     1       0       0       1


'''
[Step 4] 데이터셋 구분 - 훈련용(train data)/ 검증용(test data)
'''

# 속성(변수) 선택
X=ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 
       'town_C', 'town_Q', 'town_S']]  #독립 변수 X
y=ndf['survived']                      #종속 변수 Y

# 설명 변수 데이터를 정규화(normalization)
from sklearn import preprocessing # 데이터의 상대적 크기 차이를 없애기 위해 정규화 필요
X = preprocessing.StandardScaler().fit(X).transform(X)

# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10) 

print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)
# train data 개수:  (499, 9)
# test data 개수:  (215, 9)

'''
[Step 5] KNN 분류 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 KNN 분류 모형 가져오기
from sklearn.neighbors import KNeighborsClassifier

# 모형 객체 생성 (k=5로 설정)
knn = KNeighborsClassifier(n_neighbors=5)

# train data를 가지고 모형 학습
knn.fit(X_train, y_train)   

# test data를 가지고 y_hat을 예측 (분류) 
y_hat = knn.predict(X_test)

print(y_hat[0:10])
print(type(y_hat))
print(y_test.values[0:10])
# [0 0 1 0 0 1 1 1 0 0]
# [0 0 1 0 0 1 1 1 0 0]


# 모형 성능 평가 - Confusion Matrix 계산
from sklearn import metrics 
knn_matrix = metrics.confusion_matrix(y_test, y_hat)  
print(knn_matrix)
# [[109  16]
#  [ 25  65]]

# 모형 성능 평가 - 평가지표 계산
knn_report = metrics.classification_report(y_test, y_hat)            
print(knn_report)
'''
              precision    recall  f1-score   support

           0       0.81      0.87      0.84       125
           1       0.80      0.72      0.76        90

    accuracy                           0.81       215
   macro avg       0.81      0.80      0.80       215
weighted avg       0.81      0.81      0.81       215
'''

# 해석: f1-score지표를 보면 미생존자(0)과 생존자(1) 예측의 정확도는 상이하며 예측능력에 다소 차이가 있다는 것을 알 수 있다.
# confusion_matrix: 모형의 예측값(TF)과 실제 값(TF)을 각각 축으로 하는 2 X 2 매트릭스로 표현한 것을 말함 (True/False, Positive/Negative)
# precision: True로 예측한 분석대상 중에서 실제 값이 True인 비율을 말함, 모형의 정확성을 나타냄
# recall: 실제 값이 True인 분석대상 중에서 True로 예측하여 모형이 적중한 비율, 모형의 완전성을 나타냄
# f1-score: 정확도와 재현율이 균등하게 반영될 수 있도록 정확도와 재현율의 조화평균을 계산한 값, 모형의 예측력을 종합적으로 평가

## SVM
from sklearn import svm

# 모형 객체 생성
svm_model = svm.SVC(kernel='rbf')

# train data를 가지고 모형 학습
svm_model.fit(X_train, y_train)
y_hat = svm_model.predict(X_test)

print(y_hat[0:10])
print(y_test.values[0:10])
# [0 0 1 0 0 0 1 0 0 0]
# [0 0 1 0 0 1 1 1 0 0]
svm_metrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_metrix)
# [[120   5]
#  [ 35  55]]

# 모형 성능 평가 - 평가 지표 계산
svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)
'''
              precision    recall  f1-score   support

           0       0.77      0.96      0.86       125
           1       0.92      0.61      0.73        90

    accuracy                           0.81       215
   macro avg       0.85      0.79      0.80       215
weighted avg       0.83      0.81      0.81       215
'''

uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/\
breast-cancer-wisconsin/breast-cancer-wisconsin.data'
df = pd.read_csv(uci_path, header=None)
df.columns = ['id', 'clump', 'cell_size',  'cell_shape',  'adhesion',  'epithlial', 'bare_nuclei',
                'chromatin',  'normal_nucleoli',  'mitoses',  'class']

pd.set_option('display.max_columns', 15)
print(df.head())
print(df.info())


df['bare_nuclei'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['bare_nuclei'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['bare_nuclei'] = df['bare_nuclei'].astype('float')
print(df.describe())

'''
[Step 3] 데이터셋 구분 - 훈련용(train data)/ 검증용(test data)
'''

# 속성(변수) 선택
X=df[['clump','cell_size','cell_shape', 'adhesion','epithlial',
      'bare_nuclei','chromatin','normal_nucleoli', 'mitoses']]  #설명 변수 X
y=df['class']                                                   #예측 변수 Y

# 설명 변수 데이터를 정규화
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10) 

print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)
print('\n')


'''
[Step 4] Decision Tree 분류 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 Decision Tree 분류 모형 가져오기
from sklearn import tree

# 모형 객체 생성 (criterion='entropy' 적용) - 분류 정도를 평가하는 기준, 트리 레벨을 5로 지정, 5단계 까지 가지를 확장 가능하다는 뜻
tree_model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)

# train data를 가지고 모형 학습
tree_model.fit(X_train, y_train)   

# test data를 가지고 y_hat을 예측 (분류) 
y_hat = tree_model.predict(X_test)      # 2: benign(양성), 4: malignant(악성)

print(y_hat[0:10])
print(y_test.values[0:10])
print('\n')
# [4 4 4 4 4 4 2 2 4 4]
# [4 4 4 4 4 4 2 2 4 4]

# 모형 성능 평가 - Confusion Matrix 계산
from sklearn import metrics 
tree_matrix = metrics.confusion_matrix(y_test, y_hat)  
print(tree_matrix)
print('\n')
# [[127   4] (양성 종양 목표값 = 2, 악성 종양 = 4) 
#  [  2  72]] --> 양성을 정확히 예측한 TP는 127개, 양성을 악성으로 잘못분류한 FP는 4개, 악성을 양성으로 잘못분류한 FN은 2개, 악성을 정확하게 예측한 값은 72개이다.
# 모형 성능 평가 - 평가지표 계산
tree_report = metrics.classification_report(y_test, y_hat)            
print(tree_report)
'''
              precision    recall  f1-score   support

           2       0.98      0.97      0.98       131
           4       0.95      0.97      0.96        74

    accuracy                           0.97       205
   macro avg       0.97      0.97      0.97       205
weighted avg       0.97      0.97      0.97       205
'''

