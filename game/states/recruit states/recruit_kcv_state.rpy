label recruit_kcv_state:
    # Ganti scene ke Lab KCV

    if "kcv" not in visited_recruitment_locations:
        $ visited_recruitment_locations.add("kcv")
        call recruit_kcv_state.first_visit
    else:
        call recruit_kcv_state.revisit

    $ current_state = State.ASSEMBLE_TEAM

    return


label recruit_kcv_state.first_visit:
    "Aku kembali ke Lab KCV, mencari-cari Mas Steven di dalam ruangan."
    "'Ah, itu dia.'"

    "Mas Steven tampak sedang mengerjakan sesuatu di komputernya. Aku menghampiri dan menyapanya."

    aku "Mas Steven, maaf ganggu. Boleh minta waktu sebentar?"
    steven "Oh, kamu lagi. Boleh. Kenapa?"
    aku "Aku lagi nyari anggota tim buat hackathon. Aku kepikiran Mas Steven — kira-kira mau gabung ga?"
    steven "Hackathon? Serius kamu."

    if project_idea == "ai":
        steven "Proyeknya yang image processing itu kan?"
        aku "Iya, mas."
    elif project_idea == "game":
        steven "Yang game edukasi itu?"
        aku "Iya, mas."
    elif project_idea == "software":
        steven "Yang aplikasi keuangan itu?"
        aku "Iya, mas."

    steven "Aku sih tertarik. Tapi pastiin dulu kamu tau apa yang bisa aku kontribusiin ke tim kamu."
    aku "Nah iya mas, makanya aku mau nanya. Kalau secara keahlian, mas bisa bantu ke arah mana?"
    steven "Spesialisasiku di AI dan machine learning. Dari bangun model, training, sampai evaluasinya."
    steven "Computer vision juga. Kalau proyekmu butuh komputer untuk 'ngerti' gambar atau video, itu bidangku."
    steven "Kalau tim kamu butuh orang yang bisa handle bagian AI dari awal sampai akhir, aku bisa itu."
    steven "Jadi, yakin kalau itu yang kamu butuhin?"

    menu:
        "'Yakin, mas.'":
            aku "Yakin banget, mas. Proyekku butuh orang yang ngerti AI, dan Mas Steven yang paling tepat buat itu."
            steven "Oke. Kalau kamu yakin, aku gabung."
            aku "Wah, makasih banyak ya mas! Ini bakal ngebantu banget."
            steven "Sama-sama. Kita kerjain yang terbaik ya."

            "Dengan begitu, aku berhasil merekrut Mas Steven untuk bergabung di timku!"
            return

        "'Masih ragu, mas.'":
            aku "Hmm... Aku masih agak ragu, mas. Takutnya keahlian mas kurang cocok sama kebutuhan proyekku."
            steven "Oh, kalau gitu pikirin dulu. Kalau udah yakin, cari aku lagi."
            aku "Iya, mas. Mungkin aku coba cari yang lain dulu."
            steven "Oke, nggak masalah. Hati-hati."

            "Aku pamit dan keluar dari Lab KCV."
            "'Oke, coba cari yang lain dulu saja.'"
            return


label recruit_kcv_state.revisit:
    "Aku kembali ke Lab KCV. Mas Steven menoleh saat melihatku masuk."
    steven "Oh, balik lagi. Gimana, udah ada keputusan?"
    aku "Belum, mas. Aku mau minta penjelasan lagi soal keahlian mas kalau boleh."
    steven "Tentu. Singkatnya, aku ahli di AI dan machine learning. Bangun model, training, evaluasi."
    steven "Computer vision juga, kalau proyekmu butuh komputer untuk analisis gambar atau video."
    steven "Kalau tim kamu butuh orang yang handle bagian AI dari awal sampai akhir, itu yang bisa aku kerjain."
    steven "Sekarang gimana? Yakin kalau itu yang kamu butuhin?"

    menu:
        "'Yakin, mas.'":
            aku "Yakin banget, mas. Proyekku butuh orang yang ngerti AI, dan Mas Steven yang paling tepat buat itu."
            steven "Oke. Kalau kamu yakin, aku gabung."
            aku "Wah, makasih banyak ya mas! Ini bakal ngebantu banget."
            steven "Sama-sama. Kita kerjain yang terbaik ya."

            "Dengan begitu, aku berhasil merekrut Mas Steven untuk bergabung di timku!"
            return

        "'Masih ragu, mas.'":
            aku "Hmm... Aku masih agak ragu, mas. Takutnya keahlian mas kurang cocok sama kebutuhan proyekku."
            steven "Oh, kalau gitu pikirin dulu. Kalau udah yakin, cari aku lagi."
            aku "Iya, mas. Mungkin aku coba cari yang lain dulu."
            steven "Oke, nggak masalah. Hati-hati."

            "Aku pamit dan keluar dari Lab KCV."
            "'Oke, coba cari yang lain dulu saja.'"
            return
