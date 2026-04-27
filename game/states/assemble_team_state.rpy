label assemble_team_state:
    if first_assemble_team:
        "Aku kembali ke Gedung Informatika."
        "'Aku udah ada ide proyeknya. Terus sekarang aku sudah tau mau pake lab apa untuk ngerjainnya. Tapi aku masih butuh tim buat ngerjainnya.'"
        "'Aku harus cari temen buat ngerjain proyek ini bareng-bareng. Mungkin temen-temenku yang lagi di TC bisa aku ajak...'"
        "'Atau mungkin bahkan admin-admin lab yang aku temui kemarin? Mereka keliatan asik dan pinter-pinter, siapa tau mereka mau bantuin aku buat ngerjain proyek ini.'"
        "'Syarat dari hackathon ini juga setiap tim maksimal terdiri dari 4 orang, jadi aku harus cari 3 orang lagi buat jadi tim aku.'"
        "'Aku harus mencari orang yang benar untuk direkrut, sesuai dengan kebutuhan proyekku.'"

        if project_idea == "ai":
            "'Proyek ku adalah aplikasi image processing deteksi penyakit tanaman.'"
            "'Kira-kira aku butuh orang yang paham tentang apa saja ya...'"
            "'Aplikasi ini yang pasti perlu yang jago soal machine learning, terus juga perlu nyimpen banyak data gambar yang bisa dipake buat training."
            "'Kalau untuk desain visual, mungkin ga terlalu butuh yang jago. Aku bisa handle sendiri.'"

        elif project_idea == "game":
            "'Aku butuh orang yang punya pengalaman dengan game development, terutama yang ngerti tentang game engine dan desain game. Lab GIGA sepertinya tempat yang tepat buat cari orang kayak gitu.'"
        elif project_idea == "software":
            "'Aku butuh orang yang punya pengalaman dengan software development, terutama yang ngerti tentang aplikasi manajemen keuangan. Lab RPL mungkin tempat yang tepat buat cari orang kayak gitu.'"

    "Coba cari orang di mana ya?"

    menu:
        "Lab RPL":
            $ current_state = State.RECRUIT_RPL

        "Lab KCV":
            $ current_state = State.RECRUIT_KCV

        "Lab GIGA":
            $ current_state = State.RECRUIT_GIGA

        "Plasa":
            $ current_state = State.RECRUIT_PLASA

        "Kelas 105":
            $ current_state = State.RECRUIT_105

        "Coba keliling koridor":
            $ current_state = State.RECRUIT_KORIDOR

    return
