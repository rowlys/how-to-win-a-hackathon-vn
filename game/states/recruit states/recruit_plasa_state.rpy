label recruit_plasa_state:
    # Ganti scene ke Plasa

    if "plasa" not in visited_recruitment_locations:
        $ visited_recruitment_locations.add("plasa")
        call recruit_plasa_state.first_visit
    else:
        call recruit_plasa_state.revisit

    $ current_state = State.ASSEMBLE_TEAM
    return


label recruit_plasa_state.first_visit:
    "Aku turun ke plasa, melihat-lihat sekeliling."
    "Di salah satu bangku, ada seorang mahasiswi yang sedang duduk dengan laptop di pangkuannya, tampak fokus pada layarnya."
    "Aku memberanikan diri untuk menghampirinya."

    aku "Permisi, kak. Maaf ganggu. Boleh minta waktu sebentar?"
    lila "Eh, boleh. Ada apa ya?"
    aku "Aku lagi nyari orang buat diajak gabung di tim hackathon. Kak tertarik ga?"
    lila "Hackathon? Hmm. Proyeknya soal apa dulu?"

    if project_idea == "ai":
        aku "Image processing buat deteksi penyakit tanaman."
        lila "Oh, menarik. Pasti ada komponen dataset yang cukup besar."
    elif project_idea == "game":
        aku "Game simulasi edukasional."
        lila "Game ya. Biasanya ada data progress pengguna, leaderboard, semacam itu."
    elif project_idea == "software":
        aku "Aplikasi manajemen keuangan untuk mahasiswa."
        lila "Finansial. Itu pasti banyak data transaksi yang harus dikelola dengan baik."

    lila "Aku Lila, semester 5. Kamu?"
    aku "Aku semester 1, kak. Baru masuk."
    lila "Oh, baru. Oke."
    lila "Kalau mau ngajak aku, pastiin dulu keahlianku yang kamu butuhin ya. Biar nggak mubazir."
    aku "Iya kak, makanya aku mau nanya dulu. Keahlian kakak ke arah mana?"
    lila "Database engineering. Merancang, membangun, dan mengoptimalkan database."
    lila "Kalau proyekmu butuh tempat penyimpanan data yang terstruktur, query yang efisien, atau skema yang bisa scale, itu yang bisa aku kerjain."
    lila "Proyek hackathon yang serius pasti butuh fondasi data yang solid. Jadi, menurut kamu keahlianku itu relevan buat proyekmu?"

    menu:
        "'Relevan banget, kak.'":
            aku "Relevan banget, kak! Aku butuh banget orang yang bisa handle bagian datanya."
            lila "Oke, kalau kamu yakin. Aku ikut deh."
            aku "Wah, makasih banyak ya kak! Senang ada yang mau gabung."
            lila "Sama-sama. Kita kerjain yang terbaik ya."

            "Dengan begitu, aku berhasil merekrut Lila untuk bergabung di timku!"
            return

        "'Masih ragu, kak.'":
            aku "Hmm, aku masih agak ragu kak. Aku takut keahlian kakak kurang pas sama yang proyekku butuhin."
            lila "Oh, nggak masalah. Pikirin dulu aja. Kalau udah yakin, cari aku lagi di sini."
            aku "Iya, makasih ya kak. Mungkin aku coba cari yang lain dulu."
            lila "Oke. Semoga cepet ketemu yang cocok."

            "Aku pamit dan meninggalkan plasa."
            "'Oke, coba cari yang lain dulu saja.'"
            return


label recruit_plasa_state.revisit:
    "Aku kembali ke plasa. Lila masih ada di bangku yang sama, mendongak saat aku menghampiri."
    lila "Oh, kamu lagi. Udah ada keputusan?"
    aku "Belum, kak. Boleh minta penjelasan lagi soal keahlian kakak?"
    lila "Boleh. Singkatnya — database engineering. Merancang dan mengoptimalkan database."
    lila "Kalau proyekmu butuh penyimpanan data yang terstruktur, query yang efisien, dan skema yang bisa scale, itu yang bisa aku kerjain."
    lila "Jadi, menurutmu keahlianku itu relevan buat proyekmu?"

    menu:
        "'Relevan banget, kak.'":
            aku "Relevan banget, kak! Aku butuh banget orang yang bisa handle bagian datanya."
            lila "Oke, kalau kamu yakin. Aku ikut deh."
            aku "Wah, makasih banyak ya kak! Senang ada yang mau gabung."
            lila "Sama-sama. Kita kerjain yang terbaik ya."

            "Dengan begitu, aku berhasil merekrut Lila untuk bergabung di timku!"
            return

        "'Masih ragu, kak.'":
            aku "Hmm, aku masih agak ragu kak. Aku takut keahlian kakak kurang pas sama yang proyekku butuhin."
            lila "Oh, nggak masalah. Pikirin dulu aja. Kalau udah yakin, cari aku lagi."
            aku "Iya, makasih ya kak. Mungkin aku coba cari yang lain dulu."
            lila "Oke. Semoga cepet ketemu yang cocok."

            "Aku pamit dan meninggalkan plasa."
            "'Oke, coba cari yang lain dulu saja.'"
            return
