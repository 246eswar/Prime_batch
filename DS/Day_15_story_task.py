def analyze_story(story):
    # Count words
    words = story.split()
    word_count = len(words)
    amount = word_count * 10  # 10 paisa per word

    # Count vowels and consonants
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in story if char in vowels)
    consonant_count = sum(1 for char in story if char.isalpha() and char not in vowels)

    # Count palindrome words
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1] and len(word) > 1

    palindrome_words = [word for word in words if is_palindrome(word)]
    palindrome_count = len(palindrome_words)

    return {
        "word_count": word_count,
        "amount": amount,
        "vowel_count": vowel_count,
        "consonant_count": consonant_count,
        "palindrome_count": palindrome_count,
        "palindrome_words": palindrome_words
    }

# Example story
story = """
In a whimsical town called Blunderburg, mom dad sis  where logic took a vacation, a young inventor named Timmy decided to create a machine that could turn thoughts into reality. One day, he thought, "What if I could print my dreams?" Suddenly, his machine whirred to life, and out popped a giant pineapple wearing sunglasses. "Go to Hero!" the pineapple exclaimed, pointing to a nearby hill. Timmy scratched his head, wondering who this Hero was. Was it a person? A statue? Or perhaps a magical creature? As he followed the pineapple, he encountered a talking cloud that insisted on debating the merits of pizza toppings. "Pineapple is the best!" it shouted, while a nearby tree chimed in, "No, mushrooms are superior!" Timmy realized that in Blunderburg, even the most unnecessary topics sparked joy and laughter. He decided to embrace the chaos, inviting everyone to a grand feast where they could enjoy pizza topped with whatever they liked—pineapple, mushrooms, or even chocolate! And so, in a town where confusion reigned, Timmy learned that sometimes, the most absurd ideas lead to the best adventures.
"""

# Analyze the story
result = analyze_story(story)

# Print the results
print("Word Count:", result["word_count"])
print("Amount (in paisa):", result["amount"])
print("Vowel Count:", result["vowel_count"])
print("Consonant Count:", result["consonant_count"])
print("Palindrome Count:", result["palindrome_count"])
print("Palindrome Words:", result["palindrome_words"])
