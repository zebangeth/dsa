class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # step 1: build the graph 同时维护一个 email_to_name 用来快速查找 email 对应的名字
        graph = collections.defaultdict(set)
        email_to_name = dict()

        for account in accounts:
            name, emails = account[0], account[1:]
            first_email = account[1]
            for email in emails:
                graph[email].add(first_email)
                graph[first_email].add(email)
                email_to_name[email] = name

        # step 2: DFS to find connected components
        visited = set()
        merged_accounts = []
        for email in graph:
            if email not in visited:
                connected_emails = set()
                self.dfs(email, visited, connected_emails, graph)
                merged_accounts.append([email_to_name[email]] + sorted(connected_emails))
        return merged_accounts
    
    def dfs(self, email, visited, connected_emails, graph):
        visited.add(email)
        connected_emails.add(email)
        for nei in graph[email]:
            if nei not in visited:
                self.dfs(nei, visited, connected_emails, graph)