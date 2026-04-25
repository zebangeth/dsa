class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        for part in path.split('/'):
            if not part or part == '.':
                continue
            elif part == "..":
                if result: result.pop()
            else:
                result.append(part)
        return '/' + '/'.join(result)
                