class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.parents = dict()
        self.sizes = dict()
        email_to_name = dict()
        for a in accounts:
            for email in a[1:]:
                self.parents[email] = email
                self.sizes[email] = 1
                email_to_name[email] = a[0]

        for account in accounts:
            if len(account) > 2:
                self.connect(account[1:])
        
        roots = collections.defaultdict(list)
        for email in self.parents:
            roots[self.find(email)].append(email)
        print(roots)
        result = []
        for root in roots:
            account = []
            account.append(email_to_name[root])
            account.extend(roots[root])
            result.append(account)
        
        return result
    
    def connect(self, emails):
        for i in range(1, len(emails)):
            self.union(emails[0], emails[i])
            
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.sizes[root_x] > self.sizes[root_y]:
            self.parents[root_y] = root_x
            self.sizes[root_x] += self.sizes[root_y]
        else:
            self.parents[root_x] = root_y
            self.sizes[root_y] += self.sizes[root_x]


    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
