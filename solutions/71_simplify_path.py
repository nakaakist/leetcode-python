class Solution:
    def simplifyPath(self, path: str) -> str:
        elems = []
        for e in path.split("/"):
            if e == "" or e == ".":
                continue
            if e == "..":
                if elems:
                    elems.pop()
            else:
                elems.append(e)

        return "/" + "/".join(elems)


print(Solution().simplifyPath("/home/foo"))
print(Solution().simplifyPath("//foo/"))
print(Solution().simplifyPath("/./foo/../bar/foo//./"))
