<!DOCTYPE html>
<html lang="my">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tarot by Nwe Poe</title>
    <link href="https://fonts.googleapis.com/css2?family=Pyidaungsu:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Pyidaungsu', sans-serif;
        }
        body {
            background: radial-gradient(circle at center, #1f0c3a 0%, #0b0314 100%);
            color: #f3e8ff;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container {
            width: 100%;
            max-width: 480px;
            background: rgba(25, 10, 42, 0.9);
            border: 1px solid rgba(212, 175, 55, 0.5);
            border-radius: 28px;
            padding: 24px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.8), 0 0 20px rgba(212, 175, 55, 0.15);
            backdrop-filter: blur(15px);
            margin-bottom: 30px;
        }
        .header {
            text-align: center;
            margin-bottom: 22px;
            position: relative;
        }
        .audio-btn, .lang-btn {
            background: rgba(212, 175, 55, 0.25);
            border: 1px solid #d4af37;
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
        .audio-btn:hover, .lang-btn:hover { background: rgba(212, 175, 55, 0.4); }
        .audio-btn { right: 0; }
        .lang-btn { left: 0; font-size: 11px; font-weight: bold; border-radius: 12px; width: 48px; }

        .brand-title {
            color: #f3e76e;
            font-size: 28px;
            font-weight: 700;
            letter-spacing: 2px;
            background: linear-gradient(to right, #fff, #d4af37, #f3e76e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 2px 12px rgba(212, 175, 55, 0.4);
            margin-top: 5px;
        }
        .brand-subtitle {
            font-size: 11px;
            color: #d4af37;
            letter-spacing: 3px;
            margin-top: 4px;
            text-transform: uppercase;
        }
        .section-title {
            text-align: center;
            font-size: 15px;
            color: #e9d5ff;
            margin: 20px 0 12px 0;
        }
        .categories {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 15px;
        }
        .cat-card {
            background: linear-gradient(135deg, rgba(50, 20, 85, 0.7), rgba(30, 10, 50, 0.7));
            border: 1px solid rgba(212, 175, 55, 0.3);
            border-radius: 16px;
            padding: 16px 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .cat-card:hover, .cat-card.active {
            border-color: #d4af37;
            background: linear-gradient(135deg, rgba(80, 30, 130, 0.9), rgba(50, 15, 80, 0.9));
            box-shadow: 0 0 18px rgba(212, 175, 55, 0.4);
            transform: translateY(-2px);
        }
        .cat-card span {
            display: block;
            margin-top: 6px;
            font-size: 13px;
            font-weight: bold;
        }
        .sub-options-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 20px;
        }
        .sub-option-box {
            background: rgba(45, 18, 78, 0.6);
            border: 1px solid rgba(212, 175, 55, 0.3);
            border-radius: 14px;
            padding: 12px 16px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 13px;
            color: #e9d5ff;
        }
        .sub-option-box:hover, .sub-option-box.active {
            border-color: #d4af37;
            background: rgba(75, 30, 125, 0.9);
            box-shadow: 0 0 12px rgba(212, 175, 55, 0.35);
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
            background: linear-gradient(135deg, #35145c, #160526);
            border: 1.5px solid #d4af37;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.7);
            transition: transform 0.5s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .stacked-card::after {
            content: "🔮";
            font-size: 28px;
        }

        .action-lux-btn {
            background: linear-gradient(135deg, #f3e76e, #d4af37, #aa7c11);
            color: #12081f;
            border: none;
            padding: 13px 28px;
            border-radius: 30px;
            font-size: 14px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5);
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
            border: 2px dashed rgba(212, 175, 55, 0.5);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(25, 10, 45, 0.6);
            font-size: 11px;
            color: #bca8d4;
            text-align: center;
            padding: 5px;
        }
        .slot-box.filled {
            border-style: solid;
            border-color: #d4af37;
            background: #321255;
            color: #f3e76e;
            font-weight: bold;
        }

        .cards-spread-deck {
            display: flex;
            justify-content: center;
            gap: 6px;
            margin: 15px 0;
            overflow-x: auto;
            padding: 12px 0;
            max-width: 100%;
        }
        /* ပိုမိုလှပသော Luxury Tarot Card Design */
        .spread-card-item {
            width: 48px;
            height: 82px;
            background: linear-gradient(135deg, #35145c, #140424);
            border: 1.5px solid #d4af37;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(212, 175, 55, 0.35);
            position: relative;
        }
        .spread-card-item::after {
            content: "🔮";
            font-size: 15px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        .spread-card-item:hover { 
            transform: translateY(-12px); 
            box-shadow: 0 6px 18px rgba(212, 175, 55, 0.7);
        }
        .spread-card-item.chosen {
            opacity: 0.3;
            pointer-events: none;
        }

        .result-section {
            margin-top: 20px;
            background: rgba(25, 10, 45, 0.95);
            border-radius: 20px;
            padding: 20px;
            border: 1px solid rgba(212, 175, 55, 0.6);
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
            border: 1.5px solid #d4af37;
            box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
        }
        .result-content {
            font-size: 13px;
            line-height: 1.8;
            color: #e9d5ff;
            text-align: left;
            margin-top: 15px;
            background: rgba(50, 20, 85, 0.5);
            padding: 16px;
            border-radius: 14px;
            border: 1px solid rgba(212, 175, 55, 0.3);
        }
        
        .admin-update-section {
            margin-top: 25px;
            text-align: center;
            background: rgba(50, 20, 85, 0.75);
            border: 1px solid rgba(212, 175, 55, 0.5);
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
            background: linear-gradient(135deg, #f3e76e, #d4af37, #aa7c11);
            color: #12081f;
            padding: 15px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            font-size: 14px;
            text-align: center;
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
            transition: 0.3s;
        }
        .booking-btn:hover { transform: scale(1.02); }
        .footer {
            text-align: center;
            font-size: 11px;
            color: #9ca3af;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Header -->
        <div class="header">
            <button class="lang-btn" onclick="toggleLanguage()" id="langBtn">ENG</button>
            <button class="audio-btn" onclick="toggleAudio()" id="audioBtn" title="Jazz Music Play/Pause">🎷</button>
            <div style="font-size: 24px;">🔮</div>
            <h1 class="brand-title">Tarot by Nwe Poe</h1>
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
                <span id="c2">ငွေကြေး / စီးပွားရေး</span>
            </div>
            <div class="cat-card" onclick="selectCategory(this, 'health')" data-cat="health">
                <span style="font-size: 20px;">🍃</span>
                <span id="c3">ကျန်းမာရေး</span>
            </div>
            <div class="cat-card" onclick="selectCategory(this, 'education')" data-cat="education">
                <span style="font-size: 20px;">📖</span>
                <span id="c4">ပညာရေး / အလုပ်အကိုင်</span>
            </div>
        </div>

        <!-- Sub-options -->
        <div class="section-title" id="subTitleText" style="font-size: 13px; color: #f3e76e; margin-top: 10px;">အချစ်ရေး အမျိုးအစား ရွေးပါ။</div>
        <div class="sub-options-container" id="subOptionsContainer"></div>

        <!-- Luxury Deck & Shuffle Area -->
        <div class="deck-area" id="deckArea">
            <div class="card-stack-container" onclick="startShuffle()">
                <div class="stacked-card" style="transform: rotate(-6deg) translateY(-4px);"></div>
                <div class="stacked-card" style="transform: rotate(3deg) translateY(-2px);"></div>
                <div class="stacked-card" style="transform: rotate(0deg);"></div>
            </div>
            <button class="action-lux-btn" id="shuffleBtn" onclick="startShuffle()">✨ ကဒ်ကို မွှေမည် (Shuffle)</button>
        </div>

        <!-- Selected Slots (3 Cards Slot) -->
        <div id="selectionArea" style="display:none;">
            <div class="section-title" id="drawStatusText" style="font-size: 13px; color: #f3e76e;">ကဒ် ၃ ချပ် ရွေးချယ်ပါ (0/3)</div>
            <div class="selected-slots">
                <div class="slot-box" id="slot0">၁ ခုမြောက်</div>
                <div class="slot-box" id="slot1">၂ ခုမြောက်</div>
                <div class="slot-box" id="slot2">၃ ခုမြောက်</div>
            </div>
            <p style="text-align: center; font-size: 11px; color: #bca8d4; margin-bottom: 5px;">အောက်ပါ ကဒ်တန်းမှ ကြိုက်နှစ်သက်ရာ ရွေးပါ</p>
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
            <p id="cloudUpdateText" style="font-size: 13px; color: #f3e8ff; margin-bottom: 15px; line-height: 1.6;"></p>
            <div id="cloudWallpaperWrapper" style="display: none;">
                <img id="cloudWallpaperImg" src="" alt="Lucky Wallpaper" style="width: 100%; max-width: 220px; height: auto; border-radius: 12px; border: 1.5px solid #d4af37; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);">
                <p style="font-size: 11px; color: #bca8d4; margin-top: 8px;">ပုံကို ဖိ၍ ဖုန်းမှာ Download ဆွဲသုံးနိုင်ပါသည်</p>
            </div>
        </div>

        <!-- Telegram Direct Booking Link -->
        <div class="social-section">
            <a href="https://t.me/Poe_manager" target="_blank" class="booking-btn" id="bookingBtnText">💬 Telegram ဖြင့် ဆရာမ Nwe Poe ထံ တိုက်ရိုက် မေးမြန်းရန်</a>
        </div>

        <div class="footer" id="footerText">
            © 2026 Tarot by Nwe Poe · All Rights Reserved
        </div>
    </div>

    <!-- Smooth Jazz Music Audio Element (Smooth Cafe Jazz) -->
    <audio id="bgAudio" loop>
        <source src="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf756.mp3?filename=lofi-study-112191.mp3" type="audio/mpeg">
    </audio>

    <script>
        let currentLang = 'mm';
        let selectedCategoryType = 'love';
        let selectedSubOption = 'single';
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
                c2: "ငွေကြေး / စီးပွားရေး",
                c3: "ကျန်းမာရေး",
                c4: "ပညာရေး / အလုပ်အကိုင်",
                subTitleLove: "အချစ်ရေး အမျိုးအစား ရွေးပါ။",
                subTitleFin: "ငွေကြေး/စီးပွားရေး အမျိုးအစား ရွေးပါ။",
                shuffleBtnText: "✨ ကဒ်ကို မွှေမည် (Shuffle)",
                bookingBtnText: "💬 Telegram ဖြင့် ဆရာမ Nwe Poe ထံ တိုက်ရိုက် မေးမြန်းရန်",
                footerText: "© 2026 Tarot by Nwe Poe · All Rights Reserved",
                loveOpts: [
                    { id: 'couple', title: 'လက်ရှိ ချစ်သူ / အိမ်ထောင်ဖက် ဆက်ဆံရေး အခြေအနေ' },
                    { id: 'future', title: 'အနာဂတ် အချစ်ရေး လမ်းကြောင်း ခန့်မှန်းချက်' },
                    { id: 'single', title: 'Single များအတွက် မကြာမီ ကြုံရမည့် အချစ်ရေး နိမိတ်' }
                ],
                finOpts: [
                    { id: 'business', title: 'လုပ်ငန်းသစ် စတင်ရန် နှင့် ရင်းနှီးမြှုပ်နှံမှု အခြေအနေ' },
                    { id: 'money', title: 'ငွေကြေး ဝင်ထွက်မှုနှင့် စုဆောင်းနိုင်စွမ်း' }
                ],
                readings: {
                    love: "✨ **အတိတ် (Past):** သင့်ရဲ့ ယခင်က စိတ်ပိုင်းဆိုင်ရာ ထိခိုက်မှုတွေနဲ့ သင်ခန်းစာယူစရာတွေက ယခုအခါမှာ သင့်ကို ပိုမို ရင့်ကျက်စေခဲ့ပါပြီ။<br><br>✨ **ပစ္စုပ္ပန် (Present):** အချစ်ရေးမှာ တစ်ဦးနှင့်တစ်ဦး နားလည်မှုတည်ဆောက်ဖို့ ကြိုးစားနေရတဲ့ အချိန်ဖြစ်ပြီး သံယောဇဉ် ပိုမိုတိုးပွားလာပါမယ်။<br><br>✨ **အနာဂတ် (Future):** မကြာမီကာလအတွင်း အချစ်ရေးမှာ ပျော်ရွှင်စရာ ကောင်းမွန်တဲ့ အပြောင်းအလဲနဲ့ ဆုံမှတ်တစ်ခုကို ပိုင်ဆိုင်ရပါလိမ့်မယ်။",
                    finance: "✨ **အတိတ် (Past):** ငွေကြေးသုံးစွဲမှုနဲ့ ပတ်သက်ပြီး စဉ်းစားစရာတွေ များခဲ့ပြီး ယခုအခါမှာ အတွေ့အကြုံကောင်းများ ရရှိထားပါပြီ။<br><br>✨ **ပစ္စုပ္ပန် (Present):** စီးပွားရေးလုပ်ငန်း သို့မဟုတ် ဝင်ငွေတိုးတက်ရေးအတွက် အခွင့်အလမ်းကောင်းတွေ တံခါးခေါက်လာမယ့် အချိန်ဖြစ်ပါတယ်။<br><br>✨ **အနာဂတ် (Future):** ငွေကြေးအခက်အခဲများ ပြေလည်ပြီး တည်ငြိမ်ချမ်းသာမှုဆီသို့ အကောင်းဆုံး ဦးတည်သွားနိုင်မယ့် ကံကောင်းခြင်းများ ပိုင်ဆိုင်ရပါမယ်။",
                    health: "✨ **အတိတ် (Past):** ကိုယ်စိတ်နှစ်ပါး ပင်ပန်းနွမ်းနယ်မှုတွေ ရှိခဲ့ဖူးပြီး ခန္ဓာကိုယ် အနားယူဖို့ လိုအပ်နေခဲ့ပါတယ်။<br><br>✨ **ပစ္စုပ္ပန် (Present):** ကျန်းမာရေးအတွက် အထူးသတိထား ဂရုစိုက်ရမည့် ကာလဖြစ်ပြီး အစားအသောက်နဲ့ အနားယူမှုကို ပိုဂရုစိုက်ပါ။<br><br>✨ **အနာဂတ် (Future):** စွမ်းအင်အပြည့်နဲ့ ကျန်းမာရေး အခြေအနေများ သိသိသာသာ တိုးတက်ကောင်းမွန်လာပါလိမ့်မည်။",
                    education: "✨ **အတိတ် (Past):** ပညာရေး သို့မဟုတ် အလုပ်အကိုင် လမ်းကြောင်းမှာ အတားအဆီးအချို့ကို စိတ်ရှည်စွာ ကျော်ဖြတ်ခဲ့ရပါတယ်။<br><br>✨ **ပစ္စုပ္ပန် (Present):** အာရုံစိုက်မှု အပြည့်နဲ့ ကြိုးစားနေရမည့် အချိန်ဖြစ်ပြီး ရည်မှန်းချက်အတွက် ရှေ့ဆက်နေဆဲ ဖြစ်ပါတယ်။<br><br>✨ **အနာဂတ် (Future):** စာမေးပွဲ၊ ရာထူးတိုး သို့မဟုတ် လုပ်ငန်းကိစ္စများ အောင်မြင်မှုရရှိပြီး မျှော်မှန်းထားသည့် ပန်းတိုင်ကို အရောက်လှမ်းနိုင်မည်။"
                }
            },
            eng: {
                brandSub: "Astrology & Tarot Reading",
                secTitle: "Select Your Reading Category",
                c1: "Love & Romance",
                c2: "Finance & Business",
                c3: "Health & Wellness",
                c4: "Career & Education",
                subTitleLove: "Select Love Reading Focus",
                subTitleFin: "Select Financial Reading Focus",
                shuffleBtnText: "✨ Shuffle Deck",
                bookingBtnText: "💬 Book Direct Reading with Nwe Poe on Telegram",
                footerText: "© 2026 Tarot by Nwe Poe · All Rights Reserved",
                loveOpts: [
                    { id: 'couple', title: 'Current Relationship Status & Bond' },
                    { id: 'future', title: 'Future Romance Path Outlook' },
                    { id: 'single', title: 'Upcoming Love Signs for Singles' }
                ],
                finOpts: [
                    { id: 'business', title: 'New Ventures & Investment Prospects' },
                    { id: 'money', title: 'Financial Cash Flow & Savings Forecast' }
                ],
                readings: {
                    love: "✨ **Past:** Previous emotional lessons and experiences have made you wiser and emotionally stronger.<br><br>✨ **Present:** A time of building mutual understanding and deepening affection in your relationship.<br><br>✨ **Future:** A joyful turning point and wonderful new chapter in your romantic life are approaching.",
                    finance: "✨ **Past:** Financial challenges in the past have taught you valuable budgeting wisdom.<br><br>✨ **Present:** New doors of opportunity are opening for business and income growth.<br><br>✨ **Future:** Financial stability and prosperous outcomes are heading your way.",
                    health: "✨ **Past:** You experienced physical or mental burnout requiring careful recuperation.<br><br>✨ **Present:** A period to prioritize self-care, nutrition, and adequate rest.<br><br>✨ **Future:** Renewed energy and noticeable improvements in overall well-being.",
                    education: "✨ **Past:** You navigated obstacles in your studies or professional path with patience.<br><br>✨ **Present:** A focused time requiring dedication toward your current targets.<br><br>✨ **Future:** Success in exams, promotions, and reaching your ultimate goals is assured."
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

            if (type === 'love') {
                subTitle.style.display = 'block';
                subTitle.textContent = translations[currentLang].subTitleLove;
                container.style.display = 'flex';
                translations[currentLang].loveOpts.forEach(opt => {
                    let box = document.createElement('div');
                    box.className = `sub-option-box ${opt.id === selectedSubOption ? 'active' : ''}`;
                    box.textContent = opt.title;
                    box.onclick = () => selectSubOption(opt.id, box);
                    container.appendChild(box);
                });
            } else if (type === 'finance') {
                subTitle.style.display = 'block';
                subTitle.textContent = translations[currentLang].subTitleFin;
                container.style.display = 'flex';
                translations[currentLang].finOpts.forEach(opt => {
                    let box = document.createElement('div');
                    box.className = `sub-option-box ${opt.id === selectedSubOption ? 'active' : ''}`;
                    box.textContent = opt.title;
                    box.onclick = () => selectSubOption(opt.id, box);
                    container.appendChild(box);
                });
            } else {
                subTitle.style.display = 'none';
                container.style.display = 'none';
            }
        }

        function selectSubOption(id, element) {
            selectedSubOption = id;
            document.querySelectorAll('.sub-option-box').forEach(b => b.classList.remove('active'));
            element.classList.add('active');
        }

        function selectCategory(element, type) {
            document.querySelectorAll('.cat-card').forEach(c => c.classList.remove('active'));
            element.classList.add('active');
            selectedCategoryType = type;
            if(type === 'love') selectedSubOption = 'single';
            if(type === 'finance') selectedSubOption = 'business';
            updateSubOptions(type);
            resetApp();
        }

        let isPlaying = false;
        const audio = document.getElementById('bgAudio');
        const audioBtn = document.getElementById('audioBtn');

        function toggleAudio() {
            if (isPlaying) {
                audio.pause();
                audioBtn.textContent = "🎷";
                audioBtn.style.background = "rgba(212, 175, 55, 0.25)";
                isPlaying = false;
            } else {
                audio.play().then(() => {
                    audioBtn.textContent = "🎶";
                    audioBtn.style.background = "rgba(212, 175, 55, 0.6)";
                    isPlaying = true;
                }).catch(e => {
                    console.log("Audio play blocked");
                });
            }
        }

        function startShuffle() {
            const cards = document.querySelectorAll('.stacked-card');
            cards.forEach((card, idx) => {
                card.style.transform = `translate(${Math.random()*45 - 22}px, ${Math.random()*25 - 12}px) rotate(${Math.random()*35 - 17}deg)`;
            });

            setTimeout(() => {
                document.getElementById('deckArea').style.display = 'none';
                document.getElementById('selectionArea').style.display = 'block';
                initSpreadDeck();
            }, 500);
        }

        function initSpreadDeck() {
            const spread = document.getElementById('spreadDeck');
            spread.innerHTML = '';
            chosenCards = [];
            updateSlotsUI();

            for(let i=0; i<12; i++) {
                let cardItem = document.createElement('div');
                cardItem.className = 'spread-card-item';
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

            resContent.innerHTML = translations[currentLang].readings[selectedCategoryType] || translations[currentLang].readings.love;
            resSection.style.display = 'block';
            resSection.scrollIntoView({ behavior: 'smooth' });
        }

        function resetApp() {
            chosenCards = [];
            document.getElementById('resultSection').style.display = 'none';
            document.getElementById('selectionArea').style.display = 'none';
            document.getElementById('deckArea').style.display = 'flex';
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
