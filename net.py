import pandas as pd
import random
from sklearn.cluster import MiniBatchKMeans
import numpy as np
from scipy.spatial.distance import cdist



#carreguem datasets
df = pd.read_csv('dataset.csv')
df_concatenado = pd.read_csv('numerica.csv')
new_df= pd.read_csv('df_train.csv')
new_df=new_df.drop(columns=['Unnamed: 0'])
df = df.drop(columns=['Unnamed: 0'])
df_concatenado = df_concatenado.drop(columns=['Unnamed: 0'])

kmeans = MiniBatchKMeans(n_clusters=8, batch_size=100, random_state=42)
# Entrenar el modelo original con el dataset completo
kmeans.fit(new_df)
new_df['clusters']=kmeans.labels_


def recomenada(imatge,df,df_concatenado,likes,kmeans):
    if likes == []:
        # Seleccionar el punto de interés
        punto_interes = list(df_concatenado.loc[imatge])      
        # Ajuste del modelo con el nuevo dato
        kmeans.partial_fit([punto_interes])

        # Predicción del nuevo dato actualizado
        cluster = kmeans.predict([punto_interes])[0]
        
        # Seleccionar los puntos del mismo cluster que el punto de interés
        puntos_cluster=df_concatenado.loc[df[df['clusters'] == cluster].index]
        distancias = cdist([punto_interes], puntos_cluster)

        # Obtener los índices de los dos puntos más cercanos
        indices_cercanos = np.argsort(distancias, axis=1)# si volem afegir a la primera [:,i][0],on i va augmentant 1 per cada like

        # Seleccionar los puntos más cercanos
        puntos_cercanos = puntos_cluster.iloc[indices_cercanos[0]]
        df.loc[list(puntos_cercanos.index)]
        return list(puntos_cercanos.index)[1] #ho haurem d'aplicar com la línia anterior
    
    else:
        last=likes[-1]
        punto_interes=df_concatenado.iloc[last]
        kmeans.partial_fit([list(df_concatenado.loc[imatge])])
        cluster = kmeans.predict([list(df_concatenado.loc[imatge])])[0]
        puntos_cluster=df_concatenado.loc[df[df['clusters'] == cluster].index]
        distancias = cdist([punto_interes], puntos_cluster)
        indices_cercanos = np.argsort(distancias, axis=1)# si volem afegir a la primera [:,i][0],on i va augmentant 1 per cada like
        puntos_cercanos = puntos_cluster.iloc[indices_cercanos[0]]
        df.loc[list(puntos_cercanos.index)]
        return list(puntos_cercanos.index)[1] #ho haurem d'aplicar com la línia anterior
    
def tinder(imatge,likes,accio,df,df_concatenado):
   if accio == 'Like':#??
      seguent=recomenada(imatge,df,df_concatenado,likes)#passar seguent al html
      likes.append(imatge)
      df.drop(imatge,axis=0)
   else:
      seguent=recomenada(random.randint(0,len(df)-len(likes)),df,df_concatenado,likes)
      df.drop(imatge,axis=0)     
   return seguent,df,likes#tinder(seguent,likes,clic(seguent),df,df_concatenado)

def clic(imatge):
   return 

cases=True
imatge=..#li passem de la web
passem(df.iloc[imatge]['images'])
likes=[]
while cases:
    imatge,df,likes=tinder(imatge,likes,clic(imatge),df,df_concatenado)
    passem(df.iloc[imatge]['images']) #la seguent
    if len(df)==0:
        cases=False