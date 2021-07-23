import streamlit as st
from PIL import Image
import time
import numpy as np
import pandas as pd

st.title('Streamlit超入門')


# プログラム進捗状況を表示
st.write('プログレスバーの表示')
'Start!!'
# 空を用意する
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i + 1)
  time.sleep(0.5)



st.write('DataFrame')

df = pd.DataFrame({
  '１列目':[1,2,3,4],
  '２列目':[10,20,30,40]
})

# st.write(df)

# st.dataframe(df.style.highlight_max(axis=0))

st.table(df)


"""
```python
import streamlit as st
import pandas as pd
import numpy as np
```

"""


df2 = pd.DataFrame(
  np.random.rand(20, 3),
  columns=['a', 'b', 'c']
)


st.line_chart(df2)
st.altair_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon']
)

st.map(df3)

image = Image.open('smple.png')
st.image(image, caption='スクリーンショット', use_column_width=True)

# インタラクティブなウィジェット

# カラムの数を調整する。以下は２カラムに設定して表示場所を指定している。
left_column, regth_coloumn = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  regth_coloumn.write('ここは右カラム')

# クリックするとメニューを表示
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせを書く')


# チェックボックス
if st.checkbox('Show Image'):
  image = Image.open('smple.png')
  st.image(image, caption='スクリーンショット', use_column_width=True)

# セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,10))
  )

'あなたの好きな数字は',option,'です。'

# TextBox
option2 = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味は',option2,'です。'

# スライダー
option3 = st.slider('あなたの今の調子は', 0, 100, 50)

'コンディション',option3

st.button(label="登録", on_click=None)

