class RegexMatch:
    def __init__(self):
        self.result_mappings = {}

    def is_match(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        if text in self.result_mappings and pattern in self.result_mappings[text]:
            return self.result_mappings[text][pattern]
        
        self.result_mappings[text] = {}

        first_match = bool(text) and pattern[0] in {text[0], "."}

        if len(pattern) >= 2 and pattern[1] == "*":
            self.result_mappings[text][pattern] = (
                self.is_match(text, pattern[2:])
                or (
                    first_match
                    and 
                    self.is_match(text[1:], pattern)
                )
            )
        else:
            self.result_mappings[text][pattern] = first_match and self.is_match(text[1:], pattern[1:])
            
        return self.result_mappings[text][pattern]
