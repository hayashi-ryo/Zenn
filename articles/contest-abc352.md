---
title: "AtCoder Beginner Contest 352 振り返り"
emoji: "📒"
type: "idea" # tech: 技術記事 / idea: アイデア
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true # true: published / false: unpublished
---

# AtCoder Beginner Contest 352 振り返り

C問題までを回答した。

- A: Zが特定の範囲内に存在するかを確認していく。
- B: 二つの添字を管理しながら、条件を満たしている箇所を探していく。
- C: よく読めばB-Aの最大値を探索するだけの問題。

## [A - AtCoder Line](https://atcoder.jp/contests/abc352/tasks/abc352_a)

上り列車か下り列車の範囲内に駅Zがあることを確認すれば良い。よって、$X<=Z<=Y$か$X>=Z>=Y$を満たすかどうかを判定する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, X, Y, Z;
  cin >> N >> X >> Y >> Z;
  if ((X <= Z && Z <= Y) || (X >= Z && Z >= Y))
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc352/submissions/53542967)

## [B - Typing](https://atcoder.jp/contests/abc352/tasks/abc352_b)

文字列SとTを異なる添字で探索する問題。Tの添字(i)を増加させながら、Sの添字(Si)について確認していけばOK。
同じ列に空白区切りで回答を出力していく場合は、最初だけ空白を含ませないで済むことが多いので`if (Si != 0)cout << " ";`と実装を行なっている。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S, T;
  cin >> S >> T;
  int Si = 0;
  for (int i = 0; i < T.size(); i++)
  {
    if (S[Si] == T[i])
    {
      if (Si != 0)
      {
        cout << " ";
      }
      cout << i + 1;
      Si++;
    }
  }

  cout << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc352/submissions/53567379)

## [C - Standing On The Shoulders](https://atcoder.jp/contests/abc352/tasks/abc352_c)

この問題は整理すると、一番(Bi-Ai)が大きい巨人が一番上にのり、それ以外の巨人が土台になるということ。これを数式として整理すると、ΣAi + max[Bi-Ai]となる。ということになる。よって、入力を行ったあとで(Bi-Ai)が最大になるものを探索しながらAiを加算していく。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<ll> A(N), B(N);
  rep(i, N) cin >> A[i] >> B[i];

  /*
  方針:
    一番[Bi-Ai]が大きい巨人が一番上に乗り、それ以外の巨人は土台になる。その時の頭の高さは
    ΣAi + max[Bi-Ai]となる。
  */
  ll maxHeadSize = 0; // 一番大きな巨人のB-A
  ll totalSize = 0;   // 地面を基準とした頭の高さの最大値
  for (int i = 0; i < N; i++)
  {
    maxHeadSize = max(maxHeadSize, B[i] - A[i]);
    totalSize += A[i];
  }

  cout << totalSize + maxHeadSize << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc352/submissions/53567854)
