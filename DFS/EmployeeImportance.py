class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dicts = {}
        for i in range(len(employees)):
            dicts[employees[i].id] = employees[i]
        def sumImportance(currentId):
            emp = dicts[currentId]
            sm = 0
            for i in range(len(emp.subordinates)):
                sm += sumImportance(emp.subordinates[i])
            return emp.importance + sm
        return sumImportance(id)