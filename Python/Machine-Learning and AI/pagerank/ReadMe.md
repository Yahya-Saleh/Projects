# Page Rank

An AI that ranks Webpages using both sampling and iteration. [Watch an illustration](https://youtu.be/0Kni74X-CrI)!

## Usage

```bash
$ python pagerank.py corpus0
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
```

Pass an directory that contains html files as a second line argument and the program will rate each file's "importance" based on how many file it links to.

## Table of content

- [Page Rank](#page-rank)
  - [Usage](#usage)
  - [Table of content](#table-of-content)
  - [PageRank algorithm](#pagerank-algorithm)
  - [Calculating Page Rank](#calculating-page-rank)
    - [Random Surfer Model](#random-surfer-model)
      - [Markov chain](#markov-chain)
      - [Damping factor](#damping-factor)
    - [Iterative algorithm](#iterative-algorithm)
  - [Pagerank.py](#pagerankpy)
    - [Main](#main)
    - [Crawl](#crawl)
    - [Transition model](#transition-model)
    - [Sample pagerank](#sample-pagerank)
    - [Iterate pagerank](#iterate-pagerank)
    - [rounded](#rounded)
  - [Acknowledgements](#acknowledgements)

---

## PageRank algorithm

How do search engines, like google, decide which websites are more "important" and suitable for the user? Well one heuristic is that the more pages link to a webpage, the more important it is. One issue with this approach is that one can inflate the amount of incoming links to make their site more important.

For that reason, the **PageRank algorithm** was created by Google’s co-founders (including Larry Page, for whom the algorithm was named). In PageRank’s algorithm, a website is more important if it is linked to by other important websites, and links from less important websites have their links weighted less.

---

## Calculating Page Rank

This projects implements two distinct methods to calculate a page's rank.

### Random Surfer Model

The random surfer model images a hypothetical surfer on the internet who clicks on links at random. Consider the corpus of web pages below, where an arrow between two pages indicates a link from one page to another.

![a corpus of linked webpages](../../../Snippets/Python/AI/page%20rank/corpus.png)

If the surfer was to start at page 2, randomly, then they wil randomly go to either page 1 or page 3 randomly (duplicate links on the same page are treated as a single link, and links from a page to itself are ignored as well). And if the choose page 3 their options become either page 2 or page 4.

A page's rank would then be the probability that the random surfer would be there at any given time.

#### Markov chain

One way to interpret this model is as a Markov Chain, where each page represents a state, and each page has a transition model that chooses among its links at random. At each time step, the state switches to one of the pages linked to by the current state. This way we can generate an estimate for each page's rank by sampling the chain.

#### Damping factor

If you consider the figure below, you'll find that if the surfer started at either page 5 or page 6 the probability will be 0.5 for both pages and zero for the rest.

![disconnected network](../../../Snippets/Python/AI/page%20rank/network_disconnected.png)

To account for this issue we introduce a damping factor, `d`, usually equaling 0.85. In this new definition, when the surfer picks a page, the surfer has a `1 - d` (0.15 in this case) chance to pick a page that the page they are on is not linked to.

### Iterative algorithm

We can also define a page’s PageRank using a recursive mathematical expression. Let `PR(p)` be the PageRank of a given page `p`: the probability that a random surfer ends up on that page. there is two ways to define `PR(p)`:

- With probability `1 - d`, the surfer chose a page at random and ended up on page `p`.
- With probability `d`, the surfer followed a link from a page `i` to page `p`.

The first condition is fairly straightforward to express mathematically: it’s `1 - d` divided by `N`, where `N` is the total number of pages across the entire corpus.

For the second condition, we need to consider each possible page `i` that links to page `p`. For each of those incoming pages, let `NumLinks(i)` be the number of links on page `i`. Each page `i` that links to `p` has its own PageRank, `PR(i)`, representing the probability that we are on page `i` at any given time. And since from page `i` we travel to any of that page’s links with equal probability, we divide `PR(i)` by the number of links `NumLinks(i)` to get the probability that we were on page `i` and chose the link to page `p`.

This gives us the following definition for the PageRank for a page `p`:

![PageRank Formula](../../../Snippets/Python/AI/page%20rank/formula.png)

- `d` is the damping factor.
- `N` is the total number of pages in the corpus.
- `i` ranges over all pages that link to page `p`.
- `NumLinks(i)` is the number of links present on page `i`.

To calculate the pages' rank, we start by assuming that all pages have a probability of `1/N`, then iterating over them using teh formula to calculate the rank.

---

## [Pagerank.py](pagerank.py)

Notice first the definition of two constants at the top of the file: `DAMPING` represents the damping factor and is initially set to `0.85`. `SAMPLES` represents the number of samples we’ll use to estimate PageRank using the sampling method, initially set to `10,000` samples.

### Main

Expects two command line arguments, the latter of which is passed to the crawl function.

```bash
python pagerank.py corpus
```

After getting the dictionary representing the corpus, main runs sample_pagerank and iterate_pagerank and prints out their output.

### Crawl

Takes in a directory and loops through every html file finding the pages the files is linked to. It returns the findings as a dictionary where the filename is the key and the values are all the html files in the directory linked to it.

### Transition model

Takes in the corpus, current page, and the damping factor and returns a dictionary containing the page and probability that it will be transitioned to from the current page.

If the current page doesn't link to any page then the probability of all pages will be equal. Otherwise, the probability of each page will be one minus the damping factor over the total number of pages plus the damping factor over the total number of pages linked, if the page is linked.

This function is used by both the sample_pagerank and the iterate_pagerank functions.

### Sample pagerank

This function takes in the corpus, damping factor, and the number of samples (n). Using this input, the function picks a page at random generates its transition model and picks the next page based on the probability distribution of the transition model. This process is repeated n times, after that the function returns a dictionary containing the probability of each page appearing.

### Iterate pagerank

![PageRank Formula](../../../Snippets/Python/AI/page%20rank/formula.png)

This function starts by assigning all the page an equal probability and then recursively update the probability, [using the formula explained above](#Iterative-algorithm), until the changes to all the probabilities are less than `0.001`.

### rounded

Takes in a dictionary and an integer n and returns the dictionary with every value rounded to the nth place.

---

## Acknowledgements

Both the main and crawl functions have been defined by the CS50AI staff.
