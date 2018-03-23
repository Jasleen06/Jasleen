
# coding: utf-8

# In[19]:

def hamming_dist(s1, s2):
    a=0
    if len(s1) != len(s2):
        raise ValueError("Provide equal lengh sequences")
    for ch1,ch2 in zip(s1,s2):
         if ch1!=ch2:
            if (s1.index(ch1))==0 and (s2.index(ch2))==0 and ch1.lower()==ch2.lower():
                a=0
            elif ch1.lower()==ch2 or ch2.lower()==ch1:
                a+=0.5
            elif ((ch1=='s' and ch2=='z') or (ch1=='z' and ch2=='s') or (ch1=='S' and ch2=='Z') or (ch1=='Z' and ch2=='S')):
                a+=0
            else:
                a+=1
                if (ch1.islower() and ch2.isupper()) or (ch2.islower() and ch1.isupper()):
                    a+=0.5
                else:
                    a+=0
    return a   

    


# In[20]:

hamming_dist("make","Mage")


# In[21]:

hamming_dist("MaiSY","MaiZy")


# In[22]:

hamming_dist("Eagle","Eager")


# In[23]:

hamming_dist("Sentences work too.","Sentences wAke too.")


# In[24]:

hamming_dist("data Science","Data Sciency")


# In[25]:

hamming_dist("organizing","orGanising")


# In[26]:

hamming_dist("AGPRklafsdyweIllIIgEnXuTggzF","AgpRkliFZdiweIllIIgENXUTygSF")


# First Word                                     Second Word                               Distance Score
# data Science                                   Data Sciency                                   1
# organizing                                     orGanising                                    0.5
# AGPRklafsdyweIllIIgEnXuTggzF                   AgpRkliFZdiweIllIIgENXUTygSF                  8.5
# 
# 
# 1. Hamming distance algorithm can be used to determine the genetic distance between different species of an animal.This can be achieved by comparing the DNA sequnces of different speicies.
# 2. It can also be used for secure communication between two parties. The inputs from both the parties (secret code) are checked for their hamming distance.
# 
