def SplitPath(path: str) -> []:
    """"""
    splitPath = []
    lastIndex = 0
    for i in range(len(path)):
        if path[i] == "/" or path[i] == "\\":
            if i > lastIndex:
                chunk = path[lastIndex:i]
                splitPath.append(chunk)
                lastIndex = i + 1
    splitPath.append(path[lastIndex:len(path)])
    return splitPath



#print(SplitPath("NFL/2004/Super.Bowl.XXXIX.mp4"))