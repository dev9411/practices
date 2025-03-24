class RegexMatch:

    DOT_CHAR = '.'
    STAR_CHAR = '*'

    def is_match(self, s: str, p: str):
        return self.check(s, p, 0, 0, '')

    def check(self, s: str, p: str, s_index: int, p_index: int, previous_pattern: str):
        s_len = len(s)
        p_len = len(p)
        previous_star = -1
        while s_index < s_len and p_index < p_len:
            if s[s_index] == p[p_index] or p[p_index] == RegexMatch.DOT_CHAR:
                previous_pattern = p[p_index]
                s_index += 1
                p_index += 1
                continue

            if p[p_index] == RegexMatch.STAR_CHAR:
                if p_index == p_len - 1:
                    if previous_pattern == RegexMatch.DOT_CHAR:
                        return True
                    elif previous_pattern == s[s_index]:
                        s_index += 1
                        continue
                    else:
                        return False

                if s[s_index] == p[p_index + 1]:
                    previous_star = p_index
                    previous_pattern = p[p_index + 1]
                    p_index += 2
                    s_index += 1
                    continue

                if s[s_index] != p[p_index + 1]:
                    if previous_pattern == RegexMatch.DOT_CHAR or previous_pattern == s[s_index]:
                        s_index += 1
                        continue
                    else:
                        return False

 
            if s[s_index] != p[p_index]:
                if previous_star == -1:
                    return False
                else:
                    p_index = previous_star
                    previous_pattern = p[previous_star - 1]

        while p_index < p_len:
            if p[p_index] == RegexMatch.STAR_CHAR:
                p_index += 1
                continue
            break
        
        if s_index < s_len - 1 and p_index == p_len and previous_star != -1:
            return self.check(s, p, s_index, previous_star, p[previous_star - 1])

        if s_index != s_len or p_index != p_len:
            return False
                
        return True
