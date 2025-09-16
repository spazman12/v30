import requests
import json
import time
import random
from typing import List, Dict, Tuple, Any
from bs4 import BeautifulSoup

class HybridGameDiscovery:
    def __init__(self, lm_studio_integration=None):
        self.lm = lm_studio_integration
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/html, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        })
        self.request_delay = 2  # Delay between requests to avoid rate limiting
        
        # Configure session for unrestricted access
        self.session.verify = False  # Disable SSL verification
        self.session.timeout = 30
        
        # Disable SSL warnings
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _make_request(self, url: str, timeout: int = 15) -> requests.Response:
        """Make a request with advanced unrestricted methods"""
        import random
        import time
        
        # Try multiple methods to bypass restrictions
        for attempt in range(3):
            try:
                # Random delay to avoid detection
                time.sleep(random.uniform(0.5, 2.0))
                
                # Rotate user agent
                user_agents = [
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0'
                ]
                
                user_agent = random.choice(user_agents)
                headers = self.session.headers.copy()
                headers['User-Agent'] = user_agent
                
                # Add random headers to avoid detection
                headers.update({
                    'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                    'X-Real-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                    'X-Client-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                    'CF-Connecting-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                })
                
                # Make request with unrestricted settings
                response = requests.get(
                    url, 
                    headers=headers,
                    timeout=timeout,
                    verify=False,  # Disable SSL verification
                    allow_redirects=True,
                    stream=False
                )
                
                if response.status_code == 200:
                    return response
                elif response.status_code == 403:
                    print(f"⚠️ 403 from {url.split('/')[2]}, trying different method...")
                    continue
                elif response.status_code == 429:
                    print(f"⚠️ Rate limited by {url.split('/')[2]}, waiting...")
                    time.sleep(random.uniform(5, 10))
                    continue
                else:
                    print(f"⚠️ HTTP {response.status_code} from {url.split('/')[2]}, retrying...")
                    continue
                    
            except requests.exceptions.SSLError as e:
                print(f"⚠️ SSL error for {url.split('/')[2]}, retrying with different method...")
                continue
            except requests.exceptions.Timeout:
                print(f"⚠️ Timeout accessing {url.split('/')[2]}, retrying...")
                continue
            except requests.exceptions.RequestException as e:
                print(f"⚠️ Request error for {url.split('/')[2]}: {e}, retrying...")
                continue
            except Exception as e:
                print(f"⚠️ Unexpected error for {url.split('/')[2]}: {e}, retrying...")
                continue
        
        print(f"❌ All methods failed for {url.split('/')[2]}")
        return None

    def discover_games_hybrid(self, target_count: int = 1000) -> List[Tuple[str, Dict]]:
        """Hybrid discovery using both AI and real internet sources"""
        all_games = []
        
        print(f"🌐 Starting hybrid game discovery (target: {target_count})...")
        
        # 1. Steam API discovery - multiple endpoints
        steam_games = self._discover_from_steam_apis_comprehensive(target_count // 3)
        all_games.extend(steam_games)
        print(f"✅ Steam APIs: {len(steam_games)} games")
        
        # 2. SteamSpy comprehensive scraping
        steamspy_games = self._discover_from_steamspy_comprehensive(target_count // 3)
        all_games.extend(steamspy_games)
        print(f"✅ SteamSpy: {len(steamspy_games)} games")
        
        # 3. SteamDB comprehensive scraping
        steamdb_games = self._discover_from_steamdb_comprehensive(target_count // 3)
        all_games.extend(steamdb_games)
        print(f"✅ SteamDB: {len(steamdb_games)} games")
        
        # 4. Additional Steam sources
        additional_games = self._discover_from_additional_sources(target_count // 4)
        all_games.extend(additional_games)
        print(f"✅ Additional Sources: {len(additional_games)} games")
        
        # 5. AI generation for additional games (if available)
        if self.lm and self.lm.is_available():
            ai_games = self._discover_with_ai(min(100, target_count // 10))  # Small AI requests
            all_games.extend(ai_games)
            print(f"✅ AI Generation: {len(ai_games)} games")
        
        # Remove duplicates
        unique_games = {}
        for app_id, game_info in all_games:
            if app_id not in unique_games:
                unique_games[app_id] = game_info
        
        final_games = list(unique_games.items())
        print(f"🎉 Total unique games discovered: {len(final_games)}")
        
        return final_games

    def _discover_from_steam_apis_comprehensive(self, count: int) -> List[Tuple[str, Dict]]:
        """Comprehensive Steam API discovery with multiple endpoints and pagination"""
        games = []
        
        # Multiple Steam API endpoints
        api_endpoints = [
            "https://store.steampowered.com/api/featuredcategories/",
            "https://store.steampowered.com/api/featured/",
            "https://store.steampowered.com/api/popular/",
            "https://store.steampowered.com/api/topsellers/",
            "https://store.steampowered.com/api/newreleases/",
            "https://store.steampowered.com/api/specials/",
            "https://store.steampowered.com/api/comingsoon/",
            "https://store.steampowered.com/api/trending/",
            "https://store.steampowered.com/api/under_ten/",
            "https://store.steampowered.com/api/under_twenty/",
            "https://store.steampowered.com/api/indie/",
            "https://store.steampowered.com/api/early_access/",
            "https://store.steampowered.com/api/free_to_play/",
            "https://store.steampowered.com/api/vr/",
            "https://store.steampowered.com/api/linux/",
            "https://store.steampowered.com/api/mac/"
        ]
        
        for endpoint in api_endpoints:
            try:
                print(f"🔍 Fetching from Steam API: {endpoint}")
                response = self.session.get(endpoint, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    games.extend(self._parse_steam_api_response(data))
                    time.sleep(0.5)  # Rate limiting
            except Exception as e:
                print(f"❌ Error fetching {endpoint}: {e}")
        
        # Try to get more games by browsing different categories
        category_endpoints = [
            "https://store.steampowered.com/api/appdetails/?appids=730",  # CS2
            "https://store.steampowered.com/api/appdetails/?appids=570",  # Dota 2
            "https://store.steampowered.com/api/appdetails/?appids=271590",  # GTA V
            "https://store.steampowered.com/api/appdetails/?appids=1172470",  # Apex Legends
            "https://store.steampowered.com/api/appdetails/?appids=1244460",  # Baldur's Gate 3
        ]
        
        for endpoint in category_endpoints:
            try:
                response = self.session.get(endpoint, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    games.extend(self._parse_steam_api_response(data))
                    time.sleep(0.5)
            except Exception as e:
                print(f"❌ Error fetching category {endpoint}: {e}")
        
        return games[:count]

    def _discover_from_steam_apis(self, count: int) -> List[Tuple[str, Dict]]:
        """Discover games from Steam's public APIs"""
        games = []
        
        api_endpoints = [
            "https://store.steampowered.com/api/featuredcategories/",
            "https://store.steampowered.com/api/featured/",
            "https://store.steampowered.com/api/popular/",
            "https://store.steampowered.com/api/topsellers/",
            "https://store.steampowered.com/api/newreleases/",
            "https://store.steampowered.com/api/specials/",
            "https://store.steampowered.com/api/comingsoon/"
        ]
        
        for endpoint in api_endpoints:
            try:
                print(f"🔍 Fetching from Steam API: {endpoint}")
                response = self.session.get(endpoint, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    games.extend(self._parse_steam_api_response(data))
                    time.sleep(1)  # Rate limiting
            except Exception as e:
                print(f"❌ Error fetching {endpoint}: {e}")
        
        return games[:count]

    def _parse_steam_api_response(self, data: Dict) -> List[Tuple[str, Dict]]:
        """Parse Steam API response to extract game information"""
        games = []
        
        # Common patterns in Steam API responses
        for key, value in data.items():
            if isinstance(value, dict):
                # Check for apps list
                if 'apps' in value and isinstance(value['apps'], list):
                    for app in value['apps']:
                        if isinstance(app, dict) and 'appid' in app:
                            app_id = str(app['appid'])
                            name = app.get('name', 'Unknown')
                            games.append((app_id, {
                                "name": name,
                                "genre": "Unknown",
                                "developer": "Unknown",
                                "release_year": 0
                            }))
                
                # Check for featured items
                if 'items' in value and isinstance(value['items'], list):
                    for item in value['items']:
                        if isinstance(item, dict) and 'id' in item:
                            app_id = str(item['id'])
                            name = item.get('name', 'Unknown')
                            games.append((app_id, {
                                "name": name,
                                "genre": "Unknown",
                                "developer": "Unknown",
                                "release_year": 0
                            }))
        
        return games

    def _discover_from_steamdb_comprehensive(self, count: int) -> List[Tuple[str, Dict]]:
        """Comprehensive SteamDB discovery with reduced endpoints to avoid 403 errors"""
        games = []
        
        # Reduced endpoints to avoid rate limiting
        steamdb_endpoints = [
            "https://steamdb.info/api/GetMostPlayedGames/",
            "https://steamdb.info/api/GetTopGamesByPlayerCount/",
            "https://steamdb.info/api/GetTopGamesByRevenue/"
        ]
        
        for endpoint in steamdb_endpoints:
            try:
                print(f"🌐 Scraping SteamDB: {endpoint}")
                response = self._make_request(endpoint, timeout=15)
                
                if response is None:
                    continue
                    
                data = response.json()
                if isinstance(data, list):
                    for item in data[:count//len(steamdb_endpoints)]:
                        if isinstance(item, dict) and 'appid' in item:
                            app_id = str(item['appid'])
                            name = item.get('name', 'Unknown')
                            games.append((app_id, {
                                "name": name,
                                "genre": "Unknown",
                                "developer": "Unknown",
                                "release_year": 0
                            }))
            except Exception as e:
                print(f"❌ Error scraping SteamDB {endpoint}: {e}")
        
        return games[:count]

    def _discover_from_additional_sources(self, count: int) -> List[Tuple[str, Dict]]:
        """Discover games from additional sources"""
        games = []
        
        # Steam Charts
        try:
            print("🌐 Scraping Steam Charts...")
            response = self.session.get("https://steamcharts.com/api/v1", timeout=15)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    for item in data[:count//4]:
                        if isinstance(item, dict) and 'appid' in item:
                            app_id = str(item['appid'])
                            name = item.get('name', 'Unknown')
                            games.append((app_id, {
                                "name": name,
                                "genre": "Unknown",
                                "developer": "Unknown",
                                "release_year": 0
                            }))
        except Exception as e:
            print(f"❌ Error scraping Steam Charts: {e}")
        
        # Steam Store search results
        search_terms = [
            "action", "rpg", "strategy", "simulation", "indie", "adventure",
            "sports", "racing", "fighting", "platform", "puzzle", "shooter",
            "horror", "survival", "mmo", "free", "early access", "vr"
        ]
        
        for term in search_terms[:5]:  # Limit to avoid too many requests
            try:
                print(f"🔍 Searching Steam Store for: {term}")
                search_url = f"https://store.steampowered.com/search/?term={term}&supportedlang=english"
                response = self.session.get(search_url, timeout=15)
                if response.status_code == 200:
                    # Parse HTML for app IDs (simplified)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    app_links = soup.find_all('a', href=True)
                    for link in app_links[:count//len(search_terms)]:
                        href = link.get('href', '')
                        if '/app/' in href:
                            try:
                                app_id = href.split('/app/')[1].split('/')[0]
                                if app_id.isdigit():
                                    name = link.get_text(strip=True) or 'Unknown'
                                    games.append((app_id, {
                                        "name": name,
                                        "genre": term.title(),
                                        "developer": "Unknown",
                                        "release_year": 0
                                    }))
                            except:
                                continue
                time.sleep(2)  # Rate limiting
            except Exception as e:
                print(f"❌ Error searching Steam Store for {term}: {e}")
        
        return games[:count]

    def _discover_from_steamdb(self, count: int) -> List[Tuple[str, Dict]]:
        """Discover games by scraping SteamDB"""
        games = []
        
        try:
            print("🌐 Scraping SteamDB...")
            # SteamDB has a JSON API for popular games
            response = self.session.get("https://steamdb.info/api/GetMostPlayedGames/", timeout=15)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    for item in data[:count]:
                        if isinstance(item, dict) and 'appid' in item:
                            app_id = str(item['appid'])
                            name = item.get('name', 'Unknown')
                            games.append((app_id, {
                                "name": name,
                                "genre": "Unknown",
                                "developer": "Unknown",
                                "release_year": 0
                            }))
        except Exception as e:
            print(f"❌ Error scraping SteamDB: {e}")
        
        return games

    def _discover_from_steamspy_comprehensive(self, count: int) -> List[Tuple[str, Dict]]:
        """Comprehensive SteamSpy discovery with reduced endpoints to avoid 403 errors"""
        games = []
        
        # Reduced endpoints to avoid rate limiting
        steamspy_endpoints = [
            "https://steamspy.com/api.php?request=top100forever",
            "https://steamspy.com/api.php?request=top100in2weeks",
            "https://steamspy.com/api.php?request=top100owned",
            "https://steamspy.com/api.php?request=top100recent",
            "https://steamspy.com/api.php?request=genre&genre=Action",
            "https://steamspy.com/api.php?request=genre&genre=RPG",
            "https://steamspy.com/api.php?request=genre&genre=Puzzle",
            "https://steamspy.com/api.php?request=genre&genre=Shooter",
            "https://steamspy.com/api.php?request=genre&genre=Horror",
            "https://steamspy.com/api.php?request=genre&genre=Survival"
        ]
        
        for endpoint in steamspy_endpoints:
            try:
                print(f"🌐 Scraping SteamSpy: {endpoint}")
                response = self._make_request(endpoint, timeout=15)
                
                if response is None:
                    continue
                    
                data = response.json()
                if isinstance(data, dict):
                    for app_id, game_data in data.items():
                        if isinstance(game_data, dict) and len(games) < count:
                            name = game_data.get('name', 'Unknown')
                            genre = game_data.get('genre', 'Unknown')
                            developer = game_data.get('developer', 'Unknown')
                            release_year = 0
                            if 'release_date' in game_data:
                                try:
                                    release_year = int(game_data['release_date'].split(',')[-1].strip())
                                except:
                                    pass
                            
                            games.append((str(app_id), {
                                "name": name,
                                "genre": genre,
                                "developer": developer,
                                "release_year": release_year
                            }))
            except Exception as e:
                print(f"❌ Error scraping SteamSpy {endpoint}: {e}")
        
        return games[:count]

    def _discover_from_steamspy(self, count: int) -> List[Tuple[str, Dict]]:
        """Discover games by scraping SteamSpy"""
        games = []
        
        try:
            print("🌐 Scraping SteamSpy...")
            # SteamSpy API for top games
            response = self.session.get("https://steamspy.com/api.php?request=top100forever", timeout=15)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, dict):
                    for app_id, game_data in list(data.items())[:count]:
                        if isinstance(game_data, dict):
                            name = game_data.get('name', 'Unknown')
                            genre = game_data.get('genre', 'Unknown')
                            developer = game_data.get('developer', 'Unknown')
                            release_year = 0
                            if 'release_date' in game_data:
                                try:
                                    release_year = int(game_data['release_date'].split(',')[-1].strip())
                                except:
                                    pass
                            
                            games.append((str(app_id), {
                                "name": name,
                                "genre": genre,
                                "developer": developer,
                                "release_year": release_year
                            }))
        except Exception as e:
            print(f"❌ Error scraping SteamSpy: {e}")
        
        return games

    def _discover_with_ai(self, count: int) -> List[Tuple[str, Dict]]:
        """Use AI to generate additional games (offline mode)"""
        if not self.lm or not self.lm.is_available():
            return []
        
        games = []
        
        try:
            print(f"🤖 AI generating {count} games (offline mode)...")
            
            # Create a much smaller, focused prompt to avoid timeouts
            prompt = f"""
            List {min(count, 50)} popular Steam games. Format: app_id|name|genre|developer|year
            Examples:
            730|Counter-Strike 2|FPS|Valve|2023
            570|Dota 2|MOBA|Valve|2013
            271590|Grand Theft Auto V|Action|Rockstar North|2015
            """
            
            # Use shorter timeout and smaller token count
            response = self.lm.generate_text(prompt, max_tokens=2000, temperature=0.7)
            
            if response and response.strip():
                games = self._parse_ai_response(response)
            else:
                print("⚠️ AI returned empty response")
            
        except Exception as e:
            print(f"❌ AI generation error: {e}")
        
        return games

    def _parse_ai_response(self, response: str) -> List[Tuple[str, Dict]]:
        """Parse AI response to extract game information"""
        games = []
        
        if not response or not response.strip():
            return games
        
        try:
            # Try to parse as JSON first
            data = json.loads(response)
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and 'app_id' in item and 'name' in item:
                        games.append((str(item['app_id']), {
                            "name": item['name'],
                            "genre": item.get('genre', 'Unknown'),
                            "developer": item.get('developer', 'Unknown'),
                            "release_year": item.get('release_year', 0)
                        }))
        except (json.JSONDecodeError, TypeError):
            # Fallback parsing for pipe-separated format
            lines = response.split('\n')
            for line in lines:
                line = line.strip()
                if '|' in line and not line.startswith('#'):
                    parts = line.split('|')
                    if len(parts) >= 2:
                        try:
                            app_id = parts[0].strip()
                            name = parts[1].strip()
                            genre = parts[2].strip() if len(parts) > 2 else "Unknown"
                            developer = parts[3].strip() if len(parts) > 3 else "Unknown"
                            release_year = 0
                            if len(parts) > 4 and parts[4].strip().isdigit():
                                release_year = int(parts[4].strip())
                            
                            # Validate app_id is numeric
                            if app_id.isdigit() and name:
                                games.append((app_id, {
                                    "name": name,
                                    "genre": genre,
                                    "developer": developer,
                                    "release_year": release_year
                                }))
                        except (ValueError, IndexError):
                            continue
        
        return games

    def discover_by_genre_hybrid(self, genre: str, count: int = 500) -> List[Tuple[str, Dict]]:
        """Discover games by genre using hybrid approach"""
        all_games = self.discover_games_hybrid(count * 2)  # Get more to filter
        
        # Filter by genre
        genre_games = []
        for app_id, game_info in all_games:
            if genre.lower() in game_info.get('genre', '').lower():
                genre_games.append((app_id, game_info))
                if len(genre_games) >= count:
                    break
        
        return genre_games

    def discover_by_developer_hybrid(self, developer: str, count: int = 300) -> List[Tuple[str, Dict]]:
        """Discover games by developer using hybrid approach"""
        all_games = self.discover_games_hybrid(count * 2)  # Get more to filter
        
        # Filter by developer
        dev_games = []
        for app_id, game_info in all_games:
            if developer.lower() in game_info.get('developer', '').lower():
                dev_games.append((app_id, game_info))
                if len(dev_games) >= count:
                    break
        
        return dev_games
