def longest_word(letters):
    letter_count = {}
    for letter in letters:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    valid_words = []
    for word in words:
        char_count = {}
        for char in word:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        valid_word = True
        for chr, chr_count in char_count.items():
            if chr not in letters:
                valid_word = False
                continue
            if char_count[chr] > letter_count[chr]:
                valid_word = False
                continue
        if valid_word == True:
            valid_words.append(word)
    if not valid_words:
        return None
    max_len = max(len(word) for word in valid_words)
    longest_words = [word for word in valid_words if len(word) == max_len]
    return sorted(longest_words)
