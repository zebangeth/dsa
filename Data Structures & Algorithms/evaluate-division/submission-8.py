from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Collect all variables that appear in the equations so we can initialize Union-Find.
        variables = set()
        for a, b in equations:
            variables.add(a)
            variables.add(b)

        # parent[x] = (root_parent, weight_to_root)
        # weight_to_root means: x / root_parent = weight_to_root
        self.parents = {v: (v, 1.0) for v in variables}
        self.sizes = {v: 1 for v in variables}


        # Build the weighted graph structure through Union-Find.
        for (a, b), value in zip(equations, values):
            self.union(a, b, value)

        results = []

        # Answer each query by checking connectivity and computing the ratio.
        for c, d in queries:
            # If either variable has never appeared, the answer is unknown.
            if c not in self.parents or d not in self.parents:
                results.append(-1.0)
                continue

            c_root, c_ratio = self.find(c)  # c / c_root
            d_root, d_ratio = self.find(d)  # d / d_root

            # If they are not connected, we cannot determine the division.
            if c_root != d_root:
                results.append(-1.0)
                continue

            # Since c / root = c_ratio and d / root = d_ratio,
            # c / d = (c / root) / (d / root).
            results.append(c_ratio / d_ratio)

        return results

    def find(self, x):
        """
        Find the root parent of x with path compression.

        Returns:
            (root, ratio)
            where ratio = x / root
        """
        if self.parents[x][0] != x:
            # Recursively find the root of the current parent.
            nxt, val = self.find(self.parents[x][0])

            # Compress the path:
            # x / nxt = (x / parent) * (parent / nxt)
            self.parents[x] = (nxt, self.parents[x][1] * val)

        return self.parents[x]

    def union(self, x, y, value):
        """
        Merge the sets containing x and y using the equation:
            x / y = value
        """
        x_root, x_ratio = self.find(x)  # x / x_root
        y_root, y_ratio = self.find(y)  # y / y_root

        # If already connected, no need to union.
        if x_root == y_root:
            return

        # Union by size for better performance.
        # Attach smaller tree under larger tree.
        if self.sizes[x_root] < self.sizes[y_root]:
            # We want to connect x_root under y_root.
            # We know:
            #   x / y = value
            #   x = x_ratio * x_root
            #   y = y_ratio * y_root
            # Therefore:
            #   (x_ratio * x_root) / (y_ratio * y_root) = value
            #   x_root / y_root = value * y_ratio / x_ratio
            self.parents[x_root] = (y_root, value * y_ratio / x_ratio)
            self.sizes[y_root] += self.sizes[x_root]
        else:
            # Connect y_root under x_root.
            # From the same relationship:
            #   y_root / x_root = x_ratio / (value * y_ratio)
            self.parents[y_root] = (x_root, x_ratio / (value * y_ratio))
            self.sizes[x_root] += self.sizes[y_root]

