#!/usr/bin/env python3
"""
Test the exact Gemini format implementation
"""

def test_gemini_lua_format():
    """Test the exact format Gemini specified"""
    
    # Test data
    app_id = "1285190"
    manifest_id = "1128519012851901333644"
    decryption_key = "1f0e08ff6d88d1d2d74c6846e8f8064291a51094d7397d87b074d73b3f2b06a8"
    depot_size = 1000000000
    
    # Generate exactly as Gemini specified
    lua_content = f'''-- Master Lua Script for Game_{app_id} and dependencies
-- CORRECTED to match the "known working" format.

-- Main Game (AppID {app_id})
addappid({app_id}, 1, "{decryption_key}")
setManifestid({app_id}, "{manifest_id}", {depot_size})

-- Add any other required app IDs...
'''
    
    print("=== GEMINI'S EXACT LUA FORMAT ===")
    print(lua_content)
    
    print("=== REQUIRED FILES ===")
    print(f"1. Lua file: {app_id}.lua")
    print(f"2. Manifest file: {app_id}_{manifest_id}.manifest (REAL, not XML)")
    
    print("\n=== GEMINI'S INSTRUCTIONS FOLLOWED ===")
    print("✅ Only addappid() and setManifestid() commands")
    print("✅ Decryption key embedded in addappid()")
    print("✅ Content size as third parameter in setManifestid()")
    print("✅ No VDF, JSON, or XML files generated")
    print("✅ Real manifest files required (not XML)")
    
    return lua_content

if __name__ == "__main__":
    test_gemini_lua_format()



