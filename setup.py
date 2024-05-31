from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Model_Trainer is a Python package designed to simplify the process of training YOLO (You Only Look Once) models for object detection tasks. With Model_Trainer, users can easily train YOLO models using custom datasets and split their data into training, validation, and testing sets. The package provides classes for both model training and data splitting, allowing users to efficiently manage their training pipeline. Additionally, Model_Trainer includes functionality for saving the best-performing model weights, making it easy to deploy trained models for inference tasks.'
LONG_DESCRIPTION = 'Model_Trainer is a comprehensive Python package developed to streamline the training process of YOLO (You Only Look Once) models for object detection applications. Leveraging the ultralytics library, Model_Trainer offers a user-friendly interface for training YOLO models with custom datasets. The package includes a YOLO_Trainer class, allowing users to specify the YOLO model version and configuration for training. Model_Trainer automates the process of data splitting, enabling users to divide their dataset into training, validation, and testing sets with customizable ratios. The Data_Splitter class facilitates this functionality, ensuring proper organization of data for effective model training. Moreover, Model_Trainer handles the saving of best-performing model weights, enabling users to easily deploy trained models for inference tasks. With its intuitive design and robust functionality, Model_Trainer empowers users to efficiently train YOLO models and accelerate their object detection projects.'

# Setting up
setup(
    name="Model-Trainer",
    version=VERSION,
    author="Atri Rathore",
    author_email="<rathoreatri@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Rathoreatri03/Model_Trainer",
    packages=find_packages(),
    install_requires=['torch', 'ultralytics'],
    keywords=['python', 'model training', 'YOLO', 'data splitting', 'deep learning'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ]
)