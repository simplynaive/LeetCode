# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employees = {e.id: e for e in employees}

        def dfs(id):
            s = employees[id].importance
            s += sum(dfs(id) for id in employees[id].subordinates)
            return s

        return dfs(id)