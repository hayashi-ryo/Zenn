---
title: "AtCoder Beginner Contest 355 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 355 振り返り

久しぶりにバーチャルではなく実時間で参加したコンテストでした。結果自体はD問題まで完答。今の私のレートから考えると健闘だと思えます。そのうちにE問題、F問題まで解いていけるようにしていきたいと思います。

以下はそれぞれの問題の所感です。

- A: {1,2,3}というセットに対して、入力が重複しているか、別々のものであるかを確認するだけ。
- B: 二つの配列から生成される配列Cがそれぞれの要素を順番に持つかを確認する問題。配列Cと配列Aの要素を確認していくことで声絵を得ることができる。
- C: ビンゴカードを用意して、ターンごとにビンゴを達成するか、もしくは最後まで達成しないのかを確認する問題。縦・横・ななめの3パターンのビンゴについて丁寧に整理することで実装ができる。
- D: 複数の区間に対して共通区間を持つ組み合わせの数を数える問題。方針としては、それぞれの始点と終点を探索し、アクティブな状態を数え上げる形で実装を行った。

## [A problem](https://atcoder.jp/contests/abc355/tasks/abc355_a355_a)

2つの入力が同一であるかを確認した上で、同一の場合は特定できないため-1を、同一でない場合は合計値6から入力を引いた値を出力す流ことで求める答えを得ることができます。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int A, B;
  cin >> A >> B;
  if (A != B)
  {
    cout << 6 - A - B << endl;
  }
  else
  {
    cout << -1 << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc355/submissions/53826280)

## [B problem](https://atcoder.jp/contests/abc355/tasks/abc355_b)

数列A,Bから生成される数列Cの要素が、入れ子になっているかを確認する問題です。方針としては、

- 配列Cを用意し、全ての配列をソートする
- 配列Cの要素を探索する中で、配列Aの要素が連続するものがあるかを確認する

ことで実装可能です。配列Bの要素については配列Cの生成のためにだけ利用するため、ソートなどは不要ではありますが実装上ソートはしました。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, M;
  cin >> N >> M;
  vector<int> A(N), B(M), C;
  set<int> setA;
  rep(i, N)
  {
    cin >> A[i];
    setA.insert(A[i]);
    C.push_back(A[i]);
  }

  rep(i, M)
  {
    cin >> B[i];
    C.push_back(B[i]);
  }
  sort(A.begin(), A.end());
  sort(B.begin(), B.end());
  sort(C.begin(), C.end());
  string ans = "No";

  for (int i = 0; i < (int)C.size(); i++)
  {
    if (setA.count(C[i]) && setA.count(C[i - 1]))
    {
      ans = "Yes";
      break;
    }
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc355/submissions/53850239)

## [C problem](https://atcoder.jp/contests/abc355/tasks/abc355_c)

この問題では、ターンごとにビンゴ判定を実施していく必要がある。しかし、すでに開けられている番号を記録し毎ターン全ての縦横斜めに対してビンゴ判定を行うとTLEとなってしまう。そのため、ビンゴ判定自体を少し工夫する必要がある。今回の実装ではビンゴ判定を以下の方針で行うこととした

- 縦・横の判定
縦・横ごとの空いている数を記録する配列(今回のプログラムではrowCount,colCount)を用意して、ターンごとにインクリメントしていく。そして、インクリメントした縦、または横の配列の値がNと一致していればビンゴとなる。
- 斜めの判定
斜めの場合は配列ではなく、変数として定義した。左上から右下への斜めと右上から左下への斜めそれぞれに対して、毎ターン該当する場合はインクリメントしていく。その後、縦横の判定と同じく変数がNと一致していればビンゴしていることがわかる。

今回の問題では、「ビンゴカードの状態」自体を配列や変数として保有するのではなく、縦横斜めそれぞれがどれくらい空いているかを保有することで計算量も少なく実装することができた。

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main()
{
  int N, T;
  cin >> N >> T;

  vector<int> A(T);
  for (int i = 0; i < T; ++i)
  {
    cin >> A[i];
  }

  // 行と列と対角線のカウント
  vector<int> rowCount(N, 0);
  vector<int> colCount(N, 0);
  int diag1Count = 0, diag2Count = 0;

  // マス目に対応する行と列を保存するマップ
  unordered_map<int, pair<int, int>> positionMap;
  for (int i = 0; i < N; ++i)
  {
    for (int j = 0; j < N; ++j)
    {
      int num = N * i + j + 1;
      positionMap[num] = {i, j};
    }
  }

  // 印をつけてビンゴを判定
  for (int turn = 0; turn < T; ++turn)
  {
    int num = A[turn];
    auto pos = positionMap[num];
    int row = pos.first;
    int col = pos.second;

    // 行、列、対角線のカウントを増やす
    rowCount[row]++;
    colCount[col]++;
    if (row == col)
      diag1Count++;
    if (row + col == N - 1)
      diag2Count++;

    // ビンゴの判定
    if (rowCount[row] == N || colCount[col] == N || diag1Count == N || diag2Count == N)
    {
      cout << turn + 1 << endl;
      return 0;
    }
  }

  // ビンゴを達成しない場合
  cout << -1 << endl;
  return 0;
}

```

[提出結果](https://atcoder.jp/contests/abc355/submissions/53867340)

## [D - Intersecting Intervals](https://atcoder.jp/contests/abc355/tasks/abc355_d)

この問題は複数の区間に対して、共通区間を持つ組み合わせの数を数える問題。実装を行うために以下のように方針の整理を行った。

**方針**

l,rの値が非常に大きいため、それぞれの位置をforループなどで探索していくことは計算量の問題から難しい。そのため、入力の情報だけを整理して実装を行う必要があ理ます。
今回は、始点と終点を一つの配列にまとめて格納、ソートし処理していく方針としました。

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int N;
  cin >> N;

  vector<pair<int, int>> intervals(N);
  for (int i = 0; i < N; ++i)
  {
    cin >> intervals[i].first >> intervals[i].second;
  }

  // 区間の始点と終点を記録
  vector<pair<int, int>> events;
  for (const auto &interval : intervals)
  {
    events.emplace_back(interval.first, 1);   // 始点を +1 として記録
    events.emplace_back(interval.second, -1); // 終点を -1 として記録
  }

  // 始点と終点をソート
  sort(events.begin(), events.end(), [](const pair<int, int> &a, const pair<int, int> &b)
       {
        if (a.first != b.first) return a.first < b.first;
        return a.second > b.second; });
  long long intersectCount = 0;
  long long activeIntervals = 0;

  // イベントを順に処理
  for (const auto &event : events)
  {
    if (event.second == 1)
    {
      // 始点の場合、現在のアクティブな区間の数だけ新しい共通部分ができる
      intersectCount += activeIntervals;
      activeIntervals++;
    }
    else
    {
      // 終点の場合、アクティブな区間の数を減らす
      activeIntervals--;
    }
  }

  cout << intersectCount << endl;
  return 0;
}

```

[提出結果](https://atcoder.jp/contests/abc355/submissions/53877710)
