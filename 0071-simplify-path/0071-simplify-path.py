class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')
        for directory in directories:
            if directory not in '..':
                stack.append(directory)
            if directory == '..' and stack:
                stack.pop()
        return '/'+'/'.join(stack)
        