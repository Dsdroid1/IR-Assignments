#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int *lpsArray(const string s)
{
    int len = s.length();
    int *lps = new int[len];

    lps[0] = 0; // As single char has no prefix
    int i = 1, longest_matching_prefix_len = 0;
    while (i < len)
    {
        if (s[i] == s[longest_matching_prefix_len])
        {
            longest_matching_prefix_len++;
            lps[i] = longest_matching_prefix_len;
            i++;
        }
        else
        {
            // We need to consider the prefix from older position, if any
            if (longest_matching_prefix_len != 0)
            {
                // Some pattern had matched earlier, hence backtrack ptr to only that much portion and try to match again
                longest_matching_prefix_len = lps[longest_matching_prefix_len - 1];
            }
            else
            {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

void kmpSearch(const string text, const string pattern)
{
    int m, n;
    m = text.length();
    n = pattern.length();
    if (m >= n)
    {
        int *lps = lpsArray(pattern);
        int i = 0, j = 0, found = 0;
        while (i < m)
        {
            if (pattern[j] == text[i])
            {
                i++;
                j++;
            }
            if (j == n)
            {
                // Full matched
                cout << "Match Found at index:" << i - j << endl;
                found = 1;
                j = lps[j - 1];
            }
            else if (i < m && pattern[j] != text[i])
            {
                if (j != 0)
                {
                    j = lps[j - 1];
                }
                else
                {
                    i++;
                }
            }
        }
        if (found == 0)
        {
            cout << "No Match found!" << endl;
        }
        delete lps;
    }
    else
    {
        cout << "No Match found!" << endl;
    }
}

int main()
{
    string text, pattern;
    cout << "Enter the pattern:";
    cin >> pattern;
    transform(pattern.begin(), pattern.end(), pattern.begin(), ::tolower);
    cout << "Enter the text in which pattern has to be searched:";
    cin >> text;
    transform(text.begin(), text.end(), text.begin(), ::tolower);
    // // TESTING
    // pattern = "AAAA";
    // text = "AAAAABAAABA";
    kmpSearch(text, pattern);
    return 0;
}