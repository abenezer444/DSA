class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack=[homepage]
        self.cur=0
        
        

    def visit(self, url: str) -> None:
        while len(self.stack)!=self.cur+1:
            self.stack.pop()
        self.stack.append(url)
        self.cur+=1
        

    def back(self, steps: int) -> str:
        if self.cur<steps:
            self.cur=0
        else:
            self.cur=self.cur-steps
        return self.stack[self.cur]
        

    def forward(self, steps: int) -> str:
        if self.cur+steps>=len(self.stack):
            self.cur=len(self.stack)-1
        else:
            self.cur=self.cur+steps
        return self.stack[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)