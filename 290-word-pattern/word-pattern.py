class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for p, word in zip(pattern, words):
            if p in char_to_word:
                if char_to_word[p] != word:
                    return False
            else:
                char_to_word[p] = word

            if word in word_to_char:
                if word_to_char[word] != p:
                    return False
            else:
                word_to_char[word] = p

        return True
