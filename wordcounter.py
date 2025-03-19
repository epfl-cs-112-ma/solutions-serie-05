from __future__ import annotations

import sys

PUNCTUATION = frozenset(".,;:!?")

def clean_word(word: str) -> str:
    """Removes punctuation from a word string.

    Θ(l) where l is len(word).
    """
    return ''.join([c for c in word if c not in PUNCTUATION])

def count_words(text: str, ignored_words: str) -> list[tuple[str, int]]:
    # n = len(text)
    # m = len(ignored_words)

    # Process our input
    case_folded_text = text.casefold() # Θ(n)
    white_space_separated = case_folded_text.split() # Θ(n)
    # the sum of the lengths of words in white_space_separated is Θ(n), therefore:
    cleaned_words = [clean_word(w) for w in white_space_separated] # Θ(Σ(len(w))) = Θ(n)

    ignored_set = frozenset(ignored_words.split()) # Θ(m)

    # In the worst case, all words have the same length k. Therefore there are
    # n/k = Θ(n) words in `cleaned_words` and m/k = Θ(m) words in ignored_set.

    # Actually count frequencies
    frequencies: dict[str, int] = {}
    for word in cleaned_words: # Θ(n) iterations
        if word not in ignored_set:         # Θ(1), lookup in set
            prev = frequencies.get(word, 0) # Θ(1), lookup in dict
            frequencies[word] = prev + 1    # Θ(1), update in dict

    # Θ(n) iterations of Θ(1) each is Θ(n) overall for the loop

    # In the worst case, all the words in the text are different and not
    # ignored, so len(frequencies) is still Θ(n).

    # Sort the pairs (word, frequency) in frequencies by frequency, in decreasing order.
    # As a sorting function based on comparisons, it is Θ(n log n).
    def frequency_of(pair: tuple[str, int]) -> int:
        return pair[1]
    sorted_frequencies = sorted(frequencies.items(), key=frequency_of, reverse=True)

    # So overall we got Θ(m) + c⋅Θ(n) + Θ(n log n) = Θ(m + n log n).
    # If we assume that m is very small compared to n, that's basically Θ(n log n).

    return sorted_frequencies

def main() -> None:
    if len(sys.argv) < 3:
        print("2 arguments required")
    else:
        text_file_name = sys.argv[1]
        ignored_file_name = sys.argv[2]

        with open(text_file_name, "r", encoding="UTF-8") as f:
            text = f.read() # read the whole file

        with open(ignored_file_name, "r", encoding="UTF-8") as f:
            ignored_words = f.read() # read the whole file

        frequencies = count_words(text, ignored_words)
        largest_frequency_len = len(str(frequencies[0][1])) # the largest is necessarily first

        for word, frequency in frequencies:
            print(f"{frequency:{largest_frequency_len}} {word}")

if __name__ == "__main__":
    main()
