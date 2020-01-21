#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Automatic system which accepts the mark of a student and generates their grades
mark = int(input("Enter marks:"))
grade = ''
if mark > 75 and mark <=100:
    grade='A'
elif mark > 60 and mark <=75:
    grade='B'
elif mark >50 and mark <=60:
    grade='C'
else:
    grade='D'
print('Grade = ',grade)


# In[ ]:




