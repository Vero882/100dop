# Day 31 - Intermediate - Flash card app capstone project
This day is a capstone project to build a flashcard app.

## The video lessons are:
234. Day 31 goals: what you will make by the end of the day
235. Step 1: Create the user interface (UI) with Tkinter
236. Solution & walkthrough for creating the UI
237. Step 2: Create new flash cards
238. Solution & walkthrough for creating new flash cards
239. Step 3: Flip the cards!
240. Solution & walkthrough for flipping cards
241. Step 4: Save your progress
242. Solution & walkthrough for saving progress


## Day 31 Project
The project for today is building a flashcard app for studying different topics, such as languages. The provided one uses a .csv file to provide values of the front and back of cards. 

### Files Provided
- main.py
- data
    - french_words.covers
- images
    - card_back.png
    - card_front.png
    - right.png
    - wrong.png

## Thoughts
I had a bit of a difficult time with this. Creating the UI and everything was pretty easy, but putting everything together felt like a huge undertaking. Putting all the different pieces together felt like such a large scale project. 

For example, initially I was using labels on top of the canvas for the **language_label** and **word_label**, but realized things weren't working quite like they should. Going through the documentation I figured out thhat you can generate text onto a canvas at a certain position with **canvas.create_text**. 

Overall, it was a very interesting project to figure out how to compile the thoughts and tasks in my head in such a way to get this project built with everything we've learned so far. 