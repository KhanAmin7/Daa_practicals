practical 7

Imagine you're a traveling salesman visiting four cities: A, B, C, and D. The distance matrix graph represents the travel distances between these cities:

graph = [[0, 10, 15, 20],  # Distances from city A
         [10, 0, 35, 25],  # Distances from city B
         [15, 35, 0, 30],  # Distances from city C
         [20, 25, 30, 0]]  # Distances from city D
We'll start our journey from city A (vertex s = 0).

Step-by-Step Breakdown:

Generate All Possible Paths:

The code first creates a list vertex containing cities B, C, and D (excluding the starting city A).
Then, it uses the permutations function to generate all possible orderings of visiting these three cities. In this case, there are 6 permutations:
B, C, D
B, D, C
C, B, D
C, D, B
D, B, C
D, C, B
Evaluate Each Path:

The code iterates through each permutation (possible travel path).
For each permutation, it initializes a current_pathweight variable to 0 and a k variable to the starting city (A in this case).
It then iterates through each city in the current permutation:
It adds the distance between the current city (k) and the next city (j) in the permutation to the current_pathweight.
It updates k to the next city to move to the next leg of the journey.
Finally, after iterating through all cities in the permutation, it adds the distance from the last city back to the starting city (A) to complete the tour.
Find the Minimum Path:

The code keeps track of the current minimum path length (min_path) initialized to a very high value (maxsize).
For each evaluated permutation (path), it compares the current_pathweight with the min_path.
If the current_pathweight is less than the min_path, it updates the min_path to the new minimum value.
Example Calculation:

Let's calculate the path length for one permutation (say, B, C, D):

Start at A (k = 0).
Travel from A to B: current_pathweight += graph[0][1] = 10.
Travel from B to C: current_pathweight += graph[1][2] = 35.
Travel from C to D: current_pathweight += graph[2][3] = 30.
Travel from D back to A: current_pathweight += graph[3][0] = 20.
The total path length for this permutation (A -> B -> C -> D -> A) is 95.
The code repeats this calculation for all permutations and updates the min_path if it finds a shorter path.

Output:

After evaluating all permutations, the code will find the minimum path length, which might be different depending on the specific distances in your graph.

Important Note:

While the Brute-Force approach works for small examples, it becomes computationally impractical for larger graphs due to the exponential growth in the number of permutations. In real-world scenarios with many cities, more efficient algorithms like nearest neighbor or genetic algorithms are used to find the Travelling Salesman solution.

------------------------------------------------------------------------------------------------------------------------------------

Practical 5

This function recursively calculates the maximum profit achievable
  given a knapsack weight capacity (W), item weights (wt), item
  profits (val), and the number of items (n).

  Args:
      W: Weight capacity of the knapsack.
      wt: List of weights for each item.
      val: List of profits for each item.
      n: Number of items.

  Returns:
      The maximum achievable profit.

      Base cases:
      - If there are no items (n = 0), the maximum profit is 0.
      - If the knapsack weight capacity is 0 (W = 0), no item can be included,
        so the maximum profit is 0.

        If the weight of the last item (wt[n-1]) is greater than the knapsack
    capacity (W), we cannot include it. The maximum profit is achieved
    by considering only the first n-1 items (excluding the last item).

If the last item's weight fits (wt[n-1] <= W), we have two options:
      - Include the last item:
        - Add the profit of the last item (val[n-1]) to the maximum profit
          achievable with the remaining weight capacity (W - wt[n-1]) and the
          first n-1 items (knapSack(W-wt[n-1], wt, val, n-1)).
      - Exclude the last item:
        - Consider the maximum profit achievable only with the first n-1 items
          and the same weight capacity (knapSack(W, wt, val, n-1)).