class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        special_operations = set(["+", "C", "D"])
        for o in operations:
            if o not in special_operations:
                record.append(int(o))
            elif o == "+":
                record.append(record[-1] + record[-2])
            elif o == "C":
                record.pop()
            elif o == "D":
                record.append(record[-1] * 2)
            else:
                continue
        return sum(record)
