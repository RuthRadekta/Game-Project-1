# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Guru = Character('Guru', color="#E03B8B")
define Suma = Character('Suma', color="#86A789")
define Stefan = Character('Suma', color="#FFE17B")

# The game starts here.

label start:
    "(Bel pulang sekolah berbunyi)"
    "(Suara riuh di kelas)"
    "Guru" "Besok ulangan. Yeee~"

label sprites:
    "Huh?"
    show kusuma_suprisedface
    "Suma" "(Menghela napas)"
    show kusuma_restface
    "Suma" "Dih, males."

label character:

label background:
    scene kamar suma 
    with fade
    show kusuma_restface
    "Suma" "Mending turu."
    scene fadeout 0.5

label bgm:
    #play music "audio/suma_theme.mp3" fadein 1.0 volume 10
    show torasumaji_suprisedface
    "Suma" "Buset? Londo!"

    show stefan_restface at right
    "Stefan" "Huh?"

    hide stefan_restface
    
label sfx:

label choices:
    #default learned = False
    "Suma" "Dee londo kan ya?"
    menu:
        "Hoo":
            jump hoo
        "Lah embuh":
            jump embuh

label hoo:
    hide torasumaji_suprisedface
    show stefan_giggleface
    "Stefan" "Apa itu 'Londo'?"
    jump lanjutan_hoo

label embuh:
    hide torasumaji_suprisedface
    show stefan_restface
    "Stefan" "Embuh? Apa itu 'embuh'?"
    jump lanjutan_embuh

label lanjutan_hoo:
    "Suma" "..."
    #$ learned = True

label lanjutan_embuh:
    "Suma" "(His jaw dropped)"
    #$ learned = False

#label result:
    #if learned:
        #"Narator" "Tamat"
    #else:
        #"Narator" "Cari google: apa itu embuh?"

    

    return
