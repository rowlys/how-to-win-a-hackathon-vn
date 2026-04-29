label ending_state:
    scene black with dissolve
    pause 1.5

    "Hari hackathon pun tiba."
    "Selama berhari-hari aku dan timku bekerja keras, mengerjakan proyek kami di lab yang sudah kami pilih."

    if chosen_lab == "rpl" and project_idea == "software":
        "Lab RPL sangat membantu untuk proyek software manajemen keuangan kami. Fasilitasnya lengkap dan sesuai dengan kebutuhan proyek kami."
    elif chosen_lab == "kcv" and project_idea == "ai":
        "Lab KCV sangat mendukung untuk proyek AI deteksi penyakit tanaman kami. Komputernya kuat dan cocok untuk kebutuhan machine learning kami."
    elif chosen_lab == "giga" and project_idea == "game":
        "Lab GIGA sangat ideal untuk proyek gamified simulasi edukasional kami. Fasilitasnya mendukung untuk pengembangan game dan desain interaktif."

    else:
        "Menggunakan lab yang telah kupilih, kami tetap mencoba yang terbaik. Sekarang saat aku lihat kembali, mungkin ada pilihan lab yang lebih cocok untuk proyek kami." 
        "Tapi aku tetap bersyukur dengan fasilitas yang tersedia dan berusaha memaksimalkannya."
    
    juri "Dipersilahkan kepada tim berikutnya untuk maju ke depan."

    "'Eh, giliran kita maju tu,' ujar salah satu anggota timku."

    "Dengan pengumuman itu, aku dan timku berjalan perlahan menuju panggung. Jantungku berdebar kencang, tapi aku tetap mencoba untuk tenang."
    "'Ini dia, hackathon pertamaku. Saatnya menunjukkan hasil kerja keras kami.'"

    "Kami mempresentasikan proyek kami di hadapan para juri, dan sekarang hanya bisa menunggu hasilnya diumumkan."

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

    "Setelah beberapa jam kami menunggu, akhirnya hasil akhir diumumkan."
    juri "Selamat siang kepada semua peserta. Setelah melalui proses penjurian yang ketat, kami telah memutuskan tiga tim terbaik."
    "..."
    "..."

    if correct_lab and suitable_count >= 3:
        "Tim kami meraih juara pertama!"
        "Semua kerja keras terbayar."
        "Begitulah jalan cerita hackathon pertamaku."
        "Kami berhasil memenangkan juara pertama, mendapatkan penghargaan, dan tentu saja pengalaman yang sangat berharga."
        "'Lihat saja! Di hackathon berikutnya, aku pasti akan juara satu lagi!'"

    elif (correct_lab and suitable_count < 3) or ((not correct_lab) and suitable_count >= 3):
        "Tim kami meraih podium!"
        "Kami naik podium dan mendapatkan penghargaan."
        "Bukan juara satu, tapi tetap membanggakan."
        "Begitulah jalan cerita hackathon pertamaku."
        "Kami mungkin tidak menang juara pertama."
        "Tapi kami tetap mendapatkan penghargaan atas usaha dan kerja keras kami."
        "Dan selain itu, ini menjadi pengalaman yang sangat berharga bagiku dan timku."
        "Lihat saja! Di hackathon berikutnya, aku pasti akan juara satu!"
    
    else:
        "Tim kami tidak memenangkan apapun kali ini."
        "Setidaknya kami belajar banyak dan punya pengalaman berharga."
        "Begitulah jalan cerita hackathon pertamaku."
        "Mungkin aku tidak menang. Mungkin aku tidak mendapatkan penghargaan apapun."
        "Tapi ini tetap menjadi pengalaman yang sangat berharga bagiku."
        "'Lihat saja! Di hackathon berikutnya, aku pasti akan menang!'"

    $ current_state = State.EXIT
    return
