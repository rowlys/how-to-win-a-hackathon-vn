label recruit_rpl_state:
    scene bg rpl with dissolve

    if "rpl" not in visited_recruitment_locations:
        $ visited_recruitment_locations.add("rpl")
        call recruit_rpl_state.first_visit
    else:
        call recruit_rpl_state.revisit

    $ current_state = State.ASSEMBLE_TEAM

    return


label recruit_rpl_state.first_visit:

    "Aku memutuskan untuk mencoba ke Lab RPL, berharap aku dapat bertemu dengan Mas Andi lagi."

    "'Ah! Itu Mas Andi!'"
    "Saat aku menyadarinya, Mas Andi pun menoleh ke arahku dan tersenyum ramah."
    "Aku jalan menghampirinya, sedikit gugup tapi juga bersemangat. Mas Andi kan jago! Kalau dia mau gabung di timku, pasti proyekku bakal makin bagus!"

    aku "Permisi, Mas Andi. Uh... aku lagi cari tim buat ikut hackathon, kira-kira Mas Andi mau gabung ga ya?"
    andi "Oh, halo. Ini buat proyek yang kemarin kamu omongin itu ya?"
    aku "Iya, mas. Sekarang aku masih kekurangan anggota tim, jadi aku lagi nyari-nyari siapa tau ada yang mau gabung."
    aku "Eh, terus kepikiran tentang Mas Andi. Mas Andi kan keliatannya seru nih, tapi pinter banget juga, hehe."
    andi "Hahaha, baru juga kita ngobrol bentar kemarin."

    if project_idea == "ai":
        andi "Kalau ga salah ide proyek kamu itu tentang aplikasi image processing ya?"
        aku "Iya, mas."
    if project_idea == "game":
        andi "Kalau ga salah ide proyek kamu itu tentang game ya?"
        aku "Iya, mas."
    if project_idea == "software":
        andi "Kalau ga salah ide proyek kamu itu tentang aplikasi manajemen keuangan ya?"
        aku "Iya, mas."

    andi "Hmm... Aku sih tertarik, tapi kamu harus yakin banget ni, kalau keahlian aku itu cocok ga sama kebutuhan aplikasimu."
    aku "Iya, benar mas. Kalau gitu, aku boleh tanya ga, keahlian mas ini secara detail ke arah mana mas?"
    andi "Kalau aku, kan admin RPL ini, jadi lebih ke software development. Aku juga percaya dirinya itu dibagian desain sistem dan arsitektur software."
    andi "Kalau kamu butuh orang yang bisa bantuin coding, debugging, atau desain sistem dalam sebuah aplikasi yang memerlukan struktur yang baik, aku rasa aku bisa bantuin di situ."

    andi "Tapi sebelum kamu jawab, aku mau tes sedikit dulu ya."
    andi "Dalam desain arsitektur software, apa tujuan utama dari 'separation of concerns'?"

    "Separation of concerns... 'Separation' itu pemisahan, 'concerns' itu masalah atau tanggung jawab."
    "Mas Andi nyebut 'desain sistem dan arsitektur software'. Pasti ini salah satu konsep dasarnya."
    "Kalau tiap bagian sistem fokus pada satu tanggung jawab yang jelas, sistem jadi lebih mudah dipahami, diubah, dan di-debug."
    "Jadi ini soal memecah sistem jadi bagian-bagian yang masing-masing punya satu tanggung jawab spesifik."
    "Oke, aku yakin jawabannya."

    menu:
        "Memastikan seluruh kode ditulis oleh satu developer agar tetap konsisten.":
            andi "Hehe, bukan itu. Separation of concerns itu soal struktur kode, bukan siapa yang nulis."
            andi "Coba pelajari dulu konsep arsitektur software-nya ya. Kalau udah siap, cari aku lagi."
            "Setelah mengucapkan terima kasih, aku pun pamit dan keluar dari Lab RPL."
            return

        "Membagi sistem menjadi bagian-bagian yang masing-masing punya tanggung jawab spesifik agar mudah dikelola.":
            $ andi_pass = True
            andi "Nah, bener! Separation of concerns itu memang soal memisahkan tanggung jawab tiap bagian sistem."
            andi "Oke, kamu ngerti. Jadi, yakin kalau keahlian aku sesuai sama kebutuhan proyek kamu?"

        "Mengurangi jumlah file dalam proyek sebanyak mungkin agar lebih ringkas.":
            andi "Bukan itu tujuannya. Kalau terlalu dipaksa ringkas, strukturnya malah bisa berantakan."
            andi "Pelajari dulu ya konsep arsitektur software-nya. Cari aku lagi kalau udah siap."
            "Setelah mengucapkan terima kasih, aku pun pamit dan keluar dari Lab RPL."
            return

        "Menyatukan seluruh logika program dalam satu modul agar mudah diakses.":
            andi "Justru sebaliknya! Separation of concerns itu soal memisahkan, bukan menyatukan semuanya."
            andi "Cari aku lagi kalau udah lebih paham soal ini ya."
            "Setelah mengucapkan terima kasih, aku pun pamit dan keluar dari Lab RPL."
            return

    call recruit_rpl_state.recruit_andi
    return


label recruit_rpl_state.revisit:
    "Aku kembali ke Lab RPL. Mas Andi menoleh dan langsung menyapaku."
    andi "Oh, sudah balik lagi. Ada yang mau ditanyain?"
    aku "Iya, mas. Aku mau minta penjelasan lagi soal keahlian mas kalau boleh."
    andi "Oh, boleh. Jadi singkatnya, aku kuat di software development. Terutama di desain sistem dan arsitektur software."
    andi "Kalau proyekmu butuh struktur yang solid, orang yang bisa bantu rencanain dan coding-in sistem dari awal, itu yang bisa aku kerjain."

    andi "Pertanyaan tadi masih berlaku ya. Biar aku tau kamu beneran ngerti."
    andi "Dalam desain arsitektur software, apa tujuan utama dari 'separation of concerns'?"

    if not andi_pass:
        "Aku udah lebih siap sekarang."
        "Separation of concerns — memecah sistem jadi bagian-bagian yang masing-masing punya satu tanggung jawab spesifik."
        "Tujuannya biar lebih mudah dikelola, diubah, dan di-debug. Itu prinsip dasar arsitektur yang baik."
        "Kali ini aku harus jawab dengan bener."

        menu:
            "Memastikan seluruh kode ditulis oleh satu developer agar tetap konsisten.":
                andi "Masih salah. Ini soal struktur kode, bukan soal siapa yang nulis."
                andi "Cari aku lagi kalau udah siap ya."
                "Aku pun pamit dan keluar dari Lab RPL."
                return

            "Membagi sistem menjadi bagian-bagian yang masing-masing punya tanggung jawab spesifik agar mudah dikelola.":
                andi "Tepat! Itu dia."
                andi "Sekarang gimana? Yakin kalau keahlian aku sesuai sama kebutuhan proyek kamu?"

            "Mengurangi jumlah file dalam proyek sebanyak mungkin agar lebih ringkas.":
                andi "Masih keliru. Bukan soal jumlah file-nya."
                andi "Cari aku lagi kalau udah siap ya."
                "Aku pun pamit dan keluar dari Lab RPL."
                return

            "Menyatukan seluruh logika program dalam satu modul agar mudah diakses.":
                andi "Justru kebalikannya. Separation itu pemisahan, bukan penyatuan."
                andi "Cari aku lagi ya kalau udah lebih paham."
                "Aku pun pamit dan keluar dari Lab RPL."
                return

    call recruit_rpl_state.recruit_andi
    return


label recruit_rpl_state.recruit_andi:
    menu:
        "'Yakin, mas.'":
            $ recruited_students.add("andi")
            aku "Iya, mas. Aku yakin banget kalau keahlian mas itu cocok banget buat proyekku. Aku butuh banget orang yang bisa bantuin coding dan desain sistem."
            andi "Kalau kamu yakin, aku sih senang banget bisa gabung di tim kamu. Aku juga lagi pengen banget ikut hackathon, jadi ini kesempatan yang bagus buat aku juga."
            aku "Wah, makasih banyak ya mas! Aku senang banget Mas Andi mau gabung di timku!"
            andi "Sama-sama. Aku juga senang bisa gabung di tim kamu. Kita pasti bisa bikin proyek yang keren bareng-bareng!"

            "Dengan begitu, aku pun berhasil merekrut Mas Andi untuk bergabung di timku!"
            return

        "'Masih ragu, mas.'":
            aku "Hmm... Sebenarnya aku masih agak ragu, mas. Aku takutnya keahlian mas itu kurang cocok buat kebutuhan proyekku."
            andi "Oh, kalau gitu, pikirin aja dulu lagi ya. Nanti kalau kamu udah yakin, tanyain aja lagi ke aku."
            aku "Iya, baik mas. Mungkin aku coba cari yang lain dulu sekaligus mikirin kebutuhan proyekku, ya."
            andi "Wokee kalau gitu. Aman aja."

            "Setelah mengucapkan terima kasih, aku pun pamit dan keluar dari Lab RPL dengan perasaan campur aduk."
            "'Oke, coba cari yang lain dulu saja.'"
            return
