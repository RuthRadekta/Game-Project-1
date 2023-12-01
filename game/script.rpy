# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Guru = Character('Guru', color="#E03B8B")
define Suma = Character('Suma', color="#508D69")
define Stefan = Character('Stefan', color="#F3B664")
define Mbah = Character('Mbah', color="#872341")
define Kakek = Character('Kakek')
#image opening = "..."

#define sm = Character("Suma", image = "suma")

#image suma:
#    "side kusuma_restFace.png"

# The game starts here.

label splashscreen:
    scene black
    with Pause(1)

    show text "WELCOME TO THE PAST" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    $ renpy.movie_cutscene('flash.webm')
    scene fadeout white 0.5

    return

label start:
    centered "{color=#FFFFFF}(Bel pulang sekolah berbunyi){/color}"
    #play suara bel

label scene1:
    scene fadein 0.5
    scene ruangkelas_now
    #play suara riuh di kelas
    centered "{color=#FFFFFF}(Suara riuh di kelas){/color}"
    centered '{color=#FFF5C2}"Eh kata Pak Retno ulangan sejarah kapan?"{/color}'
    centered '{color=#FFF5C2}"Besok banget tuh"{/color}'
    show kusuma_suprisedface at left
    Suma "Huh?"
    Suma "(Menghela napas)"

label scene2:
    show kusuma_restface at left
    Suma "(Berjalan pulang dengan kesal)"
    Suma "Kenapa sih sejarah sok keras banget?"
    Suma "Toh, Sejarah kan yang penting tahu, "
    extend "gak harus WAJIB kek gini "
    extend "Ribet banget..."
    Suma "Mana pake ulangan segala lagi. "
    extend "Dikira mapel yang harus dipikir ini doang? "
    scene fadeout 1.5

label scene3:
    scene kamar suma 
    with fade
    centered "{color=#FFFFFF}(Sesampainya di rumah...){/color}"
    show kusuma_restface at left
    Suma "Ngantuk... "
    hide kusuma_restFace
    extend "Pen tidur..."
    scene fadeout 3.5

label scene4:
    scene kamar lama
    with fade
    show torasumaji_restFace at left
    Suma "Loh? "
    extend "(Melihat sekitar) "
    extend "Kamar siapa ini? "
    centered "Le, ijek durung tangi to? "
    hide torasumaji_restFace
    show torasumaji_suprisedface at left
    Suma "(Mendengar sesuatu) "
    extend "Huh? "
    extend "Ada orang jawa?! "
    Suma "Siapa?! "
    extend "Ayah ya? "
    extend "Tapi kok berat gitu... "
    centered "(Mbah Seno masuk ke kamar Suma dan berkacak pinggang)"
    Mbah "Le, le... turu teros! "
    extend "(Berjalan mendekati Suma) "
    show torasumaji_suprisedface at left
    Suma "(Membatin) Huh? "
    extend "Mbah Seno! "
    extend "Kok hidup lagi?! "
    Mbah "(Menepuk pipi Suma) "
    extend "Ngopo to koe ki? "
    extend "Ndang tangi, ngewangi simbah! "
    Mbah "(Lalu keluar dari kamar Suma) "
    Suma "(Kaget, tapi langsung nyusul)"
    scene fadeout 0.5

label scene5:
    hide torasumaji_suprisedface at left
    centered "entar nunjukin sekeliling rumah, kira-kira 4 gambar"
    centered "(Suma sampai halaman depan)"
    centered "entar nunjukin mbah seno yg berdiri dengan caping kepala dan bbrp peralatan berkebun"
    Mbah "Ayo! Gek ndang mangkat!"
    show torasumaji_suprisedface at left
    Suma "M-mau kemana mbah?"
    Mbah "Yo nyang ngendi neh? Sawah lah!"
    Suma "..."
    Suma "Ngapain ke sawah?"
    Mbah "Bosomu aneh"
    extend ". Pokoke awakdewe bakal noto sawah. "
    extend "(Melirik Suma) "
    extend "Lak takon neh"
    Suma "(Terkekeh malu)"
    extend "Anu, Mbah... "
    extend "Sebenarnya aku gak paham sama maksud mbah, "
    extend "noto sawah itu apa ya, Mbah?"
    Mbah "(entar nunjukin muka kaget atau sejenisnya)"
    Mbah "Ngene lho, le. "
    extend "Keluargane awakdewe kan nduwe sawah, makane kui awakdewe kudu njogo. "
    extend "Kui sawah iso dadi sumber awakdewe urip karo dadi lapang kerjane masyarakat kampung"
    Mbah "(Melihat Suma dengan curiga)"
    Mbah "Biasane yo ngene ki lho, le. Kok koe dadi aneh men to?"
    hide torasumaji_suprisedface
    show torasumaji_restFace at left
    Suma "(Menceritakan semua yang telah terjadi)"
    centered "..."
    Mbah "(Tertawa kecil) "
    extend "Lah... pantes kok bedo. Jebule koe cicitku to"
    Suma "(Tertawa canggung)"
    Mbah "(Berhenti tertawa)"
    Mbah "Yowes, tetep kerjo. Ayo!"
    scene fadeout 0.5

label scene6:
    

label bgm:
    #play music "audio/suma_theme.mp3" fadein 1.0 volume 10
    show torasumaji_suprisedface at left
    Suma "Buset? Londo!"

    hide torasumaji_suprisedface

    show stefan_restface at left
    Stefan "Huh?"

    hide stefan_restface
    
label sfx:

label choices:
    #default learned = False
    show torasumaji_suprisedface at left
    Suma "Dee londo kan ya?"
    menu:
        "Hoo":
            jump hoo
        "Lah embuh":
            jump embuh

label hoo:
    hide torasumaji_suprisedface
    show stefan_giggleface at left
    Stefan "Apa itu 'Londo'?"
    jump lanjutan_hoo

label lanjutan_hoo:
    Suma "..."
    scene black
    jump end

label embuh:
    hide torasumaji_suprisedface
    show stefan_restface at left
    Stefan "Embuh? Apa itu 'embuh'?"
    jump lanjutan_embuh

label lanjutan_embuh:
    Suma "(His jaw dropped)"
    scene black
    jump end

label end:
    #with fade
    $renpy.full_restart()
    return

    

    return
