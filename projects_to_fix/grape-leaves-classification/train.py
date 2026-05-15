import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pickle
import os

def train():
    # Path to dataset (assumes user has extracted it as per notebook)
    data_dir = 'Grapevine_Leaves_Image_Dataset'
    if not os.path.exists(data_dir):
        print("Dataset directory not found. Please extract '03 Leaves.zip' into 'Grapevine_Leaves_Image_Dataset'.")
        return

    img_size = (224, 224)
    batch_size = 32

    # Data Augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        validation_split=0.2
    )

    train_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    # Base Model
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(5, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    # Freeze base layers
    for layer in base_model.layers:
        layer.trainable = False

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train (Few epochs for demonstration)
    model.fit(train_generator, epochs=5, validation_data=validation_generator)

    # Save Model
    model.save('grape_leaf_model.h5')
    
    # Save class indices
    class_indices = train_generator.class_indices
    labels = {v: k for k, v in class_indices.items()}
    with open('labels.pkl', 'wb') as f:
        pickle.dump(labels, f)

    print("Model and labels saved!")

if __name__ == "__main__":
    train()
