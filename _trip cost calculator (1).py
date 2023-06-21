#!/usr/bin/env python
# coding: utf-8

# In[32]:


num = int(input('enter number of people to divide:'))


# In[33]:


names=[]
money = []
i = num
while i>0:
    n = input('enter your name')
    m = float(input('money you spent'))
    names.append(n)
    money.append(m)
    i = i-1


# In[35]:


total_spend = sum(money)
cost_per_person = total_spend / num


# In[39]:


balance = []
for y in money:
    balance.append(y-cost_per_person)


# In[40]:


print('Total budget = ',total_spend)
print('cost of individual = ',cost_per_person)


# In[41]:


j =0
while j<num:
    if balance[j] <= 0:
        print(names[j],'gives', -1*balance[j])
    else:
        print(names[j],'gets', balance[j])
    j +=1


# In[ ]:




