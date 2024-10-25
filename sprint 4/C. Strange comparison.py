def are_equivalent_strings(s, t):
    if len(s) != len(t):
        return "NO"
    
    map_s_to_t = {}
    map_t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return "NO"
        else:
            map_s_to_t[char_s] = char_t
        
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return "NO"
        else:
            map_t_to_s[char_t] = char_s
    
    return "YES"

# Пример использования
s = input().strip()
t = input().strip()

print(are_equivalent_strings(s, t))