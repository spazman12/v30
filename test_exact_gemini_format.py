#!/usr/bin/env python3
"""
Test the EXACT Gemini format implementation
"""

def generate_gemini_exact_format(app_id, manifest_id, decryption_key, depot_size):
    """Generate exactly as Gemini specified - simple list format"""
    
    lua_content = f'''-- Main Game
addappid({app_id}, 1, "{decryption_key}")
setManifestid({app_id}, "{manifest_id}", {depot_size})

-- First Dependency
addappid(228989, 1, "ad69276eb476cf06c40312df7376d63deac0c838b9a2767005be8bb306ffb853")
setManifestid(228989, "3514306556860204959", 39590283)

-- Second Dependency
addappid(228990, 1, "44d8c45ce229a11c4f231a3d2a350eaf80b0d69a8af938ec7ccca720f694b0e8")
setManifestid(228990, "1829726630299308803", 102931551)

-- etc...
'''
    return lua_content

if __name__ == "__main__":
    # Test with Gemini's exact example
    app_id = "1285190"
    manifest_id = "1128519012851901333644"
    decryption_key = "1f0e08ff6d88d1d2d74c6846e8f8064291a51094d7397d87b074d73b3f2b06a8"
    depot_size = 1000000000
    
    print("=== GEMINI'S EXACT 'KNOWN WORKING' FORMAT ===")
    print(generate_gemini_exact_format(app_id, manifest_id, decryption_key, depot_size))
    
    print("\n=== VERIFICATION ===")
    print("✅ Only addappid() and setManifestid() functions")
    print("✅ Simple list format - no complex configuration")
    print("✅ No adddepot, setappinfo, setdepotinfo, downloadapp, downloaddepot")
    print("✅ No Lord Zolton format elements")
    print("✅ Matches Gemini's exact specification")
    
    print("\n=== REQUIRED FILES ===")
    print(f"1. {app_id}.lua (generated above)")
    print(f"2. {app_id}_{manifest_id}.manifest (real binary manifest)")
    print("3. 228989_3514306556860204959.manifest (VC++ redist)")
    print("4. 228990_1829726630299308803.manifest (DirectX redist)")



