import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from matplotlib import pyplot as plt

# Učitaj podatke
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Skaliraj podatke
X_train_n = X_train.astype('float32') / 255.0
X_test_n = X_test.astype('float32') / 255.0

# One-hot encoding
y_train = to_categorical(y_train, dtype="uint8")
y_test = to_categorical(y_test, dtype="uint8")

# ========================================
# 9.4.1 - Osnovna CNN mreža
# ========================================
model = keras.Sequential()
model.add(layers.Input(shape=(32,32,3)))
model.add(layers.Conv2D(32, (3,3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128, (3,3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Flatten())
model.add(layers.Dense(500, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()  # Ovdje vidiš broj parametara

# TensorBoard
callbacks = [keras.callbacks.TensorBoard(log_dir='logs/cnn', update_freq=100)]

# Treniranje
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train_n, y_train, epochs=40, batch_size=64, callbacks=callbacks, validation_split=0.1)

# Testiranje
score = model.evaluate(X_test_n, y_test, verbose=0)
print(f'Tocnost na testnom skupu: {100.0*score[1]:.2f}%')

# ========================================
# 9.4.2 - Isti model ali sa Dropout slojevima
# ========================================
model2 = keras.Sequential()
model2.add(layers.Input(shape=(32,32,3)))
model2.add(layers.Conv2D(32, (3,3), activation='relu', padding='same'))
model2.add(layers.MaxPooling2D((2,2)))
model2.add(layers.Dropout(0.25))               # DODANO
model2.add(layers.Conv2D(64, (3,3), activation='relu', padding='same'))
model2.add(layers.MaxPooling2D((2,2)))
model2.add(layers.Dropout(0.25))               # DODANO
model2.add(layers.Conv2D(128, (3,3), activation='relu', padding='same'))
model2.add(layers.MaxPooling2D((2,2)))
model2.add(layers.Dropout(0.25))               # DODANO
model2.add(layers.Flatten())
model2.add(layers.Dense(500, activation='relu'))
model2.add(layers.Dropout(0.5))                # DODANO
model2.add(layers.Dense(10, activation='softmax'))

# Novi direktorij za TensorBoard
callbacks2 = [keras.callbacks.TensorBoard(log_dir='logs/cnn_dropout', update_freq=100)]

model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model2.fit(X_train_n, y_train, epochs=40, batch_size=64, callbacks=callbacks2, validation_split=0.1)

score2 = model2.evaluate(X_test_n, y_test, verbose=0)
print(f'Tocnost na testnom skupu (Dropout): {100.0*score2[1]:.2f}%')

# ========================================
# 9.4.3 - Dodaj Early Stopping
# ========================================
callbacks3 = [
    keras.callbacks.TensorBoard(log_dir='logs/cnn_early_stop', update_freq=100),
    keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
]

model3 = keras.Sequential()
model3.add(layers.Input(shape=(32,32,3)))
model3.add(layers.Conv2D(32, (3,3), activation='relu', padding='same'))
model3.add(layers.MaxPooling2D((2,2)))
model3.add(layers.Dropout(0.25))
model3.add(layers.Conv2D(64, (3,3), activation='relu', padding='same'))
model3.add(layers.MaxPooling2D((2,2)))
model3.add(layers.Dropout(0.25))
model3.add(layers.Conv2D(128, (3,3), activation='relu', padding='same'))
model3.add(layers.MaxPooling2D((2,2)))
model3.add(layers.Dropout(0.25))
model3.add(layers.Flatten())
model3.add(layers.Dense(500, activation='relu'))
model3.add(layers.Dropout(0.5))
model3.add(layers.Dense(10, activation='softmax'))

model3.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model3.fit(X_train_n, y_train, epochs=100, batch_size=64, callbacks=callbacks3, validation_split=0.1)

score3 = model3.evaluate(X_test_n, y_test, verbose=0)
print(f'Tocnost na testnom skupu (Early Stopping): {100.0*score3[1]:.2f}%')

# ========================================
# 9.4.4 - Samo ispis odgovora (nema kodiranja)
# ========================================
print("\n" + "="*50)
print("ODGOVORI ZA 9.4.4:")
print("="*50)
print("1. Batch size:")
print("   - Premali: sporo ucenje, sumoviti gradijenti")
print("   - Preveliki: losija generalizacija")
print("\n2. Learning rate:")
print("   - Premali: spora konvergencija")
print("   - Preveliki: divergencija (loss raste)")
print("\n3. Manja mreza:")
print("   - Brze ucenje ali manja tocnost (underfitting)")
print("\n4. 50% manje podataka:")
print("   - Veci overfitting, losija testna tocnost")
