import csv
import itertools
import sys
import numpy as np

PROBS = {
    # Unconditional probabilities for having gene
    "gene": {2: 0.01, 1: 0.03, 0: 0.96},
    "trait": {
        # Probability of trait given two copies of gene
        2: {True: 0.65, False: 0.35},
        # Probability of trait given one copy of gene
        1: {True: 0.56, False: 0.44},
        # Probability of trait given no gene
        0: {True: 0.01, False: 0.99},
    },
    # Mutation probability
    "mutation": 0.01,
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}}
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (
                people[person]["trait"] is not None
                and people[person]["trait"] != (person in have_trait)
            )
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (
                    True
                    if row["trait"] == "1"
                    else False
                    if row["trait"] == "0"
                    else None
                ),
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s)
        for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # Since we want to know the probability of the people in one gene having one copy and those in two gene having two and...
    # We store the product of each probability we calculate
    prob = 1

    # Get zero Gene
    zero_gene = people.keys() - itertools.chain(one_gene, two_genes)
    # Store all genes to loop over
    genes = [zero_gene, one_gene, two_genes]
    # Remember the index of each gene
    for i, gene in enumerate(genes):
        for person in gene:
            # If person has parents
            if people[person]["mother"]:
                # Get there genes right now
                parent_genes = []
                for j, g in enumerate(genes):
                    # Remember the copies of gene each parent has in this iteration
                    if people[person]["mother"] in g:
                        parent_genes.append(j)
                    if people[person]["father"] in g:
                        parent_genes.append(j)

                # Probability of inheriting a gene
                v = []
                for pg in parent_genes:
                    if pg == 1:
                        v.append(0.5)
                    elif pg == 2:
                        v.append(0.99)
                    else:
                        v.append(0.01)

                # Propability that the specified number of copies are inherited
                if i == 1:
                    prob *= v[0] * (1 - v[1]) + v[1] * (1 - v[0])
                elif i == 2:
                    prob *= np.prod(v)
                else:
                    prob *= np.prod([(1 - i) for i in v])

            # If person has no parents
            else:
                # Use the default probability
                prob *= PROBS["gene"][i]

            # If the person in have trait
            if person in have_trait:
                # Calculate the probability of having a trait
                # given that the person has the specified number of copies
                prob *= PROBS["trait"][i][True]

            else:
                prob *= PROBS["trait"][i][False]

    return prob


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    # Get zero Gene
    zero_gene = probabilities.keys() - itertools.chain(one_gene, two_genes)
    # Store all genes to loop over
    genes = [zero_gene, one_gene, two_genes]
    
    # Remember the index of each gene
    for i, gene in enumerate(genes):
        for person in gene:
            probabilities[person]["gene"][i] += p

            probabilities[person]["trait"][person in have_trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for a, person in probabilities.items():
        for b, category in person.items():

            # Get the total of every probability distribution
            total = 0
            for value in category.values():
                total += value

            # Calculate alpha
            alpha = 1 / total
            for c, value in category.items():
                probabilities[a][b][c] *= alpha


if __name__ == "__main__":
    main()
