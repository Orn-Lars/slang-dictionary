meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "LMAO": "Tanggapan terhadap sesuatu yang lucu",
            "AGGRO": "untuk menjadi agresif/marah",
            "CREEPY": "menakutkan, tidak menyenangkan"
            "JK": "hanya bercanda"
            }
            
for i in range(5):            
    Question = input("Ketik kata yang ingin kamu ketahui artinya:")
    Question = Question.upper()


    if Question in meme_dict.keys():
        print(meme_dict[Question])
    else:
        print("kata tidak ditemukan")
