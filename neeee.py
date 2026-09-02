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
            background: linear-gradient(135deg, #12081f, #07020d);
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
            background: rgba(30, 15, 50, 0.75);
            border: 1px solid rgba(212, 175, 55, 0.4);
            border-radius: 24px;
            padding: 22px;
            box-shadow: 0 12px 35px rgba(0,0,0,0.6);
            backdrop-filter: blur(12px);
            margin-bottom: 25px;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
            position: relative;
        }
        .audio-btn {
            position: absolute;
            top: 0;
            right: 0;
            background: rgba(212, 175, 55, 0.2);
            border: 1px solid #d4af37;
            color: #d4af37;
            border-radius: 50%;
            width: 38px;
            height: 38px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
        }
        .lang-btn {
            position: absolute;
            top: 0;
            left: 0;
            background: rgba(212, 175, 55, 0.2);
            border: 1px solid #d4af37;
            color: #d4af37;
            border-radius: 12px;
            padding: 6px 10px;
            cursor: pointer;
            font-size: 12px;
            font-weight: bold;
        }
        .logo-symbol {
            font-size: 28px;
            margin-bottom: 5px;
        }
        /* Fancy artistic font style for Tarot by Nwe Poe */
        .brand-title {
            color: #f3e76e;
            font-size: 26px;
            font-weight: 700;
            letter-spacing: 2px;
            background: linear-gradient(to right, #fff, #d4af37, #f3e76e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 2px 10px rgba(212, 175, 55, 0.3);
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
            margin: 18px 0 12px 0;
        }
        .categories {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 15px;
        }
        .cat-card {
            background: rgba(45, 20, 75, 0.6);
            border: 1px solid rgba(212, 175, 55, 0.25);
            border-radius: 14px;
            padding: 15px 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .cat-card:hover, .cat-card.active {
            border-color: #d4af37;
            background: rgba(65, 25, 110, 0.85);
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.35);
        }
        .cat-card span {
            display: block;
            margin-top: 6px;
            font-size: 14px;
        }
        .sub-options {
            margin-bottom: 15px;
        }
        .sub-select {
            width: 100%;
            background: rgba(45, 20, 75, 0.85);
            border: 1px solid #d4af37;
            color: #f3e8ff;
            padding: 12px;
            border-radius: 12px;
            font-size: 13px;
            outline: none;
            text-align: center;
        }
        .draw-btn {
            width: 100%;
            background: linear-gradient(135deg, #d4af37, #aa7c11);
            color: #12081f;
            border: none;
            padding: 14px;
            border-radius: 30px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 5px 20px rgba(212, 175, 55, 0.4);
            transition: 0.3s;
        }
        .draw-btn:active {
            transform: scale(0.98);
        }
        .cards-deck {
            display: flex;
            justify-content: center;
            gap: 6px;
            margin: 20px 0;
            overflow-x: auto;
            padding-bottom: 8px;
        }
        .tarot-card-item {
            width: 48px;
            height: 78px;
            background: linear-gradient(135deg, #2a1245, #1a082b);
            border: 1px solid #d4af37;
            border-radius: 6px;
            cursor: pointer;
            transition: transform 0.3s;
            flex-shrink: 0;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }
        .tarot-card-item.selected {
            transform: translateY(-12px);
            border-color: #fff;
            box-shadow: 0 0 12px #d4af37;
        }
        .result-section {
            margin-top: 15px;
            background: rgba(20, 8, 35, 0.85);
            border-radius: 14px;
            padding: 15px;
            border: 1px solid rgba(212, 175, 55, 0.3);
            display: none;
        }
        .result-title {
            color: #f3e76e;
            font-size: 15px;
            margin-bottom: 10px;
            text-align: center;
            border-bottom: 1px solid rgba(212, 175, 55, 0.2);
            padding-bottom: 6px;
        }
        .result-content {
            font-size: 13px;
            line-height: 1.6;
            color: #e9d5ff;
        }
        .social-section {
            text-align: center;
            margin-top: 20px;
        }
        .booking-btn {
            display: block;
            width: 100%;
            background: linear-gradient(135deg, #d4af37, #aa7c11);
            color: #12081f;
            padding: 14px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            font-size: 14px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(212, 175, 55, 0.3);
            transition: 0.3s;
        }
        .booking-btn:hover {
            opacity: 0.95;
        }
        .footer {
            text-align: center;
            font-size: 11px;
            color: #9ca3af;
            margin-top: 18px;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Header -->
        <div class="header">
            <button class="lang-btn" onclick="toggleLanguage()" id="langBtn">ENG / MM</button>
            <button class="audio-btn" onclick="toggleAudio()" id="audioBtn">🔊</button>
            <div class="logo-symbol">🔮</div>
            <h1 class="brand-title">Tarot by Nwe Poe</h1>
            <div class="brand-subtitle" id="brandSub">ဗေဒင်နှင့် ဟောကိန်းများ</div>
        </div>

        <!-- Category Selection -->
        <div class="section-title" id="secTitle">မေးလိုသော ကဏ္ဍကို ရွေးချယ်ပါ။</div>
        <div class="categories" id="catContainer">
            <div class="cat-card active" onclick="selectCategory(this, 'love')" data-cat="love">
                <span style="font-size: 18px;">❤️</span>
                <span id="c1">အချစ်ရေး</span>
            </div>
            <div class="cat-card" onclick="selectCategory(this, 'finance')" data-cat="finance">
                <span style="font-size: 18px;">🪙</span>
                <span id="c2">ငွေကြေး / စီးပွားရေး</span>
            </div>
            <div class="cat-card" onclick="selectCategory(this, 'health')" data-cat="health">
                <span style="font-size: 18px;">🍃</span>
                <span id="c3">ကျန်းမာရေး</span>
            </div>
            <div class="cat-card" onclick="selectCategory(this, 'education')" data-cat="education">
                <span style="font-size: 18px;">📖</span>
                <span id="c4">ပညာရေး / အလုပ်အကိုင်</span>
            </div>
        </div>

        <!-- Sub-options -->
        <div class="sub-options" id="subOptionsContainer">
            <select class="sub-select" id="subCategory">
                <option value="single">Single များအတွက် မကြာမီ ကြုံရမည့် အချစ်ရေး နိမိတ်</option>
                <option value="couple">လက်ရှိ ချစ်သူ / အိမ်ထောင်ဖက် ဆက်ဆံရေး အခြေအနေ</option>
                <option value="future">အနာဂတ် အချစ်ရေး လမ်းကြောင်း ခန့်မှန်းချက်</option>
            </select>
        </div>

        <!-- Draw Button -->
        <button class="draw-btn" onclick="startDrawing()" id="drawBtnText">✨ ကဒ် ၃ ကဒ် ရွေးချယ်မည်</button>

        <!-- Cards Deck Visual -->
        <div class="cards-deck" id="cardsDeck"></div>

        <!-- Result Box -->
        <div class="result-section" id="resultSection">
            <div class="result-title" id="resultTitle">သင့်ရဲ့ တာရော့တ် ဟောကိန်း ရလဒ်</div>
            <div class="result-content" id="resultContent">
                ဟောကိန်းအချက်အလက်များ ဤနေရာတွင် ပေါ်လာပါမည်။
            </div>
        </div>

        <!-- Telegram Direct Booking Link -->
        <div class="social-section">
            <a href="https://t.me/Poe_manager" target="_blank" class="booking-btn" id="bookingBtnText">💬 Telegram ဖြင့် ဆရာမ Nwe Poe ထံ တိုက်ရိုက် မေးမြန်ရန်</a>
        </div>

        <div class="footer" id="footerText">
            © 2026 Tarot by Nwe Poe · All Rights Reserved
        </div>
    </div>

    <!-- Audio Element (Cooling Music) -->
    <audio id="bgAudio" loop>
        <source src="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf756.mp3?filename=relaxing-chill-out-music-110825.mp3" type="audio/mpeg">
    </audio>

    <script>
        // Language state
        let currentLang = 'mm';

        const translations = {
            mm: {
                brandSub: "ဗေဒင်နှင့် ဟောကိန်းများ",
                secTitle: "မေးလိုသော ကဏ္ဍကို ရွေးချယ်ပါ။",
                c1: "အချစ်ရေး",
                c2: "ငွေကြေး / စီးပွားရေး",
                c3: "ကျန်းမာရေး",
                c4: "ပညာရေး / အလုပ်အကိုင်",
                drawBtnText: "✨ ကဒ် ၃ ကဒ် ရွေးချယ်မည်",
                resultTitle: "သင့်ရဲ့ တာရော့တ် ဟောကိန်း ရလဒ်",
                bookingBtnText: "💬 Telegram ဖြင့် ဆရာမ Nwe Poe ထံ တိုက်ရိုက် မေးမြန်ရန်",
                footerText: "© 2026 Tarot by Nwe Poe · All Rights Reserved",
                loveOpts: [
                    `<option value="single">Single များအတွက် မကြာမီ ကြုံရမည့် အချစ်ရေး နိမိတ်</option>`,
                    `<option value="couple">လက်ရှိ ချစ်သူ / အိမ်ထောင်ဖက် ဆက်ဆံရေး အခြေအနေ</option>`,
                    `<option value="future">အနာဂတ် အချစ်ရေး လမ်းကြောင်း ခန့်မှန်းချက်</option>`
                ],
                finOpts: [
                    `<option value="business">လုပ်ငန်းသစ် စတင်ရန် နှင့် ရင်းနှီးမြှုပ်နှံမှု အခြေအနေ</option>`,
                    `<option value="money">ငွေကြေး ဝင်ထွက်မှုနှင့် စုဆောင်းနိုင်စွမ်း</option>`
                ],
                readings: {
                    love: "✨ **အတိတ် (Past):** သင့်ရဲ့ ယခင်က စိတ်ပိုင်းဆိုင်ရာ ထိခိုက်မှုတွေနဲ့ သင်ခန်းစာယူစရာတွေက ယခုအခါမှာ သို့်ကို ပိုမို ရင့်ကျက်စေခဲ့ပါပြီ။<br><br>✨ **ပစ္စုပ္ပန် (Present):** အချစ်ရေးမှာ တစ်ဦးနှင့်တစ်ဦး နားလည်မှုတည်ဆောက်ဖို့ ကြိုးစားနေရတဲ့ အချိန်ဖြစ်ပြီး သံယောဇဉ် ပိုမိုတိုးပွားလာပါမယ်။<br><br>✨ **အနာဂတ် (Future):** မကြာမီကာလအတွင်း အချစ်ရေးမှာ ပျော်ရွှင်စရာ ကောင်းမွန်တဲ့ အပြောင်းအလဲနဲ့ ဆုံမှတ်တစ်ခုကို ပိုင်ဆိုင်ရပါလိမ့်မယ်။",
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
                drawBtnText: "✨ Draw 3 Tarot Cards",
                resultTitle: "Your Tarot Reading Result",
                bookingBtnText: "💬 Book Direct Reading with Nwe Poe on Telegram",
                footerText: "© 2026 Tarot by Nwe Poe · All Rights Reserved",
                loveOpts: [
                    `<option value="single">Upcoming Love Signs for Singles</option>`,
                    `<option value="couple">Current Relationship Status & Bond</option>`,
                    `<option value="future">Future Romance Path Outlook</option>`
                ],
                finOpts: [
                    `<option value="business">New Ventures & Investment Prospects</option>`,
                    `<option value="money">Financial Cash Flow & Savings Forecast</option>`
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
            document.getElementById('brandSub').textContent = translations[currentLang].brandSub;
            document.getElementById('secTitle').textContent = translations[currentLang].secTitle;
            document.getElementById('c1').textContent = translations[currentLang].c1;
            document.getElementById('c2').textContent = translations[currentLang].c2;
            document.getElementById('c3').textContent = translations[currentLang].c3;
            document.getElementById('c4').textContent = translations[currentLang].c4;
            document.getElementById('drawBtnText').textContent = translations[currentLang].drawBtnText;
            document.getElementById('resultTitle').textContent = translations[currentLang].resultTitle;
            document.getElementById('bookingBtnText').textContent = translations[currentLang].bookingBtnText;
            document.getElementById('footerText').textContent = translations[currentLang].footerText;

            // Update active sub-options based on current active category
            const activeCard = document.querySelector('.cat-card.active');
            if (activeCard) {
                const catType = activeCard.getAttribute('data-cat');
                updateSubOptions(catType);
            }
        }

        function updateSubOptions(type) {
            const subContainer = document.getElementById('subOptionsContainer');
            if (type === 'love') {
                subContainer.style.display = 'block';
                subContainer.innerHTML = `<select class="sub-select" id="subCategory">${translations[currentLang].loveOpts.join('')}</select>`;
            } else if (type === 'finance') {
                subContainer.style.display = 'block';
                subContainer.innerHTML = `<select class="sub-select" id="subCategory">${translations[currentLang].finOpts.join('')}</select>`;
            } else {
                subContainer.style.display = 'none';
            }
        }

        let isPlaying = false;
        const audio = document.getElementById('bgAudio');
        const audioBtn = document.getElementById('audioBtn');

        function toggleAudio() {
            if (isPlaying) {
                audio.pause();
                audioBtn.textContent = "🔊";
                isPlaying = false;
            } else {
                audio.play().then(() => {
                    audioBtn.textContent = "🔇";
                    isPlaying = true;
                }).catch(e => {
                    console.log("Audio play blocked");
                });
            }
        }

        let selectedCategoryType = 'love';

        function selectCategory(element, type) {
            document.querySelectorAll('.cat-card').forEach(c => c.classList.remove('active'));
            element.classList.add('active');
            selectedCategoryType = type;
            updateSubOptions(type);
        }

        // Generate visual cards stack
        const deck = document.getElementById('cardsDeck');
        for(let i=0; i<12; i++) {
            let card = document.createElement('div');
            card.className = 'tarot-card-item';
            deck.appendChild(card);
        }

        function startDrawing() {
            const resultSection = document.getElementById('resultSection');
            const resultContent = document.getElementById('resultContent');
            const resultTitle = document.getElementById('resultTitle');
            
            resultSection.style.display = 'block';
            resultTitle.textContent = translations[currentLang].resultTitle;
            resultContent.innerHTML = translations[currentLang].readings[selectedCategoryType] || translations[currentLang].readings.love;
            
            resultSection.scrollIntoView({ behavior: 'smooth' });
        }
    </script>
</body>
</html>
