---
title: "AtCoder Beginner Contest 370 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 370 振り返り

コンテストには参加できなかったので、後からC問題までを回答した。

- A: LとRの状態を適切に場合分けすれば良い問題。
- B: あらかじめ合成して変化する元素リストを用意しておいて、順番に合成を実施していけば良い。
- C: 要素数最小のもの、についてはSとTの異なる文字の数、とすぐにわかる。この問題のキモは変化する過程のうち辞書順最小のものを記録していくプロセス。今回はO(N^3)の計算量であることがわかったで全てシミュレートしていく方針とした。

## [A Raise Both Hands](https://atcoder.jp/contests/abc370/tasks/370_a)

この問題では、片手だけあげている状態でYesかNoを出力し、それ以外の場合はInvalidを出力する必要がある。場合分けをしっかり書いていけば回答することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int L, R;
  cin >> L >> R;
  if (L == 1 && R == 0)
  {
    cout << "Yes" << endl;
  }
  else if (L == 0 && R == 1)
  {
    cout << "No" << endl;
  }
  else
  {
    cout << "Invalid" << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc370/submissions/57670850)

## [B Binary Alchemy](https://atcoder.jp/contests/abc370/tasks/370_b)

元素番号と合成結果を表すvectorを用意して、すべての合成を実施していけば良い。合成に際しては現在の元素番号と合成する元素の元素番号の大小関係によって生成される元素が異なることに注意が必要になる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<vector<int>> A(N + 1, vector<int>(N + 1, 0));

  for (int i = 1; i <= N; i++)
  {
    for (int j = 1; j <= i; j++)
    {
      cin >> A[i][j];
    }
  }

  int ans = 1;
  for (int i = 1; i <= N; i++)
  {
    if (ans >= i)
    {
      ans = A[ans][i];
    }
    else
    {
      ans = A[i][ans];
    }
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc370/submissions/57671065)

## [C Word Ladder](https://atcoder.jp/contests/abc370/tasks/370_c)

入力文字列SとTに対して、1文字ずつ変化させたもののうち辞書順最小となるものを記録していけば良い。ここで、辞書順最小はmin関数で比較確認することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S, T;
  cin >> S >> T;
  vector<string> X;
  int N = (int)S.size();
  while (S != T)
  {
    string next(N, 'z'); // 長さNで全てzの文字列を生成する。
    for (int i = 0; i < N; i++)
    {
      if (S[i] != T[i])
      {
        string tmpS = S;
        tmpS[i] = T[i]; // S_iだけT_iに変換した文字列を生成
        next = min(next, tmpS);
      }
    }
    X.push_back(next);
    S = next;
  }

  cout << (int)X.size() << endl;
  for (auto s : X)
  {
    cout << s << endl;
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc370/submissions/57919232)
