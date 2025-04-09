# **Caesar Cypher decrypter Project**
## **Table of Contents**
1. Project Overview
2. Installation
3. Usage 
4. Deactivate Virtual Environment
## **Project Overview**
This project utilizes basic brute force techniques and the nltk module to decrypt a caesar cypher without knowing the encryption key. It decodes the encryption and provides the encryption key as well.
## **Installation**
`git clone https://github.com/Daindia/Caesar-Cipher.git`
### **Installing nltk module:**
`pip install nltk`

### **Creating a virtual environment:**

`python -m venv decrypter`

### **Activating the virtual environment**
1. **For Windows:**\
   `.\decrypter\Scripts\activate`
   
3. **For Linux:**\
   `source decrypter/bin/activate`

## **Usage**
> Runs with any code editor that supports python
- **You can provide an encrypted text like:**
  
  `decrypter("Uy tmbbk zai")`

- **Downloading word corpus:**
  > Downloads a list of English words

  ```python
  import nltk
  from nltk.corpus import words

  nltk.download("words")

  # Creates a set of englsih words
  english_words = set(words.words())
  
## **Deactivate Virtual Environment**
`deactivate`
