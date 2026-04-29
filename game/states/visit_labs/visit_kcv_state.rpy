label visit_kcv_state:
    scene bg kcv with dissolve
    if "kcv" not in visited_labs:
        $ visited_labs.add("kcv")
        call visit_kcv_state.first_visit from _call_visit_kcv_state_first_visit
    else:
        call visit_kcv_state.revisit from _call_visit_kcv_state_revisit

    $ current_state = State.HUB_EXPLORE
    return


label visit_kcv_state.first_visit:
    "Aku berjalan menuju lab yang letaknya di sebelah Laboratorium Pemrograman, dan menemukan papan nama bertuliskan \"Laboratorium Komputasi Cerdas dan Visi\"."
    "Aku masuk ke dalamnya. Suasananya cukup serius, tetapi tenang. Mungkin karena ukuran ruangannya yang tidak terlalu besar."
    "Beberapa mahasiswa tampak fokus menatap layar mereka, sebagian menampilkan grafik-grafik dan visualisasi data yang asing bagiku."

    "Seorang mahasiswa yang duduk di dekat pintu menoleh ke arahku."

    show steven neutral at character_center
    admin_kcv "Halo, nyasar, atau emang sengaja ke sini?"
    aku "Haha, sengaja, mas. Aku mahasiswa baru, lagi keliling untuk belajar tentang lab-lab di TC."
    admin_kcv "Oh, bagus dong. Jarang ada yang mau keliling lab sendiri gini. Salam kenal dong, namaku Steven."
    steven "Oke, kamu kepingin belajar tentang lab-lab TC, ya? Kalau nama lab ini tau ga?"
    aku "KCV, mas. Komputasi Cerdas dan... Visi? Aku masih kurang paham sih maksudnya apa."
    steven "Iya, benar. Komputasi Cerdas dan Visi. Dua bidang besar yang jadi fokus lab ini."
    aku "Kedengarannya canggih banget, mas."
    steven "Hahaha, emang canggih. Tapi bisa dipelajari kok, pelan-pelan."
    steven "Ngomong-ngomong, ada keperluan khusus ke sini, atau emang keliling aja?"

    if project_idea == "ai":
        aku "Ada sih, mas. Aku lagi nyari lab yang cocok buat ngerjain proyek hackathon. Proyekku tentang image processing buat deteksi penyakit tanaman."
        steven "Wah, kamu udah ketemu tempat yang paling tepat. Image processing dan computer vision itu persis spesialisasi lab ini. Komputer di sini juga biasa dipake buat training model, jadi speknya lumayan."
        aku "Serius mas? Wah, kebetulan banget kalau gitu."
        steven "Kebetulan yang bagus. Kalau mau tau lebih lanjut soal lab ini, tanya aja."

    elif project_idea == "game":
        aku "Ada sih, mas. Aku lagi nyari lab yang cocok buat ngerjain proyek hackathon. Proyekku tentang game edukasi."
        steven "Oh, game. Untuk pengembangan game, mungkin lab lain lebih cocok. Tapi kalau game-mu butuh elemen AI, kayak NPC yang cerdas atau sistem adaptif, itu nyambung sama yang kita kerjain di sini."

    elif project_idea == "software":
        aku "Ada sih, mas. Aku lagi nyari lab yang cocok buat ngerjain proyek hackathon. Proyekku tentang aplikasi manajemen keuangan."
        steven "Oh, lebih ke software ya. Kalau untuk software umum, ada lab lain yang lebih pas spesialisasinya. Tapi kalau aplikasimu mau tambahin fitur analitik atau prediksi keuangan berbasis data, itu bisa nyerempet ke bidang kita kok."

    menu:
        "Tanyakan tentang spesialisasi lab ini lebih lanjut":
    
            aku "Mas, bisa cerita lebih lengkap soal bidang-bidang yang dipelajari di lab ini?"
            steven "Tentu. Jadi ada dua sisi besar di sini. Sisi 'Komputasi Cerdas' dan sisi 'Visi'."
            steven "Di sisi Komputasi Cerdas, kita bicara soal AI secara umum, computational intelligence, dan data mining. Intinya bagaimana komputer bisa belajar dari data dan mengambil keputusan yang cerdas."
            steven "Computational intelligence itu cakupannya luas, termasuk algoritma yang terinspirasi dari alam, seperti algoritma genetika atau neural network generasi awal."
            steven "Data mining itu seni menemukan pola tersembunyi dari data yang besar. Kelihatannya sederhana, tapi kalau datanya jutaan baris, kamu butuh teknik khusus buat itu."
            aku "Dan sisi 'Visi' itu maksudnya?"
            steven "Itu computer vision dan digital image processing. Singkatnya, bagaimana komputer bisa 'melihat' dan memahami gambar atau video."
            steven "Image processing itu tentang memanipulasi gambar secara digital, misalnya menghilangkan noise, memperjelas tepi objek, atau mengubah format. Ini dasarnya."
            steven "Computer vision itu selangkah lebih jauh. Bukan cuma manipulasi gambar, tapi interpretasi. Komputer bisa mengenali wajah, mendeteksi objek, bahkan memahami gerakan."
            steven "Dan sekarang dua sisi itu makin menyatu lewat deep learning. Neural network dalam dengan banyak layer bisa sekaligus memproses dan menginterpretasi gambar dengan akurasi yang sangat tinggi."
            aku "Jadi deep learning itu seperti jembatan antara komputasi cerdas dan visi komputer ya mas?"
            steven "Bisa dibilang begitu. Deep learning sekarang jadi tulang punggung sebagian besar kemajuan di kedua bidang itu."
            aku "Wah, aku jadi makin tertarik. Makasih banyak ya mas penjelasannya."
            steven "Sama-sama. Kalau mau tanya lebih lanjut atau butuh referensi belajar, mampir lagi aja."

        "Keluar lab":
    
            aku "Wah, menarik banget mas. Baik, aku coba ke lab lain juga dulu ya mas. Terima kasih penjelasannya."
            steven "Sama-sama. Jangan sungkan buat balik lagi kalau mau tanya lebih lanjut ya."

    "Aku keluar dari lab KCV dengan banyak istilah baru di kepala. AI, data mining, computer vision, deep learning — ternyata satu lab bisa mencakup sebanyak itu."

    return

label visit_kcv_state.revisit:
    show steven neutral at character_center
    "Aku kembali ke lab KCV. Steven menoleh saat mendengar pintu terbuka."
    steven "Oh, balik lagi. Ada yang bisa aku bantu?"

    menu:
        "Tanyakan tentang spesialisasi lab ini lagi":
    
            aku "Mas, bisa minta penjelasan lagi soal bidang-bidang yang dipelajari di sini?"
            steven "Tentu. Jadi ada dua sisi besar di sini. Sisi 'Komputasi Cerdas' dan sisi 'Visi'."
            steven "Di sisi Komputasi Cerdas, kita bicara soal AI secara umum, computational intelligence, dan data mining. Intinya bagaimana komputer bisa belajar dari data dan mengambil keputusan yang cerdas."
            steven "Computational intelligence itu cakupannya luas, termasuk algoritma yang terinspirasi dari alam, seperti algoritma genetika atau neural network generasi awal."
            steven "Data mining itu seni menemukan pola tersembunyi dari data yang besar. Kelihatannya sederhana, tapi kalau datanya jutaan baris, kamu butuh teknik khusus buat itu."
            aku "Dan sisi 'Visi' itu maksudnya?"
            steven "Itu computer vision dan digital image processing. Bagaimana komputer bisa 'melihat' dan memahami gambar atau video."
            steven "Image processing itu tentang memanipulasi gambar secara digital, misalnya menghilangkan noise, memperjelas tepi objek, atau mengubah format."
            steven "Computer vision itu selangkah lebih jauh — bukan cuma manipulasi gambar, tapi interpretasi. Komputer bisa mengenali wajah, mendeteksi objek, bahkan memahami gerakan."
            steven "Dan dua sisi itu makin menyatu lewat deep learning. Neural network dalam dengan banyak layer bisa sekaligus memproses dan menginterpretasi gambar dengan akurasi yang sangat tinggi."
            aku "Oke, makasih lagi mas."
            steven "Sama-sama. Jangan sungkan kalau mau tanya lagi."

        "Keluar lab":
    
            aku "Nggak ada, mas. Makasih. Aku duluan ya."
            steven "Oke, hati-hati."

    return
