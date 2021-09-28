{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "face_detector",
      "provenance": [],
      "authorship_tag": "ABX9TyM3ciVABSa9zhO7/Z1xQ8ms"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "t6vIC3dWlo-H"
      },
      "source": [
        "import cv2\n",
        "import numpy as np\n",
        "from imutils import face_utils\n",
        "import dlib"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "itw74iA7lvV9"
      },
      "source": [
        "def detect_dlib(our_image):\n",
        "  img = np.array(our_image.convert(\"RGB\"))\n",
        "  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
        "  face_detector = dlib.get_frontal_face_detector()\n",
        "  rects = face_detector(gray,2)\n",
        "  for (i,rect) in enumerate(rects):\n",
        "      (x,y,w,h) = face_utils.rect_to_bb(rect)\n",
        "      img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)\n",
        "      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)\n",
        "  return img"
      ],
      "execution_count": 2,
      "outputs": []
    }
  ]
}