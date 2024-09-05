---
title: "AtCoder Beginner Contest 361 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 361 振り返り

コンテストには参加できなかったため、後からC問題までを実施した。そこまで難易度は高くなく、それぞれの問題について整理することができれば解答できる問題だったと思える。

- A: 整数列の特定の位置に要素を挿入する問題。`vec.insert(itr, value)`を適切に利用することができれば問題なく正答できる。
- B: 3次元空間になっているのでイメージがしにくいが、XYZ軸それぞれについて共通部分が存在するかを整理する問題。
- C: 数列の順番を考慮に入れる必要がないため、ソートして先頭・末尾の要素を消していけば条件に合致する値を得ることができる。

## [A Insert](https://atcoder.jp/contests/abc361/tasks/361_a)

数列Aに対して、K要素目に整数Xを挿入する問題。insertを適切に利用することができれば問題なく解答することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, K, X;
  cin >> N >> K >> X;
  vector<int> A(N);
  rep(i, N) cin >> A[i];
  A.insert(A.begin() + K, X);
  for (int i = 0; i < (int)A.size(); i++)
  {
    if (i != 0)
    {
      cout << " ";
    }
    cout << A[i];
  }
  cout << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc361/submissions/57420644)

## [B Intersection of Cuboids](https://atcoder.jp/contests/abc361/tasks/361_b)

三次元空間ではイメージがしにくいが、それぞれの直方体C1,C2について、XYZ軸それぞれに平行な線分l1,l2が共通であるかどうかを判定すれば良い。これは具体的には、
l1: aとdを結ぶ線分
l2: gとjを結ぶ線分
について、g<=d または a<=jであれば共通部分を持つと言える。この判定をXYZ軸それぞれに実施することで回答をえることができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

bool check(int x1, int x2, int x3, int x4)
{
  if (max(x1, x2) < min(x3, x4))
  {
    return true;
  }
  else
  {
    return false;
  }
}

int main()
{
  vector<int> C1(6), C2(6);
  rep(i, 6) cin >> C1[i];
  rep(i, 6) cin >> C2[i];

  if (check(C1[0], C2[0], C1[3], C2[3]) && check(C1[1], C2[1], C1[4], C2[4]) && check(C1[2], C2[2], C1[5], C2[5]))
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

[提出結果](https://atcoder.jp/contests/abc361/submissions/57422303)

## [C Make Them Narrow](https://atcoder.jp/contests/abc361/tasks/361_c)

この問題では自由に要素を消して良いことになっているが、実際には以下のような整理を行うことができる。

- 昇順に並べられた数列Aについて、先頭と末尾の要素を合計K個削除した時の`最大値 - 最小値`を求める

> 昇順ソートされた数列に対して、中間の要素を消しても`最大値 - 最小値`の最小値には影響を与えないため。

よって、先頭からi個の要素を削除するfor-loopによって判定を行うことで回答を得ることができる。

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

  sort(A.begin(), A.end());
  ll ans = 1'000'000'000;

  for (int i = 0; i <= K; i++)
  {
    ll maxB = A[N - 1 - (K - i)];
    ll minB = A[i];

    ans = min(ans, maxB - minB);
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc361/submissions/57440589)
