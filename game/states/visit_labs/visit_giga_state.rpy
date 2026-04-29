label visit_giga_state:
    scene bg giga with dissolve
    if "giga" not in visited_labs:
        $ visited_labs.add("giga")
        call visit_giga_state.first_visit from _call_visit_giga_state_first_visit
    else:
        call visit_giga_state.revisit from _call_visit_giga_state_revisit

    $ current_state = State.HUB_EXPLORE
    return


label visit_giga_state.first_visit:
    "Aku berjalan menuju lab yang letaknya dekat tangga, dan menemukan papan nama bertuliskan \"Laboratorium GIGA\"."
    "Aku masuk ke dalamnya. Suasana di dalam cukup ramai, dengan sebuah layar besar diujung meja besar di tengah ruangan, dan ada sudut ruangan yang entah kenapa terdapat kabel-kabel dengan headset aneh tergantung di sana."

    "Seorang mahasiswa yang duduk di dekat pintu menyadari kehadiranku."

    show anna neutral at character_center
    admin_giga "Halo, pertama kali ke sini?"
    aku "Iya, mba. Aku mahasiswa baru, lagi keliling lab nih. Kelihatan bingung ya?"
    admin_giga "Hahaha, iya, agak. Wajar sih, lab ini emang sedikit... berbeda dari yang lain."
    aku "Berbeda gimana, mba?"
    admin_giga "Coba liat dulu aja sekeliling. Kira-kira kamu bisa tebak ga, lab ini spesialisasinya apa?"

    menu:
        "Tebak berdasarkan headset yang tergantung":
            aku "Itu headset VR ya, mba? Jadi lab ini berhubungan sama VR?"
            admin_giga "Wah, hampir tepat. VR dan AR emang salah satu yang dikerjain di sini. Tapi itu bukan satu-satunya."

        "Aku tidak bisa menebak":
            aku "Aku kurang bisa nangkep, mba. Bisa dijelasin langsung aja?"
            admin_giga "Tentu, dengan senang hati."

    admin_giga "Jadi, nama GIGA itu bukan sekadar nama. Itu singkatan dari empat pilar spesialisasi lab ini."
    admin_giga "G yang pertama itu 'Grafika'. Ini tentang computer graphics, visualisasi, dan rendering. Bagaimana komputer bisa menghasilkan gambar dan animasi."
    admin_giga "I itu 'Interaksi', fokusnya ke UI/UX. Bagaimana manusia berinteraksi dengan sistem digital, gimana desain antarmuka yang intuitif dan nyaman dipakai."
    admin_giga "G yang kedua itu 'Game'. Pengembangan game, dari desain mekanik, game engine, sampai implementasinya."
    admin_giga "Dan A itu 'Analitik'. Ini sedikit menyentuh algoritma dan AI, lebih ke sisi analisis data dan kecerdasan komputasional."
    aku "Wah, ternyata itu arti GIGA."
    admin_giga "Iya, dan VR sama AR yang kamu liat tadi, itu ada di persimpangan beberapa pilar sekaligus. Grafika, interaksi, bahkan game pun bisa masuk ke sana."
    admin_giga "Ngomong-ngomong, kamu ke sini ada keperluan khusus ga?"

    if project_idea == "game":
        aku "Iya, mba. Aku lagi nyari lab yang cocok buat ngerjain proyek hackathon. Proyekku berhubungan sama game."
        admin_giga "Oh, kalau game, kamu udah di tempat yang tepat. Lab ini emang salah satu tempat paling cocok buat ngerjain proyek game. Komputer di sini juga speknya cukup oke buat itu."
    elif project_idea == "ai":
        aku "Iya, mba. Aku lagi nyari lab yang cocok buat ngerjain proyek hackathon. Proyekku berhubungan sama AI dan image processing."
        admin_giga "Menarik. Pilar Analitik di sini memang nyentuh AI, tapi kalau proyekmu lebih ke AI berat, mungkin ada lab lain yang lebih spesifik. Tapi kalau mau pakai komputer di sini dulu, boleh-boleh aja kok."
    elif project_idea == "software":
        aku "Iya, mba. Aku lagi nyari lab yang cocok buat ngerjain proyek hackathon. Proyekku berhubungan sama aplikasi manajemen keuangan."
        admin_giga "Oh, untuk software kayak gitu, mungkin lab lain lebih cocok spesialisasinya. Tapi kalau proyekmu butuh elemen UI/UX yang bagus, pilar Interaksi di sini bisa kasih banyak insight lho."

    menu:
        "Tanyakan tentang pilar-pilar GIGA lebih lanjut":
            aku "Mba, bisa cerita lebih dalam ga soal mbaing-mbaing pilarnya? Aku penasaran soal implementasinya di dunia nyata."
            admin_giga "Tentu. Grafika misalnya, ini dipakai di mana-mana, dari film animbai, simulasi arsitektur, sampai visualisasi data ilmiah."
            admin_giga "Interaksi atau UI/UX itu krusial banget. Sebuah aplikasi yang bagus secara teknis tapi susah dipakai ya percuma. Di sini kita belajar riset pengguna, prototyping, dan evaluasi desain."
            admin_giga "Game development itu multidisiplin. Kamu perlu grafika buat visuals, interaksi buat gameplay feel, dan analitik buat AI musuh atau balancing game."
            admin_giga "Dan Analitik, ini makin relevan sekarang, di mana data dan AI ada di mana-mana. Kita belajar algoritma, machine learning dasar, dan cara mengolah data jadi insight yang berguna."
            aku "Jadi keempat pilar itu saling melengkapi ya mba, bukan berdiri sendiri-sendiri."
            admin_giga "Persis. Itulah kelebihan belajar di GIGA. Kamu ga cuma spesialis di satu bidang, tapi ngerti bagaimana bidang-bidang itu saling terhubung."
            aku "Wah, makasih banyak ya mba penjelasannya. Aku jadi makin paham sekarang."
            admin_giga "Sama-sama. Kalau mau eksplorasi lebih lanjut, atau mau coba headset VR-nya, mampir lagi aja kapanpun."
            aku "Oh iya mba, aku lupa nanya. Kalau boleh tau, nama mba siapa ya?"
            admin_giga "Oh, namaku Anna, aku admin di lab ini."
            anna "Ingat ya, kalau mau mampir atau nanya-nanya, jangan sungkan cari aku aja."

        "Keluar lab":
            aku "Wah, keren banget mba."
            aku "Oh iya mba, aku lupa nanya. Kalau boleh tau, nama mba siapa ya?"
            admin_giga "Oh, namaku Anna, aku admin di lab ini."
            anna "Kalau kamu mau mampir lagi atau nanya-nanya soal lab ini, jangan sungkan cari aku aja ya."
            aku "Baik mba, makasih banyak ya penjelasannya. Aku coba ke lab lain juga dulu ya mba. Terima kasih banyak."
            anna "Sama-sama."

    "Aku keluar dari lab GIGA dengan kepala penuh informbai baru. Grafika, Interaksi, Game, dan Analitik. Lumayan banyak yang bisa dipelajari di situ."

    return

label visit_giga_state.revisit:
    show anna neutral at character_center
    "Aku kembali ke lab GIGA. Anna melambaikan tangan saat melihatku masuk."
    anna "Oh, balik lagi. Ada yang mau ditanyain?"

    menu:
        "Tanyakan tentang pilar-pilar GIGA lagi":
            aku "Mba, bisa minta penjelasan lagi soal pilar-pilar GIGA? Aku mau dengerin ulang."
            anna "Tentu. Grafika itu tentang computer graphics, visualisasi, dan rendering — bagaimana komputer menghasilkan gambar dan animasi."
            anna "Interaksi fokusnya ke UI/UX. Bagaimana desain antarmuka yang intuitif dan nyaman dipakai oleh pengguna."
            anna "Game itu pengembangan game, dari desain mekanik, game engine, sampai implementasinya."
            anna "Dan Analitik menyentuh algoritma dan AI, lebih ke sisi analisis data dan kecerdasan komputasional."
            aku "Jadi GIGA itu Grafika, Interaksi, Game, Analitik. Sudah mulai hafal."
            anna "Tepat. Dan keempat pilar itu saling melengkapi, bukan berdiri sendiri-sendiri."
            aku "Oke, makasih lagi ya mba."
            anna "Sama-sama. Kalau mau mampir lagi, jangan sungkan."

        "Keluar lab":
            aku "Nggak ada, mba. Makasih. Aku duluan ya."
            anna "Oke, hati-hati."

    return
