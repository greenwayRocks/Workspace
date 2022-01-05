import wordcloud


def word_frequencies(text_file):
    punctuations = """!@#$%^&*()_-+=[];',<.>/?"""
    remove_words = [
        "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
        "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
        "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
        "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"
    ]
    # Letter-wise
    processed_text = ""
    for letter in text_file:
        if letter not in punctuations:
            processed_text += letter
    # Word-wise
    words = processed_text.split()
    processed_words = []
    frequencies = {}

    for word in words:
        if word.isalpha() and word not in remove_words:
            processed_words.append(word)

    # Frequency/occurrence of words
    for final_word in processed_words:
        if final_word not in frequencies:
            frequencies[final_word] = 1
        else:
            frequencies[final_word] += 1

    # Wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    cloud.to_file('myfile.jpg')
