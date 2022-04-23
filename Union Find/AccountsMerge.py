class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        l = len(accounts)
        root = [0]*l
        rank = [1]*l
        emails = {}
        for i in range(l):
            root[i] = i
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in emails:
                    emails[accounts[i][j]] = []
                emails[accounts[i][j]].append(i)
        def find(ind):
            if root[ind] == ind:
                return ind
            return find(root[ind])
        def union(one, two):
            parentOne = find(one)
            parentTwo = find(two)
            if parentOne == parentTwo:
                return 0
            if rank[parentOne] > rank[parentTwo]:
                root[parentTwo] = parentOne
            elif rank[parentTwo] > rank[parentOne]:
                root[parentOne] = parentTwo
            else:
                root[parentTwo] = parentOne
                rank[parentOne] += 1
        for em in emails.values():
            temp = len(em)
            if temp > 1:
                for j in range(1,temp):
                    union(em[0],em[j])
        result = defaultdict(set)
        for i in range(l):
            parent = find(i)    
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in result[parent]:
                    result[parent].add(accounts[i][j])
        res = []
        for key, value in result.items():
            temp = [accounts[key][0]]
            val = sorted(value)
            for mails in val:
                temp.append(mails)
            res.append(temp)
        return res