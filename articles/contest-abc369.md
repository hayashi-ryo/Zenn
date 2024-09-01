---
title: "AtCoder Beginner Contest 369 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 369 振り返り

今回のコンテストは、C問題に時間がかかってしまいC問題までの回答で終わらせてしまった。難易度的にはD問題も難しいものではなかったのでコンテスト中に回答すればよかったと少し反省している。

- A: 等差数列が作成できるかを確認する問題。二つの条件についてしっかり整理することができればOK.
- B: 左右の手について疲労度をそれぞれ計算して、最後にその合計値を出力する。
- C: 数列Aに対して、その要素が等差数列であるものが幾つ存在するかを確認する問題。単独のA_iでも数列が成立するため、数え上げる条件を適切に設定した上で計算を行う必要がある。
- D: モンスターを倒すか倒さないかを動的計画法で計算していく問題。

## [A 369](https://atcoder.jp/contests/abc369/tasks/369_a)

この問題では、以下の二つの条件を確認することで回答できる。

1. A, Bの外にXを配置して等差数列を作成できるか？
  この条件を満たすためにはAとBが異なる数値である必要がある。
2. A, Bの間にXを配置して等差数列を作成できるか？
  この条件を満たすためにはAとBの差が偶数である必要がある。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int A, B;
  cin >> A >> B;
  int ans = 0;
  if (A != B)
  {
    ans += 2;
  }
  if (abs(A - B) % 2 == 0)
  {
    ans += 1;
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc369/submissions/57274120)

## [B Piano 3](https://atcoder.jp/contests/abc369/tasks/369_b)

左手Lと右手Rの初期位置を決定して、その後疲労度を個別に数え上げていけば良い。計算自体はそこまで複雑なものにはならず、絶対値の適用だけ忘れなければ大丈夫。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<pair<int, char>> piano(N);
  rep(i, N) cin >> piano[i].first >> piano[i].second;

  int ans = 0, L = 0, R = 0;
  for (int i = 0; i < N; i++)
  {
    if (piano[i].second == 'L')
    {
      if (L == 0)
      {
        L = piano[i].first;
      }
      else
      {
        ans += abs(piano[i].first - L);
        L = piano[i].first;
      }
    }
    else if (piano[i].second == 'R')
    {
      if (piano[i].second == 'R')
      {
        if (R == 0)
        {
          R = piano[i].first;
        }
        else
        {
          ans += abs(piano[i].first - R);
          R = piano[i].first;
        }
      }
    }
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc369/submissions/57282457)

## [C Count Arithmetic Subarrays](https://atcoder.jp/contests/abc369/tasks/369_c)

コンテストでは以下の方針でプログラムの実装を行った。

1. 等差数列の開始位置と終了位置の決定のため、l(区間の開始位置)、r(区間の終了位置)の計算を行う。
2. rをl+1に設定値し、rが配列の末尾に到達するか等差が異なる間で区間を広げていく。
3. その区間の等差数列の長さlenを計算し、その区間ないに含まれつ全ての部分区間を計算する。

しかし、上記方針で実装を行うと「長さ1の部分文字列を複数回計上してしまう」という問題が発生する。そのため、この問題に対応するため以下の対応を行った。

1. l!=0の場合(区間の開始位置が0でない場合)、回答変数ansをデクリメントして、重複して計上することを防ぐ。
2. while-loopの最後で終了判定を行い、rが区間の終了位置を超過した値となることを防ぐ。

上記方針に則って対応を行ったプログラムが以下となる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<ll> A(N);
  rep(i, N) cin >> A[i];
  ll ans = 0;
  ll l = 0;

  while (l < N)
  {
    ll r = l + 1;
    if (r == N)
    {
      ++ans;
      break;
    }

    ll d = A[r] - A[l];
    while (r + 1 < N && A[r + 1] - A[r] == d)
    {
      ++r;
    }

    ll len = r - l + 1;
    ans += (len * (len + 1)) / 2;
    if (l != 0)
    {
      --ans;
    }
    if (r == N - 1)
    {
      break;
    }
    l = r;
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc369/submissions/57316686)

## [D Bonus EXP](https://atcoder.jp/contests/abc369/tasks/abc369_d)

この問題は動的計画法によってプログラムを作成した。dpの方針としては以下にのみ依存して決定される。

- i番目のモンスターを倒すか逃すか
- i-1番目までのモンスターを倒した数が奇数が偶数か

この条件をもとに漸化式を作成すると

`dp_偶数[i] = max{dp[i-1]_偶数, dp[i-1]_奇数 + 2 * A[i]}`
`dp_奇数[i] = max{dp[i-1]_奇数, dp[i-1]_偶数 + A[i]}`

となる。この条件をもとにdpを計算していくことで結果を得ることができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  ll N;
  cin >> N;
  vector<ll> A(N);
  rep(i, N) cin >> A[i];
  // dp[i][0]: i番目のモンスターが偶数回目で倒される場合
  // dp[i][1]: i番目のモンスターが奇数回目で倒される場合
  vector<vector<ll>> dp(N + 1, vector<ll>(2, 0));

  // 1番目
  dp[0][0] = 0;
  dp[0][1] = A[0];

  for (int i = 1; i < N; ++i)
  {
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + 2 * A[i]); // 偶数回
    dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + A[i]);     // 奇数回
  }

  // N匹全てのモンスターを考慮した場合の最大経験値
  cout << max(dp[N - 1][0], dp[N - 1][1]) << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc369/submissions/57333432)
