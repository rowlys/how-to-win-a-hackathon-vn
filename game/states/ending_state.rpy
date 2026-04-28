label ending_state:
    scene black with dissolve
    pause 1.5

    "Hari hackathon pun tiba."
    "Kami mempresentasikan proyek kami di hadapan para juri."

    $ correct_lab_map = {"ai": "kcv", "software": "rpl", "game": "giga"}
    $ suitable_map = {
        "ai": {"steven", "andi", "lila", "popol"},
        "game": {"steven", "arif", "anna", "popol"},
        "software": {"andi", "arif", "lila", "popol"},
    }

    if project_idea not in correct_lab_map or chosen_lab == "":
        "Sepertinya ada keputusan yang belum jelas, tapi hasil tetap diumumkan."

    $ correct_lab = project_idea in correct_lab_map and chosen_lab == correct_lab_map[project_idea]
    $ suitable_teammates = suitable_map.get(project_idea, set())
    $ suitable_count = len(recruited_students.intersection(suitable_teammates))

    if correct_lab and suitable_count >= 3:
        "Hasil akhir diumumkan."
        "Tim kami meraih juara pertama!"
        "Semua kerja keras terbayar."
        "Begitulah jalan cerita hackathon pertamaku."
        "Kami berhasil memenangkan juara pertama, mendapatkan penghargaan, dan tentu saja pengalaman yang sangat berharga."
        "'Lihat saja! Di hackathon berikutnya, aku pasti akan juara satu lagi!'"

    elif (correct_lab and suitable_count < 3) or ((not correct_lab) and suitable_count >= 3):
        "Hasil akhir diumumkan."
        "Kami naik podium dan mendapatkan penghargaan."
        "Bukan juara satu, tapi tetap membanggakan."
        "Begitulah jalan cerita hackathon pertamaku."
        "Kami mungkin tidak menang juara pertama."
        "Tapi kami tetap mendapatkan penghargaan atas usaha dan kerja keras kami."
        "Dan selain itu, ini menjadi pengalaman yang sangat berharga bagiku dan timku."
        "Lihat saja! Di hackathon berikutnya, aku pasti akan juara satu!"
    
    else:
        "Hasil akhir diumumkan."
        "Kami tidak memenangkan apapun kali ini."
        "Setidaknya kami belajar banyak dan punya pengalaman berharga."
        "Begitulah jalan cerita hackathon pertamaku."
        "Mungkin aku tidak menang. Mungkin aku tidak mendapatkan penghargaan apapun."
        "Tapi ini tetap menjadi pengalaman yang sangat berharga bagiku."
        "'Lihat saja! Di hackathon berikutnya, aku pasti akan menang!'"

    $ current_state = State.EXIT
    return
