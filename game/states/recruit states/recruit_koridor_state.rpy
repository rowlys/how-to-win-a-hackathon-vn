label recruit_koridor_state:
    # Ganti scene ke Koridor

    if "koridor" not in visited_recruitment_locations:
        $ visited_recruitment_locations.add("koridor")
        call recruit_koridor_state.first_visit
    else:
        call recruit_koridor_state.revisit

    $ current_state = State.ASSEMBLE_TEAM
    return


label recruit_koridor_state.first_visit:
    "Aku berjalan menyusuri koridor lantai 3, mataku menyapu kiri kanan mencari-cari."
    "Dan di ujung koridor, aku melihat sosok yang familiar."
    "'Eh, itu Mba Anna!'"

    "Mba Anna — admin Lab GIGA yang kemarin banyak menjelaskan soal lab-nya. Aku nggak nyangka bisa ketemu dia di luar lab."
    "Aku melangkah ke arahnya. Anna menoleh dan langsung mengenaliku."

    anna "Oh! Kamu yang kemarin keliling lab-lab itu ya?"
    aku "Iya, mba! Mba Anna lagi ngapain di sini?"
    anna "Lagi istirahat sebentar. Kamu sendiri, masih keliling?"
    aku "Masih, mba. Tapi sekarang bukan nyari lab lagi. Aku lagi nyari anggota tim buat hackathon."
    anna "Oh serius? Jadi kamu beneran lanjut?"
    aku "Iya, mba. Labnya juga udah ketemu. Tinggal timnya nih yang belum lengkap."
    anna "Wah, cepet. Trus, aku bisa bantu apa?"
    aku "Itu dia, mba. Kira-kira Mba Anna mau gabung di tim aku ga?"

    anna "Hmm. Aku tertarik. Tapi tadi kan aku lebih banyak cerita soal lab-nya. Belum banyak soal keahlian aku sendiri."
    anna "Biar kamu bisa pertimbangin dengan baik."
    aku "Iya mba, boleh cerita?"
    anna "Aku spesialisasi di game development. Dari desain mekanik permainan, implementasi game logic, sampai optimasi performa game."
    anna "Bukan cuma bikin game asal jalan — tapi gimana gamenya terasa enak dimainkan. Game feel, pacing, feedback ke pemain, semua itu bagian dari yang aku kerjain."

    if project_idea == "game":
        aku "Wah, proyekku tentang game simulasi edukasional, mba. Kayaknya nyambung banget!"
        anna "Kalau gitu, aku rasa keahlianku jelas relevan buat proyekmu."
    elif project_idea == "ai":
        aku "Proyekku tentang image processing, mba. Jujur aku agak ragu nyambungnya ke mana."
        anna "Hmm, memang nggak langsung. Tapi kalau ada elemen antarmuka interaktif di proyekmu, pengalamanku di game bisa kasih perspektif yang menarik soal itu."
    elif project_idea == "software":
        aku "Proyekku tentang aplikasi keuangan, mba. Mungkin irisannya di sisi interaksi pengguna ya?"
        anna "Bisa. Pengalaman bikin game itu melatih intuisi soal interaksi pengguna yang kadang nggak kepikiran sama developer aplikasi biasa."

    anna "Jadi gimana? Yakin butuh aku di timmu?"

    menu:
        "'Yakin, mba.'":
            aku "Yakin, mba. Aku butuh orang yang bisa kasih perspektif itu ke proyekku."
            anna "Oke deh. Aku ikut."
            aku "Wah, makasih banyak ya mba Anna!"
            anna "Sama-sama. Semoga proyeknya sukses. Kita kerjain bareng yang terbaik ya."

            "Dengan begitu, aku berhasil merekrut Mba Anna untuk bergabung di timku!"
            return

        "'Masih ragu, mba.'":
            aku "Hmm, aku masih agak ragu mba. Aku takut keahlian mba kurang pas sama kebutuhan proyekku."
            anna "Oh, nggak masalah. Pikirin dulu. Kalau udah ada keputusan, cari aku lagi ya."
            aku "Iya, mba. Makasih ya."
            anna "Sama-sama. Semoga cepet ketemu yang cocok."

            "Aku pamit ke Mba Anna dan melanjutkan pencarianku."
            "'Oke, coba cari yang lain dulu saja.'"
            return


label recruit_koridor_state.revisit:
    "Aku kembali ke koridor. Mba Anna masih ada di sana, tersenyum saat melihatku mendekat."
    anna "Oh, balik lagi. Udah ada keputusan?"
    aku "Belum, mba. Boleh minta penjelasan lagi soal keahlian mba?"
    anna "Tentu. Aku di game development — desain mekanik, implementasi game logic, dan optimasi performa."
    anna "Intinya, bagaimana membuat game yang tidak hanya berjalan, tapi juga terasa enak dimainkan."
    anna "Jadi, yakin butuh aku di timmu?"

    menu:
        "'Yakin, mba.'":
            aku "Yakin, mba. Aku butuh orang yang bisa kasih perspektif itu ke proyekku."
            anna "Oke deh. Aku ikut."
            aku "Wah, makasih banyak ya mba Anna!"
            anna "Sama-sama. Semoga proyeknya sukses. Kita kerjain bareng yang terbaik ya."

            "Dengan begitu, aku berhasil merekrut Mba Anna untuk bergabung di timku!"
            return

        "'Masih ragu, mba.'":
            aku "Hmm, aku masih agak ragu mba. Aku takut keahlian mba kurang pas sama kebutuhan proyekku."
            anna "Oh, nggak masalah. Pikirin dulu. Kalau udah ada keputusan, cari aku lagi ya."
            aku "Iya, mba. Makasih ya."
            anna "Sama-sama. Semoga cepet ketemu yang cocok."

            "Aku pamit ke Mba Anna dan melanjutkan pencarianku."
            "'Oke, coba cari yang lain dulu saja.'"
            return
