def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    # Find the shortest elem in strs to compare it with the rest
    shortest = min(strs, key=len)

    # Compare characters in strs to those in shortest
    for i in range(len(shortest)):
        for elem in strs:
            if elem[i] != shortest[i]:
                # return the prefix of shortest as soon as they don't match anymore
                return shortest[:i] 
            
    # return the entire shortest if all characters match up
    return shortest

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))