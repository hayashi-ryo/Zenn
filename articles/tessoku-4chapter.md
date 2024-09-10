---
title: "【4章】競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術"
emoji: "💻"
type: "idea" # tech: 技術記事 / idea: アイデア
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true # true: published / false: unpublished
---

# この記事について

この記事では、[競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術](https://www.amazon.co.jp/%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%AE%E9%89%84%E5%89%87-Compass-Books%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E7%B1%B3%E7%94%B0-%E5%84%AA%E5%B3%BB-ebook/dp/B0BDZGDM9J)を自分なりに理解するために、作成したコードや理解した考え方を記録していくものです。記事は、章ごとに作成していき、最終的に全10記事となる予定です。

## 4章 動的計画法

動的計画法とは、**より小さい問題の結果を利用して問題を解く方法**を指します。英語ではDynamic Programming と書くため、略してDPと呼ばれることもあります。この章では、様々なタイプの動的計画法の問題を通して、イメージを掴んでいきます。

## A問題

### [A16 Dungeon 1（※初版第 1 刷の B22 も同じ問題です）](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p)

動的計画法を利用する超基本問題、それぞれの部屋にたどり着くまでの時間の最小値を記録していき、最終的にN番目の部屋にどのくらいでたどり着くのかを出力する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> A(N + 1, 0), B(N + 1, 0);
  for (int i = 2; i <= N; i++)
  {
    cin >> A[i];
  }
  for (int i = 3; i <= N; i++)
  {
    cin >> B[i];
  }

  // dp定義
  vector<int> dp(N + 1);
  dp[1] = 0;    // 初期状態
  dp[2] = A[2]; // A_1しかルートが存在しない
  for (int i = 3; i <= N; i++)
  {
    dp[i] = min(
        dp[i - 1] + A[i], // Aルート
        dp[i - 2] + B[i]  // Bルート
    );
  }

  cout << dp[N] << endl;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/56943088)

### [A17 Dungeon 2](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_q)

この問題に回答するプログラムは大きく分けて二つの部分に分けられる。

1. 動的計画法によって部屋Nまでの最短到達時間を求めるパート
このパートでは[#16](#a16-dungeon-1初版第-1-刷の-b22-も同じ問題です)で実装した形と同様に、N番目の部屋にたどり着く時間を動的計画法で求めていく。
2. 1で求めた最短時間の経路を記録するパート
1で求めたdpでは、どのようなルートできたのかを記録していない。そのため、一度求めたdpを後ろから探索することでどのようなルートを辿ると最短時間とすることができるかを確認していく。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> A(N + 1, 0), B(N + 1, 0);
  for (int i = 2; i <= N; i++)
  {
    cin >> A[i];
  }
  for (int i = 3; i <= N; i++)
  {
    cin >> B[i];
  }

  // dp定義
  vector<int> dp(N + 1);
  dp[1] = 0;    // 初期状態
  dp[2] = A[2]; // A_1しかルートが存在しない
  for (int i = 3; i <= N; i++)
  {
    dp[i] = min(
        dp[i - 1] + A[i], // Aルート
        dp[i - 2] + B[i]  // Bルート
    );
  }

  vector<int> ans;
  ans.push_back(N);
  int idx = N;
  while (idx > 0)
  {
    if (idx == 1)
    {
      break;
    }
    if (dp[idx] == dp[idx - 1] + A[idx])
    {
      idx -= 1; // Aルートを通っている場合
    }
    else
    {
      idx -= 2; // Bルートを通っている場合
    }
    ans.push_back(idx);
  }

  reverse(ans.begin(), ans.end());
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

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/56943323)

### [A18 Subset Sum](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r)

二次元のdpを利用して部分和を求める問題。このタイプの問題は個人的にも重要なので、理解を深めるためにも詳細に説明する。
この問題におけるdpは以下の意味を持つ:

#### dpの定義

`dp[i][j]`: i番目のカードまでを選択対象に含めた時に、値jを部分和として定義することができるか。すなわち、部分和としてjが存在する場合は`true`、しない場合は`false`となる。

#### 初期条件

i=0の場合、選択対象が存在しないため`false`となる。j=0の場合、カードを選択していない状態のみが定義される。

```math
\begin{cases}
  dp[0][j] = false ( 0 \leq i \leq S ) \\
  dp[0][0] = true 
\end{cases}
```

#### 漸化式

i番目($ 0 \leq i \leq N $)までの商品を選択対象とする場合、

1. i番目の商品を選択しない
2. i番目の商品を選択する

の2通りが考えられる。ここで、i番目の商品を選ばなかった場合、部分和はi-1番目までの商品の状態と同じになる。
i番目の商品を選択する場合、i-1番目までの商品を選択対象とした状態で、部分和としてj-A[i]がtrueであれば、i番目の商品を選択することによって、部分和をjにすることができる。

ここまでの内容について整理することで以下のプログラムを実装することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, S;
  cin >> N >> S;
  vector<int> A(N + 1);
  rep(i, N) cin >> A[i + 1];

  // dp定義
  vector<vector<bool>> dp(N + 1, vector<bool>(S + 1, false));
  dp[0][0] = true;
  for (int i = 1; i <= N; i++) // カードの枚数
  {
    for (int j = 0; j <= S; j++) // 整数の合計
    {
      if (j < A[i]) // A_j を選択できない場合
      {
        dp[i][j] = dp[i - 1][j];
      }
      else // A_j を選択できる場合
      {
        if (dp[i - 1][j] == true           // A_j を選択しない
            || dp[i - 1][j - A[i]] == true // A_jを選択する
        )
        {
          dp[i][j] = true;
        }
      }
    }
  }

  string ans = "No";
  if (dp[N][S] == true)
  {
    ans = "Yes";
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/56971582)

### [A19 Knapsack 1](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_s)

二次元dpを利用したナップザック問題。この問題ではA18と異なり選択するかどうかを「重さ」で判断する必要がある。そのため、今回のdpは

`dp[i][j]`: 品物iまでの中から重さがjとなるように選択する場合、合計価値としてありうる最大値はいくつか？

となる。この条件を実装していくと以下のようなプログラムが以下。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, W;
  cin >> N >> W;
  vector<pair<ll, ll>> goods(N + 1);
  rep(i, N) cin >> goods[i + 1].first >> goods[i + 1].second;
  vector<vector<ll>> dp(N + 1, vector<ll>(W + 1, 0));

  for (int i = 1; i <= N; i++) // 品物
  {
    for (int j = 0; j <= W; j++) // 重さ
    {
      if (j < goods[i].first) // 品物を選択できない場合
      {
        dp[i][j] = dp[i - 1][j];
      }
      else
      {
        dp[i][j] = max(
            dp[i - 1][j],
            dp[i - 1][j - goods[i].first] + goods[i].second);
      }
    }
  }

  ll ans = 0;
  for (int i = 0; i <= W; i++)
  {
    ans = max(ans, dp[N][i]);
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/56972746)

### [A20 LCS](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_t)

この問題では、部分文字列の共通部分を求めていきます。一見DPを利用することは関係ないように見えますが、最終的に取得したい解を考えると、以下の方針を立てていくことで計算できることがわかります。

- `dp[i][j]`の定義Sのi文字目、Tのj文字目までの部分文字列のうち、最長のものの長さ
- `dp[i][j]`の漸化式: `S[i-1] == T[j-1]`の場合、以下の3つの値のmaxを取る
  - `dp[i-1][j], dp[i][j-1]`: i-1,j-1文字目までの連続一致よりもそれ以前の部分文字列の連続一致の方が長い場合。しかし、基本的に一致している場合は採用されないことがほとんどと考えられる。
  - `dp[i-1][j-1] + 1`: i-1,j-1文字目までの連続一致の数

上記の計算を行い、最終的に求められる値が出力したい解となる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S, T;
  cin >> S >> T;
  int N = S.size();
  int M = T.size();
  vector<vector<int>> dp(N + 1, vector<int>(M + 1, 0));
  dp[0][0] = 0;
  for (int i = 1; i <= N; i++)
  {
    for (int j = 1; j <= M; j++)
    {
      if (S[i - 1] == T[j - 1])
      {
        dp[i][j] = max({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1});
      }
      else
      {
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  cout << dp[N][M] << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/54002878)

### [A21 Block Game](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_u)

区間DP問題。基本的な考え方は特定の状態`dp[l][r]`になった時の最大値がどのようになっているかを計算していく。得点の加算条件を考慮した上で、maxで値を決定していく。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> P(N + 1), A(N + 1);
  vector<vector<int>> dp(N + 1, vector<int>(N + 1, 0));
  rep(i, N) cin >> P[i + 1] >> A[i + 1];

  for (int len = N - 2; len >= 0; --len)
  {
    for (int l = 1; l <= N - len; ++l)
    {
      int r = l + len;
      int score1 = 0, score2 = 0;
      if (l <= P[l - 1] && P[l - 1] <= r) // 左端を取り除く
      {
        score1 = A[l - 1];
      }

      if (l <= P[r + 1] && P[r + 1] <= r) // 左端を取り除く
      {
        score2 = A[r + 1];
      }

      if (l == 1)
      {
        dp[l][r] = dp[l][r + 1] + score2;
      }
      else if (r == N)
      {
        dp[l][r] = dp[l - 1][r] + score1;
      }
      else
      {
        dp[l][r] = max({dp[l][r], dp[l - 1][r] + score1, dp[l][r + 1] + score2});
      }
    }
  }

  int ans = 0;
  for (int i = 1; i <= N; i++)
  {
    ans = max(ans, dp[i][i]);
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57132973)

### [A22 Sugoroku](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_v)

最後の行動で場合分けする動的計画法と異なり、この問題では1手先の状態で場合分けする動的計画法の問題。この問題では、部屋iの状態から移動先の状態をことを考慮して動的計画法を実施する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> A(N), B(N);
  rep(i, N - 1) cin >> A[i + 1];
  rep(i, N - 1) cin >> B[i + 1];

  vector<int> dp(N, 0);
  for (int i = 1; i <= N - 1; ++i)
  {
    dp[A[i]] = max(dp[A[i]], dp[i] + 100);
    dp[B[i]] = max(dp[B[i]], dp[i] + 150);
  }

  cout << dp[N] << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57144692)

### [A23 All Free](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_w)

この問題では、クーポン適用の条件を動的配列に保存して、計算を行います。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

const int MAXDEF = 1'000'000'000;

int main()
{
  int N, M;
  cin >> N >> M;
  vector<vector<int>> A(M, vector<int>(N));
  vector<int> dp(1 << N, MAXDEF); // dp配列を1次元に変更
  rep(i, M)
  {
    rep(j, N)
    {
      cin >> A[i][j];
    }
  }

  dp[0] = 0;
  for (int i = 0; i < M; i++)
  {
    int mask = 0;
    for (int j = 0; j < N; j++)
    {
      if (A[i][j] == 1)
      {
        mask |= (1 << j);
      }
    }

    for (int j = 0; j < (1 << N); j++)
    {
      dp[j | mask] = min(dp[j | mask], dp[j] + 1);
    }
  }

  if (dp[(1 << N) - 1] == MAXDEF)
  {
    cout << "-1" << endl;
  }
  else
  {
    cout << dp[(1 << N) - 1] << endl;
  }
  return 0;
}

```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57192200)

### [A24 LIS](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_x)

この問題では、lisという配列を利用して最長部分増加文字列を計算します。`lower_bond`によって現在の`A[i]`より大きい要素がlisに存在するかを確認し、存在しない場合は`A[i]`をlisに追加する。存在する場合は、その要素を`A[i]`に置き換える。これによって、最長増加部分列を保持しつつ、可能な限り小さな値で更新することが可能になる。

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
  for (int i = 0; i < N; ++i)
  {
    cin >> A[i];
  }

  vector<int> lis;

  for (int i = 0; i < N; ++i)
  {
    auto it = lower_bound(lis.begin(), lis.end(), A[i]);
    if (it == lis.end())
    {
      lis.push_back(A[i]);
    }
    else
    {
      *it = A[i];
    }
  }

  cout << lis.size() << endl;

  return 0;
}

```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57222613)

### [A25 Number of Routes](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_y)

この問題では、遷移方法が2パターン(上と左)であることと、特定のマスに対する遷移方法は遷移元のパターンの和であることを利用して計算を行う。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  ll H, W;
  cin >> H >> W;
  vector<vector<char>> c(H + 1, vector<char>(W + 1));
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
    {
      cin >> c[i][j];
    }
  }

  vector<vector<ll>> dp(H + 1, vector<ll>(W + 1, 0));
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
    {
      if (i == 1 && j == 1) // スタート地点
      {
        dp[i][j] = 1;
      }
      else
      {
        if (i > 1 && c[i - 1][j] == '.')
        {
          dp[i][j] += dp[i - 1][j];
        }
        if (j > 1 && c[i][j - 1] == '.')
        {
          dp[i][j] += dp[i][j - 1];
        }
      }
    }
  }

  cout << dp[H][W] << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57222283)

## B問題

### [B16 Frog 1](https://atcoder.jp/contests/tessoku-book/tasks/dp_a)

この問題では、i番目の足場に到達するのにかかる最小コストを動的計画法で計算していく。i番目の足場に到達するためには、

- `i-1 番目のマスまでのコスト+i-1番目からi番目までのコストの和`
- `i-2 番目のマスまでのコスト+i-2番目からi番目までのコストの和`

のうち、小さいものを計算していけば良い。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

const int DEFMAX = 1'000'000'000;
int main()
{
  int N;
  cin >> N;
  vector<int> h(N + 1, 0);
  rep(i, N) cin >> h[i + 1];

  vector<int> dp(N + 1, DEFMAX);
  dp[1] = 0;
  dp[2] = abs(h[1] - h[2]);
  for (int i = 3; i <= N; i++)
  {
    dp[i] = min(abs(h[i] - h[i - 2]) + dp[i - 2], abs(h[i] - h[i - 1]) + dp[i - 1]);
  }

  cout << dp[N] << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57222984)

### [B17 Frog 1 with Restoration](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cp)

この問題では、[B16](#b16-frog-1)で回答した足場を逆順に辿っていく必要がある。そのため、回答配列を用意してNから1まで足場を探索していけば良い。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)
const int DEFMAX = 1'000'000'000;
int main()
{
  int N;
  cin >> N;
  vector<int> h(N + 1, 0);
  rep(i, N) cin >> h[i + 1];

  vector<int> dp(N + 1, DEFMAX);
  dp[1] = 0;
  dp[2] = abs(h[1] - h[2]);
  for (int i = 3; i <= N; i++)
  {
    dp[i] = min(abs(h[i] - h[i - 2]) + dp[i - 2], abs(h[i] - h[i - 1]) + dp[i - 1]);
  }

  vector<int> ans;
  int idx = N;
  while (idx > 0)
  {
    ans.push_back(idx);
    if (dp[idx] == dp[idx - 1] + abs(h[idx] - h[idx - 1]))
    {
      idx -= 1;
    }
    else
    {
      idx -= 2;
    }
  }

  reverse(ans.begin(), ans.end());

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

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57237599)

### [B18 Subset Sum with Restoration](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cq)

基本的な考え方は[B17](#b17-frog-1-with-restoration)と同様に、動的計画法によって計算を行った後に、辿った道のりを逆順で辿っていく。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, S;
  cin >> N >> S;
  vector<int> A(N + 1, 0);
  rep(i, N) cin >> A[i + 1];

  vector<vector<bool>> dp(N + 1, vector<bool>(S + 1, false));
  dp[0][0] = true;
  for (int i = 1; i <= N; i++)
  {
    for (int j = 0; j <= S; j++)
    {
      if (j < A[i]) // A_i を選択できない
      {
        dp[i][j] = dp[i - 1][j];
      }
      else
      {
        if (
            dp[i - 1][j] == true ||     // A_i を選択しない
            dp[i - 1][j - A[i]] == true // A_i を選択する
        )
        {
          dp[i][j] = true;
        }
      }
    }
  }

  // 整数の合計がSとなる方法がない場合
  if (!dp[N][S])
  {
    cout << -1 << endl;
    return 0;
  }

  vector<int> ans;
  int total = S;
  for (int i = N; i > 0; --i)
  {
    if (dp[i - 1][total])
    {
      continue;
    }
    ans.push_back(i);
    total -= A[i];
  }

  sort(ans.begin(), ans.end());
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

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57241018)

### [B19 Knapsack 2](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cr)

```cpp
```

[提出結果]()

### [B20 Edit Distance](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cs)

この問題では、編集距離(レーベンシュタイン距離)と呼ばれるものを求めていく。編集距離とは**2つの単語がどれくらい似ているかを表す量**のことを表す。詳細な内容については[参考サイト 具体例で学ぶ数学](https://mathwords.net/hensyukyori)を参照のこと。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string sourceStr, targetStr;
  cin >> sourceStr >> targetStr;
  int sourceLen = (int)sourceStr.size(), targetLen = (int)targetStr.size();
  vector<vector<int>> dp(targetLen + 1, vector<int>(sourceLen + 1, 0));
  for (int i = 0; i <= targetLen; i++)
  {
    dp[i][0] = i;
  }
  for (int j = 0; j <= sourceLen; j++)
  {
    dp[0][j] = j;
  }

  for (int i = 1; i <= targetLen; i++)
  {
    for (int j = 1; j <= sourceLen; j++)
    {
      int cost = (sourceStr[j - 1] == targetStr[i - 1]) ? 0 : 1;
      dp[i][j] = min(
          {dp[i - 1][j] + 1,
           dp[i][j - 1] + 1,
           dp[i - 1][j - 1] + cost});
    }
  }

  cout << dp[targetLen][sourceLen] << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57597639)

### [B21 Longest Subpalindrome](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cs)

動的計画法によって文字列の部分文字列ごとの最長回文部分列を求める方針で回答していく。dpテーブルとしては`dp[l][r]`をl文字目からr文字目までの間で作ることができる最長回文部分列であると定義する。DPテーブル更新の考え方を以下で説明する。

1. DPテーブルの定義
  `dp[i][j]`: 文字列Sの区間`[i, j]`の間で作ることができる最長回文部分列の長さを示す。
2. 初期条件
  1文字区間(`i==j`)は回文であるため、`dp[i][i] = 1`と定義する。
3. DPテーブル遷移の考え方
  もし`S[i] == S[j]`ならば、`S[i]`と`S[j]`を両端に追加することで回文を作ることができる。よって、`dp[i][j]= dp[i+1][j-1]+2`となる。
  もし`S[i] != S[j]`ならば、`S[i]`と`S[j]`のどちらかを削除して最長を計算する必要がある。よって、`dp[i][j]= max(dp[i+1][j], dp[i][j-1])`となる。
4. 最終回答
  `dp[0][N-1]`が文字列S全体で作ることができる最長回文文字列となる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  string S;
  cin >> N >> S;
  vector<vector<int>> dp(N + 1, vector<int>(N + 1, 0));

  // 1文字の区間はすべて長さ1の回文となる
  for (int i = 0; i <= N; i++)
  {
    dp[i][i] = 1;
  }

  // 区間の長さが短いものから計算する
  for (int LEN = 2; LEN <= N; ++LEN)
  {
    for (int i = 0; i <= N - LEN; ++i)
    {
      int j = i + LEN - 1;
      if (S[i] == S[j])
      {
        dp[i][j] = dp[i + 1][j - 1] + 2;
      }
      else
      {
        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
      }
    }
  }

  cout << dp[0][N - 1] << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57612540)

### [B23 Traveling Salesman Problem](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cv)

この問題は巡回セールスマン問題の一種。今回は、動的計画法とビットマスクを使用してすべてのとしを訪れて開始位置に戻るための最短距離を求めていく。DPテーブル更新の考え方を以下で説明する。

1. 入力情報から、全都市間の距離をdist配列に保存する
2. `dp[mask][i]`で、以下を管理する。
  `mask`: 現在までの訪れた都市の集合をビットマスクで表現
  `i`: 現時点で滞在している都市
  `dp[mask][i]`: 現在までに訪れた都市の集合と現時点の滞在とし、またそこに至るまでの最短距離を保持
3. 初期状態として`dp[1][0] = 0`を定義する。これは、都市0から開始して、現在都市0だけに訪れていることを表現している。
4. ビットマスクと動的計画法によって、すべての経路を探索し各経路の最短距離を更新する。
5. 最後に、すべての都市の訪問後、出発地点に戻るまでの最短距離を求めて出力する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

const double INF = numeric_limits<double>::infinity();

// 2都市間の距離を計算
double calcDistance(pair<int, int> city1, pair<int, int> city2)
{
  int dx = city1.first - city2.first;
  int dy = city1.second - city2.second;
  return sqrt(dx * dx + dy * dy);
}

int main()
{
  int N;
  cin >> N;
  vector<pair<int, int>> city(N);
  vector<vector<double>> dist(N, vector<double>(N));
  vector<vector<double>> dp(1 << N, vector<double>(N, INF));

  // 都市の座標を入力
  rep(i, N) cin >> city[i].first >> city[i].second;

  // 各都市間の距離を計算
  for (int i = 0; i < N; ++i)
  {
    for (int j = 0; j < N; ++j)
    {
      dist[i][j] = calcDistance(city[i], city[j]);
    }
  }

  // 開始位置を設定（都市0をスタート地点と仮定）
  dp[1][0] = 0;

  // すべての経路を探索
  for (int mask = 1; mask < (1 << N); ++mask)
  {
    for (int u = 0; u < N; ++u)
    {
      if (mask & (1 << u)) // u が訪問済みの場合
      {
        for (int v = 0; v < N; ++v)
        {
          if (!(mask & (1 << v))) // v が未訪問の場合
          {
            dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + dist[u][v]);
          }
        }
      }
    }
  }

  // 全ての都市を訪問した後、最初の都市に戻る最短経路を計算
  double ans = INF;
  for (int i = 1; i < N; ++i)
  {
    ans = min(ans, dp[(1 << N) - 1][i] + dist[i][0]);
  }

  // 結果を出力
  cout.precision(12);
  cout << fixed << ans << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57613086)

### [B24 Many Boxes](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cw)

この問題は、箱をできるだけ多く重なるための最長増加部分列(LIS)を求める問題と似ている。そのため、LISの考え方によって計算を行なっていく。
各箱は縦横の長さが与えられるため、一定の基準でソートした上でLISアルゴリズムを適用する方法が効率的である。

具体的には、以下の方針で計算を行なった。

1. 箱を縦の長さを基準として昇順にソートする。縦の長さが同じ場合は、横の長さの降順でソートする。これによって縦の長さが同じ箱を入れ子にすることを防ぐ
2. 横の長さに注目してLISを計算する。この計算したLISが「箱を何重にできるか」を意味する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

bool compareBox(const pair<int, int> &a, const pair<int, int> &b)
{
  if (a.first == b.first)
  {
    return a.second > b.second;
  }
  return a.first < b.first;
}

int main()
{
  int N;
  cin >> N;
  vector<pair<int, int>> box(N);
  rep(i, N) cin >> box[i].first >> box[i].second;

  // 箱を縦の長さで昇順にソート
  // もし縦の長さが同じ場合は、横の長さの降順でソート
  sort(box.begin(), box.end(), compareBox);

  vector<int> LIS;
  for (int i = 0; i < N; i++)
  {
    int width = box[i].second;
    auto it = lower_bound(LIS.begin(), LIS.end(), width);
    if (it == LIS.end())
    {
      LIS.push_back(width);
    }
    else
    {
      LIS[it - LIS.begin()] = width;
    }
  }

  cout << (int)LIS.size() << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/57613486)
