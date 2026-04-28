label choose_project_state:

    menu:
        "Aku pilih..."

        "Aplikasi image processing untuk deteksi penyakit tanaman":
            $project_idea = "ai"

        "Aplikasi manajemen keuangan untuk mahasiswa":
            $project_idea = "software"

        "Gamified simulasi edukasional":
            $project_idea = "game"

    if project_idea == "ai":
        "Aku memutuskan untuk membuat sebuah aplikasi image processing untuk deteksi penyakit tanaman."

    elif project_idea == "software":
        "Aku memutuskan untuk membuat sebuah aplikasi manajemen keuangan untuk mahasiswa."

    elif project_idea == "game":
        "Aku memutuskan untuk membuat sebuah gamified simulasi edukasional."

    "'Oke, sip. Saatnya bekerja!'"
    "Aku berdiri dari kasurku dan jalan ke meja belajarku untuk mulai mengerjakan proyek ini."
    "Aku menekan tombol power pada laptopku, menunggu untuk proses booting selesai."
    "..."
    "..."
    "..."
    "'Lama amat...'"
    "'Iya juga, laptopku udah tua gini.'"
    "'Duh, cukup ga ya untuk kerjain proyek ini?'"
    "Aku menggigit kuku jempolku, berpikir."
    "'Sepertinya ga kuat... Ah, gimana dong? Masa aku ke warnet untuk ngerjain proyek dari awal sampai selesai?'"
    "Aku menggaruk-garuk kepalaku, bingung. Lama kelamaan, aku malah menggosok-gosok kepalaku seperti orang stress."

    "Tiba-tiba, aku mendapat sebuah ide."
    "'Eh, informatika katanya punya banyak lab kalau ga salah... Mungkin aku bisa pinjam salah satu lab itu untuk ngerjain proyekku ini.'"
    "Aku menjentikkan jariku, merasa ide itu cukup bagus. Aku berdiri, mematikan laptopku yang baru saja selesai booting, dan langsung pergi keluar kamar."
    "Menaikki motorku, aku memasukkan kunci, siap untuk pergi."

    scene bg tc with dissolve

    "Di depanku adalah Gedung Informatika ITS. Aku datang ke sini hampir setiap hari untuk kelas."
    "Tapi hari ini, aku datang ke sini untuk tujuan yang berbeda."

    "Aku jalan masuk ke dalam gedung, menghadap ke arah Plaza."

    scene bg entrance with dissolve

    "'Hm...'"

    "'Di lantai 1 seharusnya ga ada lab, full ruangan kelas. Di lantai 2 isinya ruangan TU dan dosen. Harusnya lab-lab ada dilantai 3,' pikirku."

    scene bg tangga with dissolve

    pause 1.5

    $ current_state = State.HUB_EXPLORE

    return