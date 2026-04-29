label start_state:
    play music "music/vntrack01.mp3" fadein 1 volume 0.5
    scene bg phone_poster with fade
    "Aku menatap poster hackathon yang ditampilkan pada HP ku."
    "Sudah lama sekali aku menunggu kesempatan untuk mengikuti sebuah hackathon, dan sekarang kesempatan itu datang."
    "Untungnya, perkuliahanku sekarang sedang renggang, jadi cukup banyak waktu untuk mempersiapkan diri."
    "'Duh, tapi aku belum punya ide proyek apa yang akan aku buat.'"
    "'Hmm...'"
    "'Proyek apa ya yang kira-kira bisa menangin hackathon ini?'"
    $ current_state = State.CHOOSE_PROJECT
    return