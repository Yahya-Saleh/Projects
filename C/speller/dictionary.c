// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "dictionary.h"

// Represents number of children for each node in a trie
#define N 27

// Represents a node in a trie
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
node;

void unloading(node *trv);
// Represents a trie
node *root;
// creating a global variable to store the size of the trie
int s = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize trie
    root = malloc(sizeof(node));
    if (!root)
    {
        return false;
    }
    root->is_word = false;
    for (int i = 0; i < N; i++)
    {
        root->children[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (!file)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into trie
    while (fscanf(file, "%s", word) != EOF)
    {
        int n = strlen(word);

        //creating a transversal pointer to move through the trie
        node *trv = root;

        for (int i = 0; i < n; i++)
        {
            //getting the index of the letter in the trie
            int index = (word[i] == 39) ? 26 : (word[i] - 97);

            //if the index of the location is NULL,i.e. empty, we create it
            if (!trv->children[index])
            {
                trv->children[index] = malloc(sizeof(node));
                if (!trv->children[index])
                {
                    unload();
                    return false;
                }

                //we move into the index
                trv = trv->children[index];

                //set it to the default state
                trv->is_word = false;
                for (int j = 0; j < N; j++)
                {
                    trv->children[j] = NULL;
                }
            }
            //otherwise we move into it
            else
            {
                trv = trv->children[index];
            }
            //if this letter is the last letter then we set it to true, indacting that the word exists
            if (i == n - 1)
            {
                trv->is_word = true;
            }
        }
        s++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return s;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int n = strlen(word);
    node *trv = root;

    for (int i = 0; i < n; i++)
    {
        //getting the index of the letter
        int index = (tolower(word[i]) == 39) ? 26 : (tolower(word[i]) - 97);

        //checking if that index exists
        if (!trv->children[index])
        {
            return false;
        }

        //we move into the index
        trv = trv->children[index];

        //if we're at the last letter we check if the word exists of not
        if (i == n - 1)
        {
            return trv->is_word;
        }
    }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    unloading(root);
    return true;
}

void unloading(node *trv)
{
    for (int i = 0; i < N; i++)
    {
        if (trv->children[i])
        {
            unloading(trv->children[i]);
        }
    }
    free(trv);
}