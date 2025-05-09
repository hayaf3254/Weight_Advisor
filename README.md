# Weight_Advisor

設計・概要

1.プロジェクト概要 ・タイトル：ウェイトアドバイザー

・目的：筋トレを始めたばかりの頃、いつ重量を上げれば良いのか分からず、同じ重量でトレーニングを続けていました。その結果、思ったほど筋肉がつかず、モチベーションが低下してしまいました。そこで、同じような悩みを抱える人々の役に立つアプリを作成しました。このアプリは、重量をいつ増やすべきかをアドバイスすることで、ユーザのモチベーションを高め、より効率的に筋力アップをサポートします。

・対象ユーザ：周1～3日ペースでジムに通う、筋トレ初心者

2.機能一覧 ・入力フォームで種目名、重量、セット数、回数、それらを何日行ったかを入力する ・入力の値にもとづきメッセージを表示する ・メッセージの内容に応じて、メッセージの背景色を変更する ・メッセージを出力する前限定でフォームをリセットできる

3.使用技術 ・フロントエンド：html、css ・バックエンド:Flask(Python) ・開発環境:VSCode 
・アプリ構成
weihgth
├──/app 
    ├── /templates 
          └── index.html # メインのHTMLテンプレート 
    ├── /static  
          └── styles.css # CSSファイル 
      ├── form.py # ロジックのファイル 
└── run.py # 実行用スクリプト

4.操作方法
・入力項目の説明 種目名：トレーニングの種目を入力 重量：その種目の重さを入力 セット数：その種目を何セット行っているか入力 回数：1セット当たり何回行っているか入力 何日行ったか：それらを何日行ったか入力

・出力メッセージの内容 セット数を増やそう！ 回数を増やそう！ 現状維持 重量を上げても良いかもしれない 今すぐ重量を上げよう！ 重量を上げよう!

5.設計詳細 サーバ側 セット数1で回数が15未満の場合　「セット数を増やそう！」　numに２を代入 セット数、出力値　継続日数関係なく　回数が3未満の場合　「回数を増やそう！」　numに２を代入 継続日数が３日未満の「場合現状維持」　numに２を代入 継続日数が３日以上５日未満　かつ　出力値が60の場合　「重量を上げてもよいかもしれない」　numに4を代入 継続日数が8日以上　かつ　出力値が　210以上の場合　「今すぐ重量を上げよう」 numに3を代入　 それ以外は「重量を上げよう！」　
フロント側 numが１の時は赤　２の時は黄色　３の時は水色　４の時は緑

6.開発スケジュール 
・開発期間：約7～10時間 
・アイデア・仕様検討:約１時間 
・機能や目的はwordに書き出し、レイアウト設計はパワポを使用 
・実装・コーディング：5～8時間 
テスト:約1時間 ④ 説明
・仕様書制作:１～2時間

7.今後の展望
- geminiAPIを追加して、メッセージをAIにまかせる仕組みをする
- flutterでも書いて、モバイルアプリ化を目指す

8.追加機能
・SQLで履歴の実装
・最新５件の履歴表示
・データベースのデータ制限
・履歴の反映
