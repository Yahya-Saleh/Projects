import nltk
import sys
import os
import math

FILE_MATCHES = 3
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {filename: tokenize(files[filename]) for filename in files}
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match, end="\n\n")


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    # The dictionary to hold the content of each file
    contents = {}
    # Corpus path
    corpus_path = os.path.join(os.getcwd(), directory)

    # For each file in the corpus
    for f in os.listdir(corpus_path):
        relative_path = os.path.join(directory, f)

        # Encoding="utf8" accounts for any encoding of formating issues
        with open(relative_path, encoding="utf8") as reader:
            contents[f] = reader.read()

    return contents


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    # Tokenize removing punctuation
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    document = tokenizer.tokenize(document)

    # Filter out stopwords
    stopwords = nltk.corpus.stopwords.words("english")
    # lowercase
    document = [word.lower() for word in document if word not in stopwords]

    return document


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = {}
    total_documents = len(documents)

    for title, content in documents.items():
        for word in set(content):
            # Check if word exists
            if word in idfs.keys():
                continue

            # Calculate the word's occurrence in the corpus
            occurrence = 1
            for key, lis in documents.items():
                if key == title:
                    continue
                elif word in lis:
                    occurrence += 1

            # Calculate IDF
            idfs[word] = math.log(total_documents / occurrence)

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    # Record the scores showing the relevance of each file
    scores = {filename: 0 for filename in files.keys()}

    for word in query:
        for filename, content in files.items():
            if word in idfs.keys():
                # Term Frequency
                tf = content.count(word)
                # Add the TF-IDF of the word to the score
                scores[filename] += tf * idfs[word]

    topFiles = sorted(scores, key=lambda key: scores[key], reverse=True)

    # Return the first n file names sorted by score
    return topFiles[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    scores = {sentence: 0 for sentence in sentences.keys()}
    qtd = {sentence: 0 for sentence in sentences.keys()}

    for sentence, tokens in sentences.items():
        for word in query:
            if word in tokens:
                # IDF
                scores[sentence] += idfs[word]
                # Query term density
                qtd[sentence] += sentence.lower().count(word) / len(tokens)

    # Sort the sentences by score
    sorted_sentences = sorted(
        scores.items(), key=lambda pair: pair[1], reverse=True)

    # Check for duplicate scores
    if len(scores.values()) != len(set(scores.values())):
        # If so sort using Query term density
        prev_score = 0
        for i, sentence in enumerate(sorted_sentences.copy()):
            # If the scores are identical
            if prev_score == sentence[1]:
                # Check if teh latter has a higher Query term density
                if qtd[sentence[0]] > qtd[sorted_sentences[i - 1][0]]:
                    # Swap
                    sorted_sentences[i - 1], sorted_sentences[i] = (
                        sorted_sentences[i],
                        sorted_sentences[i - 1],
                    )

            prev_score = sentence[1]

    for i in range(n):
        yield sorted_sentences[i][0]


if __name__ == "__main__":
    main()
