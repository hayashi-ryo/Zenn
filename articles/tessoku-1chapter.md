---
title: "【1章】競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術"
emoji: "💻"
type: "idea" # tech: 技術記事 / idea: アイデア
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true # true: published / false: unpublished
---

# この記事について

この記事では、[競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術](https://www.amazon.co.jp/%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%AE%E9%89%84%E5%89%87-Compass-Books%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E7%B1%B3%E7%94%B0-%E5%84%AA%E5%B3%BB-ebook/dp/B0BDZGDM9J)を自分なりに理解するために、作成したコードや理解した考え方を記録していくものです。記事は、章ごとに作成していき、最終的に全10記事となる予定です。

## 1章 アルゴリズムと計算量

この章では、競技プログラムを行う上で一番基本となるアルゴリズムの考え方や、時間内に動作するプログラムを作成するために必要な計算量の考え方を学びます。

## A問題

### [A01 The First Problem](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_a)

変数の定義、入出力操作といった一番の基本処理を実施する問題。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main(){
  int N;
  cin >> N;
  cout << N * N << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53466965)

### [A02 Linear Search](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_b)

A01と同じく、入出力操作を行い条件を満たしているかを確認する問題。愚直に実施する場合は、vectorを用意するのではなく入力しながら変数Xと一致するものがあるか確認すれば良いが、今回はvectorへ挿入し、find関数で存在を確認する方針で実装を行なった。

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

  if (find(A.begin(), A.end(), X) == A.end())
  {
    cout << "No" << endl;
  }
  else
  {
    cout << "Yes" << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53467277)

### [A03 Two Cards](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_c)

二つのvectorに値を挿入し、全探索を行う問題。そのまま回答しても計算量は$O(N^2)$であり、TLEになることはないが、省略のため予めソートを行なった上で求める値より大きくなった場合は次のループに進むよう実装を行なった。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, K;
  cin >> N >> K;
  vector<int> P(N), Q(N);
  rep(i, N) cin >> P[i];
  rep(i, N) cin >> Q[i];
  sort(P.begin(), P.end());
  sort(Q.begin(), Q.end());

  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < N; j++)
    {
      if (P[i] + Q[j] == K)
      {
        cout << "Yes" << endl;
        return 0;
      }
      else if (P[i] + Q[j] > K)
      {
        break;
      }
    }
  }
  cout << "No" << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53467415)

### [A04 Binary Representation](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d)

10進数から2進数へ変換を行う基本問題。二つの方法で解答を行なった。

1. 愚直に処理を実施
10進数<->2進数の変換は、$2^i$で割り算のあまりがあるかどうかで判定できる。その性質を利用して、1桁ずつ出力をおこなっていった。
2. `bitset`関数を利用
bitset関数は、任意の整数をbit変換、即ち2進数に変換することができる。変換したものをstring形に変換すれば、欲しい結果を得ることができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  for (int i = 9; i > -1; --i)
  {
    int wari = (1 << i);
    cout << ((N / wari) % 2);
  }
  cout << endl;

  // 別解
  string ans = bitset<10>(N).to_string();
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53475600)

### [A05 Three Cards](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e)

ループ処理を利用して前探索を行う問題。3重ループではTLEとなる可能性があるため、2重ループで判定を行なっていく。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, K;
  cin >> N >> K;
  int ans = 0;
  for (int i = 1; i <= N; i++)
  {
    for (int j = 1; j <= N; j++)
    {
      if (1 <= (K - i - j) && (K - i - j) <= N)
      {
        ++ans;
      }
    }
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53475839)

## B問題

### [B01 A+B Problem](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bz)

A01と同じく、変数定義と入出力をしっかり実施できれば問題ない基本問題。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int A, B;
  cin >> A >> B;
  cout << A + B << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53476009)

### [B02 Divisor Check](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ca)

入力した数値A,Bの間に100の約数であるものが含まれるか確認する問題。約数の確認は`if(100%i==0)`で100をiで割った時にあまりが0となる場合、となる。
また、個人的な実装の趣味で、途中で`return 0`をするのではなく、`return 0`は一箇所、結果出力箇所も極力1箇所、としている。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int A, B;
  cin >> A >> B;
  string ans = "No";
  for (int i = A; i <= B; i++)
  {
    if (100 % i == 0)
    {
      ans = "Yes";
      break;
    }
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53476094)

### 「B03 Supermarket 1](<https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cb>)

3重ループで実装すると、計算量が$O(N^3)$になってしまう。そのため、2重ループと二分探索を利用して計算量の改善を行なった。

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
  sort(A.begin(), A.end());

  bool ans = false;
  for (int i = 0; i < N; i++)
  {
    for (int j = i + 1; j < N; j++)
    {
      int target = 1000 - A[i] - A[j];
      // lower_bound を使用して target を配列中で探索
      auto itr = lower_bound(A.begin() + j + 1, A.end(), target); // j以降での探索を効率化
      if (itr != A.end() && *itr == target)
      {
        ans = true;
        break;
      }
    }
    if (ans)
    {
      break;
    }
  }

  if (ans)
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

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53476624)

### [B04 Binary Representation 2](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cc)

10進数から2進数に変換する基本問題。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string N;
  int ans = 0;
  cin >> N;
  int power = N.size() - 1;
  for (int i = 0; i < N.size(); i++)
  {
    if (N[i] == '1')
    {
      ans += pow(2, power);
    }
    --power;
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53476859)
