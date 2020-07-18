# Readability
 What sorts of traits are characteristic of higher reading levels? Well, longer words probably correlate with higher reading levels. Likewise, longer sentences probably correlate with higher reading levels, too. A number of “readability tests” have been developed over the years, to give a formulaic process for computing the reading level of a text. One such readability test is the Coleman-Liau index. 
 
## The Coleman-Liau index
 The Coleman-Liau index of a text is designed to output what (U.S.) grade level is needed to understand the text. The formula is:
```C
index = 0.0588 * L - 0.296 * S - 15.8
```
 Here, L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
 
## Usage
 A program that computes the approximate grade level needed to comprehend some text.
```
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```