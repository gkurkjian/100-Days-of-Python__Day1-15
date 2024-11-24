 #word_per_page = 0  ## I commented this because we don't need to set it to 0

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))  ## removed the 2 "=="
total_words = pages * word_per_page

print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)
