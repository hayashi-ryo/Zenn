---
title: "AtCoder Beginner Contest 353 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 353 振り返り

予定が合わずコンテストに参加することはできませんでしたが、バーチャルで後日参加しました。C問題まで無事に解くことができています。

- A: 入力されるHに対して、条件を満たしているかを判定する問題。
- B: 現在の乗客人数と次に乗ってくるグループの人数を利用して、何度定員を超えるのか数えていく。
- C: 二つの数字を加算して出来上がる値を条件に基づいて数え上げていく問題。そのままやると二重ループでTLEしてしまう。

## [A problem](https://atcoder.jp/contests/353/tasks/353_a)

一番左のビルの高さを基準に、それ以外のビルで高いものがあるかを判定する問題。特に難しい箇所もなく、配列に登録したあとH[0]とH[i]の比較を行っていけば問題ない。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> H(N);
  rep(i, N) cin >> H[i];
  int mostLeftBuilding = H[0];
  for (int i = 1; i < N; i++)
  {
    if (mostLeftBuilding < H[i])
    {
      cout << i + 1 << endl;
      return 0;
    }
  }
  cout << -1 << endl;
  ;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc353/submissions/53689917)

## [B problem](https://atcoder.jp/contests/353/tasks/353_b)

K人のりのアトラクションについて、全てのグループを案内するために何度動かせば良いか考える問題。条件を分けて丁寧に動かす回数を数えていく。

1. 乗客が0の場合: 動かす回数を1追加して、乗客人数をA[i]と設定する。このパターンはi=0でのみ動作する。
2. 乗客がいる場合:
   1. 現在の乗客+次のグループの人数が定員に満たない場合は乗客人数にA[i]だけ加算する。
   2. 次のグループ全員が乗り切らない場合は、人数をA[i]とした上で動かす回数に1加算する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, K;
  cin >> N >> K;
  vector<int> A(N);
  rep(i, N) cin >> A[i];
  int ans = 0, passenger = 0;
  for (int i = 0; i < N; i++)
  {
    if (passenger == 0)
    {
      passenger += A[i];
      ans++;
    }
    else if (passenger + A[i] <= K)
    {
      passenger += A[i];
    }
    else if (passenger + A[i] > K)
    {
      passenger = A[i];
      ans++;
    }
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc353/submissions/53690548)

## [C problem](https://atcoder.jp/contests/353/tasks/353_c)

条件をそのまま実装すると二重ループになり[TLEしてしまう](https://atcoder.jp/contests/abc353/submissions/53690268)。そのため、何らかの工夫が必要。今回は以下のような工夫を行った。

- 条件を確認すると、それぞれのA[i]はN-1回加算されることがわかる。そのため、全てのA[i]についてN-1倍して足し合わせた後に、$10^8$×超えた回数とすればよい。
- 超えた回数を数えるためにも工夫が必要。今回の場合は、並び順に意味はないのでソートした上で尺取り法の考え方を利用して$10^8$を超える回数を数え上げた。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

const ll wari = 100'000'000;

int main()
{
  int N;
  cin >> N;
  vector<ll> A(N);
  for (int i = 0; i < N; i++)
  {
    cin >> A[i];
  }
  ll ans = 0, cnt = 0;
  sort(A.begin(), A.end());
  for (int i = 0; i < N; i++)
  {
    ans += A[i] * (N - 1);
  }

  int j = N;
  for (int i = 0; i < N; i++)
  {
    j = max(j, i + 1);
    while (A[i] + A[j - 1] >= wari && j - 1 > i)
    {
      --j;
    }
    cnt += N - j;
  }

  cout << ans - cnt * wari << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc353/submissions/53695598)
