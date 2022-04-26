# Assessing the Performance of Vision Transformers in Generalizing to OOD Category-Viewpoint Combinations

Recent work has shown that convolutional neural networks (CNNs) fail to generalize to out-of-distribution (OOD) category-viewpoint combinations. For example, a vehicle model classification CNN trained only on the front view of vehicles may not extrapolate well to vehicles viewed from the side. We propose a comparative study of CNN and ViT architectures to classify object categories on OOD samples. The contents of this repo implement both shared and separate non-pretrained CNN, pretrained resnet18, and ViT models on the Biased-Cars dataset.

# Code Descriptions
  **Pretrained_ResNet18_Biased_casrs.ipynb** - modified demo code to implement a pretrained resnet18  
  **ViT_MINIST.ipynb** - Loads trains and test the ViT on MNIST Rotation Dataset  
  **ViT_biased_cars.ipynb** - Loads trains and test the ViT on Biased-Cars Dataset  
  **ViT_huggingface_biased-cars-rotation.ipynb** - fine-tunes a separate ViT using the huggingface library built-in functions to classify rotation  
  **ViT_huggingface_biased-cars-shared.ipynb** - fine-tunes a shared ViT using the huggingface library built-in functions  
  **ViT_huggingface_biased-cars-vehicle.ipynb** - fine-tunes a separate ViT using the huggingface library built-in functions to classify vehicle model  
  **using_biased_cars** - demo code how to load, train and test with the Biased-Cars Dataset
