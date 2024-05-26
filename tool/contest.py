import os
import sys

def createArticleFile(contestNumber):
  directory = "./articles"
  if not os.path.exists(directory):
    os.makedirs(directory)

  fileName = f"contest-abc{contestNumber}.md"
  filePath = os.path.join(directory, fileName)
  content = f"""---
title: "AtCoder Beginner Contest {contestNumber} 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: false
---

# AtCoder Beginner Contest {contestNumber} 振り返り

- A: 
- B: 
- C: 

## [A problem](https://atcoder.jp/contests/abc{contestNumber}/tasks/{contestNumber}_a)

```cpp

```

[提出結果]()

## [B problem](https://atcoder.jp/contests/abc{contestNumber}/tasks/{contestNumber}_b)

```cpp

```

[提出結果]()

## [C problem](https://atcoder.jp/contests/abc{contestNumber}/tasks/{contestNumber}_c)

```cpp

```

[提出結果]()
"""
  with open(filePath, "w", encoding="utf-8") as file:
    file.write(content)


# AtCoder Beginner Contest 354 振り返り

  print(f"Article file created at {filePath}")


def main():
  if len(sys.argv) != 2:
    print("Usage: python create_article.py abcXXX")
    return
  
  arg = sys.argv[1]
  if not arg.startswith("abc") or not arg[3:].isdigit() or len(arg[3:]) != 3:
    print("Invalid argument format. Expected format: abcXXX where XXX is a 3-digit number.")
    return
  
  contestNumber = arg[3:]
  createArticleFile(contestNumber)

if __name__ == "__main__":
  print("Start script...")
  main()
  print("End script...")