class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = dict()
        email_to_name = dict()

        for account in accounts:
            name, emails = account[0], account[1:]
            email1 = emails[0]
            for email in emails:
                if email not in parents:
                    parents[email] = email
                email_to_name[email] = name
                self._union(email1, email, parents)
        
        # Step 2: 按 root 分组
        groups = collections.defaultdict(list)
        for email in parents:
            root = self._find(email, parents)
            groups[root].append(email)
        
        result = []
        # Step 3: generate output
        for root in groups:
            name = email_to_name[root]
            emails = sorted(groups[root])
            result.append([name] + emails)
        return result

    def _find(self, account, parents):
        if parents[account] != account:
            parents[account] = self._find(parents[account], parents)
        return parents[account]

    def _union(self, a1, a2, parents):
        root1, root2 = self._find(a1, parents), self._find(a2, parents)
        if root1 == root2:
            return False
        parents[root1] = parents[root2]
        return True
