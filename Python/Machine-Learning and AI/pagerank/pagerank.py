import os
import random
import re
import sys

from numpy.random import choice

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    prob_dis = dict()
    links = corpus[page]

    # If the page has no links
    if len(links) == 0:
        # The probability would be equal
        prob = 1 / len(corpus.keys())

        for key in corpus.keys():
            prob_dis[key] = prob

    else:
        # Every page has a chance of getting picked randomly with a likelihood of (1 - damping_factor)
        prob = (1 - damping_factor) / len(corpus.keys())
        for key in corpus.keys():
            prob_dis[key] = prob

        # Adding the probability of picking a linked page
        for p in links:
            prob_dis[p] += damping_factor / len(links)

    return prob_dis


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # The number to be added to a page when it appears
    # This way we won't have to divide the number of occurrence by n at the end to calculate the probability
    cons = 1 / n
    # The corpus probability distribution each page starting at zero
    corpus_dist = {page: 0 for page in corpus.keys()}

    # The starting page will be picked at random with equal probability
    next_page = random.choice(list(corpus.keys()))
    for _ in range(n):
        corpus_dist[next_page] += cons
        # Get the transition model
        trans_dis = transition_model(corpus, next_page, damping_factor)

        # Pick the next page at random base on the probability distribution of the transition model
        distribution = list(trans_dis.values())
        # Returns the index of the page
        rand_index = choice(range(len(trans_dis)), p=distribution)

        next_page = list(trans_dis.keys())[rand_index]

    return rounded(corpus_dist)


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Calculates the probability of page p being accessed
    def PR(p):
        # Identify all the pages that can go to page p
        linked = [key for key, value in corpus.items() if p in value]

        # Calculate the probability that the surfer clicks on a link leading to page p
        sigma = 0
        for link in linked:
            sigma += corpus_dist[link] / len(corpus[link])

        # Using the formula
        return ((1 - damping_factor) / n) + (damping_factor * sigma)

    # Define the total number of pages
    n = len(corpus)
    # Every page starts with an equal probability
    corpus_dist = {page: (1 / n) for page in corpus.keys()}

    # Check if any page has no links
    for key, value in corpus.items():
        if not value:
            # A page with no links should be interpreted as having one link for every page in the corpus (including itself).
            corpus[key] = {key for key in corpus.keys()}

    # Until the probabilities stop changing
    changed = True
    while changed:
        buffer = corpus_dist.copy()
        # Update the probabilities
        for page in corpus_dist.keys():
            corpus_dist[page] = PR(page)

        # Check for change
        changed = False
        for page in corpus_dist.keys():
            if abs(corpus_dist[page] - buffer[page]) >= 0.001:
                changed = True
                break

    return rounded(corpus_dist)


def rounded(dictionary, n=4):
    """
    rounds the values in a dictionary to the nth decimal place
    """
    return {key: round(value, n) for key, value in dictionary.items()}


if __name__ == "__main__":
    main()
