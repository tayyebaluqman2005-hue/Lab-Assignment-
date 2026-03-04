#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Print all even numbers from 2 to 20
for i in range(2, 21):
    if i % 2 == 0:
        print(i)


# In[2]:


#2. Create a list of names and print each name in uppercase
names = ["Ali", "Ahmed", "Sara", "Ayesha"]

for name in names:
    print(name.upper())


# In[3]:


#3. Print numbers from 10 to 1 in reverse order
for i in range(10, 0, -1):
    print(i)


# In[5]:


#4. Print only numbers divisible by 3
for i in range(3, 51, 3):
    print(i)


# In[6]:


#5. Print squares of numbers from 1 to 10
for i in range(1, 11):
    print(i * i)


# In[7]:


#6. Convert Celsius temperatures to Fahrenheit
celsius = [0, 10, 20, 30, 40]

for c in celsius:
    fahrenheit = (c * 9/5) + 32
    print(fahrenheit)


# In[8]:


#7. Print multiplication table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)


# In[9]:


#8. Find the sum of all numbers in a list
numbers = [5, 10, 15, 20]
total = 0

for num in numbers:
    total += num

print("Sum =", total)


# In[10]:


#9. Print each character of a string separately
text = "Python"

for char in text:
    print(char)


# In[12]:


#10. Print words with more than 5 letters
words = ["apple", "banana", "grapes", "pineapple", "kiwi"]

result = filter(lambda w: len(w) > 5, words)

for word in result:
    print(word)


# In[ ]:




