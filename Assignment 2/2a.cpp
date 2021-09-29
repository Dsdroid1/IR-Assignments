#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int editDistance(const string s1, const string s2)
{
    int m, n;
    m = s1.length();
    n = s2.length();
    // Initialize the confusion matrix
    // For Lavenshtein Distance
    // int confusion_matrix[26][26] = {0};
    // for (int i = 0; i < 26; ++i)
    // {
    //     for (int j = 0; j < 26; ++j)
    //     {
    //         confusion_matrix[i][j] = 1;
    //     }
    // }
    int confusion_matrix[26][26] = {
        {0, 0, 7, 1, 342, 0, 0, 2, 118, 0, 1, 0, 0, 3, 76, 0, 0, 1, 35, 9, 9, 0, 1, 0, 5, 0},
        {0, 0, 9, 9, 2, 2, 3, 1, 0, 0, 0, 5, 11, 5, 0, 10, 0, 0, 2, 1, 0, 0, 8, 0, 0, 0},
        {6, 5, 0, 16, 0, 9, 5, 0, 0, 0, 1, 0, 7, 9, 1, 10, 2, 5, 39, 40, 1, 3, 7, 1, 1, 0},
        {1, 10, 13, 0, 12, 0, 5, 5, 0, 0, 2, 3, 7, 3, 0, 1, 0, 43, 30, 22, 0, 0, 4, 0, 2, 0},
        {388, 0, 3, 11, 0, 2, 2, 0, 89, 0, 0, 3, 0, 5, 93, 0, 0, 14, 12, 6, 15, 0, 1, 0, 18, 0},
        {0, 15, 0, 3, 1, 0, 5, 2, 0, 0, 0, 3, 4, 1, 0, 0, 0, 6, 4, 12, 0, 0, 2, 0, 0, 0},
        {4, 1, 11, 11, 9, 2, 0, 0, 0, 1, 1, 3, 0, 0, 2, 1, 3, 5, 13, 21, 0, 0, 1, 0, 3, 0},
        {1, 8, 0, 3, 0, 0, 0, 0, 0, 0, 2, 0, 12, 14, 2, 3, 0, 3, 1, 11, 0, 0, 2, 0, 0, 0},
        {103, 0, 0, 0, 146, 0, 1, 0, 0, 0, 0, 6, 0, 0, 49, 0, 0, 0, 2, 1, 47, 0, 2, 1, 15, 0},
        {0, 1, 1, 9, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0},
        {1, 2, 8, 4, 1, 1, 2, 5, 0, 0, 0, 0, 5, 0, 2, 0, 0, 0, 6, 0, 0, 0, 4, 0, 0, 3},
        {2, 10, 1, 4, 0, 4, 5, 6, 13, 0, 1, 0, 0, 14, 2, 5, 0, 11, 10, 2, 0, 0, 0, 0, 0, 0},
        {1, 3, 7, 8, 0, 2, 0, 6, 0, 0, 4, 4, 0, 180, 0, 6, 0, 0, 9, 15, 13, 3, 2, 2, 3, 0},
        {2, 7, 6, 5, 3, 0, 1, 19, 1, 0, 4, 35, 78, 0, 0, 7, 0, 28, 5, 7, 0, 0, 1, 2, 0, 2},
        {91, 1, 1, 3, 116, 0, 0, 0, 25, 0, 2, 0, 0, 0, 0, 14, 0, 2, 4, 14, 39, 0, 0, 0, 18, 0},
        {0, 11, 1, 2, 0, 6, 5, 0, 2, 9, 0, 2, 7, 6, 15, 0, 0, 1, 3, 6, 0, 4, 1, 0, 0, 0},
        {0, 0, 1, 0, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 14, 0, 30, 12, 2, 2, 8, 2, 0, 5, 8, 4, 20, 1, 14, 0, 0, 12, 22, 4, 0, 0, 1, 0, 0},
        {11, 8, 27, 33, 35, 4, 0, 1, 0, 1, 0, 27, 0, 6, 1, 7, 0, 14, 0, 15, 0, 0, 5, 3, 20, 1},
        {3, 4, 9, 42, 7, 5, 19, 5, 0, 1, 0, 14, 9, 5, 5, 6, 0, 11, 37, 0, 0, 2, 19, 0, 7, 6},
        {20, 0, 0, 0, 44, 0, 0, 0, 64, 0, 0, 0, 0, 2, 43, 0, 0, 4, 0, 0, 0, 0, 2, 0, 8, 0},
        {0, 0, 7, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 8, 3, 0, 0, 0, 0, 0, 0},
        {2, 2, 1, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 7, 0, 6, 3, 3, 1, 0, 0, 0, 0, 0},
        {0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 2, 0, 15, 0, 1, 7, 15, 0, 0, 0, 2, 0, 6, 1, 0, 7, 36, 8, 5, 0, 0, 1, 0, 0},
        {0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 5, 0, 0, 0, 0, 2, 21, 3, 0, 0, 0, 0, 3, 0}};

    // Make the edit distance matrix of dimensions (m+1)*(n+1)
    int dp[m + 1][n + 1] = {0};
    int insertion_cost = 1, deletion_cost = 1;

    // Initialize the 1st row and 1st column
    for (int i = 1; i < m + 1; ++i)
    {
        dp[i][0] = dp[i - 1][0] + deletion_cost;
    }
    for (int j = 1; j < n + 1; ++j)
    {
        dp[0][j] = dp[0][j - 1] + insertion_cost;
    }
    // Use the update rule to get the costs
    int i_cost, d_cost, s_cost;
    for (int i = 1; i < m + 1; ++i)
    {
        for (int j = 1; j < n + 1; ++j)
        {
            if (s1[i - 1] == s2[j - 1])
            {
                // Characters are same at this position, no substitution required
                s_cost = dp[i - 1][j - 1];
            }
            else
            {
                s_cost = dp[i - 1][j - 1] + confusion_matrix[(int)(s1[i - 1] - 'a')][(int)(s2[j - 1] - 'a')];
            }
            d_cost = dp[i - 1][j] + deletion_cost;
            i_cost = dp[i][j - 1] + insertion_cost;
            dp[i][j] = min(s_cost, min(d_cost, i_cost));
            // DO stuff to trace back
        }
    }
    // // DEBUG
    // for (int i = 0; i < m + 1; ++i)
    // {
    //     for (int j = 0; j < n + 1; ++j)
    //     {
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    return dp[m][n];
}

int main()
{
    string s1, s2;
    // Scan the input
    cout << "Enter the first string(the string to be converted):";
    cin >> s1;
    transform(s1.begin(), s1.end(), s1.begin(), ::tolower);
    cout << "Enter the second string(the string to which we need to convert):";
    cin >> s2;
    transform(s2.begin(), s2.end(), s2.begin(), ::tolower);
    // TESTING
    // s1 = "intuition";
    // s2 = "execution";
    int cost_to_transform = editDistance(s1, s2);
    cout << "The edit distance is " << cost_to_transform << endl;
    return 0;
}