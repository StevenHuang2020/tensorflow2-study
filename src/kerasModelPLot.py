#python3 tensorflow 2.0  09/04/2020
#plot Model
import tensorflow as tf
import tensorflow.keras as ks
from tensorflow.keras import optimizers
from tensorflow.keras import Model
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input,Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import plot_model

#1.pip install pydot
#2.install graphviz
#Url: https://www2.graphviz.org/Packages/stable/windows/10/msbuild/Release/Win32/graphviz-2.44.1-win32.zip
#3. add to your system path


def plotModel(model,dstFile,show_shapes=True):
    plot_model(model, to_file=dstFile, show_shapes=show_shapes)

def createModel():
    input = ks.Input(shape=(100,), dtype='int32', name='input')
    x = ks.layers.Embedding(
        output_dim=512, input_dim=10000, input_length=100)(input)
    x = ks.layers.LSTM(32)(x)
    x = ks.layers.Dense(64, activation='relu')(x)
    x = ks.layers.Dense(64, activation='relu')(x)
    x = ks.layers.Dense(64, activation='relu')(x)
    output = ks.layers.Dense(1, activation='sigmoid', name='output')(x)
    model = ks.Model(inputs=[input], outputs=[output])
    model.summary()
    return model

def main():
    model = createModel()

    file = r'.\res\model_1.png'
    plotModel(model,file)
    file = r'.\res\model_1s.png'
    plotModel(model,file,False)

if __name__=='__main__':
    main()
