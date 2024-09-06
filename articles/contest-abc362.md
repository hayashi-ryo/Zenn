---
title: "AtCoder Beginner Contest 362 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 362 振り返り

コンテストに参加できなかったため、後から問題演習のみを実施した。C問題まで完答している。

- A: 入力に応じて条件判定を行い、演算と出力を行う問題。
- B: 直角三角形の成立条件を適切に判定する問題。
- C: 入力情報から条件を満たす数列を生成することができるかを判定する問題。愚直にやっていくとTLEとなってしまうため、ある程度の整理が必要になる。

## [A Buy a Pen](https://atcoder.jp/contests/abc362/tasks/362_a)

入力として、「判定文字列C」と「価格」が与えられるので、判定文字列によって演算を分岐させることで実装できる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int R, G, B;
  string C;
  cin >> R >> G >> B;
  cin >> C;
  int ans = 100;

  if (C == "Red")
  {
    ans = min(G, B);
  }
  else if (C == "Green")
  {
    ans = min(R, B);
  }
  else if (C == "Blue")
  {
    ans = min(R, G);
  }
  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc362/submissions/57450463)

## [B  Right Triangle](https://atcoder.jp/contests/abc362/tasks/362_b)

直角三角形の成立条件である三平方の定理を満たすかどうかを判定する。判定を簡素化するためにいくつかの工夫を行っている。

- XY軸を跨ぐ直線の距離の判定には正負判定などが必要になるので、全ての座標を+1000することで、正負判定をなくしている。
- long long型でルートを取ると誤差が生じる可能性があるため、正規の三平方の定理ではなく2乗+2乗=2乗という条件を満たしているか判定を行った。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  vector<ll> XY(6);
  for (int i = 0; i < 6; i++)
  {
    cin >> XY[i];
    XY[i] += 1000;
  }

  ll AB2, BC2, CA2;
  AB2 = (XY[0] - XY[2]) * (XY[0] - XY[2]) + (XY[1] - XY[3]) * (XY[1] - XY[3]);
  BC2 = (XY[2] - XY[4]) * (XY[2] - XY[4]) + (XY[3] - XY[5]) * (XY[3] - XY[5]);
  CA2 = (XY[4] - XY[0]) * (XY[4] - XY[0]) + (XY[5] - XY[1]) * (XY[5] - XY[1]);

  if (AB2 == BC2 + CA2 || BC2 == CA2 + AB2 || CA2 == AB2 + BC2)
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

[提出結果](https://atcoder.jp/contests/abc362/submissions/57450712)

## [C Sum = 0](https://atcoder.jp/contests/abc362/tasks/362_c)

Xの合計値が0となる値が存在するか、だけの判定であればLの和とRの和がそれぞれ0以上0以下であることを確認すればよい。その上で、具体的な値を求めるために、以下のステップで演算を行った。

> Xの合計値が0となることがわかっている状態

1. 全てのXについてX_i = L_i(下限値)とする
2. それぞれのX_iについて、Xの総和が0となるためにどの程度Rに近づけていけば良いかを以下の式で判定する

```cpp
D = min(R[i]-L[i], -sumX)
```

この式では、現在のXの総和に対してRiまで近づけてよいのか、それともそこまで近づけることができないのかを判定している。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<ll> L(N), R(N), ans(N);
  ll minX = 0, maxX = 0, sumX = 0;
  for (int i = 0; i < N; i++)
  {
    cin >> L[i] >> R[i];
    minX += L[i];
    maxX += R[i];
    sumX += L[i];
    ans[i] = L[i];
  }

  if (minX <= 0 && 0 <= maxX)
  {
    cout << "Yes" << endl;
    for (int i = 0; i < N; i++)
    {
      ll D = min(R[i] - L[i], -sumX);
      sumX += D;
      ans[i] += D;
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
  }
  else
  {
    cout << "No" << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc362/submissions/57464251)
