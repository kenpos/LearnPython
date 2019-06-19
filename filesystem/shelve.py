import shelve
shelf_file = shelve.open('./mydata2')
cats = ['Zophie','Pooka','Simon']

shelf_file['cats'] = cats

shelf_file.close()