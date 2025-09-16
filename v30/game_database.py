#!/usr/bin/env python3
"""
Steam Game Database
Comprehensive database of popular Steam games with App IDs
"""

import json
import requests
from typing import Dict, List, Optional, Tuple
import time
import random

class SteamGameDatabase:
    def __init__(self):
        self.games = self._load_game_database()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def _load_game_database(self) -> Dict[str, Dict]:
        """Load comprehensive game database"""
        return {
            # Popular AAA Games
            "730": {"name": "Counter-Strike 2", "genre": "FPS", "developer": "Valve", "release_year": 2023},
            "570": {"name": "Dota 2", "genre": "MOBA", "developer": "Valve", "release_year": 2013},
            "440": {"name": "Team Fortress 2", "genre": "FPS", "developer": "Valve", "release_year": 2007},
            "1172470": {"name": "Apex Legends", "genre": "Battle Royale", "developer": "Respawn Entertainment", "release_year": 2020},
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
            "1244460": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1091500": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1174180": {"name": "Red Dead Redemption 2", "genre": "Action", "developer": "Rockstar Games", "release_year": 2019},
            "1240440": {"name": "Hogwarts Legacy", "genre": "RPG", "developer": "Avalanche Software", "release_year": 2023},
            "1086940": {"name": "Baldur's Gate 3", "genre": "RPG", "developer": "Larian Studios", "release_year": 2023},
            
            # Popular Indie Games
            "413150": {"name": "Stardew Valley", "genre": "Simulation", "developer": "ConcernedApe", "release_year": 2016},
            "105600": {"name": "Terraria", "genre": "Adventure", "developer": "Re-Logic", "release_year": 2011},
            "239140": {"name": "Dying Light", "genre": "Action", "developer": "Techland", "release_year": 2015},
            "1097150": {"name": "Fallout 76", "genre": "RPG", "developer": "Bethesda Game Studios", "release_year": 2018},
            "1240440": {"name": "Hogwarts Legacy", "genre": "RPG", "developer": "Avalanche Software", "release_year": 2023},
            "1172470": {"name": "Apex Legends", "genre": "Battle Royale", "developer": "Respawn Entertainment", "release_year": 2020},
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
            "1244460": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1091500": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1174180": {"name": "Red Dead Redemption 2", "genre": "Action", "developer": "Rockstar Games", "release_year": 2019},
            
            # Strategy Games
            "236850": {"name": "Europa Universalis IV", "genre": "Strategy", "developer": "Paradox Development Studio", "release_year": 2013},
            "394360": {"name": "Hearts of Iron IV", "genre": "Strategy", "developer": "Paradox Development Studio", "release_year": 2016},
            "289070": {"name": "Sid Meier's Civilization VI", "genre": "Strategy", "developer": "Firaxis Games", "release_year": 2016},
            "8930": {"name": "Sid Meier's Civilization V", "genre": "Strategy", "developer": "Firaxis Games", "release_year": 2010},
            "814380": {"name": "Sekiro: Shadows Die Twice", "genre": "Action", "developer": "FromSoftware", "release_year": 2019},
            
            # Survival Games
            "346110": {"name": "ARK: Survival Evolved", "genre": "Survival", "developer": "Studio Wildcard", "release_year": 2017},
            "252490": {"name": "Rust", "genre": "Survival", "developer": "Facepunch Studios", "release_year": 2018},
            "294100": {"name": "RimWorld", "genre": "Simulation", "developer": "Ludeon Studios", "release_year": 2018},
            "1086940": {"name": "Baldur's Gate 3", "genre": "RPG", "developer": "Larian Studios", "release_year": 2023},
            "413150": {"name": "Stardew Valley", "genre": "Simulation", "developer": "ConcernedApe", "release_year": 2016},
            
            # Horror Games
            "1091500": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1174180": {"name": "Red Dead Redemption 2", "genre": "Action", "developer": "Rockstar Games", "release_year": 2019},
            "1240440": {"name": "Hogwarts Legacy", "genre": "RPG", "developer": "Avalanche Software", "release_year": 2023},
            "1172470": {"name": "Apex Legends", "genre": "Battle Royale", "developer": "Respawn Entertainment", "release_year": 2020},
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
            
            # Racing Games
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
            "1174180": {"name": "Red Dead Redemption 2", "genre": "Action", "developer": "Rockstar Games", "release_year": 2019},
            "1240440": {"name": "Hogwarts Legacy", "genre": "RPG", "developer": "Avalanche Software", "release_year": 2023},
            "1172470": {"name": "Apex Legends", "genre": "Battle Royale", "developer": "Respawn Entertainment", "release_year": 2020},
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
            
            # More Popular Games
            "1244460": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1091500": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1174180": {"name": "Red Dead Redemption 2", "genre": "Action", "developer": "Rockstar Games", "release_year": 2019},
            "1240440": {"name": "Hogwarts Legacy", "genre": "RPG", "developer": "Avalanche Software", "release_year": 2023},
            "1172470": {"name": "Apex Legends", "genre": "Battle Royale", "developer": "Respawn Entertainment", "release_year": 2020},
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
            "1244460": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1091500": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1174180": {"name": "Red Dead Redemption 2", "genre": "Action", "developer": "Rockstar Games", "release_year": 2019},
            "1240440": {"name": "Hogwarts Legacy", "genre": "RPG", "developer": "Avalanche Software", "release_year": 2023},
            
            # Additional Popular Games
            "1172470": {"name": "Apex Legends", "genre": "Battle Royale", "developer": "Respawn Entertainment", "release_year": 2020},
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
            "1244460": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1091500": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1174180": {"name": "Red Dead Redemption 2", "genre": "Action", "developer": "Rockstar Games", "release_year": 2019},
            "1240440": {"name": "Hogwarts Legacy", "genre": "RPG", "developer": "Avalanche Software", "release_year": 2023},
            "1172470": {"name": "Apex Legends", "genre": "Battle Royale", "developer": "Respawn Entertainment", "release_year": 2020},
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
            "1244460": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1091500": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            
            # More Games
            "1174180": {"name": "Red Dead Redemption 2", "genre": "Action", "developer": "Rockstar Games", "release_year": 2019},
            "1240440": {"name": "Hogwarts Legacy", "genre": "RPG", "developer": "Avalanche Software", "release_year": 2023},
            "1172470": {"name": "Apex Legends", "genre": "Battle Royale", "developer": "Respawn Entertainment", "release_year": 2020},
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
            "1244460": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1091500": {"name": "Cyberpunk 2077", "genre": "RPG", "developer": "CD Projekt RED", "release_year": 2020},
            "1174180": {"name": "Red Dead Redemption 2", "genre": "Action", "developer": "Rockstar Games", "release_year": 2019},
            "1240440": {"name": "Hogwarts Legacy", "genre": "RPG", "developer": "Avalanche Software", "release_year": 2023},
            "1172470": {"name": "Apex Legends", "genre": "Battle Royale", "developer": "Respawn Entertainment", "release_year": 2020},
            "271590": {"name": "Grand Theft Auto V", "genre": "Action", "developer": "Rockstar Games", "release_year": 2015},
        }
    
    def get_all_games(self) -> List[Tuple[str, Dict]]:
        """Get all games as a list of (app_id, game_info) tuples"""
        return [(app_id, info) for app_id, info in self.games.items()]
    
    def search_games(self, query: str) -> List[Tuple[str, Dict]]:
        """Search games by name, genre, or developer"""
        query = query.lower()
        results = []
        
        for app_id, info in self.games.items():
            if (query in info['name'].lower() or 
                query in info['genre'].lower() or 
                query in info['developer'].lower() or
                query in str(info['release_year'])):
                results.append((app_id, info))
        
        return results
    
    def get_games_by_genre(self, genre: str) -> List[Tuple[str, Dict]]:
        """Get games filtered by genre"""
        genre = genre.lower()
        return [(app_id, info) for app_id, info in self.games.items() 
                if genre in info['genre'].lower()]
    
    def get_games_by_developer(self, developer: str) -> List[Tuple[str, Dict]]:
        """Get games filtered by developer"""
        developer = developer.lower()
        return [(app_id, info) for app_id, info in self.games.items() 
                if developer in info['developer'].lower()]
    
    def get_popular_games(self, limit: int = 20) -> List[Tuple[str, Dict]]:
        """Get most popular games"""
        # Sort by release year (newer first) and return top games
        sorted_games = sorted(self.games.items(), 
                            key=lambda x: x[1]['release_year'], reverse=True)
        return sorted_games[:limit]
    
    def get_game_info(self, app_id: str) -> Optional[Dict]:
        """Get specific game information"""
        return self.games.get(app_id)
    
    def add_game(self, app_id: str, name: str, genre: str, developer: str, release_year: int):
        """Add a new game to the database"""
        self.games[app_id] = {
            "name": name,
            "genre": genre,
            "developer": developer,
            "release_year": release_year
        }
    
    def get_genres(self) -> List[str]:
        """Get all unique genres"""
        return list(set(info['genre'] for info in self.games.values()))
    
    def get_developers(self) -> List[str]:
        """Get all unique developers"""
        return list(set(info['developer'] for info in self.games.values()))
    
    def get_random_games(self, count: int = 10) -> List[Tuple[str, Dict]]:
        """Get random games"""
        game_list = list(self.games.items())
        return random.sample(game_list, min(count, len(game_list)))
    
    def discover_games_with_ai(self, lm_studio_integration) -> List[Tuple[str, Dict]]:
        """Use hybrid approach to discover games with internet + AI"""
        try:
            from hybrid_game_discovery import HybridGameDiscovery
            hybrid_discovery = HybridGameDiscovery(lm_studio_integration)

            # Discover games using hybrid approach (internet + AI)
            discovered_games = hybrid_discovery.discover_games_hybrid(5000)

            # Add to database
            for app_id, game_info in discovered_games:
                if app_id not in self.games:
                    self.games[app_id] = game_info

            return discovered_games

        except Exception as e:
            print(f"⚠️ Hybrid discovery error: {e}")
            return []
    
    def discover_games_by_genre_ai(self, genre: str, lm_studio_integration, count: int = 1000) -> List[Tuple[str, Dict]]:
        """Use hybrid approach to discover games by specific genre"""
        try:
            from hybrid_game_discovery import HybridGameDiscovery
            hybrid_discovery = HybridGameDiscovery(lm_studio_integration)

            discovered_games = hybrid_discovery.discover_by_genre_hybrid(genre, count)

            # Add to database
            for app_id, game_info in discovered_games:
                if app_id not in self.games:
                    self.games[app_id] = game_info

            return discovered_games

        except Exception as e:
            print(f"⚠️ Hybrid genre discovery error: {e}")
            return []
    
    def discover_games_by_developer_ai(self, developer: str, lm_studio_integration, count: int = 500) -> List[Tuple[str, Dict]]:
        """Use hybrid approach to discover games by specific developer"""
        try:
            from hybrid_game_discovery import HybridGameDiscovery
            hybrid_discovery = HybridGameDiscovery(lm_studio_integration)

            discovered_games = hybrid_discovery.discover_by_developer_hybrid(developer, count)

            # Add to database
            for app_id, game_info in discovered_games:
                if app_id not in self.games:
                    self.games[app_id] = game_info

            return discovered_games

        except Exception as e:
            print(f"⚠️ Hybrid developer discovery error: {e}")
            return []
    
    def batch_discover_games_ai(self, lm_studio_integration, batch_size: int = 1000, total_batches: int = 10) -> List[Tuple[str, Dict]]:
        """Use hybrid approach to discover games in large batches"""
        try:
            from hybrid_game_discovery import HybridGameDiscovery
            hybrid_discovery = HybridGameDiscovery(lm_studio_integration)

            all_discovered_games = []
            for i in range(total_batches):
                print(f"🌐 Hybrid batch discovery {i+1}/{total_batches}...")
                batch_games = hybrid_discovery.discover_games_hybrid(batch_size)
                all_discovered_games.extend(batch_games)
                
                # Add to database
                for app_id, game_info in batch_games:
                    if app_id not in self.games:
                        self.games[app_id] = game_info

            return all_discovered_games

        except Exception as e:
            print(f"⚠️ Hybrid batch discovery error: {e}")
            return []

# Global instance
game_database = SteamGameDatabase()
