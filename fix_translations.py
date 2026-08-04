import json
import time
from deep_translator import MyMemoryTranslator, GoogleTranslator

def fix_translations():
    with open('translation_cache.json', 'r', encoding='utf-8') as f:
        cache = json.load(f)
    
    try:
        translator = GoogleTranslator(source='en', target='vi')
    except:
        translator = None
    try:
        mymemory = MyMemoryTranslator(source='en', target='vi')
    except:
        mymemory = None
    
    for k, v in cache.items():
        if 'Lỗi dịch' in v:
            res = ""
            print(f"Trying to fix: {k}")
            if translator:
                try:
                    time.sleep(1)
                    res = translator.translate(k)
                except Exception as e:
                    print("GoogleTranslator failed:", e)
            if not res and mymemory:
                try:
                    time.sleep(1)
                    res = mymemory.translate(k)
                except Exception as e:
                    print("MyMemoryTranslator failed:", e)
            
            if res:
                cache[k] = res
                print(f" -> {res}")
            
    with open('translation_cache.json', 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False)

if __name__ == '__main__':
    fix_translations()
