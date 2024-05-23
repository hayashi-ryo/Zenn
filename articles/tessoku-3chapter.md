---
title: "【3章】競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術"
emoji: "💻"
type: "idea" # tech: 技術記事 / idea: アイデア
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true # true: published / false: unpublished
---

# この記事について

この記事では、[競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術](https://www.amazon.co.jp/%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%AE%E9%89%84%E5%89%87-Compass-Books%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E7%B1%B3%E7%94%B0-%E5%84%AA%E5%B3%BB-ebook/dp/B0BDZGDM9J)を自分なりに理解するために、作成したコードや理解した考え方を記録していくものです。記事は、章ごとに作成していき、最終的に全10記事となる予定です。

## 3章 二分探索

2章同様、3章でも計算量を改善するためにアルゴリズムを学習します。二分探索は、答えや入力を中央で区切り、探索範囲を半分にしていく手法です。単純に一つ一つ数え上げるよりも、大幅に計算量を改善することができます。

## A問題

### [A11 Binary Search 1](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k)

二分探索の基本問題。この問題では、配列Aの何番目に要素Xが存在するかを確認する。(1)二分探索を手作りするパターンと(2)lower_bound関数を利用するパターンの二つの方法で実装を行った。

1. 二分探索を手作りする
2変数l, rを以下のように定義し、その中間(mid)が要素Xと比較してどのような状態であるかを確認します。

```cpp
l = 0;         // 一番左のインデックス
r = N-1;       // 一番右のインデックス
mid = (l+r)/2; // lとrの中間のインデックス
```

2. lower_bound関数を利用する
lower_bound関数は、引数に与えられたkey以上のイテレータを返す関数である。生のイテレータを返すため、itr-A.begin()とすることでインデックス番号を取得することができる。また、*itrとすることで、要素に直接アクセスすることも可能となる。
また、似た機能を持つ関数としてupper_boundがある。これは、あるkeyより大きい要素のうち、一番左側のイテレータを返すものである。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, X;
  cin >> N >> X;
  vector<int> A(N);
  rep(i, N) cin >> A[i];
  sort(A.begin(), A.end());
  int l = 0, r = N - 1;
  int mid = 0;
  while (A[mid] != X)
  {
    mid = (l + r) / 2;
    if (A[mid] < X)
    {
      l = mid + 1;
    }
    else if (A[mid] > X)
    {
      r = mid - 1;
    }
  }
  cout << mid + 1 << endl;

  // 別解
  auto ans = lower_bound(A.begin(), A.end(), X) - A.begin();
  // cout << ans + 1 << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53717453)

### [A12 Printer](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l)

「答え」で二分探索するパターンの問題。この問題のように、特定の入力と出力の関係が与えられ、出力が特定の値となることを確認するためには、出力を利用して二分探索すると効率的に演算することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

ll printPapers(vector<ll> a, int sec)
{
  ll papers = 0;
  for (int i = 0; i < (int)a.size(); i++)
  {
    papers += sec / a[i];
  }
  return papers;
}

int main()
{
  int N, K;
  cin >> N >> K;
  vector<ll> A(N);
  rep(i, N) cin >> A[i];
  ll l = 0, r = 1'000'000'000;
  while (l < r)
  {
    ll mid = (l + r) / 2;
    if (printPapers(A, mid) < K)
    {
      l = mid + 1;
    }
    else if (printPapers(A, mid) >= K)
    {
      r = mid;
    }
  }
  cout << l << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53725135)

### [A13 Close Pairs](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m)

この問題は二分探索によって回答することもできるが、しゃくとり法を利用して実装を進める。しゃくとり法とは、ソートされた配列に対してしゃくとり虫のように探索することからそのように呼ばれている。実装としては、

1. 二つのインデックス(i,j)を利用する
2. iに対して、jを条件を満たす最大まで増加させる
3. j-i-1がAiにおける条件を満たす組み合わせの総数となるので、それぞれのAiに対して同様の演算を行なっていく

このとき、jの値は初期化せず、i-1の時の値を引き継ぎます。なぜなら、Ai-1で条件を満たした場合、ソートされた配列に対してはAiでも同様に条件を満たすことが自明であるためです。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, K;
  cin >> N >> K;
  vector<ll> A(N);
  rep(i, N) cin >> A[i];
  int j = 0;
  ll ans = 0;
  for (int i = 0; i < N; i++)
  {
    while (j < N && A[j] - A[i] <= K)
    {
      j++;
    }
    ans += (j - i) - 1;
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53725532)

### [A14 Four Boxes](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_n)

事前準備した後に二分探索を利用して計算を行う。
問題文をそのまま実装して4重ループとした場合は当然TLEとなってしまうので、以下の方針で実装を行う。

1. あらかじめAとB、CとDの要素全ての組み合わせについてありうる値を計算しておく(計算量$O(N^2)$)
2. あらかじめ計算されたAB配列の全ての要素について、K-AB[i]となる値がCD配列に存在するかをlower_boundを利用して確認する

上記方針で実装できる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, K;
  cin >> N >> K;
  vector<int> A(N), B(N), C(N), D(N);
  rep(i, N) cin >> A[i];
  rep(i, N) cin >> B[i];
  rep(i, N) cin >> C[i];
  rep(i, N) cin >> D[i];
  vector<ll> AB(N * N), CD(N * N);
  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < N; j++)
    {
      AB[i * N + j] = A[i] + B[j];
      CD[i * N + j] = C[i] + D[j];
    }
  }

  sort(CD.begin(), CD.end());
  string ans = "No";
  for (int i = 0; i < (ll)AB.size(); i++)
  {
    auto it = lower_bound(CD.begin(), CD.end(), K - AB[i]);
    if (it != CD.end() && *it == K - AB[i])
    {
      ans = "Yes";
      break;
    }
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53726297)

### [A15 Compression](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_o)

lower_bound関数を利用して実装を行う。そもそもlower_bound関数は以下の出力を行う

> イテレータ範囲 [first, last) のうち、指定された要素以上の値が現れる最初の位置のイテレータを取得する。
> [cpprefjp - C++日本語リファレンスより](https://cpprefjp.github.io/reference/algorithm/lower_bound.html)

即ち、以下の操作を行うことでAiが配列の中で何番目に小さい要素であるかを確認することができる。

1. 配列Aと同じ要素を持つ配列Xを用意する。
2. 配列Xの要素を重複削除し、昇順にソートする。
3. 配列Aの要素それぞれについて、配列Xの何番目の要素であるか、lower_boundを利用して確認する。

上記操作を行うことで、配列要素の圧縮という題意に沿ったプログラムを実装することができる。

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
  vector<int> X(N); // 順番を保持する配列
  for (int i = 0; i < N; i++)
  {
    cin >> A[i];
    X[i] = A[i];
  }
  sort(X.begin(), X.end());                     // ソートする
  X.erase(unique(X.begin(), X.end()), X.end()); // 重複削除

  vector<int> ans(N);
  for (int i = 0; i < N; i++)
  {
    int it = lower_bound(X.begin(), X.end(), A[i]) - X.begin();
    ans[i] = it + 1;
  }
  for (int i = 0; i < N; i++)
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

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53753542)

## B問題

### [B11 Binary Search 2](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cj)

lower_boundを利用して、特定の要素Xiより小さい要素がいくつ配列Aに存在するかを確認する問題。lower_boundで返されるイテレータは、Xi以上の値が現れる初めての位置を示すイテレータであるため、これをそのまま出力することで回答とすることができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, Q;
  cin >> N;
  vector<int> A(N);
  rep(i, N) cin >> A[i];
  cin >> Q;
  vector<int> X(Q);
  rep(i, Q) cin >> X[i];

  sort(A.begin(), A.end());
  for (int i = 0; i < Q; i++)
  {
    int it = lower_bound(A.begin(), A.end(), X[i]) - A.begin();
    cout << it << endl;
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53753816)

### [B12 Equation](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ck)

答えで二分探索していくタイプの問題。入出力の関係から、回答は0以上100以下であることがわかるので、この範囲で二分探索を実施していく。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

double xCalculation(double x)
{
  return x + x * x * x;
}

int main()
{
  double N;
  cin >> N;
  double l = 0, r = 100;
  while (abs(r - l) > 0.0001)
  {
    double mid = (l + r) / 2;
    if (xCalculaton(mid) < N)
    {
      l = mid;
    }
    else if (xCalculaton(mid) >= N)
    {
      r = mid;
    }
  }
  cout << fixed << setprecision(5);
  cout << l << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53754395)

### [B13 Supermarket 2](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cl)

しゃくとり法で実装を行う問題。右側のインデックスをjとして、totalCostがKを超えない最大まで増加させていく。ここで、for-loopの処理の中でA[i-1]を減算していくことを忘れてはいけない。

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

  ll ans = 0;
  int j = 0, totalCost = 0;
  for (int i = 0; i < N; i++)
  {
    if (i > 0)
    {
      totalCost -= A[i - 1];
    }

    // totalCostがK以下になるまで右端を進める
    while (j < N && totalCost + A[j] <= K)
    {
      totalCost += A[j];
      j++;
    }

    ans += j - i;
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53763036)

### [B14 Another Subset Sum](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cm)

配列を分割して部分和を計算し、二分探索で求めたい結果Kを得ることができるかを確認する問題。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

void generateSubarraySums(vector<ll> &arr, vector<ll> &result)
{
  int n = arr.size();
  int totalSubsets = 1 << n; // 2^n個の部分集合
  for (int mask = 0; mask < totalSubsets; mask++)
  {
    ll sum = 0;
    for (int i = 0; i < n; i++)
    {
      if (mask & (1 << i))
      {
        sum += arr[i];
      }
    }
    result.push_back(sum);
  }
}

int main()
{
  int N, K;
  cin >> N >> K;
  vector<ll> A(N);
  rep(i, N) cin >> A[i];

  // 配列を二分割
  vector<ll> firstHalf(A.begin(), A.begin() + N / 2);
  vector<ll> secondHalf(A.begin() + N / 2, A.end());

  vector<ll> firstHalfSums, secondHalfSums;
  generateSubarraySums(firstHalf, firstHalfSums);
  generateSubarraySums(secondHalf, secondHalfSums);

  // secondHalfSumsをソート
  sort(secondHalfSums.begin(), secondHalfSums.end());

  string ans = "No";
  for (ll sum : firstHalfSums)
  {
    if (binary_search(secondHalfSums.begin(), secondHalfSums.end(), K - sum))
    {
      ans = "Yes";
      break;
    }
  }

  cout << ans << endl;
  return 0;
}

```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53763650)
