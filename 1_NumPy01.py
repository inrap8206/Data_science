#!/usr/bin/env python
# coding: utf-8

# <img src='img/1_numpy.png' width=50 style='float:left'>
# 
# # NumPy

# - Numerical Python
# - http://www.numpy.org
# 
# 
# - C언어로 구현된 파이썬 라이브러리(외부 라이브러리)
# - 고성능 수치계산을 위해 만들어진 파이썬 패키지
# - Vector, matrix, n-th array(ndarray) 등의 데이터 분석을 위한 패키지
# - 벡터 및 행렬 연산에 있어서 매우 편리한 기능을 제공
# 
# 
# - array(배열) 단위로 데이터를 관리하며 이에 대해 연산을 수행
#     - Numpy의 기본단위가 되는 array는 Dynamic type을 지원하지 않음. 한 타입만 지원
#     - 1차원의 Numpy array : Vector
#     - 2차원의 Numpy array : Matrix
#     - 3차원 이상의 Numpy array : Tensor
#     
#     
# - pandas와 matplotlib 기반
# 

# **numpy 모듈 선언**

# In[1]:


import numpy as np


# In[2]:


np.__version__


# ***참고. 선언된 모듈과 패키지의 영향 범위***
# 
# - 파이썬(or IPython) 콘솔이나 주피터 노트북의 코드 셀에서 import로 불러온 모듈이나 패키지는 한 번만 선언하면 다시 선언하지 않고 이용
# - 주피터 노트북에서 새로운 노트북을 실행한 경우 다시 선언해야 함
# - 파이썬 코드를 파일로 저장할 때도 모듈과 패키지는 이를 사용하는 코드 앞에 한번만 선언하면 됨

# # Array 정의 및 사용
# 
# - 시퀀스 데이터(리스트, 튜플 등)로부터 배열 생성
# 
# 
# - https://numpy.org/doc/stable/reference/arrays.html

# ### array(object, dtype, ... )    
# 
# 형식 : arr_obj = np.array(seq_data)    

# In[4]:


data1 = [1,2,3]
data1


# In[5]:


data2 = [1,2,3,3.5,5]
data2


# <img src='img/2_np.array.png' style='left'>

# In[6]:


# 리스트 객체를 이용하여 array 생성
arr1 = np.array(data1)
arr1


# **array 크기 확인 : shape**

# In[7]:


# array 크기 확인
arr1.shape


# In[8]:


# 리스트를 직접 입력하여 array 생성
arr2 = np.array([1,2,3,4,5])
arr2


# In[9]:


arr2.shape


# **array 자료형 확인 : dtype**

# In[10]:


# array의 자료형 확인
arr2.dtype


# In[11]:


arr3 = np.array([1, 2, 3, 3.5, 4])
arr3


# In[12]:


arr3.dtype


# In[13]:


arr3.shape


# In[17]:


arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr4


# In[15]:


arr4.shape


# In[16]:


arr4.dtype


# ## numpy 자료형
# - 부호가 있는 정수 int(8, 16, 32, 64)
# - 부호가 없는 정수 uint(8 ,16, 32, 64)
# - 실수 float(16, 32, 64, 128)
# - 복소수 complex(64, 128, 256)
# - 불리언 bool
# - 문자열 string_
# - 파이썬 오프젝트 object
# - 유니코드 unicode_

# ##  범위를 지정해 배열 생성(1) : np.arange() 함수
# 
# 
# ### 형식 : arr_obj = np.arange([start,] stop[, step])

# In[18]:


np.arange(10)


# In[19]:


np.arange(1,5)


# In[22]:


np.arange(1,10, 2)


# In[23]:


np.arange(12).reshape(3,4)


# In[24]:


b1 = np.arange(12).reshape(3,4)
b1.shape


#     reshape(m,n)의 m*n의 개수와 arange()로 생성되는 원소의 개수와 일치해야 함

# In[26]:


b2 = np.arange(7).reshape(3,3)


# In[28]:


b3 = b1.reshape(4,3)
b3


# ## 범위를 지정해 배열생성(2) : linspace() 함수
#  ### 형식 :arr.obj = np.linspace(start, stop[, num=50])

# In[29]:


np.linspace(1,10,10)


# In[30]:


np.linspace(0, np.pi, 20)


# In[33]:


np.linspace(1,10)


# ## 특별한 형태의 배열 생성
# ### np.zeros(), np.ones(), np.eye() 함수

# **1) 모든 요소가 0인 배열 생성 : np.zeros(shape, dtype=float, ...)**

# In[35]:


np.zeros(10, dtype=int)


# In[36]:


np.zeros((3,5))


# In[37]:


np.zeros((3,5)).reshape(5,3)


# **2) 모든 요소가 1인 배열 생성 : np.ones(shape, dtype=None)**

# In[38]:


np.ones(10)


# In[39]:


np.ones((3,5), dtype=int)


# **3) 대각요소가 1인 배열 생성1 : np.eye(n, m, k=K, dtype=float)**

# In[40]:


# 3행 3열의 대각요소가 1인 행렬
np.eye(3)


# In[41]:


np.eye(3,4)


# In[42]:


np.eye(3,4, k=1, dtype=int)


# In[43]:


np.eye(3,4, k=2)


# In[44]:


np.eye(3,4, k=-1)


# **4) 대각요소가 1인 배열 생성2 : np.identity(n, dtype=자료형)**

# In[46]:


# n*n 크기의 단위행렬 생성

np.identity(5, dtype=int)


# **5) 초기화되지 않은 배열 생성 : np.empty(shape, dtype=float)**

# In[47]:


# 초기화되지 않은 배열 생성
np.empty(4)


# **배열 생성 함수**

# <img src='img/3_numpy_array_function.png' width='500' style='float:left'>

# ## 배열의 데이터 타입 변환:  astype() 함수

# **[형식]**
# num_arr = str_arr.astype(dtype)

# dtype : int, float, str
# **NumPy 데이터 형식 : dtype**
# 
# <img src='img/4_numpy_dtype.jpg' width='300' style='float:left'>

# **문자열 배열을 숫자형 배열로 변환**

# In[37]:


np.array(['1.5', '0.62','2','3.14','3.141592'])


# In[53]:


str_a1 = np.array(['1.5', '0.62','2','3.14','3.141592'])
# num_a1 = str_a1.astype('float32')
num_a1 = str_a1.astype(float)
num_a1


# In[49]:


str_a1.dtype


# In[54]:


num_a1.dtype


# In[55]:


str_a2 = np.array(['1','3','5','7','9'])
num_a2 = str_a2.astype(int)
num_a2


# In[57]:


num_a3 = str_a2.astype(float)
num_a3


# In[58]:


num_a4 = str_a1.astype(int)
num_a4


# **실수형 배열을 정수형 배열로 변환**

# In[59]:


num_f1 = np.array([10, 21, 0.549, 4.75, 5.98])
num_f1


# In[60]:


num_i1 = num_f1.astype(int)
num_i1


# In[62]:


num_f1.dtype


# In[63]:


num_i1.dtype


# **숫자형 배열을 문자열 배열로 변환**

# In[64]:


num_f1.astype('U')


# In[65]:


num_f1.astype('S')


# ## 난수 배열 생성
# 
#  ### random.rand(), random.randint() 함수

# **random.rand([d0, d1, ..., dn])**
# 
# - [0과 1) 사이의 `실수` 난수를 갖는 NumPy 배열을 생성
# - rand(d0, d1, ..., dn)을 실행하면 (d0, d1, ..., dn)의 형태를 보이는 실수 난수 배열 생성

# In[67]:


np.random.rand(10)
np.random.rand(2,5)


# In[68]:


np.random.rand()


# In[69]:


np.random.rand(2,3,4)


# **random.randint([low,] high [,size])**
# 
# - [low, high) 사이의 `정수` 난수를 갖는 NumPy 배열을 생성
# - size : (d0, d1, ..., dn) 형식으로 입력

# In[70]:


np.random.randint(10)


# In[74]:


np.random.randint(10, 20)


# In[75]:


np.random.randint(10, 20, size=(3,5))


# # Array 연산

# ## 기본 연산(합, 차, 곱, 나눗셈 등) 
# 
# : 기본적으로 동일한 크기의 array 간 연산 수행

# In[77]:


arr1 = np.array([[1,3,4],[4,3,6]])
arr1


# In[78]:


arr2 = np.arange(10,16).reshape(2,3)
arr2


# In[79]:


print(arr1.shape, arr2.shape)


# **배열의 합**

# In[80]:


arr1 + arr2


# **배열의 차**

# In[81]:


arr1 - arr2


# **배열의 곱**

# In[82]:


arr1 * arr2


# **배열의 나눗셈**

# In[83]:


arr1 / arr2


# **배열의 스칼라 곱**

# In[84]:


arr2*2


# **배열의 비교 연산**

# In[87]:


arr2 > 12


# ## 배열의 Broadcasting 
# - 서로 크기가 다른 array들의 연산이 가능하도록 배열을 자동적으로 변환하여 연산 수행

# In[88]:


arr1


# In[89]:


arr3 = np.array([10,11,12])
arr3


# In[91]:


(arr1.shape, arr3.shape)


# In[92]:


arr1 + arr3


# In[93]:


arr1 ** 2


# **브로드캐스팅이 일어날 수 있는 조건**
# - 두 배열 간의 연산에서 최소한 하나의 배열의 차원이 1인 경우(0번 축이든 1번 축이든; 1행이든 1열이든)
# - 차원의 짝이 맞을 때(차원에 대해 축의 길이가 동일하면)

# ![image.png](attachment:image.png)
# 출처: http://www.astroml.org/book_figures/appendix/fig_broadcast_visual.html
