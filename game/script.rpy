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
    show normal at left
    Suma "Loh? "
    extend "(Melihat sekitar) "
    extend "Kamar siapa ini? "
    centered "Le, ijek durung tangi to? "
    hide normal
    show kaget at left
    Suma "(Mendengar sesuatu) "
    extend "Huh? "
    extend "Ada orang jawa?! "
    Suma "Siapa?! "
    extend "Ayah ya? "
    extend "Tapi kok berat gitu... "
    centered "(Mbah Seno masuk ke kamar Suma dan berkacak pinggang)"
    Mbah "Le, le... turu teros! "
    extend "(Berjalan mendekati Suma) "
    show kaget at left
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
    hide kaget
    centered "entar nunjukin sekeliling rumah, kira-kira 4 gambar"
    centered "(Suma sampai halaman depan)"
    centered "entar nunjukin mbah seno yg berdiri dengan caping kepala dan bbrp peralatan berkebun"
    Mbah "Ayo! Gek ndang mangkat!"
    show kaget at left
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
    hide kaget
    show normal at left
    Suma "(Menceritakan semua yang telah terjadi)"
    centered "..."
    Mbah "(Tertawa kecil) "
    extend "Lah... pantes kok bedo. Jebule koe cicitku to"
    Suma "(Tertawa canggung)"
    Mbah "(Berhenti tertawa)"
    Mbah "Yowes, tetep kerjo. Ayo!"
    hide normal
    scene fadeout 0.5

label scene6:
    centered "entar nampilin hamparan sawah hijau yang membentang"
    centered "terus nampilin petani yang lagi bekerja di sawah"    
    show normal at left
    Suma "Mbah, apa yang harus aku lakukan di sini?"
    hide normal
    Mbah "(Tersenyum)"
    Mbah "Yo seko kene ki, le. Lapang kerja masyarakat kampung, panggon kanggo wong-wong desa kerjo ning kene, garap sawah iki."
    extend " Iki yo bagian sekolah adat Jawa sing kudu koe reti, le. Koe bakal sinau cara garap sawah,"
    extend " nah seko kono koe bakal paham artine kerja keras karo gotong royong."
    Mbah "Kan yo manungsa urip gelem ra gelem akhire bakal bersosialisasi. Dadi ojo opo-opo ngeroso iso dewe ya, le."
    extend " Saiki, yoh mulai garap."
    show normal at left
    Suma "(Sedikit ragu, tetapi dia tetap mencoba beradaptasi dengan situasi yang dihadapi.)"
    centered "Selama mereka bekerja, Mbah Seno menceritakan kisah-kisah tentang masa lalu bagaimana Belanda datang ke Indonesia dan perjuangan rakyat Indonesia saat melawan penjajahan Belanda."
    centered "Suma mendengarkan dengan penuh perhatian"
    hide normal

    # sesi kuis
    # pertanyaan nih
    Mbah "Pie, Le? Wes paham?"
    menu:
        "Udah, mbah" :
            jump berikutnya
        "Belum..." :
            jump ulang 

    label berikutnya:
        Mbah "Yowes sip"
        jump scene7
    
    label ulang:
        Mbah "Waduh."
        Mbah "Dengerno ya, Le... "
        extend "Jadi intinya kamu harus mau bersosialisasi. Bukan masalah bakal menyebabkan ketergantungan..."
        Mbah "Tapi, "
        extend "begitulah cara manusia hidup. "
        extend "Saling tolong0-menolong dan gotong royong..."
        jump scene7

label scene7:
    centered "Setelah beberapa jam bekerja di sawah, Suma paham apa yang dimaksud Mbah Seno."
    centered "Selain itu, mereka mulai akrab layaknya keluarga."
    Mbah "Bagus, le. Kau telah belajar banyak hari ini."
    Mbah "Ini adalah langkah awal dalam perjalananmu untuk memahami sejarah dan budaya kita. "
    extend "Ingatlah, kita harus menghargai warisan nenek moyang kita dan belajar dari mereka."
    Suma "(Mengangguk paham)"
    Suma "Terima kasih, Mbah. Aku akan mencoba yang terbaik."
    Mbah "(Mengangkat sebelah alisnya)" 
    extend "Sampai kapan kau akan tinggal di sini, le?"
    Suma "Aku belum tahu, Mbah... "
    extend "(Tersenyum) "
    extend "Tapi sepertinya aku bakal betah di sini"
    Mbah "(Tersenyum kembali)" 
    Mbah "Yowes, le. Ayo bali. Kita masih punya banyak yang harus kau pelajari."  
    centered "Mereka berdua meninggalkan sawah dan kembali ke rumah yang jauh berbeda dari rumah Suma di masa kini."
    scene fadeout 0.5
    Suma "Siapa tuh, mbah?"
    extend "(tanya Suma penasaran saat ada pemuda yang menyapa mbah Seno saat hendak masuk ke halaman rumahnya)"
    Mbah "Oh.. jenenge Sutan Syahrir. "
    extend "Tapi biasane aku nyeluk ‘Si Kancil’ "
    Suma "... (gak paham bahasa jawa)"
    Mbah "(Tertawa melihat wajah bingung Suma)"
    Mbah "Maksudnya, nama orang itu Sutan Syahrir. Tapi mbah biasanya manggil ‘Si Kancil’, paham?"
    Suma "Oh..."
    extend "Terus beliau mau pergi kemana itu, mbah?"
    Mbah "Rumahnya lah."
    Mbah "Katanya habis datang dari Konferensi Rijswijk yang berlangsung pada tahun ini, 1939. "
    extend "Tujuannya untuk membahas masalah dan perselisihan antara pemerintah kolonial Belanda dan para pemimpin Indonesia."
    Mbah "Masalah utama yang dibahas termasuk otonomi ekonomi untuk Hindia Belanda, peningkatan status politik, dan kemerdekaan."
    Mbah "Pemimpin konferensi ini ya Si Kancil, tapi di didampingi Tjarda van Starkenborgh, gubernur jendral dari Belanda."
    Mbah "Tapi katanya hasil konferensi ini belum mencapai kesepakatan konkret. "
    extend "Alhasil, kontrol Belanda di Indonesia masih erat dan pokoke waspada ae ya, le."
    Suma "(Mengangguk)"
    Mbah "(Duduk di teras setelah cuci kaki dan tangan)"
    Mbah "Oiyo le, rene sek."
    Suma "(Duduk di sebelahnya) Ya, mbah?"
    Mbah "Mbah sudah cerita tentang Pangeran Diponegoro belum to?"
    Suma "(Menggelengkan kepala)"
    Mbah "Pangeran Diponogoro itu pemimpinnya Perang Diponegoro, perang yang terjadi di Jawa pada masa kolonial Belanda (1825-1830). "
    extend "Pangeran Diponegoro memimpin perlawanan terhadap tindakan Belanda yang merampas tanahnya dan mengeksploitasi rakyat dengan pajak yang tinggi. "
    Mbah "Perlawanan Diponegoro mendapatkan dukungan dari rakyat dan berlangsung sengit di berbagai wilayah Jawa."
    Mbah "Perang ini melibatkan berbagai metode perang modern, termasuk perang terbuka dan gerilya. Belanda menggunakan berbagai cara licik untuk menangkap Diponegoro, "
    extend "termasuk mengeluarkan sayembara. "
    Mbah "Terus perubahan strategi Belanda terjadi ketika Gubernur Jenderal De Kock menggunakan strategi perbentengan untuk membatasi gerak Diponegoro. "
    Mbah "Perlawanan Diponegoro semakin melemah setelah beberapa pemimpinnya ditangkap. Pada akhirnya, Diponegoro ditangkap pada hari Idulfitri tahun 1830 dan diasingkan ke Manado, lalu Makassar, hingga meninggal di Benteng Rotterdam pada tahun 1855. "
    Mbah "Paham gak?"
    Suma "..."
    menu:
        "Paham, mbah!" :
            jump paham 
        "Enggak hehe..." :
            jump gakpaham
    
    label paham:
        Mbah "Mantap!"
        extend "Cucuku pinter tenan jebule"
        jump scene8

    label gakpaham:
        Mbah "Waduh waduh..."
        extend "Rungokne ya, le..."
        Mbah "Pangeran Diponogoro itu pemimpinnya Perang Diponegoro, perang yang terjadi di Jawa pada masa kolonial Belanda (1825-1830). "
        extend "Pangeran Diponegoro memimpin perlawanan terhadap tindakan Belanda yang merampas tanahnya dan mengeksploitasi rakyat dengan pajak yang tinggi. "
        Mbah "Perlawanan Diponegoro mendapatkan dukungan dari rakyat dan berlangsung sengit di berbagai wilayah Jawa."
        Mbah "Perang ini melibatkan berbagai metode perang modern, termasuk perang terbuka dan gerilya. Belanda menggunakan berbagai cara licik untuk menangkap Diponegoro, "
        extend "termasuk mengeluarkan sayembara. "
        Mbah "Terus perubahan strategi Belanda terjadi ketika Gubernur Jenderal De Kock menggunakan strategi perbentengan untuk membatasi gerak Diponegoro. "
        Mbah "Perlawanan Diponegoro semakin melemah setelah beberapa pemimpinnya ditangkap. Pada akhirnya, Diponegoro ditangkap pada hari Idulfitri tahun 1830 dan diasingkan ke Manado, lalu Makassar, hingga meninggal di Benteng Rotterdam pada tahun 1855. "
        Mbah "Dah paham?"
        Suma "(Mengangguk) Yup!"
        jump scene8:

label scene8:
    Mbah "Sudah pernah lihat lukisannya yang di gambar Raden Saleh belum?"
    Suma "Belummm"
    centered "Lalu mbah Seno pergi ke dalam dan mengambil gambaran kecil."
    centered "Beberapa menit kemudian, mbah Seno kembali dan menunjukkan gambaran itu kepada Suma."
    centered "Walaupun hanya duplikat, tapi masih tetap mirip."

    #nah ini nunjukin gambarnya raden saleh

    #setelah itu kuis

label scene9:
    centered "Keesokkan harinya, Suma sedang berjalan di ruang tengah dan tidak sengaja menemukan sebuah buku terbuka yang tidak terlalu tebal."
    centered "Dikarenakan penasaran, dia mengambil buku tersebut dan membacanya."
    
    #nampilin bersatu kita teguh...




label bgm:
    #play music "audio/suma_theme.mp3" fadein 1.0 volume 10
    show kaget at left
    Suma "Buset? Londo!"
    hide kaget

    show stefan_restface at left
    Stefan "Huh?"

    hide stefan_restface
    
label sfx:

label choices:
    #default learned = False
    show kaget at left
    Suma "Dee londo kan ya?"
    menu:
        "Hoo":
            jump hoo
        "Lah embuh":
            jump embuh

label hoo:
    hide kaget
    show stefan_giggleface at left
    Stefan "Apa itu 'Londo'?"
    jump lanjutan_hoo

label lanjutan_hoo:
    Suma "..."
    scene black
    jump end

label embuh:
    hide kaget
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
