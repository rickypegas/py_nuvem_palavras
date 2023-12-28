import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# importar o arquivo
file = open(r"txt_unico/legendas.txt", "r", encoding='UTF-8')
df = pd.DataFrame(file)
#print(df)
df.columns = ['linhas']
df = df.sort_index()
file.close()

print(df.head())

# concatenar as frases
all_frases = " ".join(s for s in df['linhas'])
print("Quantidade de Palavras: {}".format(len(all_frases)))


# lista de stopword
stopwords = set(STOPWORDS)
stopwords.update(["a", "o", "e", "voce", "do", "da", "dos", "das", "meu", "em", "você", "de", "ao", "os", "ma", "é"])

# configurando a wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white",
                      width=1600, height=800).generate(all_frases)


fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()

# mostrar a imagem
plt.imshow(wordcloud);

# salvar a imagem no diretório
wordcloud.to_file("wordcloud.png")
