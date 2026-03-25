# Anime-super-navigation
Anime Super Navigation is the ultimate resource hub for otaku worldwide. We curate 50+ legal anime streaming platforms, manga readers, light novel sites, and international resources—so you spend less time searching and more time watching. From Crunchyroll simulcasts to hidden gem platforms in Asia, find your next obsession with our organized, 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anime Super Navigation - A Must-Have for Anime Fans</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Noto Sans JP', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 25%, #0f3460 50%, #533483 75%, #e94560 100%);
            min-height: 100vh;
            color: #ffffff;
            overflow-x: hidden;
        }

        /* Animated background particles */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
            z-index: 0;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            animation: float 15s infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) rotate(720deg); opacity: 0; }
        }

        /* Navigation Bar */
        .navbar {
            background: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            font-weight: 900;
            background: linear-gradient(90deg, #00d4ff, #7b2cbf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .logo::before {
            content: "⚡";
            font-size: 2rem;
            -webkit-text-fill-color: #00d4ff;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
            font-weight: 700;
            transition: all 0.3s ease;
            position: relative;
            padding: 0.5rem 0;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #00d4ff, #e94560);
            transition: width 0.3s ease;
        }

        .nav-links a:hover {
            color: #ffffff;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Search Section */
        .search-section {
            text-align: center;
            padding: 4rem 2rem 2rem;
            position: relative;
            z-index: 1;
        }

        .search-container {
            max-width: 700px;
            margin: 0 auto;
            position: relative;
        }

        .search-box {
            width: 100%;
            padding: 1.2rem 3rem 1.2rem 1.5rem;
            font-size: 1.1rem;
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-radius: 50px;
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
            color: #ffffff;
            outline: none;
            transition: all 0.3s ease;
        }

        .search-box::placeholder {
            color: rgba(255, 255, 255, 0.5);
        }

        .search-box:focus {
            border-color: #00d4ff;
            box-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
        }

        .search-btn {
            position: absolute;
            right: 5px;
            top: 50%;
            transform: translateY(-50%);
            background: linear-gradient(135deg, #00d4ff, #7b2cbf);
            border: none;
            padding: 0.9rem 1.5rem;
            border-radius: 50px;
            color: white;
            cursor: pointer;
            font-weight: 700;
            transition: all 0.3s ease;
        }

        .search-btn:hover {
            transform: translateY(-50%) scale(1.05);
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.4);
        }

        /* Main Content */
        .main-content {
            position: relative;
            z-index: 1;
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        /* Section Styles */
        .section {
            margin-bottom: 4rem;
            animation: fadeInUp 0.8s ease-out;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .section-header {
            text-align: center;
            margin-bottom: 2.5rem;
        }

        .section-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            background: linear-gradient(90deg, #ffffff, #00d4ff, #e94560);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .section-subtitle {
            color: rgba(255, 255, 255, 0.7);
            font-size: 1.1rem;
            font-style: italic;
        }

        /* Card Grid */
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 1.5rem;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.5s ease;
        }

        .card:hover::before {
            left: 100%;
        }

        .card:hover {
            transform: translateY(-10px) scale(1.02);
            border-color: rgba(0, 212, 255, 0.5);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 30px rgba(0, 212, 255, 0.2);
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .card-icon {
            width: 60px;
            height: 60px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.2), rgba(123, 44, 191, 0.2));
            border: 2px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }

        .card:hover .card-icon {
            transform: rotate(10deg) scale(1.1);
            border-color: #00d4ff;
        }

        .card-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: #ffffff;
        }

        .card-desc {
            color: rgba(255, 255, 255, 0.7);
            line-height: 1.6;
            font-size: 0.95rem;
        }

        .card-tags {
            display: flex;
            gap: 0.5rem;
            margin-top: 1rem;
            flex-wrap: wrap;
        }

        .tag {
            background: rgba(0, 212, 255, 0.2);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.75rem;
            color: #00d4ff;
            border: 1px solid rgba(0, 212, 255, 0.3);
        }

        /* Footer */
        .footer {
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(20px);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding: 2rem;
            text-align: center;
            position: relative;
            z-index: 1;
        }

        .footer-content {
            max-width: 800px;
            margin: 0 auto;
        }

        .copyright {
            color: rgba(255, 255, 255, 0.5);
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
        }

        .footer-links a {
            color: #00d4ff;
            text-decoration: none;
            font-weight: 700;
            transition: all 0.3s ease;
            position: relative;
        }

        .footer-links a::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 0;
            height: 2px;
            background: #e94560;
            transition: width 0.3s ease;
        }

        .footer-links a:hover {
            color: #e94560;
        }

        .footer-links a:hover::after {
            width: 100%;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                gap: 1rem;
            }

            .nav-links {
                flex-wrap: wrap;
                justify-content: center;
                gap: 1rem;
            }

            .section-title {
                font-size: 1.5rem;
            }

            .card-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Animated Particles -->
    <div class="particles" id="particles"></div>

    <!-- Navigation Bar -->
    <nav class="navbar">
        <div class="logo">ANIME NAV</div>
        <ul class="nav-links">
            <li><a href="#platforms">Main Platforms</a></li>
            <li><a href="#essential">Essential Tools</a></li>
            <li><a href="#comics">Comics & Novels</a></li>
            <li><a href="#international">International</a></li>
        </ul>
    </nav>

    <!-- Search Section -->
    <section class="search-section">
        <div class="search-container">
            <input type="text" class="search-box" placeholder="Search for anime platforms, series, or resources...">
            <button class="search-btn">Search</button>
        </div>
    </section>

    <!-- Main Content -->
    <main class="main-content">

        <!-- Section 1: Main Platforms -->
        <section class="section" id="platforms">
            <div class="section-header">
                <h2 class="section-title">Main Platforms</h2>
                <p class="section-subtitle">The biggest names in anime streaming - your gateway to endless adventures</p>
            </div>
            <div class="card-grid">
                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🍊</div>
                        <h3 class="card-title">Crunchyroll</h3>
                    </div>
                    <p class="card-desc">The world's largest anime streaming platform with over 1,000 titles. Features simulcasts one hour after Japan broadcast, including hits like Jujutsu Kaisen, Demon Slayer, and One Piece.</p>
                    <div class="card-tags">
                        <span class="tag">Simulcast</span>
                        <span class="tag">Legal</span>
                        <span class="tag">Premium</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🎬</div>
                        <h3 class="card-title">Netflix</h3>
                    </div>
                    <p class="card-desc">Home to exclusive Netflix Originals like Cyberpunk: Edgerunners, Devilman Crybaby, and Pluto. Also streams classics like Neon Genesis Evangelion with high production quality.</p>
                    <div class="card-tags">
                        <span class="tag">Originals</span>
                        <span class="tag">4K</span>
                        <span class="tag">Movies</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">📺</div>
                        <h3 class="card-title">Hulu</h3>
                    </div>
                    <p class="card-desc">Solid anime hub with 300+ titles including Attack on Titan, My Hero Academia, and exclusive rights to Bleach: Thousand-Year Blood War. Great for mainstream series.</p>
                    <div class="card-tags">
                        <span class="tag">Dubbed</span>
                        <span class="tag">Mainstream</span>
                        <span class="tag">US Only</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🌊</div>
                        <h3 class="card-title">HIDIVE</h3>
                    </div>
                    <p class="card-desc">The destination for uncensored anime and adult-oriented content. Features exclusives like Made in Abyss, Call of the Night, and extensive Lupin the 3rd collection.</p>
                    <div class="card-tags">
                        <span class="tag">Uncensored</span>
                        <span class="tag">Niche</span>
                        <span class="tag">Affordable</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">📦</div>
                        <h3 class="card-title">Prime Video</h3>
                    </div>
                    <p class="card-desc">Amazon's growing anime library includes exclusive rights to Evangelion Rebuild films and Vinland Saga. Available as standalone or bundled with Prime membership.</p>
                    <div class="card-tags">
                        <span class="tag">Movies</span>
                        <span class="tag">Bundle</span>
                        <span class="tag">Exclusive</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🆓</div>
                        <h3 class="card-title">Tubi</h3>
                    </div>
                    <p class="card-desc">100% free ad-supported streaming with licensed anime from Crunchyroll, Viz Media, and GKIDS. Features Naruto, Pokémon, Sailor Moon, and classic films by Satoshi Kon.</p>
                    <div class="card-tags">
                        <span class="tag">Free</span>
                        <span class="tag">Legal</span>
                        <span class="tag">Classics</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 2: Essential for Anime Fans -->
        <section class="section" id="essential">
            <div class="section-header">
                <h2 class="section-title">Essential for Anime Fans</h2>
                <p class="section-subtitle">Tools and communities every otaku needs in their arsenal</p>
            </div>
            <div class="card-grid">
                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">📋</div>
                        <h3 class="card-title">MyAnimeList</h3>
                    </div>
                    <p class="card-desc">The ultimate anime tracking and database platform. Track your watching progress, rate shows, read reviews, and discover new series with personalized recommendations.</p>
                    <div class="card-tags">
                        <span class="tag">Tracking</span>
                        <span class="tag">Database</span>
                        <span class="tag">Community</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🗨️</div>
                        <h3 class="card-title">AniList</h3>
                    </div>
                    <p class="card-desc">Modern anime and manga tracking with sleek UI. Features advanced filtering, custom lists, and social features to share your anime journey with friends.</p>
                    <div class="card-tags">
                        <span class="tag">Modern UI</span>
                        <span class="tag">Social</span>
                        <span class="tag">Stats</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">📱</div>
                        <h3 class="card-title">AniWatch</h3>
                    </div>
                    <p class="card-desc">Popular free streaming platform with HD quality and minimal ads. Offers both subbed and dubbed versions with a clean, user-friendly interface.</p>
                    <div class="card-tags">
                        <span class="tag">HD</span>
                        <span class="tag">Free</span>
                        <span class="tag">Dual Audio</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🎞️</div>
                        <h3 class="card-title">RetroCrush</h3>
                    </div>
                    <p class="card-desc">Free streaming service dedicated to classic anime from the 70s, 80s, and 90s. Perfect for discovering vintage gems and nostalgic favorites.</p>
                    <div class="card-tags">
                        <span class="tag">Classic</span>
                        <span class="tag">Free</span>
                        <span class="tag">Nostalgia</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🔔</div>
                        <h3 class="card-title">LiveChart</h3>
                    </div>
                    <p class="card-desc">Real-time anime airing schedule and countdown tracker. Never miss a new episode release with detailed seasonal charts and simulcast reminders.</p>
                    <div class="card-tags">
                        <span class="tag">Schedule</span>
                        <span class="tag">Countdown</span>
                        <span class="tag">Seasonal</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🎵</div>
                        <h3 class="card-title">AnimeThemes</h3>
                    </div>
                    <p class="card-desc">Comprehensive database of anime opening and ending themes. Watch high-quality OP/ED videos and discover new music from your favorite series.</p>
                    <div class="card-tags">
                        <span class="tag">Music</span>
                        <span class="tag">OP/ED</span>
                        <span class="tag">Database</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 3: Comics and Light Novels -->
        <section class="section" id="comics">
            <div class="section-header">
                <h2 class="section-title">Comics and Light Novels</h2>
                <p class="section-subtitle">Dive deeper into stories beyond the screen - manga and light novel platforms</p>
            </div>
            <div class="card-grid">
                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">📚</div>
                        <h3 class="card-title">Crunchyroll Manga</h3>
                    </div>
                    <p class="card-desc">Standalone e-reader app integrated with Crunchyroll. Continue your anime stories by reading the original manga with seamless platform switching.</p>
                    <div class="card-tags">
                        <span class="tag">Official</span>
                        <span class="tag">Integrated</span>
                        <span class="tag">Simulpub</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">📖</div>
                        <h3 class="card-title">BookWalker</h3>
                    </div>
                    <p class="card-desc">Kadokawa's digital bookstore with vast light novel and manga catalog. Frequent sales, coin rewards, and exclusive early releases for Japanese titles.</p>
                    <div class="card-tags">
                        <span class="tag">Official</span>
                        <span class="tag">Sales</span>
                        <span class="tag">Kadokawa</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">✍️</div>
                        <h3 class="card-title">J-Novel Club</h3>
                    </div>
                    <p class="card-desc">Specialized light novel publisher with regular new chapter releases. Features both popular and niche titles with professional translations.</p>
                    <div class="card-tags">
                        <span class="tag">LNs Only</span>
                        <span class="tag">Weekly</span>
                        <span class="tag">Membership</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🌐</div>
                        <h3 class="card-title">Syosetu</h3>
                    </div>
                    <p class="card-desc">Japan's largest web novel platform where many hit light novels originate. Free to read with massive collection of user-generated stories.</p>
                    <div class="card-tags">
                        <span class="tag">Web Novels</span>
                        <span class="tag">Free</span>
                        <span class="tag">Japanese</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">📗</div>
                        <h3 class="card-title">Manga Plus</h3>
                    </div>
                    <p class="card-desc">Shueisha's official manga platform offering free simultaneous releases with Japan. Read latest chapters of One Piece, Jujutsu Kaisen, and more for free.</p>
                    <div class="card-tags">
                        <span class="tag">Shueisha</span>
                        <span class="tag">Free</span>
                        <span class="tag">Simultaneous</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">📘</div>
                        <h3 class="card-title">VIZ Manga</h3>
                    </div>
                    <p class="card-desc">Official platform for Shonen Jump series and VIZ Media titles. Access to massive catalog including Dragon Ball, Naruto, and Demon Slayer.</p>
                    <div class="card-tags">
                        <span class="tag">Shonen Jump</span>
                        <span class="tag">Official</span>
                        <span class="tag">Library</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 4: International Resources -->
        <section class="section" id="international">
            <div class="section-header">
                <h2 class="section-title">International Resources</h2>
                <p class="section-subtitle">Global platforms and communities for worldwide anime culture</p>
            </div>
            <div class="card-grid">
                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🇨🇳</div>
                        <h3 class="card-title">Bilibili</h3>
                    </div>
                    <p class="card-desc">China's premier anime and manga platform with massive East Asian content library. Features danmu (bullet comments) for interactive viewing experience.</p>
                    <div class="card-tags">
                        <span class="tag">China</span>
                        <span class="tag">Danmu</span>
                        <span class="tag">Community</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🇰🇷</div>
                        <h3 class="card-title">Webnovel</h3>
                    </div>
                    <p class="card-desc">Major platform for Korean, Chinese, and Japanese web novels. Vast translated library across all genres with daily updates and mobile app.</p>
                    <div class="card-tags">
                        <span class="tag">Korean</span>
                        <span class="tag">Chinese</span>
                        <span class="tag">Web Novels</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🇯🇵</div>
                        <h3 class="card-title">Pixiv</h3>
                    </div>
                    <p class="card-desc">Japan's largest creative community for illustrations, manga, and novels. Discover fan art, original works, and connect with Japanese creators.</p>
                    <div class="card-tags">
                        <span class="tag">Art</span>
                        <span class="tag">Fan Art</span>
                        <span class="tag">Creators</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🌍</div>
                        <h3 class="card-title">AnimeLab</h3>
                    </div>
                    <p class="card-desc">Premium streaming service for Australia and New Zealand. 10,000+ episodes including simulcasts, classics, and exclusives with excellent device support.</p>
                    <div class="card-tags">
                        <span class="tag">ANZ</span>
                        <span class="tag">Simulcast</span>
                        <span class="tag">Exclusive</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🇫🇷</div>
                        <h3 class="card-title">Wakanim</h3>
                    </div>
                    <p class="card-desc">French-based streaming service serving Europe with French dubs and subs. Strong selection of seasonal anime with offline viewing support.</p>
                    <div class="card-tags">
                        <span class="tag">Europe</span>
                        <span class="tag">French</span>
                        <span class="tag">Offline</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🌏</div>
                        <h3 class="card-title">WeTV/iQIYI</h3>
                    </div>
                    <p class="card-desc">Major Asian streaming platforms with growing anime catalogs. Strong presence in Southeast Asia with local language subtitles and dubs.</p>
                    <div class="card-tags">
                        <span class="tag">Asia</span>
                        <span class="tag">Regional</span>
                        <span class="tag">Localized</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 5: Community & Forums -->
        <section class="section" id="community">
            <div class="section-header">
                <h2 class="section-title">Community & Forums</h2>
                <p class="section-subtitle">Connect with fellow fans and discuss your favorite series</p>
            </div>
            <div class="card-grid">
                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">💬</div>
                        <h3 class="card-title">r/anime</h3>
                    </div>
                    <p class="card-desc">Reddit's largest anime community with millions of members. Daily discussions, episode threads, news, and recommendations from global fans.</p>
                    <div class="card-tags">
                        <span class="tag">Reddit</span>
                        <span class="tag">Discussion</span>
                        <span class="tag">News</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🏠</div>
                        <h3 class="card-title">Anime Planet</h3>
                    </div>
                    <p class="card-desc">Legal streaming platform with 45,000+ episodes plus community features. Industry-supported with reviews, recommendations, and manga database.</p>
                    <div class="card-tags">
                        <span class="tag">Legal</span>
                        <span class="tag">Reviews</span>
                        <span class="tag">Community</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🎙️</div>
                        <h3 class="card-title">Anime News Network</h3>
                    </div>
                    <p class="card-desc">Premier anime journalism site with news, reviews, and encyclopedia. Industry authority for over two decades with comprehensive coverage.</p>
                    <div class="card-tags">
                        <span class="tag">News</span>
                        <span class="tag">Reviews</span>
                        <span class="tag">Encyclopedia</span>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <div class="card-icon">🎮</div>
                        <h3 class="card-title">Crunchyroll Forums</h3>
                    </div>
                    <p class="card-desc">Official community forums for Crunchyroll subscribers. Discuss episodes, theories, and connect with fans watching the same simulcasts.</p>
                    <div class="card-tags">
                        <span class="tag">Official</span>
                        <span class="tag">Forums</span>
                        <span class="tag">Theories</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-content">
            <p class="copyright">© 2026 Anime Super Navigation. All rights reserved. This is a fan-made resource guide.</p>
            <div class="footer-links">
                <a href="#privacy">Privacy Policy</a>
                <a href="#terms">Terms of Use</a>
            </div>
        </div>
    </footer>

    <script>
        // Create animated particles
        const particlesContainer = document.getElementById('particles');
        for (let i = 0; i < 50; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 15 + 's';
            particle.style.animationDuration = (15 + Math.random() * 10) + 's';
            particlesContainer.appendChild(particle);
        }

        // Smooth scroll for navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Search functionality
        const searchBox = document.querySelector('.search-box');
        const searchBtn = document.querySelector('.search-btn');
        const cards = document.querySelectorAll('.card');

        function performSearch() {
            const query = searchBox.value.toLowerCase();
            cards.forEach(card => {
                const title = card.querySelector('.card-title').textContent.toLowerCase();
                const desc = card.querySelector('.card-desc').textContent.toLowerCase();
                if (title.includes(query) || desc.includes(query)) {
                    card.style.display = 'block';
                    card.style.animation = 'fadeInUp 0.5s ease-out';
                } else {
                    card.style.display = query === '' ? 'block' : 'none';
                }
            });
        }

        searchBtn.addEventListener('click', performSearch);
        searchBox.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') performSearch();
        });

        // Card hover effects with tilt
        cards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = (y - centerY) / 20;
                const rotateY = (centerX - x) / 20;
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px) scale(1.02)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0) scale(1)';
            });
        });

        // Intersection Observer for scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        document.querySelectorAll('.section').forEach(section => {
            observer.observe(section);
        });
    </script>
</body>
</html>
