
def translate_english_to_hindi(word):
    if word == "hello" or word =="Hello":
        hindi_word = "Namaste"
    elif word == "goodbye" or word == "Goodbye":
        hindi_word = "Alwida"
    elif word == "thank you" or word == "Thank You" or word == "Thank you":
        hindi_word = "Dhanyawad"
    else:
        hindi_word = "shabd ka anuwad nahi mila"
    return hindi_word


# Example usage
english_word = input("Enter an English word (hello, goodbye, thank you): ")
hindi_translation = translate_english_to_hindi(english_word)
print(f"\nThe translation of '{english_word}' is: {hindi_translation} \n")