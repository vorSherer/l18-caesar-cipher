## Caesar Cipher

Lab 18 - Cryptography

### *Author: Thomas Sherer*, 2020-07-29

---

## Description
### Feature Tasks and Requirements
- Create an __`encrypt`__ function that takes in a plain text phrase and a numeric shift.
    - the phrase will then be __`shifted`__ that many letters.
        - e.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘acb’, 10) would return ‘klm’
    - shifts that exceed 26 should wrap around
        - e.g. encrypt(‘abc’,27) would return ‘bcd’
- Create a __`decrypt`__ method that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form as long as correct key is supplied.
- Break the cipher so that an encrypted message can be transformed into its original state *WITHOUT* access to the key.
- Devise a method for the computer to determine if code was broken with minimal human guidance. <br>

### Implementation Notes
In order to accomplish a certain task you’ll need access to a __`corpus`__ of English words.
A search on something like __`python list of english words`__ should get you going.

---

My code is [here](./caesar_cipher/caesar_cipher.py) <br>

---

### Collaborations and Attributions
.gitignore content courtesy of https://www.toptal.com/developers/gitignore/api/python

__likegeeks.com__ helped with [understanding chr() and ord()](https://likegeeks.com/python-caesar-cipher/)

__Geeks for Geeks__ helped with [encryptions and decryption code](https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/)

__Stack overflow__ helped with how to deal with [spaces](https://stackoverflow.com/questions/20269330/how-to-make-a-caesar-cipher-work-with-input-that-has-spaces-in-python) and how to deal with [punctuation marks](https://stackoverflow.com/questions/54172455/how-to-leave-punctuation-unchanged-in-caesar-cipher-python)

__Skyler Burger__ helped immensely when trying to import a corpus of english words when 'import' wasn't working for the cipher-breaker function.

nltk.org Word Lists downloaded directly from [here (item 61 on the list)](http://www.nltk.org/nltk_data/)

__Lee-Roy King__ helped in a big way to get caesar_cracker function working beyond brute force level.

<!-- Submission PR: NN -->
