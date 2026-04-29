label recruit_koridor_state:
    scene bg koridor with dissolve

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

    show anna neutral:
        xalign 0.5
        yalign 0.5
        zoom 1.5
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

    anna "Sebelum kamu mutusin, aku penasaran satu hal."
    anna "Tadi aku nyebut soal 'game feel'. Menurut kamu, apa yang dimaksud dengan game feel dalam game development?"

    "Game feel... Anna tadi nyebut ini pas ngomongin soal kerjaan dia."
    "'Feel' itu artinya perasaan. Dalam konteks game, pasti soal gimana rasanya main gamenya."
    "Bukan soal genrenya apa, bukan soal grafis atau soundtracknya bagus — itu semua hal yang berbeda."
    "Game feel itu respons yang pemain rasain tiap berinteraksi — suara, animasi, feedback yang bikin setiap aksi terasa nyata dan memuaskan."
    "Oke, aku yakin arahnya."

    menu:
        "Genre atau kategori dari sebuah game, seperti action, RPG, atau puzzle.":
            anna "Hmm, itu kategori game, bukan game feel."
            anna "Kayaknya kamu belum familiar sama konsep ini. Cari aku lagi kalau udah baca-baca ya."
            "Aku pamit ke Mba Anna dan melanjutkan pencarianku."
            return

        "Grafis dan soundtrack berkualitas tinggi yang membuat game terlihat keren.":
            anna "Itu presentasi — visual dan audio. Game feel itu lebih dari sekadar itu."
            anna "Coba pelajari lagi konsepnya ya. Cari aku kalau udah siap."
            "Aku pamit ke Mba Anna dan melanjutkan pencarianku."
            return

        "Respons sensoris dan feedback yang membuat setiap interaksi dalam game terasa memuaskan.":
            $ anna_pass = True
            anna "Nah, tepat! Game feel itu soal bagaimana setiap aksi pemain terasa responsif dan memuaskan."
            anna "Oke, kamu ngerti. Jadi gimana? Yakin butuh aku di timmu?"

        "Skor dan sistem pencapaian yang bisa didapat pemain selama bermain.":
            anna "Itu game progression atau reward system. Bukan game feel."
            anna "Pelajari lebih dulu ya. Cari aku kalau udah siap."
            "Aku pamit ke Mba Anna dan melanjutkan pencarianku."
            return

    call recruit_koridor_state.recruit_anna
    return


label recruit_koridor_state.revisit:
    "Aku kembali ke koridor. Mba Anna masih ada di sana, tersenyum saat melihatku mendekat."
    anna "Oh, balik lagi. Udah ada keputusan?"
    aku "Belum, mba. Boleh minta penjelasan lagi soal keahlian mba?"
    anna "Tentu. Aku di game development — desain mekanik, implementasi game logic, dan optimasi performa."
    anna "Intinya, bagaimana membuat game yang tidak hanya berjalan, tapi juga terasa enak dimainkan."

    anna "Pertanyaan tadi masih berlaku ya."
    anna "Apa yang dimaksud dengan game feel dalam game development?"

    if not anna_pass:
        "Aku udah lebih siap sekarang."
        "Game feel itu soal respons dan feedback yang pemain rasain tiap berinteraksi dengan game."
        "Bukan genre, bukan grafis semata. Ini soal gimana setiap aksi terasa nyata dan memuaskan."
        "Aku harus jawab dengan bener."

        menu:
            "Genre atau kategori dari sebuah game, seperti action, RPG, atau puzzle.":
                anna "Masih salah. Itu genre, bukan game feel."
                anna "Cari aku lagi kalau udah baca-baca ya."
                "Aku pamit ke Mba Anna."
                return

            "Grafis dan soundtrack berkualitas tinggi yang membuat game terlihat keren.":
                anna "Masih kurang tepat. Game feel itu lebih dari presentasi visual dan audio."
                anna "Cari aku lagi kalau udah siap."
                "Aku pamit ke Mba Anna."
                return

            "Respons sensoris dan feedback yang membuat setiap interaksi dalam game terasa memuaskan.":
                anna "Tepat! Itu dia."
                anna "Jadi, yakin butuh aku di timmu?"

            "Skor dan sistem pencapaian yang bisa didapat pemain selama bermain.":
                anna "Itu reward system. Berbeda dari game feel."
                anna "Cari aku lagi kalau udah siap ya."
                "Aku pamit ke Mba Anna."
                return

    call recruit_koridor_state.recruit_anna
    return


label recruit_koridor_state.recruit_anna:
    menu:
        "'Yakin, mba.'":
            $ recruited_students.add("anna")
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
