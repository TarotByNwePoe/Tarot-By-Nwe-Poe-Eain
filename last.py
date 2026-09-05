<!DOCTYPE html>
<html lang="my">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nwe Poe Eain Tarot</title>
    <link href="https://fonts.googleapis.com/css2?family=Pyidaungsu:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Pyidaungsu', sans-serif;
        }
        body {
            background: radial-gradient(circle at center, #13241d 0%, #060f0b 100%);
            color: #e2f0d9;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container {
            width: 100%;
            max-width: 480px;
            background: rgba(18, 38, 30, 0.92);
            border: 1px solid rgba(197, 160, 89, 0.5);
            border-radius: 28px;
            padding: 24px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.8), 0 0 25px rgba(46, 125, 50, 0.25);
            backdrop-filter: blur(15px);
            margin-bottom: 30px;
        }
        .header {
            text-align: center;
            margin-bottom: 22px;
            position: relative;
        }
        .audio-btn, .lang-btn {
            background: rgba(197, 160, 89, 0.2);
            border: 1px solid #c5a059;
            color: #f3e76e;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            position: absolute;
            top: 0;
            transition: 0.3s;
        }
        .audio-btn:hover, .lang-btn:hover { background: rgba(197, 160, 89, 0.4); }
        .audio-btn { right: 0; }
        .lang-btn { left: 0; font-size: 11px; font-weight: bold; border-radius: 12px; width: 48px; }

        .brand-title {
            color: #f3e76e;
            font-size: 26px;
            font-weight: 700;
            letter-spacing: 2px;
            background: linear-gradient(to right, #fff, #c5a059, #f3e76e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 2px 12px rgba(197, 160, 89, 0.4);
            margin-top: 5px;
        }
        .brand-subtitle {
            font-size: 11px;
            color: #a3c1ad;
            letter-spacing: 3px;
            margin-top: 4px;
            text-transform: uppercase;
        }
        .section-title {
            text-align: center;
            font-size: 15px;
            color: #c5a059;
            margin: 20px 0 12px 0;
        }
        .categories {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 15px;
        }
        .cat-card {
            background: linear-gradient(135deg, rgba(25, 60, 46, 0.75), rgba(12, 35, 26, 0.75));
            border: 1px solid rgba(197, 160, 89, 0.3);
            border-radius: 16px;
            padding: 16px 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .cat-card:hover, .cat-card.active {
            border-color: #f3e76e;
            background: linear-gradient(135deg, rgba(35, 85, 65, 0.95), rgba(18, 50, 36, 0.95));
            box-shadow: 0 0 18px rgba(197, 160, 89, 0.4);
            transform: translateY(-2px);
        }
        .cat-card span {
            display: block;
            margin-top: 6px;
            font-size: 13px;
            font-weight: bold;
            color: #e2f0d9;
        }
        .sub-options-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 20px;
        }
        .sub-option-box {
            background: rgba(22, 50, 38, 0.8);
            border: 1px solid rgba(197, 160, 89, 0.3);
            border-radius: 14px;
            padding: 12px 16px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 13px;
            color: #e2f0d9;
        }
        .sub-option-box:hover, .sub-option-box.active {
            border-color: #f3e76e;
            background: rgba(35, 85, 65, 0.95);
            box-shadow: 0 0 12px rgba(197, 160, 89, 0.4);
        }

        .deck-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 20px 0;
        }
        .card-stack-container {
            position: relative;
            width: 130px;
            height: 190px;
            margin-bottom: 18px;
            cursor: pointer;
        }
        .stacked-card {
            position: absolute;
            width: 120px;
            height: 180px;
            background: linear-gradient(135deg, #1b4332, #081c15);
            border: 1.5px solid #c5a059;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.7);
            transition: transform 0.5s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .stacked-card::after {
            content: "🌙";
            font-size: 28px;
        }

        .action-lux-btn {
            background: linear-gradient(135deg, #f3e76e, #c5a059, #8d6b2c);
            color: #050d0a;
            border: none;
            padding: 13px 28px;
            border-radius: 30px;
            font-size: 14px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(197, 160, 89, 0.5);
            transition: 0.3s;
        }
        .action-lux-btn:active { transform: scale(0.97); }

        .selected-slots {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin: 15px 0;
        }
        .slot-box {
            width: 75px;
            height: 115px;
            border: 2px dashed rgba(197, 160, 89, 0.5);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(12, 35, 26, 0.6);
            font-size: 11px;
            color: #a3c1ad;
            text-align: center;
            padding: 5px;
        }
        .slot-box.filled {
            border-style: solid;
            border-color: #f3e76e;
            background: #1b4332;
            color: #f3e76e;
            font-weight: bold;
        }

        /* Fan Spread Deck Layout (ပန်ကာပုံစံဖြန့်ခင်းခြင်း) */
        .cards-spread-deck {
            position: relative;
            width: 100%;
            height: 140px;
            margin: 20px 0;
            display: flex;
            justify-content: center;
            align-items: flex-end;
        }
        .spread-card-item {
            position: absolute;
            width: 52px;
            height: 90px;
            background: linear-gradient(135deg, #1b4332, #081c15);
            border: 1.5px solid #c5a059;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
            transform-origin: bottom center;
        }
        .spread-card-item::after {
            content: "🌙";
            font-size: 14px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        .spread-card-item:hover { 
            transform: translateY(-15px) scale(1.1) !important; 
            box-shadow: 0 8px 22px rgba(197, 160, 89, 0.8);
            z-index: 100;
        }
        .spread-card-item.chosen {
            opacity: 0.2;
            pointer-events: none;
        }

        .result-section {
            margin-top: 20px;
            background: rgba(18, 38, 30, 0.95);
            border-radius: 20px;
            padding: 20px;
            border: 1px solid rgba(197, 160, 89, 0.6);
            display: none;
            text-align: center;
        }
        .result-cards-row {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin: 15px 0;
        }
        .result-card-single {
            width: 95px;
            height: 150px;
            object-fit: cover;
            border-radius: 10px;
            border: 1.5px solid #c5a059;
            box-shadow: 0 5px 15px rgba(197, 160, 89, 0.4);
        }
        .result-content {
            font-size: 13px;
            line-height: 1.8;
            color: #e2f0d9;
            text-align: left;
            margin-top: 15px;
            background: rgba(25, 60, 46, 0.6);
            padding: 16px;
            border-radius: 14px;
            border: 1px solid rgba(197, 160, 89, 0.3);
        }
        
        .admin-update-section {
            margin-top: 25px;
            text-align: center;
            background: rgba(25, 60, 46, 0.8);
            border: 1px solid rgba(197, 160, 89, 0.5);
            border-radius: 18px;
            padding: 20px;
            display: none;
            box-shadow: 0 5px 20px rgba(0,0,0,0.5);
        }
        .social-section {
            text-align: center;
            margin-top: 25px;
        }
        .booking-btn {
            display: block;
            width: 100%;
            background: linear-gradient(135deg, #f3e76e, #c5a059, #8d6b2c);
            color: #050d0a;
            padding: 15px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            font-size: 14px;
            text-align: center;
            box-shadow: 0 6px 20px rgba(197, 160, 89, 0.4);
            transition: 0.3s;
        }
        .booking-btn:hover { transform: scale(1.02); }
        .footer {
            text-align: center;
            font-size: 11px;
            color: #8fa89b;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Header -->
        <div class="header">
            <button class="lang-btn" onclick="toggleLanguage()" id="langBtn">ENG</button>
            <button class="audio-btn" onclick="toggleAudio()" id="audioBtn" title="Music Play/Pause">🎵</button>
            <div style="font-size: 24px;">🔮</div>
            <h1 class="brand-title">Nwe Poe Eain Tarot</h1>
            <div class="brand-subtitle" id="brandSub">ဗေဒင်နှင့် ဟောကိန်းများ</div>
        </div>

        <!-- Category Selection -->
        <div class="section-title" id="secTitle">မေးလိုသော ကဏ္ဍကို ရွေးချယ်ပါ။</div>
        <div class="categories" id="catContainer">
            <div class="cat-card active" onclick="selectCategory(this, 'love')" data-cat="love">
                <span style="font-size: 20px;">❤️</span>
                <span id="c1">အချစ်ရေး</span>
            </div>
            <div class="cat-card" onclick="selectCategory(this, 'finance')" data-cat="finance">
                <span style="font-size: 20px;">🪙</span>
                <span id="c2">ငွေကြေးစီးပွားရေး</span>
            </div>
            <div class="cat-card" onclick="selectCategory(this, 'health')" data-cat="health">
                <span style="font-size: 20px;">🍃</span>
                <span id="c3">ကျန်းမာရေး</span>
            </div>
            <div class="cat-card" onclick="selectCategory(this, 'education')" data-cat="education">
                <span style="font-size: 20px;">📖</span>
                <span id="c4">ပညာရေး</span>
            </div>
        </div>

        <!-- Sub-options -->
        <div class="section-title" id="subTitleText" style="font-size: 13px; color: #f3e76e; margin-top: 10px;">အမျိုးအစား ရွေးပါ။</div>
        <div class="sub-options-container" id="subOptionsContainer"></div>

        <!-- Luxury Deck & Shuffle Area (4 seconds animation) -->
        <div class="deck-area" id="deckArea">
            <div class="card-stack-container" onclick="startShuffle()">
                <div class="stacked-card" style="transform: rotate(-6deg) translateY(-4px);"></div>
                <div class="stacked-card" style="transform: rotate(3deg) translateY(-2px);"></div>
                <div class="stacked-card" style="transform: rotate(0deg);"></div>
            </div>
            <button class="action-lux-btn" id="shuffleBtn" onclick="startShuffle()">✨ ကဒ်ကို မွှေမည် (4s)</button>
        </div>

        <!-- Selected Slots (3 Cards Slot) -->
        <div id="selectionArea" style="display:none;">
            <div class="section-title" id="drawStatusText" style="font-size: 13px; color: #f3e76e;">ကဒ် ၃ ချပ် ရွေးချယ်ပါ (0/3)</div>
            <div class="selected-slots">
                <div class="slot-box" id="slot0">၁ ခုမြောက်</div>
                <div class="slot-box" id="slot1">၂ ခုမြောက်</div>
                <div class="slot-box" id="slot2">၃ ခုမြောက်</div>
            </div>
            <p style="text-align: center; font-size: 11px; color: #a3c1ad; margin-bottom: 5px;">အောက်ပါ ကဒ်တန်းမှ ကြိုက်နှစ်သက်ရာ ရွေးပါ</p>
            <div class="cards-spread-deck" id="spreadDeck"></div>
        </div>

        <!-- Result Box -->
        <div class="result-section" id="resultSection">
            <div class="section-title" style="color: #f3e76e; margin-top:0;" id="resHeading">သင့်ရဲ့ တာရော့တ် ဟောကိန်း ရလဒ်</div>
            <div class="result-cards-row" id="resultCardsRow"></div>
            <div class="result-content" id="resultContent">
                ဟောကိန်းအချက်အလက်များ...
            </div>
        </div>

        <!-- Telegram Admin Dynamic Update & Wallpaper Section -->
        <div class="admin-update-section" id="adminUpdateSection">
            <h3 style="color: #f3e76e; font-size: 15px; margin-bottom: 12px;">✨ ယနေ့အတွက် အထူးဟောကိန်းနှင့် အပ်ဒိတ် ✨</h3>
            <p id="cloudUpdateText" style="font-size: 13px; color: #e2f0d9; margin-bottom: 15px; line-height: 1.6;"></p>
            <div id="cloudWallpaperWrapper" style="display: none;">
                <img id="cloudWallpaperImg" src="" alt="Lucky Wallpaper" style="width: 100%; max-width: 220px; height: auto; border-radius: 12px; border: 1.5px solid #c5a059; box-shadow: 0 4px 15px rgba(197, 160, 89, 0.4);">
                <p style="font-size: 11px; color: #a3c1ad; margin-top: 8px;">ပုံကို ဖိ၍ ဖုန်းမှာ Download ဆွဲသုံးနိုင်ပါသည်</p>
            </div>
        </div>

        <!-- Telegram Direct Booking Link -->
        <div class="social-section">
            <a href="https://t.me/Poe_manager" target="_blank" class="booking-btn" id="bookingBtnText">💬 Telegram ဖြင့် တိုက်ရိုက် မေးမြန်းရန်</a>
        </div>

        <div class="footer" id="footerText">
            © 2026 Nwe Poe Eain Tarot · All Rights Reserved
        </div>
    </div>

    <!-- Background Music Audio Element (Connected to mysong.mp3) -->
    <audio id="bgAudio" loop>
        <source src="mysong.mp3" type="audio/mpeg">
    </audio>

    <script>
        let currentLang = 'mm';
        let selectedCategoryType = 'love';
        let selectedSubOption = 'rs_active';
        let chosenCards = [];
        const totalNeeded = 3;

        const tarotImagesPool = [
            { nameMM: "ချစ်သူများ (The Lovers)", nameEN: "The Lovers", img: "https://upload.wikimedia.org/wikipedia/commons/d/db/RWS_Tarot_06_Lovers.jpg" },
            { nameMM: "ဒင်္ဂါးပြားများ၏ အစ (Ace of Pentacles)", nameEN: "Ace of Pentacles", img: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Pents01.jpg" },
            { nameMM: "ကြယ်တာရာ (The Star)", nameEN: "The Star", img: "https://upload.wikimedia.org/wikipedia/commons/d/db/Tarot_The_Star.jpg" },
            { nameMM: "မှော်ဆရာ (The Magician)", nameEN: "The Magician", img: "https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg" },
            { nameMM: "နေမင်းကြီး (The Sun)", nameEN: "The Sun", img: "https://upload.wikimedia.org/wikipedia/commons/1/17/RWS_Tarot_19_Sun.jpg" }
        ];

        const translations = {
            mm: {
                brandSub: "ဗေဒင်နှင့် ဟောကိန်းများ",
                secTitle: "မေးလိုသော ကဏ္ဍကို ရွေးချယ်ပါ။",
                c1: "အချစ်ရေး",
                c2: "ငွေကြေးစီးပွားရေး",
                c3: "ကျန်းမာရေး",
                c4: "ပညာရေး",
                subTitleDefault: "အမျိုးအစား ရွေးပါ။",
                shuffleBtnText: "✨ ကဒ်ကို မွှေမည် (4s)",
                bookingBtnText: "💬 Telegram ဖြင့် တိုက်ရိုက် မေးမြန်းရန်",
                footerText: "© 2026 Nwe Poe Eain Tarot · All Rights Reserved",
                loveOpts: [
                    { id: 'rs_active', title: 'လက်ရှိချစ်သူ / အိမ်ထောင်ဖက် (RS)' },
                    { id: 'marriage', title: 'အိမ်ထောင်ရေး' },
                    { id: 'single_love', title: 'အချစ်ရေး Single (SG)' }
                ],
                loveSubOptions: {
                    rs_active: [
                        { id: 'rs_1', title: 'ရှေ့ဆက်မြဲမလား' },
                        { id: 'rs_2', title: 'ဘာတွေကြုံရဖို့ရှိလဲ' },
                        { id: 'rs_3', title: 'လက်ရှိ RS energy' }
                    ],
                    marriage: [
                        { id: 'm_1', title: 'ရေရှည်မြဲမမြဲ' },
                        { id: 'm_2', title: 'ရှေ့ဆက်အဆင်ပြေမပြေ' }
                    ],
                    single_love: [
                        { id: 'sg_1', title: 'လက်ရှိအချစ်ရေး energy' },
                        { id: 'sg_2', title: 'ရည်းစားရနိုင်မလား' },
                        { id: 'sg_3', title: 'Crush ကပြန်ချစ်နိုင်မလား' },
                        { id: 'sg_4', title: 'Crush နဲ့ကိုယ်နဲ့ energy' },
                        { id: 'sg_5', title: 'EX ပြန်လာမလား' },
                        { id: 'sg_6', title: 'EX နဲ့ကိုယ်နဲ့ energy' },
                        { id: 'sg_7', title: 'No contact အဆက်အသွယ်ပြန်ရမလား' }
                    ]
                },
                finOpts: [
                    { id: 'f_1', title: 'ငွေကြေးပိုရနိုင်ဖို့ရှိလား' },
                    { id: 'f_2', title: 'စီးပွားရေးအဆင်ပြေမလား' },
                    { id: 'f_3', title: 'မိမိငွေကံ' },
                    { id: 'f_4', title: 'စီးပွားရေးကံ' }
                ],
                healthOpts: [
                    { id: 'h_1', title: 'ယေဘုယျကျန်းမာရေးအခြေအနေ' },
                    { id: 'h_2', title: 'ဂရုစိုက်ရမည့်အပိုင်းများ' },
                    { id: 'h_3', title: 'စိတ်ပိုင်းဆိုင်ရာစွမ်းအင်' }
                ],
                eduOpts: [
                    { id: 'e_1', title: 'လက်ရှိပညာရေး' },
                    { id: 'e_2', title: 'စာမေးပွဲအောင်နိုင်လား' }
                ],
                readings: {
                    default: "✨ **အတိတ် (Past):** ယခင်ဖြစ်ရပ်များမှ သင်ခန်းစာယူကာ ရှေ့ဆက်ရမည့် ကာလဖြစ်ပါသည်။<br><br>✨ **ပစ္စုပ္ပန် (Present):** လက်ရှိအခြေအနေကို သတိလက်လွတ်မရှိဘဲ အကောင်းဆုံး တည်ဆောက်နေရချိန် ဖြစ်သည်။<br><br>✨ **အနာဂတ် (Future):** ကြိုးစားမှုအတွက် အကောင်းဆုံးသော ရလဒ်များနှင့် အခွင့်အလမ်းသစ်များ ပိုင်ဆိုင်ရပါမည်။"
                }
            },
            eng: {
                brandSub: "Astrology & Tarot Reading",
                secTitle: "Select Reading Category",
                c1: "Love",
                c2: "Finance & Business",
                c3: "Health",
                c4: "Education",
                subTitleDefault: "Select Option",
                shuffleBtnText: "✨ Shuffle Deck (4s)",
                bookingBtnText: "💬 Book Direct Reading on Telegram",
                footerText: "© 2026 Nwe Poe Eain Tarot · All Rights Reserved",
                loveOpts: [
                    { id: 'rs_active', title: 'Current Relationship (RS)' },
                    { id: 'marriage', title: 'Marriage Outlook' },
                    { id: 'single_love', title: 'Single Love Life (SG)' }
                ],
                loveSubOptions: {
                    rs_active: [
                        { id: 'rs_1', title: 'Will it last long?' },
                        { id: 'rs_2', title: 'What to expect ahead?' },
                        { id: 'rs_3', title: 'Current RS Energy' }
                    ],
                    marriage: [
                        { id: 'm_1', title: 'Long-term stability' },
                        { id: 'm_2', title: 'Future harmony' }
                    ],
                    single_love: [
                        { id: 'sg_1', title: 'Current Love Energy' },
                        { id: 'sg_2', title: 'Will I get a partner?' },
                        { id: 'sg_3', title: 'Will my crush reciprocate?' },
                        { id: 'sg_4', title: 'Crush & My Energy' },
                        { id: 'sg_5', title: 'Will EX return?' },
                        { id: 'sg_6', title: 'EX & My Energy' },
                        { id: 'sg_7', title: 'Will No-Contact end?' }
                    ]
                },
                finOpts: [
                    { id: 'f_1', title: 'Income growth prospect' },
                    { id: 'f_2', title: 'Business success' },
                    { id: 'f_3', title: 'Personal wealth luck' },
                    { id: 'f_4', title: 'Business luck' }
                ],
                healthOpts: [
                    { id: 'h_1', title: 'General health condition' },
                    { id: 'h_2', title: 'Areas to take care of' },
                    { id: 'h_3', title: 'Mental energy status' }
                ],
                eduOpts: [
                    { id: 'e_1', title: 'Current academic progress' },
                    { id: 'e_2', title: 'Exam success likelihood' }
                ],
                readings: {
                    default: "✨ **Past:** Lessons from previous experiences are guiding you forward.<br><br>✨ **Present:** A focused time to build stability with awareness.<br><br>✨ **Future:** Rewarding outcomes and positive new chapters await you."
                }
            }
        };

        function toggleLanguage() {
            currentLang = currentLang === 'mm' ? 'eng' : 'mm';
            document.getElementById('langBtn').textContent = currentLang === 'mm' ? 'ENG' : 'MM';
            document.getElementById('brandSub').textContent = translations[currentLang].brandSub;
            document.getElementById('secTitle').textContent = translations[currentLang].secTitle;
            document.getElementById('c1').textContent = translations[currentLang].c1;
            document.getElementById('c2').textContent = translations[currentLang].c2;
            document.getElementById('c3').textContent = translations[currentLang].c3;
            document.getElementById('c4').textContent = translations[currentLang].c4;
            document.getElementById('shuffleBtn').textContent = translations[currentLang].shuffleBtnText;
            document.getElementById('bookingBtnText').textContent = translations[currentLang].bookingBtnText;
            document.getElementById('footerText').textContent = translations[currentLang].footerText;
            updateSubOptions(selectedCategoryType);
        }

        function updateSubOptions(type) {
            const container = document.getElementById('subOptionsContainer');
            const subTitle = document.getElementById('subTitleText');
            container.innerHTML = '';
            subTitle.style.display = 'block';

            let options = [];
            if (type === 'love') {
                translations[currentLang].loveOpts.forEach(opt => {
                    let box = document.createElement('div');
                    box.className = `sub-option-box ${opt.id === selectedSubOption ? 'active' : ''}`;
                    box.textContent = opt.title;
                    box.onclick = () => {
                        selectedSubOption = opt.id;
                        updateSubOptions('love');
                    };
                    container.appendChild(box);
                });

                let subContainer = document.createElement('div');
                subContainer.style.cssText = "margin-top: 10px; display: flex; flex-direction: column; gap: 6px; border-left: 2px solid #c5a059; padding-left: 10px;";
                
                let activeSubList = translations[currentLang].loveSubOptions[selectedSubOption] || [];
                activeSubList.forEach(sub => {
                    let sBox = document.createElement('div');
                    sBox.className = "sub-option-box";
                    sBox.style.fontSize = "12px";
                    sBox.style.background = "rgba(12, 35, 26, 0.5)";
                    sBox.textContent = "🔹 " + sub.title;
                    subContainer.appendChild(sBox);
                });
                container.appendChild(subContainer);

            } else {
                if (type === 'finance') options = translations[currentLang].finOpts;
                if (type === 'health') options = translations[currentLang].healthOpts;
                if (type === 'education') options = translations[currentLang].eduOpts;

                options.forEach(opt => {
                    let box = document.createElement('div');
                    box.className = `sub-option-box`;
                    box.textContent = opt.title;
                    container.appendChild(box);
                });
            }
        }

        function selectCategory(element, type) {
            document.querySelectorAll('.cat-card').forEach(c => c.classList.remove('active'));
            element.classList.add('active');
            selectedCategoryType = type;
            if(type === 'love') selectedSubOption = 'rs_active';
            updateSubOptions(type);
            resetApp();
        }

        let isPlaying = false;
        const audio = document.getElementById('bgAudio');
        const audioBtn = document.getElementById('audioBtn');

        function toggleAudio() {
            if (isPlaying) {
                audio.pause();
                audioBtn.textContent = "🎵";
                audioBtn.style.background = "rgba(197, 160, 89, 0.2)";
                isPlaying = false;
            } else {
                audio.play().then(() => {
                    audioBtn.textContent = "🎶";
                    audioBtn.style.background = "rgba(197, 160, 89, 0.5)";
                    isPlaying = true;
                }).catch(e => {
                    console.log("Audio play blocked");
                });
            }
        }

        // ကဒ်ကို 4 စက္ကန့်ကြာ မွှေပေးမည့် Animation
        function startShuffle() {
            const cards = document.querySelectorAll('.stacked-card');
            
            let shuffleInterval = setInterval(() => {
                cards.forEach((card) => {
                    card.style.transform = `translate(${Math.random()*60 - 30}px, ${Math.random()*40 - 20}px) rotate(${Math.random()*50 - 25}deg)`;
                });
            }, 300);

            document.getElementById('shuffleBtn').textContent = "✨ မွှေနေသည် (4s)...";
            document.getElementById('shuffleBtn').style.opacity = "0.7";
            document.getElementById('shuffleBtn').style.pointerEvents = "none";

            setTimeout(() => {
                clearInterval(shuffleInterval);
                document.getElementById('deckArea').style.display = 'none';
                document.getElementById('selectionArea').style.display = 'block';
                initFanSpreadDeck();
            }, 4000);
        }

        // ပန်ကာပုံစံ (Fan Spread) ဖြန့်ခင်းခြင်း
        function initFanSpreadDeck() {
            const spread = document.getElementById('spreadDeck');
            spread.innerHTML = '';
            chosenCards = [];
            updateSlotsUI();

            let totalCards = 12;
            let angleRange = 120;
            let startAngle = -60;

            for(let i=0; i<totalCards; i++) {
                let cardItem = document.createElement('div');
                cardItem.className = 'spread-card-item';
                
                let angle = startAngle + (i * (angleRange / (totalCards - 1)));
                let xOffset = (i - totalCards / 2) * 14;
                
                cardItem.style.transform = `translateX(${xOffset}px) rotate(${angle}deg)`;
                cardItem.style.transformOrigin = "bottom center";
                
                cardItem.onclick = () => pickCard(cardItem);
                spread.appendChild(cardItem);
            }
        }

        function pickCard(cardElement) {
            if(cardElement.classList.contains('chosen')) return;
            if(chosenCards.length < totalNeeded) {
                cardElement.classList.add('chosen');
                chosenCards.push(cardElement);
                updateSlotsUI();

                if(chosenCards.length === totalNeeded) {
                    setTimeout(showFinalResult, 400);
                }
            }
        }

        function updateSlotsUI() {
            for(let i=0; i<totalNeeded; i++) {
                let slot = document.getElementById(`slot${i}`);
                if(i < chosenCards.length) {
                    slot.classList.add('filled');
                    slot.textContent = currentLang === 'mm' ? `ကဒ် #${i+1} ရွေးပြီး` : `Card #${i+1} Set`;
                } else {
                    slot.classList.remove('filled');
                    slot.textContent = currentLang === 'mm' ? `${i+1} ခုမြောက်` : `Slot ${i+1}`;
                }
            }
            const statusText = document.getElementById('drawStatusText');
            if(currentLang === 'mm') {
                statusText.textContent = `ကဒ် ၃ ချပ် ရွေးချယ်ပါ (${chosenCards.length}/${totalNeeded})`;
            } else {
                statusText.textContent = `Select 3 Cards (${chosenCards.length}/${totalNeeded})`;
            }
        }

        function showFinalResult() {
            document.getElementById('selectionArea').style.display = 'none';
            const resSection = document.getElementById('resultSection');
            const resRow = document.getElementById('resultCardsRow');
            const resContent = document.getElementById('resultContent');

            resRow.innerHTML = '';
            let shuffledPool = [...tarotImagesPool].sort(() => 0.5 - Math.random());
            for(let i=0; i<3; i++) {
                let img = document.createElement('img');
                img.className = 'result-card-single';
                img.src = shuffledPool[i].img;
                resRow.appendChild(img);
            }

            resContent.innerHTML = translations[currentLang].readings.default;
            resSection.style.display = 'block';
            resSection.scrollIntoView({ behavior: 'smooth' });
        }

        function resetApp() {
            chosenCards = [];
            document.getElementById('resultSection').style.display = 'none';
            document.getElementById('selectionArea').style.display = 'none';
            document.getElementById('deckArea').style.display = 'flex';
            document.getElementById('shuffleBtn').textContent = "✨ ကဒ်ကို မွှေမည် (4s)";
            document.getElementById('shuffleBtn').style.opacity = "1";
            document.getElementById('shuffleBtn').style.pointerEvents = "auto";
            
            const cards = document.querySelectorAll('.stacked-card');
            if(cards.length >= 3) {
                cards[0].style.transform = 'rotate(-6deg) translateY(-4px)';
                cards[1].style.transform = 'rotate(3deg) translateY(-2px)';
                cards[2].style.transform = 'rotate(0deg)';
            }
        }

        // Fetch Cloud Updates & Wallpaper from JSONbin automatically
        async function loadCloudUpdate() {
            try {
                let response = await fetch('https://api.jsonbin.io/v3/b/6a9bbd0cda38895dfe3b586a/latest', {
                    headers: {
                        'X-Master-Key': '$2a$10$5eUPNJ5q3AqVn4CZ9imWoecZ/iqGOVjmPy48kAneG6P.YzdS0aTbm'
                    }
                });
                let data = await response.json();
                
                if(data.record) {
                    let updateSection = document.getElementById('adminUpdateSection');
                    let updateText = document.getElementById('cloudUpdateText');
                    let wallImg = document.getElementById('cloudWallpaperImg');
                    let wallWrapper = document.getElementById('cloudWallpaperWrapper');

                    if(data.record.daily_update) {
                        updateText.innerHTML = data.record.daily_update;
                        updateSection.style.display = 'block';
                    }

                    if(data.record.wallpaper_url) {
                        wallImg.src = data.record.wallpaper_url;
                        wallWrapper.style.display = 'block';
                    }
                }
            } catch (e) {
                console.log("Error fetching cloud update:", e);
            }
        }

        updateSubOptions('love');
        window.addEventListener('DOMContentLoaded', () => {
            loadCloudUpdate();
        });
    </script>
</body>
</html>
