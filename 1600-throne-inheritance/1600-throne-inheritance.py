class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.successor = defaultdict(list)
        self.d = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.successor[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.d.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        self.res = []
        def dfs(name):
            if name not in self.d:
                self.res.append(name)
            for n in self.successor[name]:
                dfs(n)
            return
            
        dfs(self.kingName)
        return self.res