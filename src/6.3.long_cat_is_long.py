def long_cat_is_long(text):

    clean_text = ''.join(ch.lower() if ch.isalpha() else ' ' for ch in text)
    dict = {word: len(word) for word in clean_text.split()}
    
    return dict

if __name__ == "__main__":
    text = """
            You see, wire telegraph is a kind of a very, very long cat.
            You pull his tail in New York and his head is meowing in Los Angeles.
            Do you understand this?
            And radio operates exactly the same way: you send signals here, they receive them there.
            The only difference is that there is no cat.
            """
    print(long_cat_is_long(text))