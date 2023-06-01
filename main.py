import streamlit as st
# import numpy as np
# import pandas as pd

###streamlitの基本的な使い方

##タイトル・テキストの追加
#タイトルの追加
st.title("Streamlit 超入門")
# #テキストを追加する
# st.write("DataFrame")

# ##表の使い方
# #データフレームを作成
# df=pd.DataFrame({
#   "1列目":[1,2,3,4],
#   "2列目":[10,20,30,40]
# })
# #表の表示1
# #st.write
# st.write(df)
# #表の表示2
# #st.dataframe
# #引数を指定することができる
# st.dataframe(df)
# st.dataframe(df,width =100,height=100)
# st.dataframe(df.style.highlight_max(axis=0))
# #表の表示3
# #st.table
# #静的な表を作成できる
# st.table(df)

# ##文字列の書き方
# #マジックコマンド
# #コードの表示はバックコーテーション
# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# # バックコーテーション：Shift+@
# ```
# """

# ##グラフを描く
# #データフレームを作成
# df=pd.DataFrame(
#   np.random.rand(20,3),
#   columns=["a","b","c"]
# )
# #折れ線グラフ
# st.line_chart(df)
# #エリアグラフ
# st.area_chart(df)
# #棒グラフ
# st.bar_chart(df)

# ##マップのプロット
# #データフレームの作成
# #今回は新宿付近の座標を用意
# df=pd.DataFrame(
#   np.random.rand(100,2)/[50,50]+[35.69,139.70],
#   columns=["lat","lon"]
# )
# #マッピング
# st.map(df)

# ##画像の表示 
# from PIL import Image
# st.write("Display Image")
# #画像の読み込み
# img=Image.open("079.png")
# #画像の表示
# st.image(img,caption="イナズマイレブン",use_column_width=True)















# ###インタラクティブなウィジェット

# ##チェックボックスによる画像の表示の可否
# from PIL import Image
# st.write("Interactive Widgets")
# #チェックボックス
# #チェックボックスにチェックが入ればTrue、入らなければFalse
# if st.checkbox("Show Image"):
#   img=Image.open("079.png")
#   st.image(img,caption="イナズマイレブン",use_column_width=True)

# ##セレクトボックス
# option=st.selectbox(
#     "あなたが好きな数字を教えてください、",
#     list(range(1,11))
# )
# "あなたの好きな数字は、",option,"です。"

# ##テキスト入力
# text=st.text_input("あなたの趣味を教えてください。")
# "あなたの好きな趣味は、",text,"です。"

# ##スライダーによる動的変化
# condition=st.slider("あなたの今の調子は？",0,100,50)
# "コンディション：",condition















# # ###レイアウトを整える

# # ##サイドバーの追加
# # #テキスト入力
# # text1=st.sidebar.text_input("あなたの趣味を教えてください。")
# # "あなたの好きな趣味は、",text1,"です。"
# # #スライダーによる動的変化
# # condition=st.sidebar.slider("あなたの今の調子は？",0,100,50)
# # "コンディション：",condition

# ##ツーカラムレイアウト
# #カラム
# left_column,right_column=st.columns(2)
# button=left_column.button("右カラムに文字を表示")
# if button:
#   right_column.write("ここは右カラム")

# ##エクスパンダ
# expander=st.expander("問い合わせ")
# expander.write("問い合わせ内容を書く")















###プログレスバーの表示
import time
st.write("プログレスバーの表示")
"Start!!"
#空の状態をセット
latest_iteration=st.empty()
#バーを0にセット
bar=st.progress(0)
#プログレスバーの表示
for i in range(100):
  latest_iteration.text(f"Iteration{i+1}")
  bar.progress(i+1)
  time.sleep(0.1)
"Done"















###Webアプリの公開
