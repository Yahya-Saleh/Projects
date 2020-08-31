# Heredity

An AI to assess the likelihood that a person will have a particular genetic trait. [Watch an illustration!](https://youtu.be/s8RXy5BAfZ8)

## Usage

```bash
$ python heredity.py data/family0.csv
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
James:
  Gene:
    2: 0.1976
    1: 0.5106
    0: 0.2918
  Trait:
    True: 1.0000
    False: 0.0000
Lily:
  Gene:
    2: 0.0036
    1: 0.0136
    0: 0.9827
  Trait:
    True: 0.0000
    False: 1.0000
```

## Table of content

- [Heredity](#heredity)
  - [Usage](#usage)
  - [Table of content](#table-of-content)
  - [GJB2](#gjb2)
  - [Bayesian network](#bayesian-network)
  - [Data](#data)
  - [Acknowledgements](#acknowledgements)

---

## GJB2

Mutated versions of the [GJB2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1285178/) gene are one of the leading causes of hearing impairment in newborns. Each person carries two versions of the gene, so each person has the potential to possess either 0, 1, or 2 copies of the hearing impairment version GJB2. Unless a person undergoes genetic testing, though, it’s not so easy to know how many copies of mutated GJB2 a person has. This is some “hidden state”: information that has an effect that we can observe (hearing impairment), but that we don’t necessarily directly know. After all, some people might have 1 or 2 copies of mutated GJB2 but not exhibit hearing impairment, while others might have no copies of mutated GJB2 yet still exhibit hearing impairment.

Every Child inherits one gene from each of their parents:

- If the parent has two copies of the mutated gene, then the parent pass down the mutated gene.
- If the parent has no copies then the child doesn't inherit a mutated gene from teh parent.
- If the parent has one mutated gene then there's a 50% percent chance that the parent will pass it on.

After a gene is passed on, though, it has some probability of undergoing additional mutation: changing from a version of the gene that causes hearing impairment to a version that doesn’t, or vice versa.

## Bayesian network

We can model this relationship of random variables with a Bayesian network:

![gene network](../../../Snippets/Python/AI/heredity/gene_network.png)

- Each person in the family has a `Gene` random variable representing how many copies of a particular gene (e.g., the hearing impairment version of GJB2) a person has: a value that is `0`, `1`, or `2`.
- Each person in the family also has a `Trait` random variable, which is `yes` or `no` depending on whether that person expresses a trait (e.g., hearing impairment) based on that gene.
- There’s an arrow from each person’s Gene variable to their `Trait` variable to encode the idea that a person’s genes affect the probability that they have a particular trait.
- There’s also an arrow from both the mother and father’s Gene random variable to their child’s Gene random variable: the child’s genes are dependent on the genes of their parents.

---

## Data

The data folder contains csv files that, as indicated by the csv's header, present the name of a person and both his mother and father and then either a 0 to indicate that person does not have the disease or 1 to indicate that they do. Note that with the exception of the person's name, any of the data could be unknown for a given person.

```csv
name,mother,father,trait
Arthur,,,0
Charlie,Molly,Arthur,0
Fred,Molly,Arthur,1
Ginny,Molly,Arthur,
Molly,,,0
Ron,Molly,Arthur,
```

---

## Acknowledgements

With the exception of the joint_probability, update, and normalize, everything was implements by CS50AI's staff.
