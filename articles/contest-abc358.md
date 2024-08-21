---
title: "AtCoder Beginner Contest 358 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 358 振り返り

コンテスト自体に参加することはできていないので、後からプログラムの作成だけを実施した。D問題間で回答しており、そこまで難易度は高くなかった印象。AtCoderProblemsを見ても灰色問題になっているので感触と合っていた

- A: 入力文字列の判定を愚直に実施するだけ。
- B: 行列の合計待ち時間を計算する。それぞれの来園客が「待つのか」「そのまま購入に移れるのか」を管理しながら計算していく問題。
- C: 基本的なbit全探索問題。2^Nの個数がそこまで多くないため、愚直に確認を行っていけば回答できる。
- D: D問題としては過去最高レベルに簡単だと感じた問題。配列の順番を意識する必要もないので回答変数の型だけ注意すればOK。

## [A Welcome to AtCoder Land](https://atcoder.jp/contests/abc358/tasks/358_a)

入力変数S,Tに対して愚直に確認を行った。論理積の考慮さえできていれば何も問題なく回答することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S, T;
  cin >> S >> T;
  if (S == "AtCoder" && T == "Land")
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

[提出結果](https://atcoder.jp/contests/abc358/submissions/56886931)

## [B Ticket Counter](https://atcoder.jp/contests/abc358/tasks/358_b)

現在時刻と来園客の到着時刻を管理して計算を行なっていく。ステータスとしては待つか待たないかだけなので、その分岐だけを計算していく問題

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, A;
  cin >> N >> A;
  vector<int> time(N);
  rep(i, N) cin >> time[i];
  int nowTime = 0;
  for (int i = 0; i < N; i++)
  {
    if (nowTime < time[i]) // 誰も並んでいない場合
    {
      nowTime = time[i] + A;
      cout << nowTime << endl;
    }
    else
    { // 並んでいる人がいる場合
      nowTime += A;
      cout << nowTime << endl;
    }
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc358/submissions/56887061)

## [C Popcorn](https://atcoder.jp/contests/abc358/tasks/358_c)

それぞれの売り場に対して購入するか/しないかをbitで探索していく。探索した結果として一番売り場数が少ないものをmin関数で計算していけばOK。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, M;
  cin >> N >> M;
  vector<string> S(N);
  rep(i, N) cin >> S[i];
  int ans = N;
  for (int bit = 0; bit < (1 << N); ++bit) // 2^N 通りの選び方をビット全探索
  {
    bitset<10> coveredFlavors;
    int cnt = 0;
    for (int i = 0; i < N; i++)
    {
      if (bit & (1 << i))
      {
        ++cnt;
        for (int j = 0; j < M; j++)
        {
          if (S[i][j] == 'o')
          {
            coveredFlavors.set(j);
          }
        }
      }
    }
    if (coveredFlavors.count() == M)
    {
      ans = min(ans, cnt);
    }
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc358/submissions/56891668)

## [D Souvenirs](https://atcoder.jp/contests/abc358/tasks/358_d)

箱の番号や渡す相手の番号を考慮する必要がないので、それぞれソートして小さい順に全て確認していけば最適考慮の形になる。計算量としても大きくないためこの方法で十分高速なプログラムを作成できる。
1点注意事項として、解答変数(自分の場合は`totalCost`)をint型で作成するとオーバーフローしてしまいWAになる。一度気づかずにint型のままで提出してしまってWAになってしまった。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, M;
  cin >> N >> M;
  vector<int> A(N), B(M);
  rep(i, N) cin >> A[i];
  rep(i, M) cin >> B[i];
  sort(A.begin(), A.end());
  sort(B.begin(), B.end());

  ll totalCost = 0;
  int i = 0, j = 0;
  while (i < N && j < M)
  {
    if (A[i] >= B[j])
    {
      totalCost += A[i];
      ++j;
    }
    ++i;
  }

  if (j == M)
  {
    cout << totalCost << endl;
  }
  else
  {
    cout << -1 << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc358/submissions/56940741)
