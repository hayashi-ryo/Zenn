---
title: "AtCoder Beginner Contest 366 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: false
---

# AtCoder Beginner Contest 366 振り返り

コンテストには参加できなかったため後からC問題までの演習を実施した。内容として難しいとは感じなかったが、私の思い込みでC問題の回答に時間がかかってしまった。。

- A: 入力情報から全体に対する状況を見極める問題。得票数が過半数を超えているかどうかだけが考慮すべき点となる。
- B: 入力に対して転置行列を作成する問題。基本的な操作となるのでそこまで難しくは感じなかった。
- C: 入力クエリに対して操作を実施していく問題。入力が一定でない点を考慮できておらず時間がかかってしまった。

## [A Election 2](https://atcoder.jp/contests/abc366/tasks/366_a)

入力情報から、どちらかの候補者の得票数が過半数を超えているかを判定すれば良い。今回の問題では全体票数が奇数であるため、細かい考慮も不要となる。(もしこの制約がなければ偶奇に応じて処理を分岐する必要がある。)

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, T, A;
  cin >> N >> T >> A;
  if (T > N / 2 || A > N / 2)
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

[提出結果](https://atcoder.jp/contests/abc366/submissions/57579501)

## [B problem](https://atcoder.jp/contests/abc366/tasks/366_b)

入力文字列を並べて配列Sから転置行列Tを作成する問題。配列のサイズに関しての条件はあらかじめ決定されているため、全体を✳️で初期化し、対応する部分の変換を行なっていく形で対応した。

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
  int maxLength = 0;
  rep(i, N) maxLength = max(maxLength, (int)S[i].size());
  vector<string> T(maxLength, string(N, '*'));

  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < (int)S[i].size(); j++)
    {
      T[j][N - i - 1] = S[i][j];
    }
  }

  for (int i = 0; i < maxLength; i++)
  {
    while (T[i].back() == '*')
    {
      T[i].pop_back();
    }
    cout << T[i] << endl;
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc366/submissions/57594343)

## [C problem](https://atcoder.jp/contests/abc366/tasks/366_c)

入力クエリに応じた操作を実施していく問題。この問題に回答するために私は辞書型配列を利用したが、その場合は要素を減らすときに以下の考慮が必要になる。

> 要素の削除後ボールの数が0になった場合、該当のキーを削除する必要がある。なぜならば、配列.size()で取得する要素数に影響が発生してしまうため。もしこの操作を行わない場合、出力操作を行う際にすべての要素に対して1以上の要素が存在しているものの数を数え上げる必要がある。

また、クエリの処理自体の実装は簡単に実施することができたが、なぜだか出力が想定した値にならな買った。原因としては、頭の中で勝手に入力の形式が一定であると判断してしまっていたためである。クエリが3(出力)の場合は、要素xが入力としてあたえられないため、結果として入力クエリ3が発生するたび入力が一つずつズレていってしまっていた。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  map<int, int> ball;
  for (int i = 0; i < N; i++)
  {
    int query = 0, x = 0;
    cin >> query;
    if (query == 1)
    {
      cin >> x;
      ball[x]++;
    }
    else if (query == 2)
    {
      cin >> x;
      ball[x] -= 1;
      if (ball[x] == 0)
      {
        auto it = ball.find(x);
        ball.erase(it);
      }
    }
    else if (query == 3)
    {
      cout << ball.size() << endl;
    }
  }

  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc366/submissions/57594785)
