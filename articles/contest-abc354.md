---
title: "AtCoder Beginner Contest 354 振り返り"
emoji: "📒"
type: "idea" # tech: 技術記事 / idea: アイデア
topics: ["AtCoder","study","CS","競技プログラミング"]
published: true # true: published / false: unpublished
---

# AtCoder Beginner Contest 354 振り返り

AB問題を解答し、C問題について時間内にTLEとならない方法で実装することができなかった。。

- A: 公比2の等比数列の和が、入力Hを超える日数を計算する問題。
- B: 各ユーザーを辞書順でソートし、出力したい番号のユーザを特定する問題。
- C: コンテスト中 -> {A,C}をタプルで持つvectorを用意して、捨てるカードのリストを記録していく方針で実装を進めたところTLE..他の方法をコンテスト中に思いつくことができなかった。

## [A Exponential Plant](https://atcoder.jp/contests/abc354/tasks/abc354_a)

whileを使ってn日後の植物の高さを記録していき、植物の高さがHを超えたらloopを抜ける。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int H;
  cin >> H;
  int tall = 0, i = 0;
  while (tall <= H)
  {
    tall += pow(2, i);
    i++;
  }
  cout << i << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc354/submissions/53590799)

## [B AtCoder Janken 2](https://atcoder.jp/contests/abc354/tasks/abc354_b)

各ユーザの情報をpair{ユーザ名Si,レートCi}としてvectorに記録し、ユーザ名の辞書順ソートをstd標準機能で実行できるようにする。あとは、入力しながら記録しておいたレートの総和を用いて出力したいユーザのインデックスを求めて出力する。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

int main()
{
  int N;
  cin >> N;
  vector<pair<string, int>> a(N);
  int rateTotal = 0, winUserNo = 0;
  for (int i = 0; i < N; i++)
  {
    string s;
    int c;
    cin >> s >> c;
    a[i] = {s, c};
    rateTotal += c;
  }
  sort(a.begin(), a.end());
  winUserNo = rateTotal % N;

  cout << a.at(winUserNo).first << endl;
  return 0;
}
```

[提出結果](https://atcoder.jp/contests/abc354/submissions/53598854)

## [C AtCoder Magics](https://atcoder.jp/contests/abc354/tasks/abc354_c)

コンテスト中にドツボのハマってしまった問題。当初は以下の方針で実装を行った。

- {カードの強さA,コストC}でvectorにそれぞれのカードの情報を記録
- 二重ループでそれぞれの要素を探索し、捨てるカードのインデックスを専用の配列に保存
- 全てのカードのインデックスリストと捨てるカードのインデックスリストを突合し、最終的に出力したいカードのリストを作成する

[TLEとなった提出結果](https://atcoder.jp/contests/abc354/submissions/53620491)
上記方針で実装を行ったところ、全20ケース中2ケースでTLEとなる結果に。。この時点でコンテスト時間内に他の方法を実装することを諦めた。

コンテスト後解説を読み、自分なりに理解した内容と実装方針を説明する。

- この問題では、「コストが最小のカード」か「強さが最大のカード」は絶対に捨てられることはない。
- そのため、コストが低い順に確認していき、それまでに出現したカードの強さの最大値より低いカードがあれば捨てる対象のカードになる。
- 逆に、カードの強さがそれまでに出てきたカードより大きいものであれば、捨てる条件を満たすことはない。
- 上記の条件に基づいてカードのコスト昇順ソート＋カードの強さ最大の記録を行なっていくことで実装することができる。

解説をよく読むと理解することはできたが、コンテスト時間内にここまでの整理ができなかった。

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, x) for (int i = 0; i < (x); i++)

struct Card
{
  int a;
  int c;
  int idx;
};

int main()
{
  int N;
  cin >> N;
  vector<Card> cardList(N);
  vector<int> ans;

  for (int i = 0; i < N; i++)
  {
    int a, c;
    cin >> a >> c;
    cardList[i] = {a, c, i};
  }

  // cardListをcの昇順でソート
  sort(cardList.begin(), cardList.end(), [](const Card &card1, const Card &card2)
       { return card1.c < card2.c; });

  // ansのリストに追加していく
  int maxA = 0;
  for (int i = 0; i < N; i++)
  {
    if (cardList[i].a > maxA)
    {
      maxA = cardList[i].a;
      ans.push_back(cardList[i].idx);
    }
  }

  // 答えを出力
  sort(ans.begin(), ans.end());
  cout << ans.size() << endl;
  for (int i = 0; i < ans.size(); i++)
  {
    if (i != 0)
    {
      cout << " ";
    }
    cout << ans[i] + 1;
  }
  cout << endl;

  return 0;
}

```

[提出結果](https://atcoder.jp/contests/abc354/submissions/53660786)
