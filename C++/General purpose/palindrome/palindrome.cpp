#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Get a word from the user
    string word;
    cout << "Enter a word and I'll tell you if its a palindrome: ";
    cin >> word;

    // word length
    int word_len = word.size();
    // Initialize outside to check for loop completion
    int i;
    for (i = 0; i < word_len / 2; i++)
    {
        if (word[i] != word[word_len - 1 - i])
        {
            break;
        }
    }

    cout << word << " is ";
    // If we didn't loop over the whole word
    if (i != word_len / 2)
    {
        cout << "not a palindrome";
    }
    else
    {
        cout << "a palindrome";
    }
}
