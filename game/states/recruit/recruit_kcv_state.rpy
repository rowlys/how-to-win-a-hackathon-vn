label recruit_kcv_state:
    scene bg kcv with dissolve

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

    steven "Tapi sebelum kamu jawab, aku mau tes sedikit dulu ya."
    steven "Dalam machine learning, apa yang sebenernya terjadi saat sebuah model di-'training'?"

    "Training... Aku coba inget-inget apa yang pernah aku baca soal ini."
    "Machine learning itu tentang komputer yang belajar dari data. 'Training' itu proses belajarnya itu sendiri."
    "Model dikasih banyak contoh data, lalu dia belajar ngenalin pola-pola dari contoh itu."
    "Tujuannya supaya nanti model bisa bikin prediksi yang akurat ketemu data baru. Bukan soal nulis kode manual."
    "Oke, aku ngerti arahnya."

    menu:
        "Menulis kode program secara manual untuk menentukan setiap keputusan model.":
            steven "Itu bukan machine learning — itu rule-based programming. Dua hal yang berbeda."
            steven "Sepertinya pemahamanmu soal AI masih perlu diasah. Cari aku lagi kalau udah lebih siap."
            "Aku pamit dan keluar dari Lab KCV."
            return

        "Proses model mempelajari pola dari data latih agar bisa membuat prediksi.":
            $ steven_pass = True
            steven "Tepat. Training itu inti dari machine learning — model belajar dari data."
            steven "Oke, kamu ngerti bidangku. Jadi, yakin kalau itu yang kamu butuhin?"

        "Mengunduh dan menginstal library AI yang dibutuhkan untuk proyek.":
            steven "Itu setup environment. Training itu sesuatu yang berbeda."
            steven "Pelajari dulu konsep dasarnya ya. Kalau udah siap, cari aku lagi."
            "Aku pamit dan keluar dari Lab KCV."
            return

        "Mendesain antarmuka visual dari aplikasi yang menggunakan AI.":
            steven "Itu UI/UX, bukan machine learning."
            steven "Kayaknya kamu perlu baca lebih soal AI dulu. Cari aku lagi ya."
            "Aku pamit dan keluar dari Lab KCV."
            return

    call recruit_kcv_state.recruit_steven
    return


label recruit_kcv_state.revisit:
    "Aku kembali ke Lab KCV. Mas Steven menoleh saat melihatku masuk."
    steven "Oh, balik lagi. Gimana, udah ada keputusan?"
    aku "Belum, mas. Aku mau minta penjelasan lagi soal keahlian mas kalau boleh."
    steven "Tentu. Singkatnya, aku ahli di AI dan machine learning. Bangun model, training, evaluasi."
    steven "Computer vision juga, kalau proyekmu butuh komputer untuk analisis gambar atau video."
    steven "Kalau tim kamu butuh orang yang handle bagian AI dari awal sampai akhir, itu yang bisa aku kerjain."

    steven "Pertanyaanku masih sama — biar aku tau kamu beneran ngerti."
    steven "Dalam machine learning, apa yang terjadi saat sebuah model di-'training'?"

    if not steven_pass:
        "Aku udah lebih siap sekarang."
        "Training itu proses belajarnya model dari data. Model ngenalin pola, lalu bisa prediksi data baru."
        "Bukan soal nulis kode manual, bukan soal install library. Ini soal model belajar dari contoh."
        "Aku harus jawab dengan bener kali ini."

        menu:
            "Menulis kode program secara manual untuk menentukan setiap keputusan model.":
                steven "Masih keliru. Itu rule-based, bukan machine learning."
                steven "Cari aku lagi kalau udah siap ya."
                "Aku pamit dan keluar dari Lab KCV."
                return

            "Proses model mempelajari pola dari data latih agar bisa membuat prediksi.":
                steven "Bener. Itu jawabannya."
                steven "Sekarang gimana? Yakin kalau itu yang kamu butuhin?"

            "Mengunduh dan menginstal library AI yang dibutuhkan untuk proyek.":
                steven "Itu setup. Training berbeda dari itu."
                steven "Cari aku lagi kalau udah siap ya."
                "Aku pamit dan keluar dari Lab KCV."
                return

            "Mendesain antarmuka visual dari aplikasi yang menggunakan AI.":
                steven "Masih salah. Itu UI/UX."
                steven "Pelajari dulu konsep ML-nya. Cari aku lagi."
                "Aku pamit dan keluar dari Lab KCV."
                return

    call recruit_kcv_state.recruit_steven
    return


label recruit_kcv_state.recruit_steven:
    menu:
        "'Yakin, mas.'":
            $ recruited_students.add("steven")
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
