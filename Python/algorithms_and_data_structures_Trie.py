# Trie data structure AKA Directed Character Tree
class TrieNode:

    # Initialize an empty Trie
    def __init__(self):
        self.is_word: bool = False
        self.children: dict = {}

    # Insert a word into the Trie
    def insert_word(self, word: str) -> None:
        curr = self  # This is unnecessary in Python because self is a local variable,
        # but I do believe this is good, hygienic practice, and it costs almost nothing.

        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.is_word = True

    # Check if a word is in the Trie
    def find_word(self, word: str) -> bool:
        curr = self  # This is unnecessary in Python because self is a local variable,
        # but I do believe this is good, hygienic practice, and it costs almost nothing.

        for c in word:
            if not c in curr.children:
                return False
            curr = curr.children[c]

        if curr.is_word:
            return True
        else:
            return False

    # Reconstruct the list of all the words in the Trie
    def words(self) -> list:
        chars = list(self.children.keys())
        lst = []
        if self.is_word:
            lst += [""]

        for c in chars:
            suffixes = self.children[c].words()
            if suffixes is not None:
                lst += [c + suff for suff in suffixes]

        if lst != []:
            return lst
        else:
            return None

    # Reconstruct the list of all the words in the Trie. Tail recursion variant.
    def words_tr(self, prefix: str = "") -> list:
        chars = list(self.children.keys())
        lst = []
        if self.is_word:
            lst += [prefix]
            # print(prefix) # or do something else since the prefix is now the full word

        for c in chars:
            prefixes = self.children[c].words_tr(prefix + c)
            if prefixes is not None:
                lst += [prefixes]

        if lst != []:
            return lst
        else:
            return None


t = TrieNode()
t.insert_word("asdf")

# TODO document better
