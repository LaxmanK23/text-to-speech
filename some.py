import os
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ===== CONFIGURATION =====
PROJECT_PATH = "C:/office/vms"  # <-- Change this to your project path
FILE_EXTENSIONS = [".py", ".js", ".java", ".cpp", ".c", ".ts", ".dart"]  # Added Dart

# Common keywords to ignore for multiple languages
COMMON_KEYWORDS = {
    "python": [
        "def","class","import","from","as","with","return","if","else","elif",
        "for","while","try","except","finally","in","is","None","True","False",
        "self","cls","and","or","not"
    ],
    "js": [
        "function","const","let","var","return","if","else","for","while","switch",
        "case","break","continue","new","this","class","extends","import","export",
        "default","true","false","null","undefined","try","catch","finally","throw"
    ],
    "java": [
        "public","private","protected","class","interface","extends","implements",
        "void","int","float","double","boolean","char","long","short","byte",
        "static","final","return","if","else","for","while","try","catch","new",
        "true","false","null","switch","case","break","continue"
    ],
    "cpp": [
        "int","float","double","char","long","short","unsigned","signed","void",
        "return","if","else","for","while","switch","case","break","continue",
        "new","class","struct","true","false","NULL","namespace","using","include"
    ],
    # "dart": [
    #     "import","library","part","of","show","hide","as","is","in","on","sync",
    #     "async","await","yield","try","catch","finally","throw","if","else","for",
    #     "while","do","switch","case","continue","break","default","true","false",
    #     "null","class","extends","implements","with","enum","typedef","mixin","new",
    #     "const","final","var","late","static","abstract","factory","super","this"
    # ]
}

# Merge all keywords into one set (lowercased)
STOP_WORDS = set(word.lower() for words in COMMON_KEYWORDS.values() for word in words)

# ===== PROCESS CODE FILES =====
all_words = []

for root, dirs, files in os.walk(PROJECT_PATH):
    for file in files:
        if any(file.endswith(ext) for ext in FILE_EXTENSIONS):
            with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()
                # Extract identifiers (variable/function/class names)
                words = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', code)
                # Filter out common keywords
                words = [w for w in words if w.lower() not in STOP_WORDS]
                all_words.extend(words)

# ===== GENERATE WORD CLOUD =====
wordcloud = WordCloud(
    width=1600, height=800,
    background_color='white',
    max_words=200,
    collocations=False
).generate(" ".join(all_words))

# Show Word Cloud
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Optional: Save to file
wordcloud.to_file("smart_code_wordcloud.png")
print("Word cloud saved as smart_code_wordcloud.png")
