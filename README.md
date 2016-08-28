# Markov Text Generator #

### How Do I Use It?

Clone this repo into the directory in which you'll be using it. Then in your file, you can use the following:

```
import markovgenerator as m

print(m.generate_text(file="example.txt")) # generates text from a file

print(m.generate_text(string="some sample text")) # generates text from a string

m.generate_text(file="example.txt",resolution=2,output_size=100) # outputs 100 words, 
# and each word is chosen by looking up the two previous word (2-token lookback).

```


### Features


### What Is It?

This Python script utilizes a Markov Chain (a non-deterministic finite state machine that doesn't track history) to generate text based on source text. Below is an example where the script uses one previous word to identify the next. My implementation lets the user decide how much history should be retained (how many consecutive tokens make up the key for each state), and whether words or letters should be used as the tokens (`"her" -> "fleece"` vs `"her fleece" -> "as"` vs `"he" -> "r"`).

### Example

```
"Mary had a little lamb,
her fleece as white as snow."
```

We can divide this text into a series of tokens (words), and then use this to build our state machine.
Each word acts as a dictionary key for the word after it.
```
{
"Mary" 	-> 	"had"
"had" 	-> 	"a"
"a" 	-> 	"little"
...
}
```
In this example so far, each word has one word that follows it, and thus is deterministic. Running it, starting at Mary, it would go through every word in the correct order. But what happens when we get to "as"?

`"as" -> ["white","snow"]`

Here, the state machine is confronted with two possible actions. Follow the edge to "white," or follow the edge to "snow." By my design decision, this choice is made using a random number generator. Possible outputs include:

```
>"her fleece as white as white as white as white as snow"
>"her fleece as snow"
```
Or any combination thereof. Note that because nothing comes after "snow," "snow" is a terminal state that stops the machine and returns the accumulated output.


### Future Plans
1. ~~add ability to clip sentence fragments from beginning and end of output~~ DONE
2. ~~add ability to retain newline characters~~
3. add different, less random ways to pick which edge to take from a state with multiple leaving edges
4. clean up this documentation
