---
title: "AtCoder Beginner Contest 372 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 372 振り返り

コンテスト自体には参加できなかったため、後からC問題までを実施した。

- A: 入力文字列に対して、特定の文字'.'を含まないものだけを生成すれば良い問題
- B: 3進数変換して出力する
- C: クエリを発行して文字を変化させるたびに全量探索しているとTLEになってしまう。そのため、変化させた後で変わる可能性のある最小限の範囲だけを確認していけば良い。

## [A delete .](https://atcoder.jp/contests/abc372/tasks/372_a)

入力文字列Sから、'.'を含まない文字列を生成して出力すれば良い。if文で'.'以外の文字の場合に回答変数に追加していけば良い。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S, ans;
  cin >> S;
  for (auto c : S)
  {
    if (c != '.')
    {
      ans += c;
    }
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc372/submissions/58124008)

## [B 3^A](https://atcoder.jp/contests/abc372/tasks/372_b)

正の整数Mを3の倍数で表現したい=>Mを3進数表記した時に各桁の値がそのまま答え、と変換して問題を読むことができる。あとはそのまま3進数変換と各桁の値を追加した配列を用意すればよい。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int M;
  cin >> M;
  vector<int> ans;
  for (int k = 0; k <= 10; ++k)
  {
    for (int i = 0; i < (M % 3); i++)
    {
      ans.push_back(k);
    }
    M /= 3;
  }

  cout << (int)ans.size() << endl;
  for (int i = 0; i < (int)ans.size(); i++)
  {
    if (i != 0)
    {
      cout << " ";
    }
    cout << ans[i];
  }
  cout << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc372/submissions/58124277)

## [C Count ABC Again](https://atcoder.jp/contests/abc372/tasks/372_c)

X文字目を文字Cに変更した文字列Sに含まれる文字列ABCの個数を都度数え上げる、方針ではTLEとなってしまう。そのため、この問題では必要最低限の範囲だけ確認して、含まれるABCの個数が減ったか増えたを確認していく。具体的には

i番目の文字を変更した場合
i-2 => i,i => i+1,i => i+2
の3箇所にABCが含まれていたか、また変更した後に含まれるかを確認すれば良い。確認した結果を変化として記録することで必要な範囲のみの確認を行うことができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, Q;
  string S;
  cin >> N >> Q >> S;
  int ans = 0;
  for (int i = 0; i < (int)S.size() - 2; i++)
  {
    if (S.substr(i, 3) == "ABC")
    {
      ++ans;
    }
  }

  for (int i = 0; i < Q; i++)
  {
    int X;
    char C;
    cin >> X >> C;
    --X;
    // 減少分
    if (2 <= X && S.substr(X - 2, 3) == "ABC")
    {
      --ans;
    }
    if (1 <= X && S.substr(X - 1, 3) == "ABC")
    {
      --ans;
    }
    if (S.substr(X, 3) == "ABC")
    {
      --ans;
    }

    S[X] = C;

    // 増加分
    if (2 <= X && S.substr(X - 2, 3) == "ABC")
    {
      ++ans;
    }
    if (1 <= X && S.substr(X - 1, 3) == "ABC")
    {
      ++ans;
    }
    if (S.substr(X, 3) == "ABC")
    {
      ++ans;
    }
    cout << ans << endl;
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc372/submissions/58124847)
