label recruit_vending_state:
    scene bg vending with dissolve

    if "vending" not in visited_recruitment_locations:
        $ visited_recruitment_locations.add("vending")
        call recruit_vending_state.first_visit from _call_recruit_vending_state_first_visit
    else:
        call recruit_vending_state.revisit from _call_recruit_vending_state_revisit

    $ current_state = State.ASSEMBLE_TEAM
    return


label recruit_vending_state.first_visit:
    "Aku pergi ke area dekat vending machine. Areanya sepi, hanya ada satu orang yang duduk di meja dekat vending machine."
    "Dia tampak sedang mengetik serius di laptopnya."
    "Aku menghampirinya."

    show popol neutral at character_center
    aku "Permisi, mas. Maaf ganggu. Boleh minta waktu sebentar?"
    popol "Eh, boleh. Ada apa?"
    aku "Salam kenal mas, aku mahasiswa baru di sini. Aku lagi nyari orang buat diajak gabung di tim hackathon. Mas tertarik ga?"
    popol "Iya, kenalin juga, aku Popol. Semester 3."
    popol "Hackathon, ya... "
    popol "Proyeknya soal apa?"

    if project_idea == "ai":
        aku "Image processing buat deteksi penyakit tanaman."
        popol "Oh. Pasti butuh server buat jalanin modelnya."
    elif project_idea == "game":
        aku "Game simulasi edukasional."
        popol "Game. Ada komponen backend-nya? Multiplayer, leaderboard, atau semacamnya?"
    elif project_idea == "software":
        aku "Aplikasi manajemen keuangan untuk mahasiswa."
        popol "Aplikasi. Pasti butuh backend yang solid."

    popol "Aku sih terbuka buat ikut. Tapi pastiin dulu keahlianku yang kamu butuhin."
    aku "Iya, mas. Keahlian mas ke arah mana?"
    popol "Backend development. Server, API, semua yang jalan di balik layar aplikasi."
    popol "Kalau proyekmu butuh sistem yang bisa handle request dengan baik, integrasi antar komponen, atau deployment yang stabil, itu ranah aku."

    popol "Tapi sebelum kamu jawab, aku mau tes sedikit dulu ya."
    popol "Dalam pengembangan backend, apa fungsi utama dari sebuah API?"

    "API... Itu singkatan dari 'Application Programming Interface' kalau ga salah.'"
    "'Terus, 'Interface' itu artinya antarmuka, jembatan.'"
    "'Backend itu yang jalan di balik layar. API itu cara bagian lain dari sistem, kayak frontend, bisa ngomong sama backend.'"
    "'Oke, aku ngerti arahnya.'"

    menu:
        "Mengatur tampilan dan komponen visual dari sebuah aplikasi.":
            popol "Itu frontend. Beda sama backend."
            popol "Kayaknya kamu perlu belajar lebih soal ini dulu. Cari aku lagi kalau udah siap."
            "Aku pamit dan keluar dari kelas."
            return

        "Menjadi jembatan komunikasi antara frontend dan sistem backend.":
            $ popol_pass = True
            popol "Tepat. API itu yang ngehubungin antar komponen sistem."
            popol "Oke, kamu ngerti. Nah, itu yang kamu butuhin di proyekmu?"

        "Menyimpan dan mengelola seluruh data pengguna secara permanen.":
            popol "Itu fungsi database. API dan database itu beda."
            popol "Belajar dulu deh soal arsitektur backend. Kalau udah siap, cari aku lagi."
            "Aku pamit dan keluar dari kelas."
            return

        "Menggantikan fungsi database dalam sebuah aplikasi.":
            popol "Salah. API itu bukan pengganti database."
            popol "Kamu perlu pahami dulu perbedaan tiap komponen backend. Cari aku lagi ya."
            "Aku pamit dan keluar dari kelas."
            return

    call recruit_vending_state.recruit_popol from _call_recruit_vending_state_recruit_popol
    return


label recruit_vending_state.revisit:
    show popol neutral at character_center
    "Aku kembali ke area dekat vending machine. Popol masih ada di tempat yang sama, menoleh saat aku masuk."
    popol "Oh, balik lagi. Gimana?"
    aku "Belum ada keputusan, mas. Boleh minta penjelasan lagi soal keahlian mas?"
    popol "Boleh. Singkatnya — backend. Server, API, infrastruktur."
    popol "Handle request, integrasi komponen, deployment yang stabil. Semua yang jalan di balik layar."

    popol "Tapi pertanyaan yang sama masih berlaku."
    popol "Dalam pengembangan backend, apa fungsi utama dari sebuah API?"

    if not popol_pass:
        "Aku udah lebih siap sekarang."
        "API itu Application Programming Interface — jembatan komunikasi antara komponen-komponen sistem."
        "Bukan penyimpan data, bukan pengatur tampilan. API itu yang ngehubungin semuanya."
        "Aku nggak boleh salah lagi."

        menu:
            "Mengatur tampilan dan komponen visual dari sebuah aplikasi.":
                popol "Masih salah. Itu frontend."
                popol "Cari aku lagi kalau udah belajar lebih soal ini."
                "Aku pamit dan keluar dari kelas."
                return

            "Menjadi jembatan komunikasi antara frontend dan sistem backend.":
                popol "Bener. Itu fungsinya."
                popol "Oke. Nah, itu yang kamu butuhin di proyekmu?"

            "Menyimpan dan mengelola seluruh data pengguna secara permanen.":
                popol "Itu database. Beda sama API."
                popol "Belajar lagi dulu ya. Cari aku kalau udah siap."
                "Aku pamit dan keluar dari kelas."
                return

            "Menggantikan fungsi database dalam sebuah aplikasi.":
                popol "Masih salah. API bukan pengganti database."
                popol "Cari aku lagi kalau udah siap ya."
                "Aku pamit dan keluar dari kelas."
                return

    call recruit_vending_state.recruit_popol from _call_recruit_vending_state_recruit_popol_1
    return


label recruit_vending_state.recruit_popol:
    menu:
        "'Butuhin banget, mas.'":
            $ recruited_students.add("popol")
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
