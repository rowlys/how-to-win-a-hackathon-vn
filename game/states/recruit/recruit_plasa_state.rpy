label recruit_plasa_state:
    scene bg plasa with dissolve

    if "plasa" not in visited_recruitment_locations:
        $ visited_recruitment_locations.add("plasa")
        call recruit_plasa_state.first_visit from _call_recruit_plasa_state_first_visit
    else:
        call recruit_plasa_state.revisit from _call_recruit_plasa_state_revisit

    $ current_state = State.ASSEMBLE_TEAM
    return


label recruit_plasa_state.first_visit:
    "Aku turun ke plasa, melihat-lihat sekeliling."
    "Di salah satu bangku, ada seorang mahasiswi yang sedang duduk dengan laptop di pangkuannya, tampak fokus pada layarnya."
    "Aku memberanikan diri untuk menghampirinya."

    show lila neutral at character_center
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

    lila "Sebelum kamu jawab, aku mau tes sedikit dulu ya."
    lila "Dalam database, apa fungsi utama dari sebuah 'index'?"

    "Index... Aku coba inget-inget pelajaran yang pernah lewat."
    "Index itu mirip daftar isi di buku. Kamu nggak perlu baca seluruh buku buat nemuin topik tertentu — langsung cek daftar isinya."
    "Sama kayak di database — index membantu sistem nemuin data lebih cepat tanpa harus scan seluruh tabel satu per satu."
    "Jadi fungsinya untuk mempercepat pencarian dan pengambilan data. Bukan untuk nyimpen backup, bukan untuk atur akses."
    "Oke, aku tau arahnya."

    menu:
        "Menyimpan salinan cadangan dari seluruh data dalam tabel.":
            lila "Itu fungsi backup, bukan index."
            lila "Kayaknya kamu perlu belajar lebih soal database dulu. Cari aku lagi kalau udah siap."
            "Aku pamit dan meninggalkan plasa."
            return

        "Mempercepat pencarian dan pengambilan data dari sebuah tabel.":
            $ lila_pass = True
            lila "Tepat. Index itu memang untuk optimasi query — biar pencarian lebih cepat."
            lila "Oke, kamu ngerti. Jadi, menurutmu keahlianku itu relevan buat proyekmu?"

        "Menentukan siapa saja yang berhak mengakses data dalam tabel.":
            lila "Itu access control atau permissions. Bukan fungsi index."
            lila "Belajar lebih soal konsep database dulu ya. Cari aku kalau udah siap."
            "Aku pamit dan meninggalkan plasa."
            return

        "Menggabungkan beberapa tabel menjadi satu kesatuan yang lebih besar.":
            lila "Itu lebih ke join atau relasi antar tabel. Beda sama index."
            lila "Pelajari dulu ya. Kalau udah siap, cari aku lagi."
            "Aku pamit dan meninggalkan plasa."
            return

    call recruit_plasa_state.recruit_lila from _call_recruit_plasa_state_recruit_lila
    return


label recruit_plasa_state.revisit:
    show lila neutral at character_center
    "Aku kembali ke plasa. Lila masih ada di bangku yang sama, mendongak saat aku menghampiri."
    lila "Oh, kamu lagi. Udah ada keputusan?"
    aku "Belum, kak. Boleh minta penjelasan lagi soal keahlian kakak?"
    lila "Boleh. Singkatnya — database engineering. Merancang dan mengoptimalkan database."
    lila "Kalau proyekmu butuh penyimpanan data yang terstruktur, query yang efisien, dan skema yang bisa scale, itu yang bisa aku kerjain."

    lila "Pertanyaan yang sama masih berlaku."
    lila "Dalam database, apa fungsi utama dari sebuah 'index'?"

    if not lila_pass:
        "Aku udah lebih siap sekarang."
        "Index itu kayak daftar isi, bantu sistem nemuin data lebih cepat tanpa scan seluruh tabel."
        "Fungsinya untuk mempercepat pencarian dan pengambilan data. Itu intinya."
        "Kali ini aku harus bener."

        menu:
            "Menyimpan salinan cadangan dari seluruh data dalam tabel.":
                lila "Masih salah. Itu backup."
                lila "Cari aku lagi kalau udah siap ya."
                "Aku pamit dan meninggalkan plasa."
                return

            "Mempercepat pencarian dan pengambilan data dari sebuah tabel.":
                lila "Bener. Itu fungsinya."
                lila "Jadi, menurutmu keahlianku relevan buat proyekmu?"

            "Menentukan siapa saja yang berhak mengakses data dalam tabel.":
                lila "Masih keliru. Itu access control."
                lila "Cari aku kalau udah siap ya."
                "Aku pamit dan meninggalkan plasa."
                return

            "Menggabungkan beberapa tabel menjadi satu kesatuan yang lebih besar.":
                lila "Bukan. Itu join atau relasi antar tabel."
                lila "Pelajari lagi ya. Cari aku kalau udah siap."
                "Aku pamit dan meninggalkan plasa."
                return

    call recruit_plasa_state.recruit_lila from _call_recruit_plasa_state_recruit_lila_1
    return


label recruit_plasa_state.recruit_lila:
    menu:
        "'Relevan banget, kak.'":
            $ recruited_students.add("lila")
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
