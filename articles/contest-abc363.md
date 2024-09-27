---
title: "AtCoder Beginner Contest 363 振り返り"
emoji: "📒"
type: "idea"
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true
---

# AtCoder Beginner Contest 363 振り返り

C問題までを実施、内容的には基本問題が中心の印象。

- A: 入力からレーティンググレード的なものが上がるタイミングを確認する。この問題の定義では、すべてのレーティングの幅が等しいのでその幅で割って余りを求めることで実装できる。
- B: 全員に対して髪が伸びていくシミュレーションはしていく必要はない、初日の時点で髪の長さがP番目に長い人がT以上の長さになるまでの日数を確認する
- C: 文字列Sに対して、組み合わせを順列で生成する。その後、生成した文字列に長さKの回文部分文字列が含まれるかを判定していけば良い。この問題においてはそのまま実装してもTLEとはならない。

## [A Piling Up](https://atcoder.jp/contests/abc363/tasks/363_a)

現在のレーティングが入力で与えられる。問題で定義されているグレードの範囲は100で固定であるため、入力されたレーティングを100で割ったあまりを100から引いた値が次のグレードに上がるまでに必要な値になる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int rate;
  cin >> rate;
  cout << (int)(100 - (rate % 100)) << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc363/submissions/58140751)

## [B Japanese Cursed Doll](https://atcoder.jp/contests/abc363/tasks/363_b)

N人の人すべての髪を伸ばしていって長さT以上になった人がP人以上になったことを確認する実装は冗長となる。髪の長さ伸びるペースがすべての人で一定であるため、初日の時点で長さがP番目である人が長さT以上になるまでの日数を考えれば良い。
逆に、髪の伸びるペースが一定ではなくとも、一人一人の髪の長さがT以上になるまでの日数を記録して、P番目の人がTを超えるタイミングを出力する方針でもOK。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N, T, P;
  cin >> N >> T >> P;
  vector<int> L(N);
  rep(i, N) cin >> L[i];

  sort(L.rbegin(), L.rend());

  if (T - L[P - 1] < 0) // 初期状態で超えている場合
  {
    cout << 0 << endl;
  }
  else // 髪の長さがP番目の人がT以上の長さになる場合
  {
    cout << T - L[P - 1] << endl;
  }
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc363/submissions/58140814)

## [C problem](https://atcoder.jp/contests/abc363/tasks/363_c)

この問題に回答するために必要な知識は二つ

- 文字列Sの並び替えて得られる文字列を生成すること
- 長さKの回文部分文字列判定を適切に行うことができること

これらを考慮した上で実装したプログラムが以下となる。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

// Kの長さの部分文字列が回文であるかどうかをチェックする関数
bool contains_palindrome(const string &str, int K)
{
  int N = str.size();
  // 長さKの部分文字列をチェック
  for (int i = 0; i <= N - K; ++i)
  {
    bool is_palindrome = true;
    // 部分文字列が回文かどうかを確認
    for (int j = 0; j < K / 2; ++j)
    {
      if (str[i + j] != str[i + K - 1 - j])
      {
        is_palindrome = false;
        break;
      }
    }
    if (is_palindrome)
      return true;
  }
  return false;
}

int main()
{
  int N, K;
  string S;

  // 入力を受け取る
  cin >> N >> K >> S;

  // 回文を含まない順列の個数を数える
  int count = 0;
  sort(S.begin(), S.end());
  do
  {
    if (!contains_palindrome(S, K))
    {
      ++count;
    }
  } while (next_permutation(S.begin(), S.end()));

  // 結果を出力
  cout << count << endl;

  return 0;
}

```

[提出結果](https://atcoder.jp/contests/abc363/submissions/58141054)
