import nltk
import string
from nltk.corpus import words

nltk.download("words")

def cypher_decryption(encrypted_string=None):
    
    if not encrypted_string:
        raise ValueError("No user input provided")
    
    elif not isinstance(encrypted_string, str):
        raise TypeError("User input should be text")
    
    alphabets = string.ascii_letters + " "
    lowercase_alphabets = string.ascii_lowercase
    get_english_words = list(set(words.words()))
    clean_encrypted_string = ""
    for letter in encrypted_string:
        if letter in alphabets:
            clean_encrypted_string += letter
    convert_list = list(clean_encrypted_string.split())

    if len(convert_list) > 1:
        get_string_length = [len(word) for word in convert_list]
        index_of_largest_word = get_string_length.index(max(get_string_length))
        
        for encryption_key in range(26):
            decrypted_string = ""
            for letter in convert_list[index_of_largest_word]:
                if letter.lower() in lowercase_alphabets:
                    index = lowercase_alphabets.index(letter.lower()) - encryption_key
                    if index < 0:
                        index += 26
                        decrypted_string += lowercase_alphabets[index]

                    else:
                        decrypted_string += lowercase_alphabets[index]
                else:
                    decrypted_string += letter
                    
            if decrypted_string in get_english_words:
            
                decrypted_string_list = []
                for word in convert_list:
                    decrypted_string = ""
                    word = word.lower()
                    for letter in word:
                        index = lowercase_alphabets.index(letter) - encryption_key
                        if index < 0:
                            index += 26
                            decrypted_string  += lowercase_alphabets[index]
                            
                        else:
                            decrypted_string += lowercase_alphabets[index]
                    decrypted_string_list.append(decrypted_string)
                    
                return f"'{encrypted_string}' decrypts to '{' '.join(decrypted_string_list[:-1])} {decrypted_string_list[-1]}' with '{encryption_key}' as the encryption key"       
    
    else:
        for encryption_key in range(26):
            decrypted_string = ""
            for letter in clean_encrypted_string:
                if letter.lower() in lowercase_alphabets:
                    n = lowercase_alphabets.index(letter.lower())
                    n -= encryption_key
                    if n < 0:
                        n += 26
                        decrypted_string += lowercase_alphabets[n]

                    else:
                        decrypted_string += lowercase_alphabets[n]
                else:
                    decrypted_string += letter

            if decrypted_string in get_english_words:
                return f"'{encrypted_string}' decrypts to '{decrypted_string}' with '{encryption_key}' as the encryption key"