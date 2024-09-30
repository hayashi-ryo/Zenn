---
title: "AtCoder Beginner Contest 364 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 364 振り返り

- A: i=1からN-2の範囲で2回連続"sweet"となっていないかを判定する。
- B: H行W列の2次元配列を用意して、Xの1文字ずつ移動判定を行なっていく。
- C: 料理の個数の最小値を計算すれば良いので、甘さとしょっぱさそれぞれについて一番大きなもの方食べたときに上限値となるものを確認する。

## [A Glutton Takahashi](https://atcoder.jp/contests/abc364/tasks/364_a)

一つ前の時の料理の区分を`previousMeal`として記録し、iを1からN-2まで連続してsweetとなっているものがないかを確認する。ここで、最後の料理で連続してsweetとなってしまう場合はそれ以上食べる必要がないので確認する必要がない。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<string> S(N);
  rep(i, N) cin >> S[i];
  string previousMeal = S[0];
  for (int i = 1; i < N - 1; i++)
  {
    if (S[i] == previousMeal && S[i] == "sweet")
    {
      cout << "No" << endl;
      return 0;
    }
    previousMeal = S[i];
  }
  cout << "Yes" << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc364/submissions/58284007)

## [B Grid Walk](https://atcoder.jp/contests/abc364/tasks/364_b)

H行W列の範囲をルールに従って移動していく問題。典型問題ではグリッドの外に出てしまう場合を条件式に入れることもあるが、今回は、グリッドの外側部分をあらかじめ移動することができない壁と定義して、位置と移動先の条件を無視できるように実装した。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int H, W, Si, Sj;
  cin >> H >> W >> Si >> Sj;
  vector<vector<char>> C(H + 2, vector<char>(W + 2, '#'));
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
    {
      cin >> C[i][j];
    }
  }
  string X;
  cin >> X;

  for (auto x : X)
  {
    if (x == 'L' && C[Si][Sj - 1] == '.')
    {
      Sj--;
    }
    else if (x == 'R' && C[Si][Sj + 1] == '.')
    {
      Sj++;
    }
    else if (x == 'U' && C[Si - 1][Sj] == '.')
    {
      Si--;
    }
    else if (x == 'D' && C[Si + 1][Sj] == '.')
    {
      Si++;
    }
  }

  cout << Si << " " << Sj << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc364/submissions/58284113)

## [C probMinimum Gluttonlem](https://atcoder.jp/contests/abc364/tasks/364_c)

甘さとしょっぱさ、それぞれについて値が大きい順で食べていって、制限値を超えるかどうかを判定していく。甘さとしょっぱさの間に直接的な関係式を導入する必要がないので、同時にループを回していくことで判定することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  ll X, Y;
  cin >> N >> X >> Y;
  vector<int> A(N), B(N);
  rep(i, N) cin >> A[i];
  rep(i, N) cin >> B[i];
  sort(A.rbegin(), A.rend());
  sort(B.rbegin(), B.rend());

  ll sumA = 0, sumB = 0;
  for (int i = 0; i < N; i++)
  {
    sumA += A[i];
    sumB += B[i];
    if (X < sumA || Y < sumB)
    {
      cout << i + 1 << endl;
      return 0;
    }
  }
  cout << N << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc364/submissions/58285396)
