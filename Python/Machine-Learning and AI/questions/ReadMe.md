# Questions

An AI that answers questions. [Watch it in action!](https://youtu.be/A00L1E7Kn70)

## Usage

```bash
python questions.py corpus
Query: the word probability is derived from?
The word probability derives from the Latin probabilitas, which can also mean "probity", a measure of the authority of a witness in a legal case in Europe, and often correlated with the witness's nobility.
```

## Background

**Question Answering (QA)** is a field within natural language processing focused on designing systems that can answer questions. Among the more famous question answering systems is *Watson*, the IBM computer that competed (and won) on *Jeopardy*!. This project implements a less complex question answering AI based on **inverse document frequency**.

The question answering system will perform two tasks: document retrieval and passage retrieval. When presented with a query (a question in English asked by the user), document retrieval will first identify which document(s) of the one provided are most relevant to the query. Once the top documents are found, the top document(s) will be subdivided into passages (in this case, sentences) so that the most relevant passage to the question can be determined.

To find the most relevant documents, we’ll use **tf-idf** to rank documents based both on term frequency for words in the query as well as inverse document frequency for words in the query. Once we’ve found the most relevant documents, there [many possible metrics](https://groups.csail.mit.edu/infolab/publications/Tellex-etal-SIGIR03.pdf) for scoring passages, but we’ll use a combination of inverse document frequency and a query term density measure.

---

## Acknowledgement

the `main` function was done the CS50AI staff.
