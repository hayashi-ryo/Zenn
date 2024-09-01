---
title: "AtCoder Beginner Contest 368 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 368 振り返り

コンテスト中にC問題まで回答を作成して終了した。それぞれの問題は基本操作を実施することで愚直に回答を作成することができる。

- A: 特定の条件で配列Aを操作する問題
- B: 配列のソート、操作、条件を満たしているかを確認する問題
- C: TLEとならないために、少し工夫が必要だが、Nまでのモンスターを倒すターン数を計算する問題

## [A problem](https://atcoder.jp/contests/abc368/tasks/368_a)

条件に則って、K+1番目から下のカードを全て回答配列に挿入し、その後K番目までのカードを挿入することで回答配列を作成することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, K;
  cin >> N >> K;
  vector<int> A(N), ans(N);
  rep(i, N) cin >> A[i];

  for (int i = 0; i < K; i++)
  {
    ans[i] = A[N - K + i];
  }

  // 残りのN-K枚のカードをそのまま続ける
  for (int i = 0; i < N - K; i++)
  {
    ans[K + i] = A[i];
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
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc368/submissions/57039964)

## [B problem](https://atcoder.jp/contests/abc368/tasks/368_b)

条件に則って以下の操作を繰り返していく。

1. 配列の降順ソート
2. 先頭2要素のデクリメント
3. 条件判定チェック

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

bool check(vector<int> c)
{
  int cnt = 0;
  for (int i = 0; i < c.size(); i++)
  {
    if (c[i] > 0)
    {
      cnt++;
    }
  }
  if (cnt >= 2)
  {
    return false;
  }
  else
  {
    return true;
  }
}
int main()
{
  int N;
  cin >> N;
  vector<int> A(N);
  rep(i, N) cin >> A[i];
  int ans = 0;
  while (true)
  {
    ans++;
    sort(A.rbegin(), A.rend());
    A[0]--;
    A[1]--;

    if (check(A))
    {
      break;
    }
  }
  cout << ans << endl;
  return 0;
}

```

[提出結果](https://atcoder.jp/contests/abc368/submissions/57053512)

## [C problem](https://atcoder.jp/contests/abc368/tasks/368_c)

愚直にN体のモンスターを1ターンずつダメージを与えていく方法ではTLEとなってしまう。そのため、少し工夫が必要になる。今回の問題では、

- 開始ターンに関わらず、体力Xのモンスターを倒すためには X/5 + αのターンが必要になる。
- αは、現状のターン数によってダメージが31や13、11と変化するためその操作を実施する必要がある。

上記の工夫を行うことでTLEとならずプログラムを作成することができる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  ll N;
  cin >> N;
  vector<ll> H(N);
  rep(i, N) cin >> H[i];
  ll T = 0; //
  for (int i = 0; i < N; i++)
  {
    int turn = H[i] / 5;
    T += turn * 3;
    H[i] -= turn * 5;

    while (H[i] > 0)
    {
      ++T;
      if (T % 3 == 0)
      {
        H[i] -= 3;
      }
      else
      {
        --H[i];
      }
    }
  }
  cout << T << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc368/submissions/57364856)
