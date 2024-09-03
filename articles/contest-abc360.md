---
title: "AtCoder Beginner Contest 360 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 360 振り返り

コンテストには参加することができなかったため、後から問題を解いた。D問題まで回答できている。

- A: 入力の文字列を適切に処理することができればOK
- B: 組み合わせの総数がそこまで多くないため、c/wについて全ての組み合わせを検証して条件を満たしているものが存在するか確認する。
- C: 荷物の数と箱の数が一致しているため、移動させる荷物の条件を決定した上で計算を行う。
- D: 配列の並び順を変更しても結果に影響しないため、ソートした上で求めたい結果を尺取り法で計算する。

## [A A Healthy Breakfast](https://atcoder.jp/contests/abc360/tasks/360_a)

入力文字列Sについて、RMSがどこに存在するかを確認すれば良い。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S;
  int R, M;
  cin >> S;
  for (int i = 0; i < (int)S.size(); i++)
  {
    if (S[i] == 'R')
    {
      R = i;
    }
    if (S[i] == 'M')
    {
      M = i;
    }
  }

  if (R < M)
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

[提出結果](https://atcoder.jp/contests/abc360/submissions/57393395)

## [B Vertical Reading](https://atcoder.jp/contests/abc360/tasks/360_b)

全組み合わせを確認してもTLEとならないくらいの計算量である。そのため、c/wの条件を確認して組み合わせの検証を行なっていく。

- c/wの条件
c: 1以上wの文字数より少ない。よってループとしては`for (int c = 0; c < w; ++c)`の確認を行う
w: c以上Sの文字数以下。よってループとしては`for (int w = 1; w < (int)S.size(); ++w)`の確認を行う。

これらの条件をループさせながら、条件を満たす文字列が存在するかを判定していく。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S, T;
  cin >> S >> T;
  for (int w = 1; w < (int)S.size(); ++w)
  {
    for (int c = 0; c < w; ++c)
    {
      string tmp = "";
      for (int i = c; i < (int)S.size(); i += w)
      {
        tmp += S[i];
      }

      if (tmp == T)
      {
        cout << "Yes" << endl;
        return 0;
      }
    }
  }

  cout << "No" << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc360/submissions/57393502)

## [C Move It](https://atcoder.jp/contests/abc360/tasks/360_c)

移動させない荷物の条件は以下となる。

- 一つの箱に複数の荷物が存在する
- 一つの箱の中に存在する荷物のうち、最重量でない

これらの条件について考慮すると、全ての荷物の重量の合計(sumW)、全ての箱に存在する荷物の最重量値の合計値(sumMaxW)を計算することができれば、以下で結果を得ることができる。

`ans = sumW - sumMaxW`

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> A(N), W(N);

  rep(i, N) cin >> A[i];
  rep(i, N) cin >> W[i];

  vector<int> maxW(N, 0);
  for (int i = 0; i < N; i++)
  {
    A[i]--;
    maxW[A[i]] = max(maxW[A[i]], W[i]);
  }

  ll sumW = accumulate(W.begin(), W.end(), 0);
  ll sumMaxW = accumulate(maxW.begin(), maxW.end(), 0);

  cout << sumW - sumMaxW << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc360/submissions/57393654)

## [D Ghost Ants](https://atcoder.jp/contests/abc360/tasks/360_d)

正負それぞれの方向に進むアリについて、新しい配列を用意してソート。その後尺取り法によってすれ違う条件`Xi - Xj <= 2T`を満たしている組み合わせを数え上げていく。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  ll T;
  string S;
  cin >> N >> T >> S;
  vector<ll> X(N), x1, x2;
  rep(i, N) cin >> X[i];
  for (int i = 0; i < N; i++)
  {
    if (S[i] == '1')
    {
      x1.push_back(X[i]);
    }
    else
    {
      x2.push_back(X[i]);
    }
  }

  sort(x1.begin(), x1.end());
  sort(x2.begin(), x2.end());

  int l = 0, r = 0;
  ll ans = 0;

  for (int i = 0; i < (int)x1.size(); i++)
  {
    while (l < (int)x2.size() && x2[l] < x1[i])
    {
      l++;
    }
    while (r < (int)x2.size() && x2[r] - x1[i] <= 2 * T)
    {
      r++;
    }
    ans += r - l;
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc360/submissions/57393811)
