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
    scene ruangkelas_now
    #play suara riuh di kelas
    play sound "audio/sound_riuh.ogg"
    centered "{color=#FFFFFF}(Suara riuh di kelas){/color}"
    centered '{color=#FFF5C2}"Eh kata Pak Retno ulangan sejarah kapan?"{/color}'
    centered '{color=#FFF5C2}"Besok banget tuh"{/color}'
    show kusuma_suprisedface at left
    Suma "Huh?"
    Suma "(Menghela napas)"
    stop sound

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
    centered '"Le, ijek durung tangi to?"'
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
    # nunjukin sekeliling rumah
    centered "(EDIT)entar nunjukin sekeliling rumah, kira-kira 4 gambar"
    centered "(Suma sampai halaman depan)"
    centered "(EDIT)entar nunjukin mbah seno yg berdiri dengan caping kepala dan bbrp peralatan berkebun"
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
    # scene fadeout 0.5

label scene6:
    centered "(EDIT)entar nampilin hamparan sawah hijau yang membentang"
    centered "(EDIT)terus nampilin petani yang lagi bekerja di sawah"    
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
    centered "(Selama mereka bekerja, Mbah Seno menceritakan kisah-kisah tentang masa lalu bagaimana Belanda datang ke Indonesia dan perjuangan rakyat Indonesia saat melawan penjajahan Belanda)"
    centered "(Suma mendengarkan dengan penuh perhatian)"
    hide normal

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
    centered "(Setelah beberapa jam bekerja di sawah, Suma paham apa yang dimaksud Mbah Seno)"
    centered "(Selain itu, mereka mulai akrab layaknya keluarga)"
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
    centered "(Mereka berdua meninggalkan sawah dan kembali ke rumah yang jauh berbeda dari rumah Suma di masa kini)"
    # scene fadeout 0.5
    Suma "Siapa tuh, mbah?"
    extend "(tanya Suma penasaran saat ada pemuda yang menyapa mbah Seno saat hendak masuk ke halaman rumahnya)"
    Mbah "Oh.. jenenge Sutan Syahrir. "
    extend "Tapi biasane aku nyeluk 'Si Kancil' "
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
        jump scene8

label scene8:
    Mbah "Sudah pernah lihat lukisannya yang di gambar Raden Saleh belum?"
    Suma "Belummm"
    centered "(Lalu mbah Seno pergi ke dalam dan mengambil gambaran kecil)"
    centered "(Beberapa menit kemudian, mbah Seno kembali dan menunjukkan gambaran itu kepada Suma)"
    centered "(Walaupun hanya duplikat, tapi masih tetap mirip)"

    # nah ini nunjukin gambarnya raden saleh

    # setelah itu kuis
    label pertanyaanCH1_1:
        centered "Pertanyaan!"
        "Konferensi apa yang didatangi sekaligus dipimpin oleh Sutan Syahrir?"
        menu:
            "Konferensi Meja Bundar":
                jump pertanyaanCH1_2
                $ nilai += 2
            "Konferensi Rijswijk 1939":
                $ nilai += 5
                jump pertanyaanCH1_2
            "Konferensi Hindia Belanda":
                $ nilai += 2
                jump pertanyaanCH1_2
            "Koferensi Rijswijk 1940":
                $ nilai += 2
                jump pertanyaanCH1_2
    
    label pertanyaanCH1_2:
        "Apa tujuan konferensi itu diadakan?"
        menu:
            "Membahas masalah dan perselisihan antara pemerintah kolonial Belanda dan para pemimpin Indonesia":
                $ nilai += 5
                jump pertanyaanCH1_3
            "Memundurkan Belanda dari Indonesia":
                $ nilai += 2
                jump pertanyaanCH1_3
            "Memperoleh kemerdekaan Indonesia dari tangan Belanda":
                $ nilai += 2
                jump pertanyaanCH1_3
            "Demo untuk kesejahteraan Indonesia":
                $ nilai += 2
                jump pertanyaanCH1_3
    
    label pertanyaanCH1_3:
        "Pangeran Diponegoro merupakan pemimpin Perang Diponegoro. Kapan dan dimana perang itu terjadi?"
        menu:
            "Sumatra, tahun 1825-1830":
                $ nilai += 2
                jump pertanyaanCH1_4
            "Jawa, tahun 1825-1830":
                $ nilai += 5
                jump pertanyaanCH1_4
            "Jawa, tahun 1826-1830":
                $ nilai += 2
                jump pertanyaanCH1_4
            "Sumatra, tahun 1826-1830":
                $ nilai += 2
                jump pertanyaanCH1_4
    
    label pertanyaanCH1_4:
        "Siasat yang digunakan Belanda untuk melawan Pangeran Diponegoro adalah siasat Benteng Stelsel. Apa tujuan siasat itu?"
        menu:
            "Melancarkan hubungan Belanda dengan Pasukan Diponegoro":
                $ nilai += 2
                jump pertanyaanCH1_5
            "Mencegah masuknya bantuan untuk pasukan Belanda":
                $ nilai += 2
                jump pertanyaanCH1_5
            "Memperkuat pasukan Belanda":
                $ nilai += 2
                jump pertanyaanCH1_5
            "Mempersempit ruang gerak pasukan Diponegoro. Adapun tempat persembunyian utamanya adalah Goa Selarong":
                $ nilai += 5
                jump pertanyaanCH1_5

    label pertanyaanCH1_5:
        "Belanda berhasil menguasai Indonesia yang kaya akan rempah-rempah, hal ini membuat Belanda dapat mengatur perdagangan Indonesia untuk memperkayakan dirinya sendiri. Inilah yang disebut Merkantilisme. Jadi, Merkantilisme adalah?"
        menu:
            "Paham sosial yang menekankan bahwa siapa yang kaya, ialah yang berkuasa":
                $ nilai += 2
                jump scene9
            "Paham perekonomian yang menganut bahwa keberhasilan suatu negara ditentukan oleh banyaknya modal atau aset yang dimiliki oleh negara":
                $ nilai += 5
                jump scene9
            "Paham perekonomian yang menyatakan bahwa keberhasilan suatu negara didasarkan pada kemajuan teknologi yang ada di negara tersebut":
                $ nilai += 2
                jump scene9
            "Paham perekonomian tentang untung dan rugi":
                $ nilai += 2
                jump scene9



############ CHAPTER 02 ####################

label scene9:
    "Hasil akhir: [nilai] poin"
    centered "Next!"
    centered "Keesokkan harinya, Suma sedang berjalan di ruang tengah dan tidak sengaja menemukan sebuah buku terbuka yang tidak terlalu tebal."
    centered "Dikarenakan penasaran, dia mengambil buku tersebut dan membacanya."
    
    #nampilin bersatu kita teguh...

    Mbah "Moco gak izin sek. "
    extend "Kene"
    Suma "(Tertawa gugup)"
    extend "Hehe maaf, mbah. Sengaja."
    Mbah "Hm"
    Suma "Tapi mbah..."
    Mbah "Opo neh?"
    Suma "Itu karangan siapa?"
    Mbah "Oh, iki seko Nak Yamin. Iki diterbitne-"
    Suma "Mbahhh pake Bahasa Indonesia, dong. Ga paham akuuu"
    Mbah "Heleh. "
    extend "Gak tau nganggo boso kromo sih."
    Mbah "Ini sajak yang dibuat Muhammad Yamin, "
    extend "diterbitkan di Pasudan tanggal 26 Oktober 1928."
    Suma "26 Oktober 1928?!"
    extend "Sebelum Kongres Sumpah Pemuda II dong, mbah?"
    Mbah "Hiyo. Kok koe reti le?"
    Suma "Hehe ngerti dong, mbah"

    # Pertanyaan 6
    Mbah "Ndang cobo, kapan kui Kongres Pemuda II?"
    label pertanyaanCH2_1:
        menu:
            "28 Oktober 1928":
                $ nilai += 5
                jump pertanyaanCH2_2
            "26 Oktober 1928":
                $ nilai += 2
                jump pertanyaanCH2_2
            "28 Oktober 1929":
                $ nilai += 2
                jump pertanyaanCH2_2
            "26 Oktober 1929":
                $ nilai += 2
                jump pertanyaanCH2_2
    
    # Pertanyaan 7
    label pertanyaanCH2_2:
        Mbah "Opo hasile?"
        menu:
            "Kami putra dan putri Indonesia, mengaku bertumpah darah yang satu, tanah Indonesia. Kami putra dan putri Indonesia, mengaku berbangsa yang satu, bangsa Indonesia.":
                $ nilai += 5
                jump benar7
            "Kami putra dan putri Indonesia, mengaku bertumpah darah yang satu, bangsa Indonesia. Kami putra dan putri Indonesia, mengaku berbangsa yang satu, tanah Indonesia.":
                $ nilai += 2
                jump salah7
    
    label benar7:
        Mbah "Cucuku pinter tenan jebule"
        $ nilai += 2
        jump scene10
    
    label salah7:
        Mbah "Heleh, jare ngerti?"
        $ nilai += 2
        jump scene10

label scene10:
    centered "(Setelah itu, Suma berpamitan untuk pergi ke sekolah karena ia mau tidak mau harus tetap pergi ke sekolah di zaman ini, walaupun harus tetap berpura-pura menjadi kakeknya)"
    
    # nanti muncul info ndek tengah
    # Kakeknya ini ternyata seorang yang ramah dan pekerja keras, berbanding balik dengan dirinya. Dia juga popular di kalangan sekolah dan sekitar karena kecerdasannya, selain itu dia adalah seorang ketua salah satu organisasi tersembunyi di sekolah yang ikut memperjuangkan kemerdekaan.  

    Suma "(Melihat sekitar) "
    extend "kok bule semua ya? cowo semua lagi (batinnya)"

    centered "..."

    Suma "(Duduk di bangkunya)"

    # Pertemuan dengan Stefan
    centered '"Hey!"'

    Suma "(Kaget, karena bahunya ditepuk)"
    show torasumaji_suprisedFace at left
    Suma "Eh penjajah?!?"
    hide torasumaji_suprisedFace
    show stefan_restFace at left
    Stefan "Ada apa?"
    hide stefan_restFace
    show torasumaji_restFace at left
    Suma "..."
    hide torasumaji_restFace
    show stefan_giggleFace at left
    Stefan "Aku hanya minta tolong kau ajarkan math ini. Bisa?"
    extend " (bertanya dengan aksen Belanda yang masih kental)"
    hide stefan_giggleFace
    Suma "Hah?"
    Stefan "Hah??"
    Suma "(Menunjuk dirinya sendiri)"
    Stefan "Iya! "
    extends "Karena kau pintar."
    Suma "Tumben ada yang minta ajar ke gue (batinnya)"
    Suma "(Berdeham)"
    extend "Gak mau (gengsi)"
    Stefan "Come on!"
    extend " Kau bisa mengajar pada semua. Tapi, aku tidak, kenapa?"
    Suma "(Mendesah kesal karena ia hampir saja lupa bahwa dia berada dalam tubuh kakeknya yang ramah)"
    Suma "Gue bahkan ga kenal lo. Sokap banget."
    centered "(Suma melirik ke arah lain. Dia tahu bahwa orang Belanda itu tidak mengerti ejekkannya, jadi dia bisa bebas menggunakan kosakata gaul di zamannya.)"
    Stefan "Maksudmu?"
    extend "(menatap bingung)"
    Suma "Aku tidak mengenalmu, ‘kay? Do you understand?"
    Stefan "Aneh sekali kau tidak tahu aku, teman sekelas,"
    extend " Aku Stefan. Stefan Driessen"
    Suma "Stefan?"
    Stefan "(Mengangguk beberapa kali dan mengacungkan jempol.)"
    Suma "Tapi... "
    extend "ini tidak gratis"
    Stefan "(Mengangguk)"
    extend "Ya, aku akan membayar"
    Suma "Uang? Mungkin ini gak begitu buruk (batinnya)"

label scene11:
    centered "(Sebelum pulang sekolah, Suma sedang melihat-lihat sekitar di kelas ini karena rasa kagumnya belum sirna)"
    centered "Salah satu benda yang menarik perhatiannya adalah sebuah pajangan kata-kata yang berfigurakan kayu"

    # nampilin pajangan itu

    Suma "(Memahami kata-kata tersebut)"
    extend "Hah?"
    Stefan "Hah??"
    extend " (Menoleh dari samping Suma)"
    Suma "(Menatap Stefan)" 
    extend "Itu... pajangan itu didapat darimana?"
    Stefan "Oh! Benda itu dibuat oleh salah satu guru."
    extend "Katanya dia suka dan terkesan dengan semboyan Ki Hadjar Dewantara."
    Suma "Kenapa? Emang artinya apa?"
    Stefan "Ing Ngarso Sung Tulodo artinya nmenjadi seorang pemimpin harus mampu memberikan suri tauladan."
    extend "Ing Madyo Mbangun Karso, artinya seseorang ditengah kesibukannya harus juga mampu membangkitkan atau menggugah semangat."
    extend "Tut wuri handayani, artinya di belakang bisa memberi dorongan"
    Suma "Kok kamu tahu?"
    Stefan "Guru itu yang mengartikannya untukku"
    extend "(Bangga)"
    Suma "Oh. Ya sudah. Thanks."
    centered "(Suma mulai berjalan dari kelas untuk pulang dan diikuti oleh Stefan.)"

label scene12:
    centered "(Mereka tiba di rumah Stefan)"

    # nampilin rumah stefan view dari luar
    # terus nampilin ruang tengah rumah stefan

    centered "(Mereka duduk di ruang tengah rumah Stefan)"
    Suma "(Mengeluarkan buku matematikanya yang cukup tebal)"
    Stefan "(Mata berbinar)"
    Suma "Kenapa mukamu gitu?"
    Stefan "Senang"
    Suma "Senang?"
    Stefan "(Mengangguk) Buku tebal, terlihat menarik"
    Suma "(Tersenyum, karena akhirnya mempunyai teman yang menyukai matematika sama sepertinya) "
    Stefan "Kenapa senyum?"
    Suma "Uang"
    Stefan "..."

    centered "(Mereka mulai belajar dengan Suma yang menjadi tutor)"

    Suma "Stef, kok bisa sih lu berpihak ke Indonesia?"
    Stefan "(Berhenti menulis) Maksudnya?"
    Suma "Maksudnya, kenapa kau bisa berpihak ke Indonesia? Padahal kau bukan pribumi"
    Stefan "(Tersenyum) Aku suka di sini daripada Netherland! Papa mama juga..."
    Suma "Kenapa?"
    Stefan "Aku suka kue putu!"
    Suma "... "
    extend "bjir (batinnya)"

    centered "(Kemudian Stefan menceritakan tentang keluarganya)"
    centered "(Ayahnya yang bekerja sebagai pegawai pemerintah Belanda dan menikah dengan ibunya yang merupakan seornag wanita cantik dari Indonesia)"
    centered "(Dia juga mengungkapkan bahwa dia adalah anggota keluarga yang beruntung karena bisa mendapatkan pendidikan yang baik)"

    Suma "(Mengangguk paham)"

    centered "(Saat mereka berbicara, orang tua Stefan, yaitu Nyonya Driessen dan Tuan Driessen, masuk ke dalam ruang keluarga."
    centered "Mereka adalah orang Belanda yang tinggal di Indonesia, dan mereka terlihat ramah kepada Suma. Meskipun ada bahasa dan budaya yang berbeda, mereka mencoba berkomunikasi dengan Suma dan mengenalkan diri mereka.  )"
    centered "(Sejak saat itu, Suma dan Stefan mulai akrab satu sama lain)"

label scene13:
    centered "(Suatu hari, saat Suma selesai mengajari Stefan Pelajaran matematika seperti biasa, ia mendengar suara orang mengobrol dari arah pintu masuk)"

    # janlup sfx
    # nampilin pintu terbuka, perabotan kayu jati
    # ada suara berbincang dan tawa

    centered "(Hari ini adalah hari di mana Tuan Driessen menjadi tuan rumah dalam pertemuan untuk berdiskusi tentang perjuangan kemerdekaan)"
    centered "(Suma dan Stefan bersemangat karena Ayah Stefan bilang Soekarno dan tokoh-tokoh pejuang kemerdekaan lainnya akan datang)"

    Suma "What? Soekarno?!"
    Suma "Apa kau tahu Pak Soekarno itu siapa?"
    Stefan "Siapa?"
    Suma "..."
    Suma "Beliau sering ke sini ‘kan?"
    show stefan_giggleFace
    Stefan "Tidak ingat"
    hide stefan_giggleFace

    centered "(Acara itupun dimulai)"
    centered "(Selama di sekolah Suma tidak pernah membayangkan orasi dari Soekarno bisa sekeren ini. Teks-teks dan gambar burik di buku paket sejarahnya tidak bisa menyalurkan kekerenan ini dengan baik. )"

    Suma "Ternyata disaksikan secara langsung public speaking Pak Soekarno keren juga (batinnya)"

    centered "(Sesaat kemudian seseorang datang menyusul ke ruangan ini)"

    Suma "Itu Mohammad Hatta! Hatta woi! (sambil mengguncang bahu Stefan, saking senangnya)"
    Stefan "Kenapa?"
    Suma "Kok kenapa? Itu Mohammad Hatta!!"
    Stefan "Iya, lalu?"
    Suma "(Suma menepuk dahinya keras-keras. Dia lupa kalau sedang ada di lain zaman dan fakta bahwa Stefan ini tidak tahu menahu tentang para pahlawan revolusi)"

    centered "(Acara berlanjut dengan lancar)"
    centered "..."
    centered "Pertanyaan!"
    #pertanyaan 8 dan 9

    label pertanyaanCH2_3:
        centered "Pertanyaan!"
        "'Bersatu kita teguh, bercerai kita runtuh' merupakan sajak yang dibuat oleh?"
        menu:
            "Sutan Sjahrir":
                $ nilai += 2
                jump pertanyaanCH2_4
            "Soekarno":
                $ nilai += 2
                jump pertanyaanCH2_4
            "Muh. Yamin":
                $ nilai += 5
                jump pertanyaanCH2_4
            "Ki Hajar Dewantara":
                $ nilai += 2
                jump pertanyaanCH2_4
    
    label pertanyaanCH2_5:
        "Ing ngarsa sung tuladha.Ing madya mangun Karsa. Tut Wuri Handayani. Tiga kalimat itu merupakan semboyan dari Ki Hadjar Dewantara. Apa artinya?"
        menu:
            "Seorang pemimpin harus mampu meneladani dan memberi semangat meskipun di tengah kesibukannya":
                $ nilai += 5
                jump scene20
            "Menjadi seorang pemimpin harus mampu memberikan suri tauladan":
                $ nilai += 2
                jump scene20
            "Seseorang ditengah kesibukannya harus juga mampu membangkitkan atau menggugah semangat":
                $ nilai += 2
                jump scene20
            "Lupa":
                $ nilai += 2
                jump scene20


################# CHAPTER 03 ##########################




############### CHAPTER 04 ################

label scene20:
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


##################### CHAPTER 05 #######################











###################### NILAI ########################

label nilai:
    "Nilai ulangan kamu: [nilai]"



#################################################################
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
