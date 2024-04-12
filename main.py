meme_dict = {
            "CRINGE": "Sesuatu yang sangat buruk atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon"
            }
word = input("Ketik kata yang tidak kamu mengerti (huruf kapital):")
if word in meme_dict.keys():
    print("Artinya:",meme_dict[word])
else:
    print("Kata tidak ditemukan")
