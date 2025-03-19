from wordcounter import count_words

def test_count_words() -> None:
    assert count_words("si ton tonton tond ton tonton, ton tonton sera tondu", "si") \
        == [('ton', 3), ('tonton', 3), ('tond', 1), ('sera', 1), ('tondu', 1)]

    assert count_words("si six cent six sangsues sur Sissi sont sans sucer son sang, ces six cent six sangsues sont sans succès", "ces sont") \
        == [('six', 4), ('cent', 2), ('sangsues', 2), ('sans', 2), ('si', 1), ('sur', 1), ('sissi', 1), ('sucer', 1), ('son', 1), ('sang', 1), ('succès', 1)]
