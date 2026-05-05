class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_map = collections.defaultdict(set)
        trusting_map = collections.defaultdict(set)
        for (trusting, trusted) in trust:
            if trusting == trusted:
                continue
            trusted_map[trusted].add(trusting)
            trusting_map[trusting].add(trusted)
        
        potential_judge = list()
        for trusted in trusted_map:
            if len(trusted_map[trusted]) == n - 1:
                potential_judge.append(trusted)
        
        judge_cnt = 0
        judge = -1
        for j in potential_judge:
            if not trusting_map[j]:
                judge_cnt += 1
                judge = j
        return judge if judge_cnt == 1 else -1
