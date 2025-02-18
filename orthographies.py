import yiddish

f = open("ybc_stopwords.txt")
text = f.read()

# hasidify
hasidified = yiddish.hasidify(text)

hasidified_out = open("hasidic_stopwords.txt", "w")

hasidified_out.write(hasidified)

# make combined file
combined_out = open("combined_stopwords.txt", "w")

combined_out.write(text + "\n" + hasidified)
