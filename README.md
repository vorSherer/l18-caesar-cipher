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

### Getting Started
- Clone this repository to your local machine.

```
$ git clone [repo clone url here]
```

### To run the program from VS Code:
<!-- - Select ```File``` -> ```Open``` -> ```Project/Solution``` -->

- Next navigate to the location into which you cloned the Repository.

<!-- - Double click on the ```Lab01-About-Me``` directory. -->

<!-- - Then select and open ```AboutMe.py``` -->

---

### Visuals
<!-- 
***[Add screenshots of your application in action]***
 -->

#### Application Start
![Image 1](https://via.placeholder.com/750x500)
#### Using the Application
![Image 1](https://via.placeholder.com/750x500)
#### Application End
![Image 1](https://via.placeholder.com/750x500)

---

### Change Log
<!-- 
***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]***  
1.3: *Added summary comments to the methods* - 8 Nov 2010  
1.2: *Changed variable names to follow proper convention* - 6 Nov 2010  
1.1: *Added a Try/Catch/Finally for Question 2* - 5 Nov 2010  
 -->
0.1.0: Poetry-created baseline project - 2020-07-29

### Collaborations and Attributions
.gitignore content courtesy of https://www.toptal.com/developers/gitignore/api/python


<!-- Submission PR: NN -->
