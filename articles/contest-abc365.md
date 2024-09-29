---
title: "AtCoder Beginner Contest 365 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 365 振り返り

C問題までを実施した。

- A: 閏年であるかを判定する問題。じょうけんが厳しいものから順に判定していけば良い。
- B: 配列の中で2番目の大きい要素を探して、その要素のイテレータをfind関数によって取得する問題。
- C: 補助額を効率的に探索する必要がある。今回は上限値と加減値が明確であるため二分探索によって探索を行なった。

## [A Leap Year](https://atcoder.jp/contests/abc365/tasks/365_a)

入力したYに対して、制約の厳しいものから順にif文で確認していく具体的には400,100,4と順に確認していくことで、100の倍数だが400の倍数ではない、と言った部分を判定することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int Y;
  cin >> Y;
  if (Y % 400 == 0)
  {
    cout << 366 << endl;
  }
  else if (Y % 100 == 0)
  {
    cout << 365 << endl;
  }
  else if (Y % 4 == 0)
  {
    cout << 366 << endl;
  }
  else
  {
    cout << 365 << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc365/submissions/58173015)

## [B Second Best](https://atcoder.jp/contests/abc365/tasks/365_b)

この問題では、配列に含まれる要素のうち2番目に大きなものを求めた上で、その要素番号を出力する必要がある。
今回は、2番目に大きな値を探すためにsort用配列にコピーしてを用意して、2番目に大きな要素を取得。その後、元の配列の何番目の要素であるかをfind関数によって探索する方針で実装を行なった。

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
  vector<int> sortA = A;
  sort(sortA.begin(), sortA.end());
  auto it = find(A.begin(), A.end(), sortA[N - 2]);
  cout << it - A.begin() + 1 << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc365/submissions/58173089)

## [C Transportation Expenses](https://atcoder.jp/contests/abc365/tasks/365_c)

この問題は、愚直に補助額をループで探索していくとTLEになってしまう。そのため、補助額を二分探索によって計算した。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  ll M;
  cin >> N >> M;
  vector<int> A(N);
  rep(i, N) cin >> A[i];
  ll sumA = 0;
  rep(i, N) sumA += A[i];

  if (sumA <= M)
  {
    cout << "infinite" << endl;
    return 0;
  }

  int l = 0, r = 1'000'000'000;
  while (abs(l - r) > 1)
  {
    int mid = (l + r) / 2;
    ll sum = 0;
    for (int i = 0; i < N; i++)
    {
      sum += min(mid, A[i]);
    }

    if (sum <= M)
    {
      l = mid;
    }
    else
    {
      r = mid;
    }
  }
  cout << l << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc365/submissions/58177263)
