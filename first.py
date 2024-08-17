def word_frequency_counter(file_name, top_n):
    try:
        # Open and read the file
        with open(file_name, 'r') as file:
            text = file.read()

        # Tokenize the text into words
        words = text.split()

        # Create a dictionary to store word frequencies
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        # Sort the words by frequency in descending order
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

        # Display the top N words with their frequencies
        print(f"Top {top_n} Most Frequent Words:")
        for i, (word, freq) in enumerate(sorted_words[:top_n], 1):
            print(f"{i}. {word} - {freq} times")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: Count and display the top 5 most frequent words
file_name = "C://Users//danie//Downloads//sample.txt"  # Replace with the path to your text file
top_n = 5
word_frequency_counter(file_name,top_n)
print ("hi")