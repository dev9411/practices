class RegexMatch:

    DOT_CHAR = '.'
    STAR_CHAR = '*'

    def is_match(self, s: str, p: str):
        return self.check(s, p, 0, 0, '', -1)

    def check(self, s: str, p: str, s_index: int, p_index: int, previous_pattern: str, previous_star: int):
        s_len = len(s)
        p_len = len(p)
        while s_index < s_len and p_index < p_len:
            if s[s_index] == p[p_index] or p[p_index] == RegexMatch.DOT_CHAR:
                return self.check(s, p, s_index + 1, p_index + 1, p[p_index], previous_star)

            if p[p_index] == RegexMatch.STAR_CHAR:
                if p_index == p_len - 1:
                    if previous_pattern == RegexMatch.DOT_CHAR:
                        return True
                    elif previous_pattern == s[s_index]:
                        return self.check(s, p, s_index + 1, p_index, previous_pattern, previous_star)
                    else:
                        return False

                if s[s_index] == p[p_index + 1]:
                    return self.check(s, p, s_index + 1, p_index + 2, p[p_index + 1], p_index)

                if previous_pattern == p[p_index + 1]:
                    return self.check(s, p, s_index - 1, p_index + 1, previous_pattern, p_index)
                                        
                if s[s_index] != p[p_index + 1]:
                    if p_index + 2 < p_len and p[p_index + 2] == RegexMatch.STAR_CHAR and previous_pattern != s[s_index]:
                        return self.check(s, p, s_index, p_index + 2, previous_pattern, p_index + 2)
                    if previous_pattern == RegexMatch.DOT_CHAR or previous_pattern == s[s_index]:
                        return self.check(s, p, s_index + 1, p_index, previous_pattern, previous_star)
                    else:
                        return False

            if s[s_index] != p[p_index]:
                if p_index + 1 < p_len and p[p_index + 1] == RegexMatch.STAR_CHAR:
                    return self.check(s, p, s_index, p_index + 2, previous_pattern, previous_star)
                if previous_star == -1:
                    return False
                else:
                    return self.check(s, p, s_index, previous_star, p[previous_star - 1], previous_star)

        while p_index < p_len:
            if p[p_index] == RegexMatch.STAR_CHAR:
                return self.check(s, p, s_index, p_index + 1, previous_pattern, previous_star)
            break
        
        if s_index < s_len - 1 and p_index == p_len and previous_star != -1:
            return self.check(s, p, s_index, previous_star, p[previous_star - 1], -1)

        if s_index != s_len or p_index != p_len:
            return False

        return True
