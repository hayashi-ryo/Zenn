---
title: "【2章】競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術"
emoji: "💻"
type: "idea" # tech: 技術記事 / idea: アイデア
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true # true: published / false: unpublished
---

# この記事について

この記事では、[競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術](https://www.amazon.co.jp/%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%AE%E9%89%84%E5%89%87-Compass-Books%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E7%B1%B3%E7%94%B0-%E5%84%AA%E5%B3%BB-ebook/dp/B0BDZGDM9J)を自分なりに理解するために、作成したコードや理解した考え方を記録していくものです。記事は、章ごとに作成していき、最終的に全10記事となる予定です。

## 2章 累積和

競技プログラミングを行う上で、計算量は必ず意識する必要があります。1章で学んだ全探索では計算量が大きくなり、TLEとなってしまうような場合に、累積和の考え方を利用してアルゴリズムを効率化することができます。
累積和とは一言でいうと、計算に必要な要素を予め計算しておく方法です。例えば、日付ごとの来場者数がインプットとして与えられる場合、特定の期間の来場者数合計は全探索によって計算することができます。しかし、計算する項目数が多い場合や、大量の出力を求められる場合、愚直な計算では間に合いません。そこで累積和の考え方を利用します。

## A問題

### [A06 How Many Guests?](https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai)

累積和を扱う基本問題。実装方針として、「添字は0から使う」を意識して累積和の計算を行い、出力したい内容を計算する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, Q;
  cin >> N >> Q;
  vector<int> A(N), L(Q), R(Q), sumA(N, 0);

  for (int i = 0; i < N; i++)
  {
    cin >> A[i];
    if (i != 0)
    {
      sumA[i] = sumA[i - 1] + A[i];
    }
    else
    {
      sumA[i] = A[i];
    }
  }

  for (int i = 0; i < Q; i++)
  {
    cin >> L[i] >> R[i];
    L[i]--;
    R[i]--;
  }

  for (int i = 0; i < Q; i++)
  {
    cout << sumA[R[i]] - sumA[L[i] - 1] << endl;
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53484428)

### [A07 Event Attendance](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g)

累積和を計算するために、まずは誰かが参加した日を$+$、帰った翌日に$-$として累積和を計算する。その後、予め計算した累積和を取ると、それぞれの日ごとに参加した出席者数を求めることができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int D, N;
  cin >> D >> N;
  vector<int> L(N), R(N), AttendanceOfDay(D, 0), TotalOfAttendance(D, 0);
  for (int i = 0; i < N; i++)
  {
    cin >> L[i] >> R[i];
    L[i]--;
    R[i]--;
    AttendanceOfDay[L[i]]++;
    if (R[i] + 1 < D)
    { // 範囲内であることを確認
      AttendanceOfDay[R[i] + 1]--;
    }
  }

  for (int i = 0; i < D; i++)
  {
    if (i == 0)
    {
      TotalOfAttendance[i] = AttendanceOfDay[i];
    }
    else
    {
      TotalOfAttendance[i] = TotalOfAttendance[i - 1] + AttendanceOfDay[i];
    }
  }

  for (int i = 0; i < D; i++)
  {
    cout << TotalOfAttendance[i] << endl;
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53484510)

### [A08 Two Dimensional Sum](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h)

1次元の累積和ではなく、2次元の累積和を計算する問題。縦方向と横方向を個別に累積していくのが王道だが、今回は同時に累積和を計算する方針とした。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int H, W, Q;
  cin >> H >> W;
  vector<vector<int>> cell(H, vector<int>(W, 0));
  for (int i = 0; i < H; i++)
  {
    for (int j = 0; j < W; j++)
    {
      cin >> cell[i][j];
    }
  }
  cin >> Q;
  vector<int> A(Q), B(Q), C(Q), D(Q);
  for (int i = 0; i < Q; i++)
  {
    cin >> A[i] >> B[i] >> C[i] >> D[i];
    A[i]--;
    B[i]--;
    C[i]--;
    D[i]--;
  }

  // 二次元累積和の計算
  vector<vector<int>> sumCell(H + 1, vector<int>(W + 1, 0));
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
    {
      sumCell[i][j] = cell[i - 1][j - 1] + sumCell[i - 1][j] + sumCell[i][j - 1] - sumCell[i - 1][j - 1];
    }
  }

  // クエリに応じた範囲内の合計値を計算
  for (int i = 0; i < Q; i++)
  {
    int ans = sumCell[C[i] + 1][D[i] + 1];
    if (A[i] > 0)
      ans -= sumCell[A[i]][D[i] + 1];
    if (B[i] > 0)
      ans -= sumCell[C[i] + 1][B[i]];
    if (A[i] > 0 && B[i] > 0)
      ans += sumCell[A[i]][B[i]];
    cout << ans << endl;
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53520200)

### [A09 Winter in ALGO Kingdom](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i)

A08であらかじめ与えられていたそれぞれのセルの情報を自分で作り出す必要がある問題。積雪する範囲の左上(A,B)と右下(C,D)が与えられており、この条件を累積和の計算のために分解すると

(A,B) : +1
(A,D+1) : -1
(C+1,B) : -1
(C+1,D+1) : +1

とすれば良いことがわかる。この値をあらかじめ準備することができたら、その行列に対して累積和の計算を実施すればOK。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int H, W, N;
  cin >> H >> W >> N;
  vector<int> A(N), B(N), C(N), D(N);
  for (int i = 0; i < N; i++)
  {
    cin >> A[i] >> B[i] >> C[i] >> D[i];
    A[i]--;
    B[i]--;
    C[i]--;
    D[i]--;
  }

  // 積雪情報を登録
  vector<vector<int>> snow(H + 1, vector<int>(W + 1, 0));
  for (int i = 0; i < N; i++)
  {
    snow[A[i]][B[i]]++;
    snow[A[i]][D[i] + 1]--;
    snow[C[i] + 1][B[i]]--;
    snow[C[i] + 1][D[i] + 1]++;
  }

  // 累積和を計算
  vector<vector<int>> sumSnow(H + 1, vector<int>(W + 1, 0));
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
    {
      sumSnow[i][j] = snow[i - 1][j - 1] + sumSnow[i - 1][j] + sumSnow[i][j - 1] - sumSnow[i - 1][j - 1];
    }
  }

  // 結果を出力
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
    {
      if (j != 1)
      {
        cout << " ";
      }
      cout << sumSnow[i][j];
    }
    cout << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53533407)

### [A10 Resort Hotel](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_j)

**累積和**を計算するわけではないが、累積和の考え方を利用して実装を行う。そもそも累積和とは、部分的な集合をあらかじめ計算しておくことで最終的な計算量を改善しようとする考え方である。この問題でも「左右の端からみた最大の部屋人数」をあらかじめ計算しておくことによって、最終的な出力を高速に実施することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, D;
  cin >> N;
  vector<int> A(N);
  for (int i = 0; i < N; i++)
  {
    cin >> A[i];
  }
  cin >> D;
  vector<int> L(D), R(D);
  for (int i = 0; i < D; i++)
  {
    cin >> L[i] >> R[i];
    L[i]--;
    R[i]--;
  }

  // 左右の端から最も大きい部屋の情報を記録していって、L-Rの範囲外で最大の部屋を決定する。
  vector<int> leftMaxRoom(N, 0);
  vector<int> rightMaxRoom(N, 0);

  // 左から最大値を記録
  for (int i = 0; i < N; i++)
  {
    if (i == 0)
    {
      leftMaxRoom[i] = A[i];
    }
    else
    {
      leftMaxRoom[i] = max(leftMaxRoom[i - 1], A[i]);
    }
  }

  // 右から最大値を記録
  for (int i = N - 1; i >= 0; i--)
  {
    if (i == N - 1)
    {
      rightMaxRoom[i] = A[i];
    }
    else
    {
      rightMaxRoom[i] = max(rightMaxRoom[i + 1], A[i]);
    }
  }

  // 出力
  for (int i = 0; i < D; i++)
  {
    int maxOutside = 0;
    if (L[i] > 0)
      maxOutside = max(maxOutside, leftMaxRoom[L[i] - 1]);
    if (R[i] + 1 < N)
      maxOutside = max(maxOutside, rightMaxRoom[R[i] + 1]);
    cout << maxOutside << endl;
  }

  return 0;
}

```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53533938)

## B問題

### [B06 Lottery](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ce)

累積和の基本問題。n回目までの勝ち数をあらかじめ計算しておき、LからRの範囲の勝ち数と負け数を計算する。

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
  vector<int> L(Q), R(Q);
  for (int i = 0; i < Q; i++)
  {
    cin >> L[i] >> R[i];
    L[i]--;
    R[i]--;
  }

  // n回目までの累積和を計算
  vector<int> sumLottery(N);
  for (int i = 0; i < N; i++)
  {
    if (i == 0)
    {
      sumLottery[i] = A[i];
    }
    else
    {
      sumLottery[i] = sumLottery[i - 1] + A[i];
    }
  }

  // 結果を出力していく
  for (int i = 0; i < Q; i++)
  {
    int win = sumLottery[R[i]] - sumLottery[L[i] - 1];
    int lose = R[i] - (L[i] - 1) - win;
    string ans = "";
    if (win > lose)
    {
      ans = "win";
    }
    else if (win < lose)
    {
      ans = "lose";
    }
    else if (win == lose)
    {
      ans = "draw";
    }
    cout << ans << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53536181)

### [B07 Convenience Store 2](https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_al)

出勤情報から各時間帯ごとの従業員数を数え上げる問題。この問題では、時間帯ごとの従業員数を累積和として計算すれば良い。また、その前情報の整理として、出勤したら+、退勤したら-とするリストを作成しておく。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int T, N;
  cin >> T >> N;
  vector<int> L(N), R(N);
  rep(i, N) cin >> L[i] >> R[i];
  vector<int> workSchedule(T, 0), sumWorkSchedule(T, 0);

  for (int i = 0; i < N; i++)
  {
    workSchedule[L[i]]++;
    workSchedule[R[i]]--;
  }

  for (int i = 0; i < T; i++)
  {
    if (i == 0)
    {
      sumWorkSchedule[i] = workSchedule[i];
    }
    else
    {
      sumWorkSchedule[i] = sumWorkSchedule[i - 1] + workSchedule[i];
    }
  }

  for (int i = 0; i < T; i++)
  {
    cout << sumWorkSchedule[i] << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53536278)

### [B08 Counting Points](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cg)

固定範囲の累積和を計算する問題です。この問題では、与えられた座標情報を集計し、その左上全ての点の数を座標ごとに記録していきます。この記録した累積和を利用して、最終的な出力を行います。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, Q;
  cin >> N;
  vector<vector<int>> cell(1600, vector<int>(1600, 0));
  for (int i = 0; i < N; i++)
  {
    int x, y;
    cin >> x >> y;
    cell[x][y]++;
  }
  cin >> Q;
  vector<int> a(Q), b(Q), c(Q), d(Q);
  rep(i, Q) cin >> a[i] >> b[i] >> c[i] >> d[i];
  // 累積和を計算
  vector<vector<int>> sumCell(1600, vector<int>(1600, 0));
  for (int i = 1; i <= 1500; i++)
  {
    for (int j = 1; j <= 1500; j++)
    {
      sumCell[i][j] = cell[i][j] + sumCell[i - 1][j] + sumCell[i][j - 1] - sumCell[i - 1][j - 1];
    }
  }

  // 累積和の情報を元に結果を出力
  for (int i = 0; i < Q; i++)
  {
    cout << sumCell[c[i]][d[i]] - sumCell[c[i]][b[i] - 1] - sumCell[a[i] - 1][d[i]] + sumCell[a[i] - 1][b[i] - 1] << endl;
  }
  return 0;
}

```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53536377)

### [B09 Papers](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ch)

それぞれの座標に紙が置かれているかどうかを累積和として計算する。特定の座標について累積和>0となる場合の点の数を数え上げれば良い。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<int> A(N), B(N), C(N), D(N);
  vector<vector<int>> cell(1600, vector<int>(1600, 0));
  for (int i = 0; i < N; i++)
  {
    cin >> A[i] >> B[i] >> C[i] >> D[i];
    cell[A[i]][B[i]]++;
    cell[A[i]][D[i]]--;
    cell[C[i]][B[i]]--;
    cell[C[i]][D[i]]++;
  }
  // 累積和を計算する
  vector<vector<int>> sumCell(1600, vector<int>(1600, 0));
  for (int i = 0; i <= 1500; i++)
  {
    for (int j = 0; j <= 1500; j++)
    {
      sumCell[i][j] = cell[i][j] + (i > 0 ? sumCell[i - 1][j] : 0) + (j > 0 ? sumCell[i][j - 1] : 0) - (i > 0 && j > 0 ? sumCell[i - 1][j - 1] : 0);
    }
  }

  // 結果を集計する
  int ans = 0;
  for (int i = 0; i <= 1500; i++)
  {
    for (int j = 0; j <= 1500; j++)
    {
      if (sumCell[i][j] > 0)
      {
        ans++;
      }
    }
  }

  cout << ans << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/tessoku-book/submissions/53536421)
