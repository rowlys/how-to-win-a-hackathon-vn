label hub_explore_state:
    scene bg hub with dissolve

    if first_visit_hub:
        "Aku sekarang berada di lantai 3. Di sini terdapat 8 lab yang bisa dimanfaatkan mahasiswa."
        "'Seperti untuk menggunakan komputernya demi mengerjakan proyek hackathon,' aku tersenyum."
        $ first_visit_hub = False

    menu:
        "'Aku kunjungin lab yang mana dulu ya?'"

        "[lab_rpl_label()]":
            $ current_state = State.VISIT_RPL

        "[lab_kcv_label()]":
            $ current_state = State.VISIT_KCV

        "[lab_giga_label()]":
            $ current_state = State.VISIT_GIGA

        # "Lab 4":

        # "Lab 5":

        # "Lab 6":

        # "Lab 7":

        # "Lab 8":

        "Sepertinya sudah cukup. Saatnya memilih lab." if {"rpl", "kcv", "giga"}.issubset(visited_labs):
            $ current_state = State.CHOOSE_LAB

    return
