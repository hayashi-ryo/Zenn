---
title: "【5章】競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術"
emoji: "💻"
type: "idea" # tech: 技術記事 / idea: アイデア
topics: ["AtCoder","study","CS","競技プログラミング"]
published: false # true: published / false: unpublished
---

# この記事について

この記事では、[競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術](https://www.amazon.co.jp/%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%AE%E9%89%84%E5%89%87-Compass-Books%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E7%B1%B3%E7%94%B0-%E5%84%AA%E5%B3%BB-ebook/dp/B0BDZGDM9J)を自分なりに理解するために、作成したコードや理解した考え方を記録していくものです。記事は、章ごとに作成していき、最終的に全10記事となる予定です。

## 5章 数学的問題

この章では、競技プログラミングで頻出される「数学的なテクニック」について学習する。

## A問題

### [A26 Prime Check](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_z)

ある数Xが素数であるかを判定する問題。今回の問題では制約が厳しくないため2以上sqrt(X)の範囲でXを割り切れる数が存在するかの判定を行なった。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

bool isPrime(int x)
{
  for (int i = 2; i <= sqrt(x); ++i)
  {
    if (x % i == 0)
    {
      return false;
    }
  }
  return true;
}
int main()
{
  int Q;
  cin >> Q;
  for (int i = 0; i < Q; i++)
  {
    int X;
    cin >> X;
    if (isPrime(X))
    {
      cout << "Yes" << endl;
    }
    else
    {
      cout << "No" << endl;
    }
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57616047)

### [A27 Calculate GCD](https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_o)

- 解法1: ユークリッドの互除法
二つの数について最大公約数を求めたい場合、ユークリッドの互除法を用いると高速に計算をすることができる。手順は以下の通り。

1. 二つの数のうち、大きい方を「小さい数で割ったあまり」に変更することを繰り返す。
2. 片方の数が0になったら終了。もう片方の数が回答となる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int A, B;
  cin >> A >> B;
  while (A >= 1 && B >= 1)
  {
    if (A >= B)
    {
      A = A % B;
    }
    else
    {
      B = B % A;
    }
  }
  if (A == 0)
  {
    cout << B << endl;
  }
  else
  {
    cout << A << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57616139)

- 解法2: GCD関数の利用
C++標準ライブラリには最大公約数を求める`GCD(A, B)`関数が存在する。この関数を利用すればこの問題に簡単に回答することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int A, B;
  cin >> A >> B;
  cout << gcd(A, B) << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57616163)

### [A28 Blackboard](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ab)

演算子と値が入力されるので、計算を行なっていく問題。工夫せずにそのまま実施していくと、`long long`の範囲を超えてしまう可能性がある。そのため、足し算・引き算・掛け算においては、どのようなタイミングであまりを計算しても答えが変わらないという性質がある。そのため、演算とあまりの算出を都度行っていくことで範囲超過を防ぐことができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)
const int MOD = 10'000;

ll calculate(ll current, char operation, ll value)
{
  switch (operation)
  {
  case '+':
    current += value;
    break;
  case '-':
    current -= value;
    break;
  case '*':
    current *= value;
    break;
  }
  current %= MOD;
  if (current < 0)
  {
    current += MOD;
  }
  return current;
}

int main()
{
  int N;
  cin >> N;
  ll ans = 0;

  for (int i = 0; i < N; i++)
  {
    char operation;
    ll value;
    cin >> operation >> value;

    ans = calculate(ans, operation, value);
    cout << ans << endl;
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57623588)

### [A29 Power](https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_aq)

a^b をそのまま計算していくとTLEとなってしまう可能性が高い。そうならないような工夫として、bを2進数表現した時に1であれば計算を行うことを想定上限まで実施していくことで高速に計算することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

const ll MOD = 1000'000'007;

int main()
{
  ll a, b;
  cin >> a >> b;
  ll ans = 1;
  for (int i = 0; i < 30; ++i)
  {
    int wari = (1 << i);
    if ((b / wari) % 2 == 1)
    {
      ans = (ans * a) % MOD;
    }
    a = (a * a) % MOD;
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57637059)

### [A30 Combination](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ad)

割り算では計算の途中であまりをとっても上手くいかない。そのため、この問題ではフェルマーの小定理を使って割り算を掛け算に変更して計算を行う。フェルマーの小定理は以下。

素数 \(p\) に対して、

\[
a^{p-1} ≡ 1 \pmod{p}
\]

が成り立つ。これにより、\(a\) の逆元は以下で計算できる：

\[
a^{-1} ≡ a^{p-2} \pmod{p}
\]

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

const int MOD = 1000000007;
const int MAX = 100000;

long long fac[MAX + 1], inv[MAX + 1], facInv[MAX + 1];

// 素数MODでの階乗とその逆元を事前計算
void preprocess()
{
  fac[0] = fac[1] = 1;
  inv[1] = 1;
  facInv[0] = facInv[1] = 1;

  for (int i = 2; i <= MAX; i++)
  {
    fac[i] = fac[i - 1] * i % MOD;                 // n! % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD / i) % MOD; // フェルマーの小定理を用いて逆元計算
    facInv[i] = facInv[i - 1] * inv[i] % MOD;      // n!の逆元を累積計算
  }
}

// nCr % MOD を計算
long long nCr(int n, int r)
{
  if (r > n)
    return 0;
  return fac[n] * facInv[r] % MOD * facInv[n - r] % MOD;
}

int main()
{
  int n, r;
  cin >> n >> r;

  // 階乗の事前計算
  preprocess();

  // nCrの計算と出力
  cout << nCr(n, r) << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57669581)

### [A31 Divisors](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ae)

和集合の要素数に関しては、包除原理を利用して計算を行うことができる。
> 包除原理とは、特定の集合に対して、奇数個の共通部分に関してはプラス、偶数個の共通部分に関してはマイナスとすることで全体の要素数を求めることができる原理。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  ll N;
  cin >> N;
  ll divide3 = N / 3;
  ll divide5 = N / 5;
  ll divide15 = N / 15;
  cout << divide3 + divide5 - divide15 << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57669700)

### [A32 Game 1](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_af)

この問題では、残りの石の数ごとに勝ちの状態と負けの状態を判断する。従って、残りの石の数を元にDPテーブルを作成してそれぞれの状態が勝ちか負けかを判定する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, A, B;
  cin >> N >> A >> B;
  vector<bool> dp(N + 1, false);
  dp[0] = false;

  for (int i = 1; i <= N; i++)
  {
    if (i >= A && dp[i - A] == false)
    {
      dp[i] = true;
    }
    else if (i >= B && dp[i - B] == false)
    {
      dp[i] = true;
    }
  }

  if (dp[N])
  {
    cout << "First" << endl;
  }
  else
  {
    cout << "Second" << endl;
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57670426)

### [A33 Game 2](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ag)

ゲーム理論において、石取りゲームを行った場合、石の数のXORをとることで先手と後手どちらが勝利するかを判定することができる。この解法については暗記してしまおうと思う。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> A(N);
  rep(i, N) cin >> A[i];
  int XOR_SUM = A[0];
  for (int i = 1; i < N; ++i)
  {
    XOR_SUM = (XOR_SUM ^ A[i]);
  }
  if (XOR_SUM != 0)
  {
    cout << "First" << endl;
  }
  else
  {
    cout << "Second" << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57924727)

### [A34 Game 3](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ah)

この問題では最善手を取るのではなく、石の取り方があらかじめ決まっている状態になる。このような場合、**Grundy数**を考えて解答を求めていく。

>　一回の操作でGrundy数がx1,x2,...,xkに遷移することができる場合、この盤面のGrundy数は「x1,x2,...,xk以外の最小尾非負整数」である。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, X, Y;
  cin >> N >> X >> Y;
  vector<int> A(N);
  rep(i, N) cin >> A[i];

  vector<int> grundy(100009, 0);
  for (int i = 0; i < 100009; i++)
  {
    vector<bool> transit(3, false);

    if (i >= X)
    {
      transit[grundy[i - X]] = true;
    }
    if (i >= Y)
    {
      transit[grundy[i - Y]] = true;
    }

    if (transit[0] == false)
    {
      grundy[i] = 0;
    }
    else if (transit[1] == false)
    {
      grundy[i] = 1;
    }
    else
    {
      grundy[i] = 2;
    }
  }

  int XOR_SUM = grundy[A[0]];
  for (int i = 1; i < N; ++i)
  {
    XOR_SUM = (XOR_SUM ^ grundy[A[i]]);
  }
  if (XOR_SUM != 0)
  {
    cout << "First" << endl;
  }
  else
  {
    cout << "Second" << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57925431)

### [A35 Game 4](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ai)

この問題では、ターンごとに最善手の考え方が異なってくる。先手ターン(奇数ターン)であれば最大遷移できるスコアの最大値を選択するし、後手ターン(偶数ターン)であればスコアの最低値を選択する。動的計画法によってターンごと選択値を記録し、一番上のコマまで探索することで解答を得ることができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> A(N + 1);
  for (int i = 1; i <= N; i++)
  {
    cin >> A[i];
  }

  vector<vector<int>> dp(N + 1, vector<int>(N + 1, 0));
  for (int i = 1; i <= N; i++)
  {
    dp[N][i] = A[i];
  }

  for (int i = N - 1; i >= 1; --i)
  {
    for (int j = 1; j <= i; j++)
    {
      if (i % 2 == 1)
      {
        dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]);
      }
      else
      {
        dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]);
      }
    }
  }

  cout << dp[1][1] << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57925658)

## B問題

### [B26 Output Prime Numbers]()

```cpp
```

[提出結果]()

### [B27 Calculate LCM]()

```cpp
```

[提出結果]()

### [B28 Fibonacci Easy (mod 1000000007)]()

```cpp
```

[提出結果]()

### [B29 Power Hard]()

```cpp
```

[提出結果]()

### [B30 Combination 2]()

```cpp
```

[提出結果]()

### [B31 Divisors Hard]()

```cpp
```

[提出結果]()

### [B32 Game 5]()

```cpp
```

[提出結果]()

### [B33 Game 6]()

```cpp
```

[提出結果]()

### [B34 Game 7]()

```cpp
```

[提出結果]()
