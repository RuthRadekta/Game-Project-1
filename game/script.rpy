# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Guru = Character('Guru', color="#E03B8B")
define Suma = Character('Suma', color="#508D69")
define Stefan = Character('Stefan', color="#F3B664")
define Mbah = Character('Mbah', color="#872341")
define Kakek = Character('Kakek')

define Soekarno = Character('Soekarno', color="#0d1a73")
define Hatta = Character('Hatta', color="#373e6e")
define Radio = Character ('Radio', color="#030303")
define Massa = Character('Massa', color="#030303")
define Syahrir = Character('Syahrir', color="#4a0202")

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

#################################################

default nilai = 0

#################################################

label start:
    play sound "audio/bgm_bel.ogg"
    centered "{color=#FFFFFF}(Bel pulang sekolah berbunyi){/color}"
    stop sound

label scene1:
    scene fadein 0.5
    scene kelas sekarang
    #play suara riuh di kelas
    play sound "audio/sound_riuh.ogg" loop
    centered "{color=#FFFFFF}(Suara riuh di kelas){/color}"
    centered '{color=#FFF5C2}"Eh kata Pak Retno ulangan sejarah kapan?"{/color}'
    centered '{color=#FFF5C2}"Besok banget tuh"{/color}'
    show kusuma_suprisedface at left
    Suma "Huh?"
    Suma "(Menghela napas)"
    stop sound

label scene2:
    play sound "audio/steps-in-corridor.mp3" volume 5.0
    show kusuma_restface at left
    Suma "(Berjalan pulang dengan kesal)"
    play sound "audio/sigh.mp3"
    Suma "Kenapa sih sejarah sok keras banget?"
    Suma "Toh, Sejarah kan yang penting tahu, gak harus WAJIB kek gini. "
    extend "Ribet banget..."
    Suma "Mana pake ulangan segala lagi. Dikira mapel yang harus dipikir ini doang? "
    scene fadeout 1.5
    stop sound

label scene3:
    # eh ini scenenya masih ada creditnya
    scene kamar suma 
    with fade
    play sound "audio/pintu buka.mp3"
    centered "{color=#FFFFFF}(Sesampainya di rumah...){/color}"
    show kusuma_restface at left
    Suma "Ngantuk... "
    hide kusuma_restFace
    extend "Pen tidur..."
    scene fadeout 3.5
    stop sound

label scene4:
    scene kamar lama
    with fade
    play music "audio/ambient-dream.mp3" loop
    show normal at left
    Suma "Loh? (Melihat sekitar) "
    extend "Kamar siapa ini? "
    centered '"Le, ijek durung tangi to?"'
    hide normal
    show kaget at left
    Suma "(Mendengar sesuatu) Huh? "
    extend "Ada orang jawa?! "
    Suma "Siapa?! Ayah ya? "
    extend "Tapi kok berat gitu... "
    play sound "audio/squeaky-door.mp3"
    centered "(Mbah Seno masuk ke kamar Suma dan berkacak pinggang)"
    play sound "audio/foot-steps.mp3" volume 6.0
    hide kaget
    show mbah_normal at left
    Mbah "Le, le... turu teros! (Berjalan mendekati Suma)"
    hide mbah_normal
    show kaget at left
    Suma "(Membatin) Huh? "
    extend "Mbah Seno! "
    extend "Kok hidup lagi?! "
    stop sound
    stop music

    play sound "audio/pat.mp3"
    hide kaget
    show mbah_normal at left
    Mbah "(Menepuk pipi Suma) "
    extend "Ngopo to koe ki? Ndang tangi, ngewangi simbah! "
    Mbah "(Lalu keluar dari kamar Suma)"
    hide mbah_normal
    show kaget at left
    Suma "(Kaget, tapi langsung nyusul)"
    stop sound
    scene fadeout 0.5

label scene5:
    hide kaget
    play music "audio/bgm2.mp3"
    # nunjukin sekeliling rumah
    # centered "(EDIT)entar nunjukin sekeliling rumah, kira-kira 4 gambar"
    
    scene halaman rumah old
    with fade
    centered "(Suma sampai halaman depan)"
    
    #centered "(EDIT)entar nunjukin mbah seno yg berdiri dengan caping kepala dan bbrp peralatan berkebun"
    show mbah_normal at left
    Mbah "Ayo! Gek ndang mangkat!"
    hide mbah_normal
    show kaget at left
    Suma "M-mau kemana mbah?"
    hide kaget
    show mbah_normal at left
    Mbah "Yo nyang ngendi neh? Sawah lah!"
    hide mbah_normal
    show normal at left
    Suma "..."
    Suma "Ngapain ke sawah?"
    hide normal
    show mbah_normal at left
    Mbah "Bosomu aneh"
    extend ". Pokoke awakdewe bakal noto sawah. "
    extend "(Melirik Suma) "
    extend "Lak takon neh"
    hide mbah_normal
    show senyum at left
    Suma "(Terkekeh malu) "
    extend "Anu, Mbah... "
    extend "Sebenarnya aku gak paham sama maksud mbah..."
    Suma "Noto sawah itu apa ya, Mbah?"
    hide senyum
    show mbah_marah at left
    Mbah "... ?"
    show mbah_normal at left
    Mbah "Ngene lho, le. "
    extend "Keluargane awakdewe kan nduwe sawah, makane kui awakdewe kudu njogo. "
    extend "Kui sawah iso dadi sumber awakdewe urip karo dadi lapang kerjane masyarakat kampung"
    Mbah "(Melihat Suma dengan curiga)"
    Mbah "Biasane yo ngene ki lho, le. Kok koe dadi aneh men to?"
    hide mbah_marah
    hide mbah_normal
    show normal at left
    Suma "(Menceritakan semua yang telah terjadi)"
    centered "..."
    hide normal
    show mbah_senyum at left
    Mbah "(Tertawa kecil) "
    extend "Lah... pantes kok bedo. Jebule koe cicitku to"
    hide mbah_senyum
    show senyum at left
    Suma "(Tertawa canggung)"
    hide senyum
    show mbah_normal at left
    Mbah "(Berhenti tertawa)"
    Mbah "Yowes, tetep kerjo. Ayo!"
    hide mbah_normal
    scene fadeout 0.5

label scene6:
    scene sawah1 
    with fade
    show normal at left
    Suma "Mbah, apa yang harus aku lakukan di sini?"
    hide normal
    show mbah_senyum at left
    Mbah "(Tersenyum)"
    Mbah "Yo seko kene ki, le. Lapang kerja masyarakat kampung, panggon kanggo wong-wong desa kerjo ning kene, garap sawah iki"
    extend " Iki yo bagian sekolah adat Jawa sing kudu koe reti, le. Koe bakal sinau cara garap sawah"
    Mbah "Nah seko kono koe bakal paham artine kerja keras karo gotong royong"
    # bawah: teksnya terlalu panjang /opo-opo/
    Mbah "Kan yo manungsa urip gelem ra gelem akhire bakal bersosialisasi. Dadi ojo opo-opo ngeroso iso dewe ya, le"
    Mbah " Saiki, yoh mulai garap"
    hide mbah_senyum
    show normal at left
    Suma "(Sedikit ragu, tapi dia tetap mencoba beradaptasi dengan situasi yang dihadapi)"
    hide normal
    with fade
    centered "(Selama mereka bekerja, Mbah Seno menceritakan kisah-kisah tentang masa lalu bagaimana Belanda datang ke Indonesia dan perjuangan rakyat Indonesia saat melawan penjajahan Belanda)"
    centered "(Suma mendengarkan dengan penuh perhatian)"

    show mbah_normal at left
    Mbah "Pie, Le? Wes paham?"
    menu:
        "Udah, mbah" :
            jump berikutnya
        "Belum..." :
            jump ulang 

    label berikutnya:
        show mbah_normal at left
        Mbah "Yowes sip"
        jump scene7
    
    label ulang:
        show mbah_normal at left
        Mbah "Waduh."
        Mbah "Dengerno ya, Le... "
        # bawah: /bakal/
        extend "Jadi intinya kamu harus mau bersosialisasi. Bukan masalah bakal menyebabkan ketergantungan..."
        Mbah "Tapi, "
        extend "begitulah cara manusia hidup. "
        extend "Saling tolong-menolong dan gotong royong..."
        jump scene7

label scene7:
    hide mbah_normal
    stop music
    with fade
    centered "(Setelah beberapa jam bekerja di sawah, Suma paham apa yang dimaksud Mbah Seno)"
    centered "(Selain itu, mereka mulai akrab layaknya keluarga)"
    with fade
    
    play music "audio/afternoon.mp3" volume 2.0
    show mbah_normal at left
    Mbah "Bagus, le. Kau telah belajar banyak hari ini."
    # bawah: teksnya terlalu panjang /budaya/
    Mbah "Ini adalah langkah awal dalam perjalananmu untuk memahami sejarah dan budaya kita. "
    extend "Ingatlah, kita harus menghargai warisan nenek moyang kita dan belajar dari mereka."
    hide mbah_normal
    show normal at left
    Suma "(Mengangguk paham)"
    Suma "Terima kasih, Mbah. Aku akan mencoba yang terbaik."
    hide normal
    show mbah_normal at left
    Mbah "(Mengangkat sebelah alisnya) " 
    extend "Sampai kapan kau akan tinggal di sini, le?"
    hide mbah_normal
    show senyum at left
    Suma "Aku belum tahu, Mbah... (Tersenyum) "
    extend "Tapi sepertinya aku bakal betah di sini"
    hide senyum
    show mbah_senyum at left
    Mbah "(Tersenyum kembali)" 
    Mbah "Yowes, le. Ayo bali. Kita masih punya banyak yang harus kau pelajari."  
    hide mbah_senyum
    centered "(Mereka berdua meninggalkan sawah dan kembali ke rumah yang jauh berbeda dari rumah Suma di masa kini)"
    
    scene halaman rumah old
    with fade
    show pahlawan_syahrir at left
    Syahrir "(Menyapa Mbah Seno, lalu berjalan lagi)"
    show normal at right
    centered "..."
    hide normal
    hide pahlawan_syahrir
    show normal at left
    Suma "Siapa tuh, mbah?"
    hide normal
    show mbah_normal at left
    Mbah "Oh.. jenenge Sutan Syahrir. "
    extend "Tapi biasane aku nyeluk 'Si Kancil' "
    hide mbah_normal
    show kaget at left
    Suma "... (gak paham bahasa jawa)"
    hide kaget
    show mbah_senyum at left
    Mbah "(Tertawa melihat wajah bingung Suma)"
    Mbah "Maksudnya, nama orang itu Sutan Syahrir. Tapi mbah biasanya manggil ‘Si Kancil’, paham?"
    hide mbah_senyum
    show normal at left
    Suma "Oh..."
    extend "Terus beliau mau pergi kemana itu, mbah?"
    hide normal
    show mbah_normal at left
    Mbah "Rumahnya lah."
    Mbah "Katanya habis datang dari Konferensi Rijswijk yang berlangsung pada tahun ini, 1939. "
    extend "Tujuannya untuk membahas masalah dan perselisihan antara pemerintah kolonial Belanda dan para pemimpin Indonesia."
    Mbah "Masalah utama yang dibahas termasuk otonomi ekonomi untuk Hindia Belanda, peningkatan status politik, dan kemerdekaan."
    Mbah "Pemimpin konferensi ini ya Si Kancil, tapi di didampingi Tjarda van Starkenborgh, gubernur jendral dari Belanda."
    Mbah "Tapi katanya hasil konferensi ini belum mencapai kesepakatan konkret. "
    extend "Alhasil, kontrol Belanda di Indonesia masih erat dan pokoke waspada ae ya, le."
    hide mbah_normal
    show senyum at left
    Suma "(Mengangguk)"
    hide senyum
    show mbah_normal at left
    Mbah "(Duduk di teras setelah cuci kaki dan tangan)"
    Mbah "Oiyo le, rene sek."
    hide mbah_normal
    show kaget at left
    Suma "(Duduk di sebelahnya) Ya, mbah?"
    hide kaget
    show mbah_normal at left
    Mbah "Mbah sudah cerita tentang Pangeran Diponegoro belum to?"
    hide mbah_normal
    show normal at left
    Suma "(Menggelengkan kepala)"
    hide normal
    show mbah_senyum at left
    Mbah "Pangeran Diponogoro itu pemimpinnya Perang Diponegoro, perang yang terjadi di Jawa pada masa kolonial Belanda (1825-1830). "
    extend "Pangeran Diponegoro memimpin perlawanan terhadap tindakan Belanda yang merampas tanahnya dan mengeksploitasi rakyat dengan pajak yang tinggi. "
    # bawah: /sengit/
    Mbah "Perlawanan Diponegoro mendapatkan dukungan dari rakyat dan berlangsung sengit di berbagai wilayah Jawa."
    Mbah "Perang ini melibatkan berbagai metode perang modern, termasuk perang terbuka dan gerilya. Belanda menggunakan berbagai cara licik untuk menangkap Diponegoro, "
    extend "termasuk mengeluarkan sayembara. "
    Mbah "Terus perubahan strategi Belanda terjadi ketika Gubernur Jenderal De Kock menggunakan strategi perbentengan untuk membatasi gerak Diponegoro. "
    Mbah "Perlawanan Diponegoro semakin melemah setelah beberapa pemimpinnya ditangkap. Pada akhirnya, Diponegoro ditangkap pada hari Idulfitri tahun 1830 dan diasingkan ke Manado, lalu Makassar, hingga meninggal di Benteng Rotterdam pada tahun 1855. "
    Mbah "Paham gak?"
    hide mbah_senyum
    show normal at left
    Suma "..."
    menu:
        "Paham, mbah!" :
            jump paham 
        "Enggak hehe..." :
            jump gakpaham
    
    label paham:
        hide normal
        show mbah_senyum at left
        Mbah "Mantap!"
        hide mbah_senyum
        jump scene8

    label gakpaham:
        show mbah_normal at left
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
        hide mbah_normal
        show senyum at left
        Suma "(Mengangguk) Yup!"
        hide senyum
        jump scene8

label scene8:
    show mbah_senyum at left
    Mbah "Sudah pernah lihat lukisannya yang di gambar Raden Saleh belum?"
    hide mbah_senyum
    show senyum at left
    Suma "Belummm"
    hide senyum
    centered "(Lalu mbah Seno pergi ke dalam dan mengambil gambaran kecil)"
    centered "(Beberapa menit kemudian, mbah Seno kembali dan menunjukkan gambaran itu kepada Suma)"
    centered "(Walaupun hanya duplikat, tapi masih tetap mirip)"

    # nah ini nunjukin gambarnya raden saleh

    stop music
    # setelah itu kuis
    scene bg2

    label pertanyaanCH1_1:
        play sound "audio/bell.mp3"
        centered "Pertanyaan!"
        # semua pertanyaan pake centered ya
        centered "Konferensi apa yang didatangi sekaligus dipimpin oleh Sutan Syahrir?"
        menu:
            "Konferensi Meja Bundar":
                play sound "audio/klik.mp3"
                jump pertanyaanCH1_2
                $ nilai += 2
            "Konferensi Rijswijk 1939":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH1_2
            "Konferensi Hindia Belanda":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_2
            "Koferensi Rijswijk 1940":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_2
    
    label pertanyaanCH1_2:
        centered "Apa tujuan konferensi itu diadakan?"
        menu:
            "Membahas masalah dan perselisihan antara pemerintah kolonial Belanda dan para pemimpin Indonesia":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH1_3
            "Memundurkan Belanda dari Indonesia":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_3
            "Memperoleh kemerdekaan Indonesia dari tangan Belanda":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_3
            "Demo untuk kesejahteraan Indonesia":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_3
    
    label pertanyaanCH1_3:
        centered "Pangeran Diponegoro merupakan pemimpin Perang Diponegoro. Kapan dan dimana perang itu terjadi?"
        menu:
            "Sumatra, tahun 1825-1830":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_4
            "Jawa, tahun 1825-1830":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH1_4
            "Jawa, tahun 1826-1830":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_4
            "Sumatra, tahun 1826-1830":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_4
    
    label pertanyaanCH1_4:
        centered "Siasat yang digunakan Belanda untuk melawan Pangeran Diponegoro adalah siasat Benteng Stelsel. Apa tujuan siasat itu?"
        menu:
            "Melancarkan hubungan Belanda dengan Pasukan Diponegoro":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_5
            "Mencegah masuknya bantuan untuk pasukan Belanda":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_5
            "Memperkuat pasukan Belanda":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH1_5
            "Mempersempit ruang gerak pasukan Diponegoro. Adapun tempat persembunyian utamanya adalah Goa Selarong":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH1_5

    label pertanyaanCH1_5:
        centered "Belanda berhasil menguasai Indonesia yang kaya akan rempah-rempah, hal ini membuat Belanda dapat mengatur perdagangan Indonesia untuk memperkayakan dirinya sendiri. Inilah yang disebut Merkantilisme. Jadi, Merkantilisme adalah?"
        menu:
            "Paham sosial yang menekankan bahwa siapa yang kaya, ialah yang berkuasa":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump scene9
            "Paham perekonomian yang menganut bahwa keberhasilan suatu negara ditentukan oleh banyaknya modal atau aset yang dimiliki oleh negara":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump scene9
            "Paham perekonomian yang menyatakan bahwa keberhasilan suatu negara didasarkan pada kemajuan teknologi yang ada di negara tersebut":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump scene9
            "Paham perekonomian tentang untung dan rugi":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump scene9



############ CHAPTER 02 ####################
stop music

label scene9:
    centered "Next!"
    scene fadeout 3.0
    scene ruang tengah dulu
    with fade

    centered "Keesokkan harinya, Suma sedang berjalan di ruang tengah dan tidak sengaja menemukan sebuah buku terbuka yang tidak terlalu tebal."
    centered "Dikarenakan penasaran, dia mengambil buku tersebut dan membacanya."
    
    #nampilin bersatu kita teguh...

    show mbah_marah at left
    Mbah "Moco gak izin sek. "
    extend "Kene"
    hide mbah_marah
    show kaget at left
    show senyum at left
    hide kaget
    Suma "(Tertawa gugup) "
    extend "Hehe maaf, mbah. Sengaja."
    hide senyum
    show mbah_normal at left
    Mbah "Hm"
    hide mbah_normal
    show normal at left
    Suma "Tapi mbah..."
    hide normal
    show mbah_normal at left
    Mbah "Opo neh?"
    hide mbah_normal
    show normal at left
    Suma "Itu karangan siapa?"
    hide normal
    show mbah_normal at left
    Mbah "Oh, iki seko Nak Yamin. Iki diterbitne-"
    hide mbah_normal
    show pout at left
    Suma "Mbahhh pake Bahasa Indonesia, dong. Ga paham akuuu"
    hide pout
    show mbah_normal at left
    Mbah "Heleh. "
    extend "Gak tau nganggo boso kromo sih."
    Mbah "Ini sajak yang dibuat Muhammad Yamin, diterbitkan di Pasudan tanggal 26 Oktober 1928."
    hide mbah_normal
    show kaget at left
    Suma "26 Oktober 1928?! "
    extend "Sebelum Kongres Sumpah Pemuda II dong, mbah?"
    hide kaget
    show mbah_normal at left
    Mbah "Hiyo. Kok koe reti le?"
    hide mbah_normal
    show senyum at left
    Suma "Hehe ngerti dong, mbah"
    hide senyum

    # Pertanyaan 6
    show mbah_senyum at left
    Mbah "Kalo begitu, kapan hayo dilaksanakan Sumpah Pemuda II?"
    hide mbah_senyum
    label pertanyaanCH2_1:
        menu:
            "28 Oktober 1928":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH2_2
            "26 Oktober 1928":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH2_2
            "28 Oktober 1929":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH2_2
            "26 Oktober 1929":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH2_2
    
    # Pertanyaan 7
    label pertanyaanCH2_2:
        show mbah_senyum at left
        Mbah "Apa hasilnya?"
        hide mbah_senyum
        menu:
            "Kami putra dan putri Indonesia, mengaku bertumpah darah yang satu, tanah Indonesia. Kami putra dan putri Indonesia, mengaku berbangsa yang satu, bangsa Indonesia.":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump benar7
            "Kami putra dan putri Indonesia, mengaku bertumpah darah yang satu, bangsa Indonesia. Kami putra dan putri Indonesia, mengaku berbangsa yang satu, tanah Indonesia.":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump salah7
    
    label benar7:
        show mbah_senyum at left
        Mbah "Cucuku pinter tenan jebule"
        $ nilai += 2
        jump scene10
    
    label salah7:
        show mbah_senyum at left
        Mbah "Heleh, jare ngerti?"
        $ nilai += 2
        jump scene10

label scene10:
    hide mbah_senyum

    centered "(Setelah itu, Suma berpamitan untuk pergi ke sekolah karena ia mau tidak mau harus tetap pergi ke sekolah di zaman ini, walaupun harus tetap berpura-pura menjadi kakeknya)"
    scene fadeout 1.0

    # nanti muncul info ndek tengah
    # Kakeknya ini ternyata seorang yang ramah dan pekerja keras, berbanding balik dengan dirinya. Dia juga popular di kalangan sekolah dan sekitar karena kecerdasannya, selain itu dia adalah seorang ketua salah satu organisasi tersembunyi di sekolah yang ikut memperjuangkan kemerdekaan.  

    scene kelas old
    with fade
    show normal at left
    Suma "(Melihat sekitar) "
    extend "kok bule semua ya? cowo semua lagi (batinnya)"

    centered "..."

    Suma "(Duduk di bangkunya)"

    # Pertemuan dengan Stefan
    hide normal
    centered '"Hey!"'

    show kaget at left
    Suma "(Kaget, karena bahunya ditepuk)"
    Suma "Eh penjajah?!?"
    hide kaget
    show stefan_normal at left
    Stefan "Ada apa?"
    show normal at right
    centered "..."
    hide stefan_normal
    hide normal
    show stefan_giggle at left
    Stefan "Aku hanya minta tolong kau ajarkan math ini. Bisa?"
    extend " (bertanya dengan aksen Belanda yang masih kental)"
    hide stefan_giggle
    show kaget at left
    Suma "Hah?"
    hide kaget
    show stefan_normal at left
    Stefan "Hah??"
    hide stefan_normal
    show kaget at left
    Suma "(Menunjuk dirinya sendiri)"
    hide kaget
    show stefan_senyum at left
    Stefan "Iya! "
    extend "Karena kau pintar."
    hide stefan_senyum
    show normal at left
    Suma "Tumben ada yang minta ajar ke gue (batinnya)"
    Suma "(Berdeham)"
    extend "Gak mau (gengsi)"
    hide normal
    show stefan_pout at left
    Stefan "Come on!"
    extend " Kau bisa mengajar pada semua. Tapi, aku tidak, kenapa?"
    hide stefan_pout
    show normal at left
    Suma "(Mendesah kesal karena ia hampir saja lupa bahwa dia berada dalam tubuh kakeknya yang ramah)"
    Suma "Gue bahkan ga kenal lo. Sokap banget."
    hide normal
    centered "(Suma melirik ke arah lain. Dia tahu bahwa orang Belanda itu tidak mengerti ejekkannya, jadi dia bisa bebas menggunakan kosakata gaul di zamannya.)"
    show stefan_senyum at left
    Stefan "Maksudmu?"
    extend "(menatap bingung)"
    hide stefan_senyum
    show normal at left
    Suma "Aku tidak mengenalmu, ‘kay? Do you understand?"
    hide normal
    show stefan_senyum at left
    Stefan "Aneh sekali kau tidak tahu aku, teman sekelas,"
    extend " Aku Stefan. Stefan Driessen"
    hide stefan_senyum
    show kaget at left
    Suma "Stefan?"
    hide kaget
    show stefan_giggle at left
    Stefan "(Mengangguk beberapa kali dan mengacungkan jempol)"
    hide stefan_giggle
    show normal at left
    Suma "Tapi... "
    extend "ini tidak gratis"
    hide normal
    show stefan_senyum at left
    Stefan "(Mengangguk)"
    extend "Ya, aku akan membayar"
    hide stefan_senyum
    show normal at left
    Suma "Uang? Mungkin ini gak begitu buruk (batinnya)"
    hide normal
    centered " "

label scene11:
    with fade
    centered "(Sebelum pulang sekolah, Suma sedang melihat-lihat sekitar di kelas ini karena rasa kagumnya belum sirna)"
    centered "Salah satu benda yang menarik perhatiannya adalah sebuah pajangan kata-kata yang berfigurakan kayu"

    # nampilin pajangan itu

    show normal at left
    Suma "(Memahami kata-kata tersebut) "
    hide normal
    show kaget at left
    Suma "Hah?"
    hide kaget
    show stefan_normal at left
    Stefan "Hah??"
    extend " (Menoleh dari samping Suma)"
    show kaget at right
    centered " "
    hide stefan_normal
    hide kaget
    show normal at left
    Suma "(Menatap Stefan) " 
    extend "Itu... pajangan itu didapat darimana?"
    hide normal
    show stefan_senyum at left
    Stefan "Oh! Benda itu dibuat oleh salah satu guru. "
    extend "Katanya dia suka dan terkesan dengan semboyan Ki Hadjar Dewantara."
    hide stefan_senyum
    show normal at left
    Suma "Kenapa? Emang artinya apa?"
    hide normal
    show stefan_senyum at left
    Stefan "Ing Ngarso Sung Tulodo artinya menjadi seorang pemimpin harus mampu memberikan suri tauladan. "
    extend "Ing Madyo Mbangun Karso, artinya seseorang ditengah kesibukannya harus juga mampu membangkitkan atau menggugah semangat. "
    extend "Tut wuri handayani, artinya di belakang bisa memberi dorongan"
    hide stefan_senyum
    show kaget at left
    Suma "Kok kamu tahu?"
    hide kaget
    show stefan_giggle at left
    Stefan "Guru itu yang mengartikannya untukku "
    extend "(Bangga)"
    hide stefan_giggle
    show normal at left
    Suma "Oh. Ya sudah. Thanks."
    hide normal
    centered "(Suma mulai berjalan dari kelas untuk pulang dan diikuti oleh Stefan)"
    scene fadeout

label scene12:
    scene ruang tengah stefan_1
    with fade
    centered "(Mereka tiba di rumah Stefan)"

    # nampilin rumah stefan view dari luar
    # terus nampilin ruang tengah rumah stefan

    centered "(Mereka duduk di ruang tengah rumah Stefan)"
    show normal at left
    Suma "(Mengeluarkan buku matematikanya yang cukup tebal)"
    hide normal
    show stefan_pout at left
    Stefan "(Mata berbinar)"
    hide stefan_pout
    show kaget at left
    Suma "Kenapa mukamu gitu?"
    hide kaget
    show stefan_giggle at left
    Stefan "Senang"
    hide stefan_giggle
    show kaget at left
    Suma "Senang?"
    hide kaget
    show stefan_senyum at left
    Stefan "(Mengangguk) Buku tebal, terlihat menarik"
    hide stefan_senyum
    show senyum at left
    Suma "Lah, gue kira gue aneh sendiri (batinnya)"
    hide senyum
    show stefan_normal at left
    Stefan "Kenapa senyum?"
    hide stefan_normal
    show normal at left
    Suma "Uang"
    hide normal
    show stefan_normal at left
    Stefan "..."
    hide stefan_normal

    centered " "
    centered "(Mereka mulai belajar dengan Suma yang menjadi tutor)"
    with fade

    show normal at left
    Suma "Stef, kok bisa sih lu berpihak ke Indonesia?"
    hide normal
    show stefan_pout at left
    Stefan "(Berhenti menulis) Maksudnya?"
    hide stefan_pout
    show normal at left
    Suma "Maksudnya, kenapa kau bisa berpihak ke Indonesia? Padahal kau bukan pribumi"
    hide normal
    show stefan_senyum at left
    Stefan "(Tersenyum) Aku suka di sini daripada Netherland! Papa mama juga..."
    hide stefan_senyum
    show normal at left
    Suma "Kenapa?"
    hide normal
    show stefan_giggle at left
    Stefan "Aku suka kue putu!"
    hide stefan_giggle
    show kaget at left
    Suma "... "
    extend "bjir (batinnya)"
    hide kaget

    centered " "
    with fade
    centered "(Kemudian Stefan menceritakan tentang keluarganya)"
    centered "(Ayahnya yang bekerja sebagai pegawai pemerintah Belanda dan menikah dengan ibunya yang merupakan seorang wanita cantik dari Indonesia)"
    centered "(Dia juga mengungkapkan bahwa dia adalah anggota keluarga yang beruntung karena bisa mendapatkan pendidikan yang baik)"

    show normal at left
    Suma "(Mengangguk paham)"
    hide normal

    centered "(Saat mereka berbicara, orang tua Stefan, yaitu Nyonya Driessen dan Tuan Driessen, masuk ke dalam ruang keluarga."
    centered "Mereka adalah orang Belanda yang tinggal di Indonesia, dan mereka terlihat ramah kepada Suma. Meskipun ada bahasa dan budaya yang berbeda, mereka mencoba berkomunikasi dengan Suma dan mengenalkan diri mereka.  )"
    centered "(Sejak saat itu, Suma dan Stefan mulai akrab satu sama lain)"
    centered " "

label scene13:
    with fade
    centered "(Suatu hari, saat Suma selesai mengajari Stefan Pelajaran matematika seperti biasa, ia mendengar suara orang mengobrol dari arah pintu masuk)"

    # janlup sfx
    # nampilin pintu terbuka, perabotan kayu jati
    # ada suara berbincang dan tawa

    centered "(Hari ini adalah hari di mana Tuan Driessen menjadi tuan rumah dalam pertemuan untuk berdiskusi tentang perjuangan kemerdekaan)"
    centered "(Suma dan Stefan bersemangat karena Ayah Stefan bilang Soekarno dan tokoh-tokoh pejuang kemerdekaan lainnya akan datang)"

    show kaget at left
    Suma "What? Soekarno?!"
    show pahlawan_soekarno at right
    centered " "
    hide pahlawan_soekarno
    Suma "Apa kau tahu Pak Soekarno itu siapa?"
    hide kaget
    show stefan_normal at left
    Stefan "Siapa?"
    hide stefan_normal
    show normal at left
    Suma "..."
    Suma "Beliau sering ke sini ‘kan?"
    hide normal
    show stefan_giggle at left
    Stefan "Tidak ingat"
    hide stefan_giggle
    show normal at left
    Suma "..."
    hide normal

    centered " "
    with fade
    centered "(Acara itupun dimulai)"
    centered "(Selama di sekolah Suma tidak pernah membayangkan orasi dari Soekarno bisa sekeren ini. Teks-teks dan gambar burik di buku paket sejarahnya tidak bisa menyalurkan kekerenan ini dengan baik. )"

    show senyum at left
    Suma "Ternyata disaksikan secara langsung public speaking Pak Soekarno keren juga (batinnya)"
    hide senyum

    centered "(Sesaat kemudian seseorang datang menyusul ke ruangan ini)"

    show kaget at left
    Suma "Itu Mohammad Hatta! Hatta woi! (sambil mengguncang bahu Stefan, saking senangnya)"
    show pahlawan_hatta at right
    centered " "
    hide pahlawan_hatta
    hide kaget
    show stefan_normal at left
    Stefan "Kenapa?"
    hide stefan_normal
    show kaget at left
    Suma "Kok kenapa? Itu Mohammad Hatta!!"
    hide kaget
    show stefan_pout at left
    Stefan "Iya, lalu?"
    hide stefan_pout
    show normal at left
    Suma "(Suma menepuk dahinya keras-keras. Dia lupa kalau sedang ada di lain zaman dan fakta bahwa Stefan ini tidak tahu menahu tentang para pahlawan revolusi)"
    hide normal

    centered "(Acara berlanjut dengan lancar)"
    centered "..."
    scene fadeout 1.0

    scene bg2
    with fade
    play sound "audio/bell.mp3"
    centered "Pertanyaan!"
    #pertanyaan 8 dan 9

    label pertanyaanCH2_3:
        centered "'Bersatu kita teguh, bercerai kita runtuh' merupakan sajak yang dibuat oleh?"
        menu:
            "Sutan Sjahrir":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH2_4
            "Soekarno":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH2_4
            "Muh. Yamin":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH2_4
            "Ki Hajar Dewantara":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH2_4
    
    label pertanyaanCH2_4:
        centered "Ing ngarsa sung tuladha.Ing madya mangun Karsa. Tut Wuri Handayani. Tiga kalimat itu merupakan semboyan dari Ki Hadjar Dewantara. Apa artinya?"
        menu:
            "Seorang pemimpin harus mampu meneladani dan memberi semangat meskipun di tengah kesibukannya":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump scene20
            "Menjadi seorang pemimpin harus mampu memberikan suri tauladan":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump scene20
            "Seseorang ditengah kesibukannya harus juga mampu membangkitkan atau menggugah semangat":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump scene20
            "Lupa":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump scene20


################# CHAPTER 03 ##########################




############### CHAPTER 04 ################

label scene20:
    scene fadeout 1.0
    scene ruang tengah dulu
    with fade
    centered "Kami bangsa Indonesia..."
    # play bgm indonesia raya
    # ini radionya latarnya di rumah Stefan

    Suma "Huh?"

    Radio "... diselenggarakan dengan tjara seksama..."
    Radio "Disoearakan oleh Soekarno di Djalan Pengangsaan Timoer 56."
    extend "Djakarta, hari 17 boelan 8 tahoen 5"

    Suma "Yes! Akhirnya merdeka!"
    Stefan "Benar! Merdeka!"
    extend "(Tertawa bersama Suma)"

    #nanti dikasih fade out ya buat nutup scenenya

    centered "(Beberapa bulan kemudian, Agresi Militer Belanda I terjadi)"
    centered "(Hal ini dikarenakan Belanda menolak mengakui kemerdekaan Indonesia dan memutuskan untuk melancarkan serangan militer)"
    centered "(Inilah yang disebut sebagai Masa Bersiap)"
    centered "(Selama Masa Bersiap, Indonesia terus berusaha mempertahankan kemerdekaannya dan mempersiapkan diri untuk menghadapi serangan militer lebih lanjut)"
    centered "(Masa Bersiap juga mencakup upaya diplomatik untuk memperoleh pengakuan internasional atas kemerdekaan Indonesia)"
    centered "(Bahkan pertempuran hebat terjadi di kota Surabaya karena ketidaksetujuan Masyarakat terhadapat datangnya sekutu yang merupakan aliansi dari Belanda)"
    # dikasi sticky notenya bung tomo

    centered "(Tiba-tiba, saat Suma yang sedang berbincang di rumah Stefan, sekelompok Masyarakat berbondong-bondong datang dengan membawa celurit, bambu runcing, golok dan satu-dua senjata api seperti pistol serta bender merah-putih)"
    Massa "Andjing NICA! Pergi!"
    centered "(Suma dan Stefan yang berada di ruang tengah langsung beranjak karena merasa kaget. Sekian detik kemudian, suara teriakan dari ibu Stefan terdengar dan seruan dari ayah Stefan berhasil membuat Stefan ketakutan)"
    centered '"Het huis uit, Stefan!!"'

    Suma "Kenapa? Apa??!"
    Stefan "Lari!"

    centered "(Stefan berlari keluar dari rumah melalui pintu belakang dan diikuti oleh Suma)"
    centered "(Namun, massa berhasil memaksa masuk ke dalam rumah dan menembakkan peluru dua kali ke punggung Stefan. Suma yang kaget melihat Stefan tergeletak pun berhenti dan membantu Stefan)"
    Massa "Masih ada satu pro-Belanda!"
    Suma "A-aku bukan. Aku orang Indonesia!"
    centered "(Tapi sepertinya massa mengabaikan pernyataan Suma. Maka saat salah satu warga mengangkatkan golok ke arah Suma, dia tanpa sadar berteriak dan menutup mata erat karena ketakutan)"
    # scenenya dikasih fade out agak lama

##################### CHAPTER 05 #######################

    centered "(Suma terbangun di kamarnya. Dia terengah-engah dan menatap sekeliling. Ini kamarnya yang dulu. Dia sudah kembali ke zamannya)"
    Suma "(Bernapas lega. Mimpiny tadi terasa seperti nyata)"
    centered "(Saat Suma keluar dari kamar untuk pergi mengambil minum di dapur, dia melihat kakeknya (Torasumaji Prasasta) sedang menulis sesuatu di ruang Tengah)"
    Suma "Kakek?"
    centered "(Kakek menoleh, lalu tersenyum. Suma yang penasaran pun berjalan mendekat untuk melihat apa yang ditulis sang kakek)"

    # nanti nampilin tuh tulisan

    Suma "(Terkejut)"

    # tampilin aja semua ekspresi yang sesuai ama dialog, ndak harus dikasih keterangan "(...)"

    centered "(Maka dari itu dia berlari kembali ke kamarnya dan mengambil buku paket sejarahnya. Dikarenakan penasaran, dia mencari-cari kejadian relevan yang terjadi setelah kemerdekaan)"
    centered "(Tanpa sadar ia mulai belajar)"

    # nampilin sticky note materi (ada di script.docx)

    centered "Suma mungkin tidak dapat memberikan kontribusi langsung dalam perjuangan Indonesia)"
    centered "Tapi dia mendapatkan pelajaran berharga tentang arti perjuangan, kemerdekaan, dan tekad yang dibutuhkan untuk mencapai tujuan besar, kemerdekaan Indonesia"

    # scene di fade out karena ini bakal ganti hari

    centered "(Keesokkan harinya...)"

    #nampilin latar dan bgm kek di sekolah

    centered "(Soal ulangan sejarah dibagikan)"

    Suma "(Terkejut) Huh? Sama??"

    centered "(Tidak disangka, soal-soal sejarah itu sebagian besar sama persis seperti di mimpi dan apa yang dia tidak sadar pelajari)"

    centered "Pertanyaan!"

    # Pertanyaan berdasarkan ch04 dan ch05 = jumlah 6
    label pertanyaanCH4_1:
        centered "Kemerdekaan Indonesia diumumkan pada 17 Agustus 1945 silam. Siapa yang memproklamirkan kemerdekaan Indonesia?"
        menu:
            "Soekarno Hatta":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH4_2
            "Sayuti Melik":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH4_2
            "Soekarno":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH4_2
            "Muh Yamin":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH4_2

    label pertanyaanCH4_2:
        centered "Agresi Militer Belanda terjadi beberapa bulan setelah diproklamirkan Kemerdekaan Indonesia, lalu berakhir pada 5 Agustus 1947. Apa tujuan Agresi Militer Belanda I?"
        menu:
            "Merebut kembali hak milik Belanda":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH4_3
            "Merebut kembali kendali atas Indonesia":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH4_3
            "Membubarkan Kemerdekaan Indonesia":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH4_3
            "Menyatakan perang dengan Indonesia":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH4_3

    label pertanyaanCH4_3:
        centered "Penyebab terjadinya Agresi Militer Belanda I adalah karena Indonesia menolak Rencana Van Mook. Dari kejadian itu terbentuk Perjanjian Renville. Apa salah satu isinya?"
        menu:
            "Belanda membentuk lima belas negara federal yang terdiri dari negara-negara boneka, dengan Van Mook sebagai kepala pemerintahannya":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH4_4
            "Tidak disetujuinya sebuah garis demarkasi (Van Mook) yang memisahkan wilayah Indonesia dan daerah pendudukan Belanda":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH4_4
            "Belanda hanya mengakui Jawa Tengah, Yogyakarta, dan Sumatra sebagai bagian wilayah Republik Indonesia":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH4_4

    label pertanyaanCH4_4:
        centered "Pemberontakan salah satu wilayah di Indonesoa akibat Agresi Militer I Belanda adalah di Surabaya. Saking heoriknya, peristiwa itu diperingati sebagai hari pahlawan. Kapan tepatnya peristiwa itu terjadi?"
        menu:
            "10 Oktober 1945":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH5_1
            "10 November 1945":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH5_1
    
    label pertanyaanCH5_1:
        centered "Belanda kembali melanggar Perjanjian Renville dengan melancarkan Agresi Militer Belanda II. Hal ini menyebabkan Indonesia terpaksa mendirikan Pemerintahan Darurat Republik Indonesia di Bukittinggi, Sumatra Barat di bawah komando Syafruddin Prawiranegara. Acara apa yang menandai akhir Agresi Militer Belanda II?"
        menu:
            "Perundingan Roem-Royen":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump pertanyaanCH5_2
            "Konferensi Meja Bundar":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH5_2
            "Konferensi Inter-Indonesia":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH5_2
            "Perundingan Renville":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump pertanyaanCH5_2

    label pertanyaanCH5_2:
        centered "Konferensi Meja Bundar dilaksanakan di Den Haag, Belanda. Delegasi Belanda dipimpin oleh van Maarseveen. Delegasi Indonesia dipimpin Drs. Moh. Hatta. Apa hasil dari Konferensi Meja Bundar?"
        menu:
            "Menghentikan perang gerilya dan Indonesia-Belanda bekerja sama dalam memelihara ketertiban dan keamanan":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump nilai
            "Dibentuk negara federal yang dinamakan Republik Indonesia Serikat":
                play sound "audio/klik.mp3"
                $ nilai += 2
                jump nilai
            "Belanda mengakui kedaulatan Indonesia paling lambat 30 Desember 1949":
                play sound "audio/klik.mp3"
                $ nilai += 5
                jump nilai


    #scene fade out ke situasi pulang sekolah


###################### NILAI ########################

label nilai:
    Suma "Berapa ya nilaiku?"
    play sound "audio/success.mp3"
    centered "{color=#FFFFFF}Nilai ulangan kamu: {color=#a10b0b}[nilai]{/color}{/color}"

#################################################################

label end:
    #with fade
    $renpy.full_restart()
    return

################## END #################