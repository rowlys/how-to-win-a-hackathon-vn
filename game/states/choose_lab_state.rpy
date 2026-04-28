label choose_lab_state:
    "Aku sudah mengunjungi ketiga lab. Saatnya memutuskan."

    menu:
        "'Lab mana yang akan aku pilih untuk mengerjakan hackathon ini?'"

        "Lab RPL": # Benar kalau pilih proyek software keuangan
            $ chosen_lab = "rpl"
            if project_idea == "software":
                "'Lab software untuk proyek software. Masuk akal banget.'"
            elif project_idea == "ai":
                "'RPL punya setup yang solid. Meski adminnya sempat menyarankan KCV, tapi aku rasa RPL juga bisa.'"
            else:
                "'Mereka punya proses yang terstruktur. Harusnya cocok buat kita.'"

        "Lab KCV": #Benar kalau pilih proyek AI
            $ chosen_lab = "kcv"
            if project_idea == "ai":
                "'KCV sudah jelas pilihannya. Proyek AI di lab AI — paling logis.'" 
            elif project_idea == "game":
                "'Analytics pillar-nya bisa berguna buat beberapa aspek game yang aku rencanain.'"
            else:
                "'Tools mereka keliatan powerful. Bisa kita manfaatin.'"

        "Lab GIGA": # Benar kalau pilih proyek Game
            $ chosen_lab = "giga"
            if project_idea == "game":
                "'Game project di lab game. Nggak ada yang lebih simpel dari itu.'"
            elif project_idea == "software":
                "'Interaction pillar-nya menarik. UI/UX yang bagus bisa jadi nilai plus.'"
            else:
                "'Mereka juga punya analytics. Harusnya cukup buat kebutuhan proyek kita.'"

 
    "Aku menarik napas panjang."
    "'Oke. Keputusan sudah dibuat.'"

    scene black with dissolve
    pause 1.5

    "Sore itu aku pulang dengan kepala penuh rencana."
    "'Besok, aku harus mulai cari rekan tim. Nggak mungkin ngerjain ini sendirian.'"

    "Hari berikutnya..."

    $ current_state = State.ASSEMBLE_TEAM
    return
