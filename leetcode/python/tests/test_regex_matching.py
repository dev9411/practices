import unittest
from regex_matching import RegexMatch

class TestRegexMatch(unittest.TestCase):
    def setUp(self):
        self.check = RegexMatch()

    def test_full_word_match(self):
        self.assertFalse(self.check.is_match('aaa','a'))
        self.assertFalse(self.check.is_match('aa','a'))
        self.assertTrue(self.check.is_match('a','a'))
        self.assertTrue(self.check.is_match('qwertyuiop','qwertyuiop'))
        self.assertFalse(self.check.is_match('qwetyuiop','qwertyuiop'))
        self.assertFalse(self.check.is_match('qwertyuio','qwertyuiop'))
        self.assertFalse(self.check.is_match('qwertyuio','qwertyui'))
        self.assertFalse(self.check.is_match('wertyuio','qwertyui'))
        self.assertFalse(self.check.is_match('wertyuio','ertyui'))
        
    def test_starting_with_dot(self):
        self.assertTrue(self.check.is_match('ab','a.'))
        self.assertTrue(self.check.is_match('ab','.b'))
        self.assertTrue(self.check.is_match('qwe','.we'))
        self.assertTrue(self.check.is_match('qwe','q.e'))
        self.assertTrue(self.check.is_match('qwe','qw.'))
        self.assertFalse(self.check.is_match('abc','a.'))
        self.assertFalse(self.check.is_match('abc','abc.'))
        self.assertFalse(self.check.is_match('abc','.abc'))
        self.assertFalse(self.check.is_match('abc','a.b'))
        self.assertFalse(self.check.is_match('abc','.ab'))
        self.assertFalse(self.check.is_match('abc','bc.'))

    def test_starting_with_dot_star(self):
        self.assertTrue(self.check.is_match('ab','.*'))
        self.assertTrue(self.check.is_match('ab','.****'))
        self.assertTrue(self.check.is_match('aaa','.*'))
        self.assertTrue(self.check.is_match('abc','.*'))

    def test_simple_scenarios(self):
        self.assertTrue(self.check.is_match('a','a*'))
        self.assertTrue(self.check.is_match('a','a***'))
        self.assertTrue(self.check.is_match('aa','a*'))
        self.assertTrue(self.check.is_match('aaaaa','a*'))
        self.assertFalse(self.check.is_match('aaaabbbb','a*'))
        self.assertFalse(self.check.is_match('abc','a*'))
        self.assertFalse(self.check.is_match('aab','c*a*b'))

    def test_with_single_star(self):
        self.assertTrue(self.check.is_match('aaabc', 'a*bc'))
        self.assertTrue(self.check.is_match('abc', 'a*bc'))
        self.assertFalse(self.check.is_match('abac', 'a*bc'))
        self.assertFalse(self.check.is_match('abcc', 'a*bc'))
        self.assertFalse(self.check.is_match('abbcc', 'a*bc'))
        
    def test_with_stars_mixed(self):
        self.assertTrue(self.check.is_match('aaabc', 'a*b*c'))
        self.assertTrue(self.check.is_match('abc', 'a*b*c'))
        self.assertFalse(self.check.is_match('abac', 'a*b*c'))
        self.assertFalse(self.check.is_match('abcc', 'a*b*c'))
        self.assertTrue(self.check.is_match('abbc', 'a*b*c'))
        self.assertFalse(self.check.is_match('abbcc', 'a*b*c'))

    def test_starting_with_dot_and_has_end_pattern(self):
        self.assertTrue(self.check.is_match('abadkhsauhbcsaysabdasdbhxy','.*xy'))
        self.assertFalse(self.check.is_match('abadkhsauhbcsaysabdasdbhy','.*xy'))
        self.assertFalse(self.check.is_match('abadkhsauhbcsaysabdasdbhx','.*xy'))
        
    def test_complex_pattern(self):
        self.assertFalse(self.check.is_match('abxy','ab.*xy'))
        self.assertTrue(self.check.is_match('abxyzxy','ab.*xy'))
        self.assertTrue(self.check.is_match('abcxymnxyz','ab.*xy.*xyz'))
        self.assertTrue(self.check.is_match('abcxymnxyzxyxyxy','ab.*xy.*xyz.*xy'))
        self.assertTrue(self.check.is_match('zxyxyxy','z.*xy'))
        self.assertTrue(self.check.is_match('abcxymnxyzmnxy','ab.*xy.*xyz.*xy'))
        self.assertTrue(self.check.is_match('abcxymnxyzmnxyzmnxyzmnxyz','ab.*xy.*xyz.*xy.*xyz'))
        self.assertTrue(self.check.is_match('abxyxyxyxyzxyxyzxyxyzxyxyz','ab.*xy.*xyz.*xy.*xyz'))
        self.assertFalse(self.check.is_match('abxyxyxyxyxyxyxyxyzxyxyz','ab.*xy.*xyz.*xy.*xyz'))
        self.assertTrue(self.check.is_match('abxyxyxyxyxyxyxymxyzmxymxyz','ab.*xy.*xyz.*xy.*xyz'))
        self.assertFalse(self.check.is_match('abxyxyxyxyxyxyxyxyzxyxyzabc','ab.*xy.*xyz.*xy.*xyz.*'))
        self.assertTrue(self.check.is_match('abxyxyxyxyxyxyxymxyzmxymxyzabc','ab.*xy.*xyz.*xy.*xyz.*'))
        self.assertFalse(self.check.is_match('abxyxyxyxyxyxyxyxyzxyxyzx','ab.*xy.*xyz.*xy.*xyz.'))
        self.assertTrue(self.check.is_match('abxyxyxyxyxyxyxymxyzmxymxyza','ab.*xy.*xyz.*xy.*xyz.'))
        self.assertFalse(self.check.is_match('abxyxyxyxyxyxyxyxyzxyxyz','ab.*xy.*xyz.*xy.*xyz*'))
        self.assertTrue(self.check.is_match('abxyxyxyxyxyxyxymxyzmxymxyz','ab.*xy.*xyz.*xy.*xyz*'))
        self.assertTrue(self.check.is_match('abxyxyxyxyxyxyxymxyzmxymxyzzz','ab.*xy.*xyz.*xy.*xyz*'))
