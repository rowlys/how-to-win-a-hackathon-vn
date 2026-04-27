label recruit_105_state:
    # Ganti scene ke Kelas 105

    if "105" not in visited_recruitment_locations:
        $ visited_recruitment_locations.add("105")
        call recruit_105_state.first_visit
    else:
        call recruit_105_state.revisit

    $ current_state = State.ASSEMBLE_TEAM
    return


label recruit_105_state.first_visit:
    "Aku masuk ke Kelas 105. Ruangannya sepi, hanya ada beberapa orang yang belajar sendiri-sendiri."
    "Di salah satu kursi, ada seorang mahasiswa yang tampak sedang mengetik serius di laptopnya."
    "Aku menghampirinya."

    aku "Permisi, mas. Maaf ganggu. Boleh minta waktu sebentar?"
    popol "Eh, boleh. Ada apa?"
    aku "Aku lagi nyari orang buat diajak gabung di tim hackathon. Mas tertarik ga?"
    popol "Hackathon. Proyeknya soal apa?"

    if project_idea == "ai":
        aku "Image processing buat deteksi penyakit tanaman."
        popol "Oh. Pasti butuh server buat jalanin modelnya."
    elif project_idea == "game":
        aku "Game simulasi edukasional."
        popol "Game. Ada komponen backend-nya? Multiplayer, leaderboard, atau semacamnya?"
    elif project_idea == "software":
        aku "Aplikasi manajemen keuangan untuk mahasiswa."
        popol "Aplikasi. Pasti butuh backend yang solid."

    popol "Aku Popol. Semester 3."
    aku "Aku semester 1, mas. Baru."
    popol "Oh, oke."
    popol "Aku sih terbuka buat ikut. Tapi pastiin dulu keahlianku yang kamu butuhin."
    aku "Iya, mas. Keahlian mas ke arah mana?"
    popol "Backend development. Server, API, semua yang jalan di balik layar aplikasi."
    popol "Kalau proyekmu butuh sistem yang bisa handle request dengan baik, integrasi antar komponen, atau deployment yang stabil, itu ranah aku."
    popol "Nah, itu yang kamu butuhin?"

    menu:
        "'Butuhin banget, mas.'":
            aku "Butuhin banget, mas. Proyekku pasti butuh backend yang kuat."
            popol "Oke. Aku gabung."
            aku "Sip, makasih ya mas!"
            popol "Santai. Kita kerjain serius nanti."

            "Dengan begitu, aku berhasil merekrut Popol untuk bergabung di timku!"
            return

        "'Masih ragu, mas.'":
            aku "Hmm, aku masih agak ragu mas. Takutnya keahlian mas bukan yang paling dibutuhin proyekku sekarang."
            popol "Oh, oke. Pikirin dulu. Kalau udah yakin, cari aku di sini lagi."
            aku "Iya, mas. Mungkin aku coba cari yang lain dulu."
            popol "Oke."

            "Aku pamit dan keluar dari kelas."
            "'Oke, coba cari yang lain dulu saja.'"
            return


label recruit_105_state.revisit:
    "Aku kembali ke Kelas 105. Popol masih ada di tempat yang sama, menoleh saat aku masuk."
    popol "Oh, balik lagi. Gimana?"
    aku "Belum ada keputusan, mas. Boleh minta penjelasan lagi soal keahlian mas?"
    popol "Boleh. Singkatnya — backend. Server, API, infrastruktur."
    popol "Handle request, integrasi komponen, deployment yang stabil. Semua yang jalan di balik layar."
    popol "Itu yang kamu butuhin?"

    menu:
        "'Butuhin banget, mas.'":
            aku "Butuhin banget, mas. Proyekku pasti butuh backend yang kuat."
            popol "Oke. Aku gabung."
            aku "Sip, makasih ya mas!"
            popol "Santai. Kita kerjain serius nanti."

            "Dengan begitu, aku berhasil merekrut Popol untuk bergabung di timku!"
            return

        "'Masih ragu, mas.'":
            aku "Hmm, aku masih agak ragu mas. Takutnya keahlian mas bukan yang paling dibutuhin proyekku sekarang."
            popol "Oh, oke. Pikirin dulu. Kalau udah yakin, cari aku di sini lagi."
            aku "Iya, mas. Mungkin aku coba cari yang lain dulu."
            popol "Oke."

            "Aku pamit dan keluar dari kelas."
            "'Oke, coba cari yang lain dulu saja.'"
            return
