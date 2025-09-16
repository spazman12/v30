#!/usr/bin/env python3
"""
LM Studio Integration for Steam Tools Generator
Provides AI-powered features using local LM Studio server
"""

import requests
import json
import time
from typing import Dict, Any, Optional, List
import threading
from concurrent.futures import ThreadPoolExecutor

class LMStudioIntegration:
    def __init__(self, base_url: str = "http://localhost:1234"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'SteamTools-LMStudio/1.0'
        })
        self.model_id = None
        self.available = False
        self.setup_model()
    
    def setup_model(self) -> bool:
        """Setup and verify model is available"""
        try:
            print("🤖 Setting up LM Studio integration...")
            
            # Get available models
            response = self.session.get(f"{self.base_url}/v1/models", timeout=5)
            if response.status_code != 200:
                print("❌ LM Studio server not accessible")
                self.available = False
                return False
            
            models_data = response.json()
            if 'data' not in models_data or len(models_data['data']) == 0:
                print("❌ No models available in LM Studio")
                self.available = False
                return False
            
            # Use the first available model
            self.model_id = models_data['data'][0]['id']
            self.available = True
            print(f"✅ LM Studio ready with model: {self.model_id}")
            return True
            
        except Exception as e:
            print(f"❌ LM Studio setup failed: {e}")
            self.available = False
            return False
    
    def is_available(self) -> bool:
        """Check if LM Studio is available"""
        return self.available and self.model_id is not None
    
    def generate_text(self, prompt: str, max_tokens: int = 200, temperature: float = 0.7) -> Optional[str]:
        """Generate text using LM Studio"""
        if not self.is_available():
            return None
        
        try:
            payload = {
                "model": self.model_id,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": max_tokens,
                "temperature": temperature
            }
            
            response = self.session.post(
                f"{self.base_url}/v1/chat/completions",
                json=payload,
                timeout=10  # Shorter timeout to avoid hanging
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'choices' in result and len(result['choices']) > 0:
                    return result['choices'][0]['message']['content']
            
            return None
            
        except requests.exceptions.Timeout:
            print(f"❌ LM Studio timeout after 10 seconds")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ LM Studio request error: {e}")
            return None
        except Exception as e:
            print(f"❌ LM Studio generation error: {e}")
            return None
    
    def generate_game_description(self, game_name: str, genre: str = "Game") -> Optional[str]:
        """Generate AI-powered game description"""
        prompt = f"""Generate a professional, engaging description for the Steam game "{game_name}".
        
        Requirements:
        - Genre: {genre}
        - Length: 2-3 sentences (under 150 words)
        - Style: Professional Steam store description
        - Include key features and what makes it unique
        - Make it sound appealing to potential players
        
        Return only the description text, no additional formatting."""
        
        return self.generate_text(prompt, max_tokens=150, temperature=0.7)
    
    def optimize_lua_script(self, lua_script: str) -> Optional[str]:
        """Optimize Lua script with AI suggestions"""
        prompt = f"""Optimize this Steam Tools Lua script for better performance and add helpful comments.
        
        Original script:
        ```lua
        {lua_script}
        ```
        
        Requirements:
        - Add helpful comments explaining each section
        - Optimize for performance where possible
        - Follow Steam Tools best practices
        - Keep the same functionality
        - Make it more readable and maintainable
        
        Return only the optimized Lua code with comments."""
        
        return self.generate_text(prompt, max_tokens=500, temperature=0.3)
    
    def diagnose_steam_error(self, error_message: str, app_id: str = "", depot_id: str = "") -> Optional[str]:
        """Diagnose Steam Tools errors with AI"""
        context = f"App ID: {app_id}" if app_id else ""
        context += f", Depot ID: {depot_id}" if depot_id else ""
        
        prompt = f"""Diagnose this Steam Tools error and provide a solution.
        
        Error: {error_message}
        Context: {context}
        
        Provide:
        1. Likely cause of the error
        2. Step-by-step solution
        3. Prevention tips for the future
        
        Be specific and helpful. Focus on practical solutions."""
        
        return self.generate_text(prompt, max_tokens=400, temperature=0.5)
    
    def generate_steam_tips(self, topic: str = "general") -> Optional[str]:
        """Generate helpful Steam Tools tips"""
        prompt = f"""Generate helpful tips for using Steam Tools, specifically about {topic}.
        
        Include:
        - 3-5 practical tips
        - Common mistakes to avoid
        - Best practices
        - Troubleshooting advice
        
        Make it concise and actionable."""
        
        return self.generate_text(prompt, max_tokens=300, temperature=0.6)
    
    def suggest_improvements(self, current_setup: str) -> Optional[str]:
        """Suggest improvements for current Steam Tools setup"""
        prompt = f"""Analyze this Steam Tools setup and suggest improvements:
        
        Current setup:
        {current_setup}
        
        Suggest:
        - Performance optimizations
        - Security improvements
        - Better organization
        - Additional features to consider
        
        Be specific and practical."""
        
        return self.generate_text(prompt, max_tokens=400, temperature=0.4)
    
    def generate_async(self, prompt: str, callback, max_tokens: int = 200, temperature: float = 0.7):
        """Generate text asynchronously with callback"""
        def _generate():
            result = self.generate_text(prompt, max_tokens, temperature)
            callback(result)
        
        thread = threading.Thread(target=_generate)
        thread.daemon = True
        thread.start()
    
    def test_connection(self) -> Dict[str, Any]:
        """Test LM Studio connection and return status"""
        status = {
            'available': self.is_available(),
            'model_id': self.model_id,
            'base_url': self.base_url,
            'response_time': None,
            'test_result': None
        }
        
        if not self.available:
            return status
        
        try:
            start_time = time.time()
            test_result = self.generate_text("Hello! This is a connection test.", max_tokens=10)
            end_time = time.time()
            
            status['response_time'] = end_time - start_time
            status['test_result'] = test_result is not None
            
        except Exception as e:
            status['test_result'] = False
            status['error'] = str(e)
        
        return status

# Global instance for easy access
lm_studio = LMStudioIntegration()
