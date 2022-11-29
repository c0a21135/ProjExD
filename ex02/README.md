# 第2回
## 計算機（ex02/calc.py）
### 追加した機能
* 各演算子の実装
* クリア機能の実装
* 演算子の連続入力を防止
* 2進数と10進数の変換
* 2進数の際は適切なボタンのみが正常に入力される(演算子は+のみ)
### プログラム内䛾解説
* ch_ope：演算子の連続入力を判定するフラッグ
* mode：10進数か2進数かを判別
* 10進数から2進数への変換はbin()関数を使用。先頭二文字は0bが付くので、3文字目以降を表示するようにスライス
* 2進数から10進数への変換はint()関数を使用。第2引数の指定で10進数に変換している。