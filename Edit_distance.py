# Edit Distance Problem
# Compute the edit distance between two strings.
# Input: Two strings.
# Output: The minimum number of single-symbol insertions, deletions,and substitutions to transform one string into the other one.



def EditDistance(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    n = len(s1)
    m = len(s2)
    edm = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        edm[i][0] = i
    for j in range(1, m+1):
        edm[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                edm[i][j] = edm[i-1][j-1]
            elif s1[i-1] != s2[j-1]:
                edm[i][j] = min(edm[i-1][j-1] + 1, edm[i-1][j] + 1, edm[i][j-1] + 1)

    return edm[n][m]


print(EditDistance(input(), input()))
