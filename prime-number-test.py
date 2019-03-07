#!/usr/bin/env python
# coding: utf-8

# In[7]:


def primetest(num):
   for y in range(2,num-1):
    z = num % y
    if z != 0 and y < num-1:
        print(str(num) + " is not divisble by " + str(y))
    elif z == 0:
            print(str(num) + " is divisble by " + str(y) + "; \n" + str(num) + " is not a prime number")
            return
    elif z != 0:
          print(str(num) + " is not divisble by " + str(num-1) + "; \n" + str(num) +
                " is not divisble by any number; \n" + str(num) + " is a prime number")
    else:
        print(str(num)+ " is not a prime number................")
primetest(12)


# In[ ]:





# In[ ]:




