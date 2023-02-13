import tensorflow as tf
import pickle

filename = 1
lastImage = 220
x_train = []
y_train = []
path = "data_full/{}"
cont = 0
index = 0

while filename <= lastImage:
    if cont == 10:
        cont = 0
        index+=1
    y_train.append(index)
    cont+=1
    filename+=1

print(y_train)

filename = 1

while filename <= lastImage:
    with open(path.format(filename), "rb") as fp:  # Unpickling

        filename += 1

        b = pickle.load(fp)
        #print(len(b))
        #print(b)

        x_train.append(b)

print(len(x_train))
print(len(y_train))

model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(22, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=17)
model.save('saved_model_full_5')

# saved_model_full_2 ficou com 90% acc
# saved_model_full_3 ficou com 95% acc
# saved_model_full_4 ficou com 90% acc
# saved_model_full_5 ficou com 93% acc