#!/usr/bin/env python3
"""
Test script to demonstrate the corrected file generation
based on Gemini AI feedback
"""

# Simulate the corrected generation functions
def generate_corrected_lua(app_id, game_name, depot_id, manifest_id, decryption_key):
    """Generate corrected Lua file with proper setappinfo and setdepotinfo commands"""
    lua_content = f'''-- Steam Tools Lua File for {game_name}
-- App ID: {app_id}
-- Depot ID: {depot_id}
-- Manifest ID: {manifest_id}

-- Add the app and depot with their respective keys and manifest IDs
addappid({app_id}, 1, "{decryption_key}")
adddepot({depot_id}, 1, "{manifest_id}")

-- Set app information to make it visible in the tool
setappinfo({app_id}, "name", "{game_name}")
setappinfo({app_id}, "type", "Game")
setappinfo({app_id}, "oslist", "windows")
setappinfo({app_id}, "depots", "{depot_id}")
setappinfo({app_id}, "state", "4")
setappinfo({app_id}, "installdir", "{game_name}")
setappinfo({app_id}, "launch", "{game_name}.exe")
setappinfo({app_id}, "userconfig", "")

-- Set depot information
setdepotinfo({depot_id}, "name", "{game_name} Depot")
setdepotinfo({depot_id}, "config", "depot")
setdepotinfo({depot_id}, "oslist", "windows")
setdepotinfo({depot_id}, "manifests", "{manifest_id}")

-- Force download trigger
downloadapp({app_id})
downloaddepot({depot_id})

print("Steam Tools: {game_name} added successfully!")
'''
    return lua_content

def generate_corrected_vdf(depot_id, decryption_key):
    """Generate corrected VDF file in the proper format"""
    vdf_content = f'''"DepotDecryptionKey"
{{
\t"{depot_id}" "{decryption_key}"
}}'''
    return vdf_content

def generate_placeholder_manifest(app_id, depot_id, manifest_id):
    """Generate placeholder manifest with size 0"""
    manifest_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest>
    <appid>{app_id}</appid>
    <depotid>{depot_id}</depotid>
    <manifestid>{manifest_id}</manifestid>
    <size>0</size>
    <compressed_size>0</compressed_size>
    <files>
        <!-- Placeholder manifest - Steam Tools will download the real one -->
    </files>
</manifest>'''
    return manifest_content

# Test with Borderlands 4 example
if __name__ == "__main__":
    app_id = "1285191"
    game_name = "Borderlands 4"
    depot_id = "1285191"
    manifest_id = "1365220543604298942"
    decryption_key = "aabb315ef5573fc2633c461cd2ac9b553e2713ca90a67ad2df09781274cbb20f"
    
    print("=== CORRECTED LUA FILE ===")
    print(generate_corrected_lua(app_id, game_name, depot_id, manifest_id, decryption_key))
    
    print("\n=== CORRECTED VDF FILE ===")
    print(generate_corrected_vdf(depot_id, decryption_key))
    
    print("\n=== PLACEHOLDER MANIFEST ===")
    print(generate_placeholder_manifest(app_id, depot_id, manifest_id))
    
    print("\n=== SUMMARY ===")
    print("✅ Lua file now uses setappinfo() and setdepotinfo() commands")
    print("✅ VDF file uses correct 'DepotDecryptionKey' format")
    print("✅ Manifest is a placeholder with size 0 (Steam Tools will download real one)")
    print("✅ Files are structured for single app configuration (not multiple apps)")
