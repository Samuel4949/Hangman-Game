# Hangman-Game
<h3>How it Works</h3>
<ol>
  <li>The program chooses a random word from a text file</li>
  <li>Two variables are set: one with the randomly chosen word and the other the length of the word in underscores "_"</li>
  <li>Asks for the user input and checks if the user has entered a letter they have not guessed before and if it is only one letter</li>
  <li>Then if the inputted letter is in the random word, the position of the letter will be revealed under the corresponding underscore position</li>
  <li>If the letter is not in the random word, then the number of times the user guessed wrongly will be incremented till one</li>
  <li>This program will repeat the above steps (3-5) till the user either gets the random word or till the hits the limit of allowed wrong guesses</li>
</ol>
<hr>
<h3>Features</h3>
<ul>
  <li>Random Module</li>
  <li>String Module</li>
</ul>
