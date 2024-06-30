def main():
    booktoread = "books/frankenstein.txt"
    with open(booktoread) as f:
        file_contents = f.read()
        total_word_count, letter_count = countwords(file_contents)
        print(f'--- Begin report of {booktoread} ---')
        print(f'{total_word_count} words found in the document')
        convdict(letter_count)
        print('--- End report ---')
        
def countwords(text):
    words = text.split()
    word_count = len(words)
    letter_count = {}
    for char in text.lower():
        if 'a' <= char <= 'z':    
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return word_count, letter_count

def convdict(letter_count):
    letter_list = list(letter_count.items())
    for key, value in letter_list:
        print(f'The {key} character was found {value} times')

main()