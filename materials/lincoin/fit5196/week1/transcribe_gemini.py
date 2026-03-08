#!/usr/bin/env python3
"""
使用 Google Gemini 批量转录 quiz 图片
"""

import os
import re
import time

# 配置
IMAGE_DIR = "quiz_images"
OUTPUT_FILE = "quiz_transcribed_gemini.md"
API_KEY = "AIzaSyCUsvpOZ3Q33qhldGUYJsCMER7RNPFI9I8"
BATCH_SIZE = 5
DELAY = 1  # 每次请求间隔（秒）

def natural_sort_key(s):
    """自然排序"""
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split('([0-9]+)', s)]

def get_mime_type(image_path):
    """获取图片 MIME 类型"""
    if image_path.endswith('.png'):
        return "image/png"
    elif image_path.endswith('.jpg') or image_path.endswith('.jpeg'):
        return "image/jpeg"
    return "image/jpeg"

def transcribe_with_gemini(image_path, api_key, model):
    """使用 Google Gemini 转录"""
    try:
        with open(image_path, "rb") as f:
            image_data = f.read()
        
        mime_type = get_mime_type(image_path)
        
        prompt = """Please transcribe this quiz question image into text format.

Requirements:
1. Extract the complete question text
2. Extract all options (a, b, c, d, e, etc.)
3. Preserve the original formatting
4. If there are multiple correct answers, note "(Select all that apply)"
5. Use markdown format

Output format:
**[Question text]**

a. [Option a]
b. [Option b]
c. [Option c]
d. [Option d]
..."""
        
        response = model.generate_content([
            prompt,
            {"mime_type": mime_type, "data": image_data}
        ])
        
        return response.text
    except Exception as e:
        return f"Error: {e}"

def main():
    """主函数"""
    import google.generativeai as genai
    
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-flash-latest')
    
    # 获取所有图片
    images = [f for f in os.listdir(IMAGE_DIR) 
              if f.endswith(('.png', '.jpg', '.jpeg'))]
    images.sort(key=natural_sort_key)
    
    print(f"Found {len(images)} images")
    print(f"Using Gemini API")
    print(f"Estimated time: {len(images) * (DELAY + 2)} seconds\n")
    
    # 批量处理
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("# FIT5196 Week 1 Quiz - Gemini 自动转录版\n\n")
        out.write("> 使用 Google Gemini Flash 自动转录\n")
        out.write(f"> 总题数: {len(images)}\n\n---\n\n")
        
        for i, img in enumerate(images, 1):
            img_path = os.path.join(IMAGE_DIR, img)
            print(f"[{i}/{len(images)}] Processing {img}...", end=" ", flush=True)
            
            # 转录
            result = transcribe_with_gemini(img_path, API_KEY, model)
            
            # 写入文件
            out.write(f"## Question {i}\n\n")
            out.write(f"![Image]({IMAGE_DIR}/{img})\n\n")
            out.write(result)
            out.write("\n\n---\n\n")
            out.flush()
            
            print("Done")
            
            # 暂停避免速率限制
            if i < len(images):
                time.sleep(DELAY)
            
            # 每批处理后显示进度
            if i % BATCH_SIZE == 0:
                progress = i * 100 // len(images)
                print(f"\nProgress: {i}/{len(images)} ({progress}%)\n")
    
    print(f"\n✓ Done! Output saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
