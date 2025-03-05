import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, BatchNormalization
from tensorflow.keras.optimizers.legacy import Adam

EPOCHS = args.epochs or 200
LEARNING_RATE = args.learning_rate or 0.0005
ENSURE_DETERMINISM = args.ensure_determinism
BATCH_SIZE = args.batch_size or 32

if not ENSURE_DETERMINISM:
    train_dataset = train_dataset.shuffle(buffer_size=BATCH_SIZE * 4)
train_dataset = train_dataset.batch(BATCH_SIZE, drop_remainder=False)
validation_dataset = validation_dataset.batch(BATCH_SIZE, drop_remainder=False)

# LSTM model architecture
model = Sequential()
model.add(LSTM(64, return_sequences=True, input_shape=(time_steps, feature_dim)))
model.add(BatchNormalization())
model.add(Dropout(0.3))
model.add(LSTM(32, return_sequences=False))
model.add(Dropout(0.3))
model.add(Dense(20, activation='relu'))
model.add(Dense(classes, name='y_pred', activation='softmax'))

# Optimizer
opt = Adam(learning_rate=LEARNING_RATE, beta_1=0.9, beta_2=0.999)

# Callbacks
callbacks.append(BatchLoggerCallback(BATCH_SIZE, train_sample_count, epochs=EPOCHS, ensure_determinism=ENSURE_DETERMINISM))

# Compile and train
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.fit(train_dataset, epochs=EPOCHS, validation_data=validation_dataset, verbose=2, callbacks=callbacks, class_weight=ei_tensorflow.training.get_class_weights(Y_train))

# Per-channel quantization flag
disable_per_channel_quantization = False

# Let me know if you want to tweak the architecture further or try another approach! 🚀
