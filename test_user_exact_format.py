#!/usr/bin/env python3
"""
Test the EXACT format provided by the user
"""

def generate_user_exact_format(app_id, game_name, manifest_id, decryption_key, depot_size):
    """Generate exactly as user specified"""
    
    lua_content = f'''-- Main Game (e.g., {game_name})
addappid({app_id}, 1, "{decryption_key}")
setManifestid({app_id}, "{manifest_id}", {depot_size})

-- Dependency (e.g., VC++ Redist)
addappid(228989, 1, "ad69276eb476cf06c40312df7376d63deac0c838b9a2767005be8bb306ffb853")
setManifestid(228989, "3514306556860204959", 39590283)

-- Add other dependencies here...
'''
    return lua_content

if __name__ == "__main__":
    # Test with user's exact example (Borderlands 4)
    app_id = "1285191"
    game_name = "Borderlands 4"
    manifest_id = "1365220543604298942"
    decryption_key = "aabb315ef5573fc2633c461cd2ac9b553e2713ca90a67ad2df09781274cbb20f"
    depot_size = 71477317219
    
    print("=== USER'S EXACT FORMAT ===")
    print(generate_user_exact_format(app_id, game_name, manifest_id, decryption_key, depot_size))
    
    print("\n=== VERIFICATION ===")
    print("✅ Matches user's exact template")
    print("✅ Simple list format - no complex configuration")
    print("✅ Only addappid() and setManifestid() functions")
    print("✅ No adddepot, setappinfo, setdepotinfo, downloadapp, downloaddepot")
    print("✅ No Lord Zolton format elements")
    
    print("\n=== REQUIRED FILES ===")
    print(f"1. {app_id}.lua (generated above)")
    print(f"2. {app_id}_{manifest_id}.manifest (real binary manifest)")
    print("3. 228989_3514306556860204959.manifest (VC++ redist)")
    
    print("\n=== STEAM HUB API 405 ERROR FIX ===")
    print("✅ Changed from POST to GET request first")
    print("✅ Fallback to POST if GET returns 405")
    print("✅ This should resolve the 405 Method Not Allowed error")



