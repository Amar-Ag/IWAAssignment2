"""
3. Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.
"""
inputParagraph = str(input("Enter a paragraph to find anagrams from:")) or \
                 "Python is a great language!, said Fred.I don't ever remember having this much fun before."
# Removed fullstop as Fred.I might cause problems when an matching anagram is ruled out due to fullstop.
modifiedParagraph = inputParagraph.replace(".", " ")
wordsList = modifiedParagraph.split()
anagramsList = []
for word in wordsList:
    for compareword in wordsList:
        if word != compareword and sorted(word) == sorted(compareword):
            anagramsList.append(word)

print(f"Entered Paragraph:{inputParagraph}")
print(f"Anagrams from the paragraph:{anagramsList}")
