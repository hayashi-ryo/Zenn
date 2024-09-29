---
title: "AtCoder Beginner Contest 373 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 373 振り返り

久しぶりにコンテストに参加。C問題までを回答。D問題はグラフで無理と判断したが、E問題に解答できそうな雰囲気を感じる。しかし解くことができず。。

- A: 入力文字列の長さが条件を満たしているかを確認する。
- B: 与えられば配列のキーボードにおいて、A-Zの順番で押していく。charを適切にインデックスとして処理することができれば問題ない。
- C: 最大化する以外に条件がないため、AとBを配列に入れて最大値を取得。その和を出力する。

## [A September](https://atcoder.jp/contests/abc373/tasks/373_a)

12の入力が与えられ、順番==文字列の長さであることを確認していけば良い。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int ans = 0;
  for (int i = 1; i <= 12; i++)
  {
    string a;
    cin >> a;
    if ((int)a.size() == i)
    {
      ++ans;
    }
  }
  cout << ans << endl;

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc373/submissions/58180421)

## [B 1D Keyboard](https://atcoder.jp/contests/abc373/tasks/373_b)

入力として与えられたキーボードのそれぞれの位置をあらかじめ記録しておき、その後A-Zの順番で移動距離の合計を計算していく。ここで、c-'Aのような形で文字のインデックスを得ることができることを利用する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S;
  cin >> S;
  vector<int> position(26);
  for (int i = 0; i < 26; ++i)
  {
    position[S[i] - 'A'] = i;
  }

  // 最初の位置は 'A' の場所
  int currentPos = position[0]; // 'A'の位置
  int totalDistance = 0;        // 合計移動距離

  // 'B' から 'Z' まで順に移動していく
  for (char c = 'B'; c <= 'Z'; ++c)
  {
    int nextPos = position[c - 'A'];            // 次の文字の位置
    totalDistance += abs(nextPos - currentPos); // 移動距離を足す
    currentPos = nextPos;                       // 現在の位置を更新
  }

  // 結果を出力
  cout << totalDistance << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc373/submissions/58184466)

## [C problem](https://atcoder.jp/contests/abc373/tasks/373_c)

正直なところこの問題がC問題であることに疑問を感じた。。入力として配列AとBを与えてそれぞれの配列の最大値の合計を出力すれば良い。要素の選択に関わる条件などは存在しない。

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
  rep(i, N) cin >> A[i];
  rep(i, N) cin >> B[i];

  sort(A.begin(), A.end());
  sort(B.begin(), B.end());

  cout << A[N - 1] + B[N - 1] << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc373/submissions/58189798)
