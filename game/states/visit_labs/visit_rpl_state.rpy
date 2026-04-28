label visit_rpl_state:
    scene bg rpl with dissolve
    if "rpl" not in visited_labs:
        $ visited_labs.add("rpl")
        call visit_rpl_state.first_visit
    else:
        call visit_rpl_state.revisit

    $ current_state = State.HUB_EXPLORE
    return


label visit_rpl_state.first_visit:
    "Aku berjalan sampai ke pojok lantai 3 dan menemukan papan nama bertuliskan \"Laboratorium Rekayasa Perangkat Lunak\"."
    "Aku masuk ke dalamnya, disambut barisan meja yang mengelilingi ruangan, masing-masing dilengkapi komputer. Di tengah ruangan terdapat dua barisan meja panjang yang tampaknya dipakai untuk diskusi atau kerja kelompok."
    "Sudah banyak meja yang terisi, tapi karena mejanya cukup banyak, ruangan ini masih terasa lapang."

    "Aku melangkah pelan menuju salah satu meja kosong, sedikit canggung karena tidak tahu aturannya."

    "Saat hampir sampai, seseorang menepuk bahuku dari belakang. Aku menoleh dan menemukan seorang mahasiswa yang tersenyum ke arahku."
    # Kasi liat admin rpl

    admin_rpl "Halo, mahasiswa baru ya?"
    aku "Iya, mas. Semester 1. Kok ketahuan?"
    admin_rpl "Hahaha, gara-gara kelihatan bingung sih. Yang belum pernah ke sini biasanya emang gitu."
    admin_rpl "Salam kenal ya. Namaku Andi, aku admin di lab ini."
    andi "Kamau ada keperluan apa ke sini? Mau pakai komputer?"
    aku "Iya, mas. Aku lagi nyari lab buat ngerjain proyek hackathon. Laptopku kayaknya kurang kuat."
    andi "Oh, hackathon? Proyeknya soal apa?"

    if project_idea == "ai":
        aku "Image processing buat deteksi penyakit tanaman, mas."
        andi "Wah, menarik tuh. Kalau buat proyek kayak gitu, ada lab lain yang lebih cocok sih spesialisasinya. Tapi kalau mau pakai komputer di sini dulu juga bisa, ga masalah."
    elif project_idea == "software":
        aku "Aplikasi manajemen keuangan untuk mahasiswa, mas."
        andi "Oh, kalau buat aplikasi software gitu, cocok banget dikerjain di lab ini. Spesialisasi lab ini memang untuk pengembangan software."
    elif project_idea == "game":
        aku "Game simulasi edukasional, mas."
        andi "Seru tuh. Untuk game, ada lab yang lebih cocok spesialisasinya. Tapi komputer di sini bebas dipakai kok, ga masalah."

    menu:
        "Tanyakan tentang spesialisasi lab ini lebih lanjut":
            aku "Mas, aku penasaran, lab ini spesialisasinya apa sebenernya?"
            andi "Sesuai namanya, 'Rekayasa Perangkat Lunak'. Fokusnya ke pengembangan software secara menyeluruh."
            andi "Kamu semester 1, jadi mungkin belum ketemu mata kuliahnya. Tapi nanti bakal belajar soal keseluruhan proses pengembangan software, dari perencanaan, desain, implementasi, sampai testing dan deployment."
            andi "Bukan cuma coding. Di RPL, kamu belajar bikin dokumen perencanaan dulu, kayak requirement analysis, user story, use case, dan sebagainya."
            aku "Jadi prosesnya panjang ya mas, bukan langsung coding begitu saja?"
            andi "Betul. Di dunia kerja, kemampuan merencanakan dan mendokumentasikan itu sama pentingnya dengan bisa coding. Makanya di sini kita latih itu semua dari awal."
            aku "Wah, masuk akal. Makasih banyak ya mas penjelasannya."
            andi "Sama-sama. Kalau mau tanya-tanya lagi, mampir aja."

        "Keluar lab":
            aku "Baik, makasih mas. Aku mau keliling ke lab lain dulu."
            andi "Iya, silahkan. Mampir lagi kalau butuh apa-apa ya."

    "Aku keluar dari lab RPL. Cukup banyak yang aku pelajari, dan ini baru lab pertama."

    return

label visit_rpl_state.revisit:
    "Aku kembali ke lab RPL. Andi mengangguk saat melihatku masuk."
    andi "Oh, balik lagi. Ada yang mau ditanyain?"

    menu:
        "Tanyakan tentang spesialisasi lab ini lagi":
            aku "Mas, aku mau minta penjelasan lagi soal spesialisasi lab ini. Boleh?"
            andi "Tentu. Jadi lab ini fokusnya ke pengembangan software secara menyeluruh."
            andi "Keseluruhan prosesnya, dari perencanaan, desain, implementasi, sampai testing dan deployment."
            andi "Bukan cuma coding. Di RPL, kamu belajar bikin dokumen perencanaan dulu, kayak requirement analysis, user story, use case, dan sebagainya."
            aku "Jadi prosesnya panjang ya mas, bukan langsung coding begitu saja?"
            andi "Betul. Di dunia kerja, kemampuan merencanakan dan mendokumentasikan itu sama pentingnya dengan bisa coding. Makanya di sini kita latih itu semua dari awal."
            aku "Oke, makasih lagi mas."
            andi "Sama-sama. Kalau mau tanya lagi, mampir aja."

        "Keluar lab":
            aku "Nggak ada, mas. Makasih. Aku duluan ya."
            andi "Oke, hati-hati."

    return