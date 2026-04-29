label recruit_giga_state:
    scene bg giga with dissolve

    if "giga" not in visited_recruitment_locations:
        $ visited_recruitment_locations.add("giga")
        call recruit_giga_state.first_visit from _call_recruit_giga_state_first_visit
    else:
        call recruit_giga_state.revisit from _call_recruit_giga_state_revisit

    $ current_state = State.ASSEMBLE_TEAM
    return


label recruit_giga_state.first_visit:
    "Aku masuk ke Lab GIGA, dan langsung mengenali sosok yang sedang duduk di pojok ruangan."
    "'Eh, itu Arif!'"

    "Arif adalah teman sekelasku. Aku tau dia sering ngabisin waktu di sekitar sini, tapi nggak nyangka bakal ketemu dia pas lagi nyari-nyari orang."
    "Aku berjalan ke arahnya. Arif mendongak dari laptopnya dan langsung nyengir."

    show arif neutral at character_center
    arif "Eh, tumben nongol sini! Lagi ngapain?"
    aku "Lagi nyari-nyari orang buat diajak gabung di tim hackathon. Kamu sendiri ngapain di sini?"
    arif "Biasalah, ngerjain tugas desain. Lab ini enak, vibes-nya bagus."
    arif "Eh tapi serius, kamu mau ikut hackathon?"

    aku "Iya, serius. Ide proyeknya udah ada, labnya udah ketemu. Cuma masih butuh tim."
    arif "Wah, kamu udah sejauh itu? Baru tau nih aku."
    aku "Makanya aku ke sini. Kamu mau gabung ga?"

    arif "Hmm. Proyek kamu tentang apa emangnya?"

    if project_idea == "ai":
        aku "Proyekku itu ngebuat aplikasi image processing buat deteksi penyakit tanaman."
        arif "Oh, yang teknis banget ya. Interesting."
    elif project_idea == "game":
        aku "Proyekku itu ngebuat game simulasi edukasional."
        arif "Ooh, ada unsur desain dong pastinya."
    elif project_idea == "software":
        aku "Proyekku itu ngebuat aplikasi manajemen keuangan untuk mahasiswa."
        arif "Aplikasi ya. Pasti butuh tampilan yang bagus biar enak dipake."

    arif "Boleh-boleh. Tapi kamu yakin nggak, kalau keahlianku itu nyambung sama yang kamu butuhin?"
    aku "Makanya aku mau nanya dulu. Keahlian kamu ke arah mana sebenernya, Rif?"
    arif "Aku lebih ke desain sih. Ke arah User Interface sama User Experience. Gimana bikin tampilan yang nggak cuma cakep, tapi juga enak dan intuitif buat dipake."
    arif "Dari riset pengguna, wireframe, prototyping, sampai evaluasi desainnya. Itu yang aku kerjain."

    arif "Eh, tapi sebelum kamu mutusin — aku penasaran nih. Kalau kamu mau ngajak aku, harusnya kamu ngerti dong kerjaan aku."
    arif "Menurut kamu, apa tujuan utama dari UX design?"

    "'Hmm... UX design. Aku coba nginget-nginget pelajaran yang pernah lewat. Dari kelas sama workshop yang pernah ku ikutin."
    "'UX itu singkatan dari User Experience, yang artinya'pengalaman pengguna'. Jadi bukan cuma soal tampilannya yang cakep.'"
    "'Bukan sekadar bikin visual aplikasi, tapi seberapa mudah, nyaman, dan bermakna produk itu buat dipake.'"
    "'Yang ditekanin itu kata 'Experience'-nya. Keseluruhan perasaan dan interaksi pengguna sama produk.'"
    "'Oke, kayaknya aku ngerti arahnya. Jawaban yang bener pasti yang paling dekat sama konsep 'pengalaman' itu.'"

    hide arif
    menu:
        "Membuat tampilan aplikasi semenarik mungkin secara visual.":
            show arif neutral at character_center
            arif "Hmm, kalau untuk tampilan menarik itu lebih ke UI. UX itu cakupannya jauh lebih luas dari sekadar estetika."
            "Arif kembali ke laptopnya. Sepertinya aku harus belajar lebih dulu sebelum balik ke sini."
            arif "Kayaknya kamu belum bener-bener ngerti bidang aku. Aku nggak yakin kita bakal cocok di tim yang sama."
            "'Sepertinya aku harus coba lagi nanti.'"
            aku "Duh, oke. Untuk sekarang, aku pamit dulu ya, Rif."
            return

        "Merancang pengalaman pengguna yang mudah, nyaman, dan bermakna.":
            show arif neutral at character_center
            $ arif_pass = True
            arif "Nah, tepat! UX itu emang soal keseluruhan pengalaman pengguna, bukan cuma soal cakepnya tampilan."
            arif "Oke, kamu ngerti kerjaan aku. Jadi kamu emang butuh orang kayak aku dong di proyekmu?"

        "Menulis kode untuk mengoptimalkan performa aplikasi.":
            show arif neutral at character_center
            arif "Itu kerjaan developer, bukan desainer. Kayaknya kamu belum paham bidang aku sama sekali."
            arif "Cari tau dulu deh sebelum ngajak orang. Aku tunggu kalau kamu udah siap."
            "Arif kembali ke laptopnya. Aku harus belajar lebih dulu."
            "'Sepertinya aku harus coba lagi nanti.'"
            aku "Duh, oke. Untuk sekarang, aku pamit dulu ya, Rif."
            return

        "Mengatur alur logika dan sistem di balik antarmuka.":
            show arif neutral at character_center
            arif "Hmm, itu lebih ke ranah system design atau information architecture."
            arif "Pemahamanmu soal UX masih kurang, kayaknya. Kita ngobrol lagi kalau kamu udah lebih paham ya."
            "Arif kembali ke laptopnya."
            "'Sepertinya aku harus coba lagi nanti.'"
            aku "Duh, oke. Untuk sekarang, aku pamit dulu ya, Rif."
            return

    call recruit_giga_state.recruit_arif from _call_recruit_giga_state_recruit_arif
    return


label recruit_giga_state.revisit:
    show arif neutral at character_center
    "Aku kembali ke Lab GIGA. Arif masih di tempat yang sama, langsung melirik ke arahku."
    arif "Eh, balik lagi. Udah ada keputusan?"
    aku "Belum. Aku mau nanya lagi soal keahlian kamu, boleh?"
    arif "Boleh. Singkatnya, aku di UI/UX — desain tampilan yang enak dan intuitif. Dari riset pengguna, wireframe, sampai prototyping."
    arif "Kalau proyekmu butuh orang yang mikirin sisi desain dan pengalaman penggunanya, itu aku."

    arif "Tapi sebelum kamu jawab — tadi aku sempet kepikiran satu hal."
    arif "Biar aku tau kamu serius, jawab dulu: apa tujuan utama dari UX design?"

    if not arif_pass:
        "Hmm, pertanyaan yang sama. Aku udah lebih siap sekarang."
        "UX — User Experience. Intinya bukan soal visualnya yang bagus, tapi soal keseluruhan pengalaman pengguna."
        "Mudah dipake, nyaman, dan bermakna. Itu yang dicari dari UX yang baik."
        "Aku nggak boleh salah kali ini."

        hide arif
        menu:
            "Membuat tampilan aplikasi semenarik mungkin secara visual.":
                show arif neutral at character_center
                arif "Masih belum bener. Itu UI, bukan UX. Beda ya konsepnya."
                arif "Aku rasa kamu perlu baca-baca dulu soal ini. Kabarin aku kalau udah siap."
                "Aku mengangkat tangan pamit ke Arif."
                "Sepertinya aku harus coba lagi nanti."
                return

            "Merancang pengalaman pengguna yang mudah, nyaman, dan bermakna.":
                show arif neutral at character_center
                arif "Nah, bener! Itu dia intinya."
                arif "Oke, jadi gimana? Masih butuh orang kayak aku di timmu?"

            "Menulis kode untuk mengoptimalkan performa aplikasi.":
                show arif neutral at character_center
                arif "Itu kerjaan developer. Jauh dari UX."
                arif "Pelajarin dulu deh bidangku sebelum balik lagi."
                "Aku mengangkat tangan pamit ke Arif."
                "Sepertinya aku harus coba lagi nanti."
                return

            "Mengatur alur logika dan sistem di balik antarmuka.":
                show arif neutral at character_center
                arif "Masih melenceng. Itu lebih ke system design."
                arif "Kalau udah lebih paham, balik lagi ya."
                "Aku mengangkat tangan pamit ke Arif."
                "Sepertinya aku harus coba lagi nanti."
                return

    call recruit_giga_state.recruit_arif from _call_recruit_giga_state_recruit_arif_1
    return


label recruit_giga_state.recruit_arif:
    hide arif
    menu:
        "'Butuh banget, Rif.'":
            show arif neutral at character_center
            $ recruited_students.add("arif")
            aku "Butuh banget! Siapa yang mau pake aplikasi kalau tampilannya nggak enak, kan?"
            arif "Nah, bener. Oke deh, aku masuk."
            aku "Serius? Makasih banyak ya, Rif!"
            arif "Santai aja. Lumayan buat pengalaman, daripada di sini sendirian ngerjain tugas mulu."

            "Dengan begitu, aku berhasil mengajak Arif untuk bergabung di timku!"
            return

        "'Hmm, aku pikirin dulu.'":
            show arif neutral at character_center
            aku "Hmm, sebenarnya aku masih belum yakin sih proyekku perlu UI/UX yang bagus banget apa ga."
            arif "Oh, oke. Santai, nggak masalah. Pikirin aja dulu."
            aku "Iya, mungkin aku cari-cari yang lain dulu ya, Rif."
            arif "Siap. Kalau udah ada keputusan, kabarin aku aja."

            "Aku mengangkat tangan pamit ke Arif dan melanjutkan pencarianku."
            return
