# Assessing the Performance of Vision Transformers in Generalizing to OOD Category-Viewpoint Combinations

Recent work has shown that convolutional neural networks (CNNs) fail to generalize to out-of-distribution (OOD) category-viewpoint combinations. For example, a vehicle model classification CNN trained only on the front view of vehicles may not extrapolate well to vehicles viewed from the side. We propose a comparative study of CNN and ViT architectures to classify object categories on OOD samples. The contents of this repo implement both shared and separate non-pretrained CNN, pretrained resnet18, and ViT models on the Biased-Cars dataset.

# Code Descriptions
  **ViT_biased_cars.ipynb** - Loads trains and test the Vit on Biased cars
  **Pretrained_ResNet18_Biased_casrs.ipynb** - modified demo code to implement a pretrained resnet18
  **?.ipynb** - fine-tunes a ViT using the huggingface library for the Biased-Cars dataset
  **ViT_skyler_biased-cars-rotation.ipynb** - fine-tunes a separate ViT using the huggingface library built-in functions to classify rotation
  **ViT_skyler_biased-cars-shared.ipynb** - fine-tunes a shared ViT using the huggingface library built-in functions
  **ViT_skyler_biased-cars-vehicle.ipynb** - fine-tunes a separate ViT using the huggingface library built-in functions to classify vehicle model
