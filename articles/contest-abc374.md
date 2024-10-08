---
title: "AtCoder Beginner Contest 374 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 374 振り返り

コンテスト中にD問題までを回答。C問題までは基本問題、D問題は少し計算に工夫が必要な問題出会った

- A: 文字列操作の超基本問題
- B: 異なる文章であるかどうかを判定するフローを整理することができれば回答できる
- C: Nの上限がそこまで大きくないため、全ての組み合わせについて人数差を確認していく問題
- D: 線分を結ぶ順番、始点終点の選び方を確認していき最小値を求めていく問題

## [A Takahashi san 2](https://atcoder.jp/contests/abc374/tasks/374_a)

与えられた文字列の末尾3文字が`san`であるかどうかを判定する問題。末尾3文字を切り取ることができれば回答はできる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S;
  cin >> S;
  string ans = "";
  for (int i = 0; i < 3; i++)
  {
    ans += S[S.size() - 3 + i];
  }

  if (ans == "san")
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

[提出結果](https://atcoder.jp/contests/abc374/submissions/58433823)

## [B Unvarnished Report](https://atcoder.jp/contests/abc374/tasks/374_b)

文書が改竄されているかどうかの判定は以下のフローで行う。

1. 文書が一致するかどうかを判定する
2. それぞれの文書の文字数を確認して、その文字までに異なる文字が存在するか確認する
3. 2までに異なる文字が存在しない場合、短い方の文字数＋1が答えとなる。

コンテスト中はSとTの文字列の長さを比較して条件分岐でそれぞれfor-loopを作成したが、よく考えると`min(S.size(),T.size())`でよかった。ここは反省点。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  string S, T;
  cin >> S >> T;
  int sizeS = (int)S.size();
  int sizeT = (int)T.size();
  if (S == T)
  {
    cout << 0 << endl;
    return 0;
  }

  if (sizeS <= sizeT)
  {
    for (int i = 0; i < sizeS; i++)
    {
      if (S[i] != T[i])
      {
        cout << i + 1 << endl;
        return 0;
      }
    }
    cout << sizeS + 1 << endl;
  }
  else
  {
    for (int i = 0; i < sizeT; i++)
    {
      if (S[i] != T[i])
      {
        cout << i + 1 << endl;
        return 0;
      }
    }
    cout << sizeT + 1 << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc374/submissions/58443995)

## [C Separated Lunch](https://atcoder.jp/contests/abc374/tasks/374_c)

Nの制約が大きくないため、$2^N$とおりの全ての組み合わせに対して人数差を確認して、もっとも小さいものを探し出せば良い。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> K(N);
  for (int i = 0; i < N; i++)
  {
    cin >> K[i];
  }
  int total_sum = accumulate(K.begin(), K.end(), 0);
  int min_diff = total_sum;

  for (int mask = 0; mask < (1 << N); ++mask)
  {
    int sum_A = 0;
    for (int i = 0; i < N; ++i)
    {
      if (mask & (1 << i))
      {
        sum_A += K[i];
      }
    }
    int sum_B = total_sum - sum_A;              
    min_diff = min(min_diff, max(sum_A, sum_B));
  }

  cout << min_diff << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc374/submissions/58447199)

## [D Laser Marking](https://atcoder.jp/contests/abc374/tasks/374_d)

この問題では、いくつかのパラメータを全探索で確認していく必要がある。

- 印字する順序をどうするか
- 始点をどちらに置くか
- 照射している時としていない時で移動速度が異なる。

これらを考慮して全探索するプログラムが以下です。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

double distance(double x1, double y1, double x2, double y2)
{
  return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

int main()
{
  int N, S, T;
  cin >> N >> S >> T;

  vector<pair<pair<double, double>, pair<double, double>>> segments(N);

  for (int i = 0; i < N; ++i)
  {
    cin >> segments[i].first.first >> segments[i].first.second;  
    cin >> segments[i].second.first >> segments[i].second.second;
  }

  double min_time = 1e9;
  vector<int> indices(N);
  for (int i = 0; i < N; ++i)
    indices[i] = i;

  do
  {
    for (int start_mask = 0; start_mask < (1 << N); ++start_mask)
    {
      double current_time = 0;
      double current_x = 0, current_y = 0;

      for (int i = 0; i < N; ++i)
      {
        int idx = indices[i];

        // 始点と終点を選択
        double ax, ay, bx, by;
        if (start_mask & (1 << i))
        {
          ax = segments[idx].first.first;
          ay = segments[idx].first.second;
          bx = segments[idx].second.first;
          by = segments[idx].second.second;
        }
        else
        {
          ax = segments[idx].second.first;
          ay = segments[idx].second.second;
          bx = segments[idx].first.first;
          by = segments[idx].first.second;
        }
        current_time += distance(current_x, current_y, ax, ay) / S;
        current_time += distance(ax, ay, bx, by) / T;

        current_x = bx;
        current_y = by;
      }
      min_time = min(min_time, current_time);
    }
  } while (next_permutation(indices.begin(), indices.end()));

  cout << fixed << min_time << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc374/submissions/58449798)
