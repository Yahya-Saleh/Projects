#include <cs50.c>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has the index of the winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        //if the candidate exists put him on the rankth rank
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    //iterates over each rank
    for (int i = 0; i < candidate_count; i++)
    {
        //for each rank this loop runs a number of times equal to the number of candidates the rank defeated
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
}
// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        //this iterates over each candidates table a number of times equal to number of candidate minus 1 (we can ignore comparing it to itself) and minus the comparisons we already did with it in other candidates
        for (int j = i + 1; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
            //this way we don't add any ties
            else if (preferences[i][j] < preferences[j][i])
            {
                pairs[pair_count].winner = j;
                pairs[pair_count].loser = i;
                pair_count++;
            }
        }
    }
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    //create an array to hold the margin of victory
    int margin[pair_count];

    //get the margin of victory for each pair
    for (int i = 0; i < pair_count; i++)
    {
        margin[i] = preferences[pairs[i].winner][pairs[i].loser] - preferences[pairs[i].loser][pairs[i].winner];
    }

    //create a temporary storage to swap
    pair buffer;
    int tmp;

    //sort the pairs using the margin
    for (int i = 0; i < pair_count; i++)
    {
        for (int j = i + 1; j < pair_count; j++)
        {
            //if jth margin is greater than the ith swap them
            if (margin[i] < margin[j])
            {
                buffer = pairs[i];
                pairs[i] = pairs[j];
                pairs[j] = buffer;

                tmp = margin[i];
                margin[i] = margin[j];
                margin[j] = tmp;
            }
        }
    }
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        //this loop permits us to add an edge if one other candidate isn't pointing at anything
        //since 2 candidates can't point at the same person
        for (int j = 0; j < candidate_count; j++)
        {
            bool cycle = false;

            //if j isn't the winner's index, because the candidate can point at more than one person without creating a cycle
            if (j != pairs[i].winner)
            {
                for (int k = 0; k < candidate_count; k++)
                {
                    //if indeed the kth candidate is pointing at someone then we don't add the edge until we find one that doesn't
                    if (locked[j][k])
                    {
                        cycle = true;
                        break;
                    }
                }
                //if we get out of the k loop and cycle is still false then we add the edge
                if (!cycle)
                {
                    locked[pairs[i].winner][pairs[i].loser] = true;
                    break;
                }
            }
        }
    }
}

// Print the winner of the election
void print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        bool pointed_at = false;

        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i])
            {
                pointed_at = true;
            }
        }

        if (pointed_at == false)
        {
            printf("%s\n", candidates[i]);
        }
    }

}

