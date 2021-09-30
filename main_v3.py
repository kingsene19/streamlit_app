{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "main_v1_.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6_xbATYNUs-v",
        "outputId": "834fb98d-d609-4001-a428-fd5b7b139605"
      },
      "source": [
        "!pip install caer --quiet\n",
        "!pip install keras-tuner --quiet\n",
        "!pip -q install streamlit\n",
        "!pip -q install pyngrok\n",
        "!pip install ipykernel>=5.1.2\n",
        "!pip install pydeck\n",
        "!pip install streamlit"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pydeck in /usr/local/lib/python3.7/dist-packages (0.7.0)\n",
            "Requirement already satisfied: jinja2>=2.10.1 in /usr/local/lib/python3.7/dist-packages (from pydeck) (2.11.3)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck) (5.1.0)\n",
            "Requirement already satisfied: ipykernel>=5.1.2 in /usr/local/lib/python3.7/dist-packages (from pydeck) (6.4.1)\n",
            "Requirement already satisfied: numpy>=1.16.4 in /usr/local/lib/python3.7/dist-packages (from pydeck) (1.19.5)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck) (7.6.5)\n",
            "Requirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (5.3.5)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (0.2.0)\n",
            "Requirement already satisfied: tornado<7.0,>=4.2 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (5.1.1)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (0.1.3)\n",
            "Requirement already satisfied: argcomplete>=1.12.3 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (1.12.3)\n",
            "Requirement already satisfied: ipython<8.0,>=7.23.1 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (7.28.0)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (1.0.0)\n",
            "Requirement already satisfied: importlib-metadata<5 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (4.8.1)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck) (3.5.0)\n",
            "Requirement already satisfied: typing-extensions>=3.6.4 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck) (3.7.4.3)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (2.6.1)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (3.0.20)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (4.4.2)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (57.4.0)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.2.0)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (4.8.0)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.18.0)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.7.5)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (1.0.2)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (5.1.3)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (3.5.1)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.7/dist-packages (from jedi>=0.16->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.8.2)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2>=2.10.1->pydeck) (2.0.1)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (2.8.2)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (22.3.0)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (4.8.1)\n",
            "Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /usr/local/lib/python3.7/dist-packages (from nbformat>=4.2.0->ipywidgets>=7.0.0->pydeck) (2.6.0)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect>4.3->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.2.5)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.1->jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (1.15.0)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (5.3.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (1.8.0)\n",
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.12.1)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (5.6.1)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.8.4)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (4.1.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.7.1)\n",
            "Requirement already satisfied: entrypoints>=0.2.2 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.3)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.5.0)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (1.5.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (21.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.5.1)\n",
            "Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (2.4.7)\n",
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.7/dist-packages (0.89.0)\n",
            "Requirement already satisfied: attrs in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.2.0)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: tzlocal in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.5.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.0)\n",
            "Requirement already satisfied: watchdog in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.1.5)\n",
            "Requirement already satisfied: astor in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.8.1)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.17.3)\n",
            "Requirement already satisfied: pyarrow in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.0.0)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: click<8.0,>=7.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (5.1.1)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.1.5)\n",
            "Requirement already satisfied: blinker in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.19.5)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.23.0)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.1.0)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: validators in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.18.2)\n",
            "Requirement already satisfied: base58 in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.1.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.1.24)\n",
            "Requirement already satisfied: pydeck>=0.1.dev5 in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.7.0)\n",
            "Requirement already satisfied: jsonschema in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.6.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.11.1)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit) (3.7.4.3)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit) (4.0.7)\n",
            "Requirement already satisfied: smmap<5,>=3.0.1 in /usr/local/lib/python3.7/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (4.0.0)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.21.0->streamlit) (2018.9)\n",
            "Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.7/dist-packages (from protobuf!=3.11,>=3.6.0->streamlit) (1.15.0)\n",
            "Requirement already satisfied: ipykernel>=5.1.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (6.4.1)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (7.6.5)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (5.1.0)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.3)\n",
            "Requirement already satisfied: argcomplete>=1.12.3 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.12.3)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: importlib-metadata<5 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.1)\n",
            "Requirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (5.3.5)\n",
            "Requirement already satisfied: ipython<8.0,>=7.23.1 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (7.28.0)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.0.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.5.0)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.4.2)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.18.0)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (57.4.0)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.0)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.0.20)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.6.1)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.1.3)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.0.2)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.7/dist-packages (from jedi>=0.16->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.8.2)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.1)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (22.3.0)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect>4.3->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.5)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.3.1)\n",
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.12.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.8.0)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.6.1)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.1.0)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.0)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.1)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
            "Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->streamlit) (2.4.7)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (2.10)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (3.0.4)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (1.24.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (2021.5.30)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oBKHzan5lWUd"
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "from PIL import Image\n",
        "import os\n",
        "import cv2\n",
        "import caer\n",
        "from  matplotlib import pyplot as plt\n",
        "import keras_tuner\n",
        "from keras_tuner import *\n",
        "from sklearn.metrics import confusion_matrix,classification_report\n",
        "from keras_tuner.applications import HyperResNet,HyperXception\n",
        "from sklearn.utils import shuffle\n",
        "import streamlit as st\n",
        "import dlib\n",
        "from imutils import face_utils\n",
        "from keras_tuner import HyperParameters\n",
        "import tensorflow as tf\n",
        "from tensorflow import keras\n",
        "from tensorflow.keras import layers,models\n",
        "from tensorflow.keras.models import Sequential, Model\n",
        "from tensorflow.keras.preprocessing.image import ImageDataGenerator \n",
        "from tensorflow.keras.utils import to_categorical\n",
        "from tensorflow.keras.preprocessing.image import ImageDataGenerator \n",
        "from tensorflow.keras.callbacks import ModelCheckpoint"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BciVMSajdKTD",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7bf9d709-f821-4b9b-925c-d0e976d239b3"
      },
      "source": [
        "%tensorflow_version 2.x\n",
        "import tensorflow as tf\n",
        "from tensorflow import keras\n",
        "from tensorflow.keras import layers,models\n",
        "from tensorflow.keras.models import Sequential, Model\n",
        "from tensorflow.keras.preprocessing.image import ImageDataGenerator \n",
        "from tensorflow.keras.utils import to_categorical\n",
        "from tensorflow.keras.preprocessing.image import ImageDataGenerator \n",
        "from tensorflow.keras.callbacks import ModelCheckpoint\n",
        "import timeit\n",
        "\n",
        "device_name = tf.test.gpu_device_name()\n",
        "if device_name != '/device:GPU:0':\n",
        "  raise SystemError('GPU device not found')\n",
        "print('Found GPU at: {}'.format(device_name))\n",
        "\n",
        "def cpu():\n",
        "  with tf.device('/cpu:0'):\n",
        "    random_image_cpu = tf.random.normal((100, 100, 100, 3))\n",
        "    net_cpu = tf.keras.layers.Conv2D(32, 7)(random_image_cpu)\n",
        "    return tf.math.reduce_sum(net_cpu)\n",
        "\n",
        "def gpu():\n",
        "  with tf.device('/device:GPU:0'):\n",
        "    random_image_gpu = tf.random.normal((100, 100, 100, 3))\n",
        "    net_gpu = tf.keras.layers.Conv2D(32, 7)(random_image_gpu)\n",
        "    return tf.math.reduce_sum(net_gpu)\n",
        "  \n",
        "# We run each op once to warm up; see: https://stackoverflow.com/a/45067900\n",
        "cpu()\n",
        "gpu()\n",
        "\n",
        "# Run the op several times.\n",
        "print('Time (s) to convolve 32x7x7x3 filter over random 100x100x100x3 images '\n",
        "      '(batch x height x width x channel). Sum of ten runs.')\n",
        "print('CPU (s):')\n",
        "cpu_time = timeit.timeit('cpu()', number=10, setup=\"from __main__ import cpu\")\n",
        "print(cpu_time)\n",
        "print('GPU (s):')\n",
        "gpu_time = timeit.timeit('gpu()', number=10, setup=\"from __main__ import gpu\")\n",
        "print(gpu_time)\n",
        "print('GPU speedup over CPU: {}x'.format(int(cpu_time/gpu_time)))"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found GPU at: /device:GPU:0\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2021-09-30 15:39:28.297770: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.327246: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.328005: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.847302: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.848157: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.848882: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.849528: W tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc:39] Overriding allow_growth setting because the TF_FORCE_GPU_ALLOW_GROWTH environment variable is set. Original config value was 0.\n",
            "2021-09-30 15:39:28.849576: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /device:GPU:0 with 10819 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7\n",
            "2021-09-30 15:39:28.852095: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.852865: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.853621: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.854718: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.855739: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.856453: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.857291: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.858046: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 15:39:28.858788: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 10819 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7\n",
            "2021-09-30 15:39:31.312847: I tensorflow/stream_executor/cuda/cuda_dnn.cc:369] Loaded cuDNN version 8005\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Time (s) to convolve 32x7x7x3 filter over random 100x100x100x3 images (batch x height x width x channel). Sum of ten runs.\n",
            "CPU (s):\n",
            "3.7615726589992846\n",
            "GPU (s):\n",
            "0.0637206330011395\n",
            "GPU speedup over CPU: 59x\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TDGdVeEplnGy"
      },
      "source": [
        "def detect_dlib(our_image):\n",
        "  img = np.array(our_image.convert(\"RGB\"))\n",
        "  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
        "  face_detector = dlib.get_frontal_face_detector()\n",
        "  rects = face_detector(gray,2)\n",
        "  for (i,rect) in enumerate(rects):\n",
        "    (x,y,w,h) = face_utils.rect_to_bb(rect)\n",
        "    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)\n",
        "    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)\n",
        "  return img"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fWAE083VVJBi",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f40c1ca7-6164-42cc-9a69-cc8125b84921"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive',force_remount=True)"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vgrvPanAnxuN"
      },
      "source": [
        "IMG_SIZE = (80,80)\n",
        "char_path = \"/content/drive/MyDrive/simpsons_characters_dataset/simpsons_dataset\"\n",
        "char_dict = {}\n",
        "for char in os.listdir(char_path):\n",
        "  char_dict[char] = len(os.listdir(os.path.join(char_path,char)))\n",
        "char_dict = caer.sort_dict(char_dict, descending=True)\n",
        "characters = []\n",
        "count = 0\n",
        "for item in char_dict:\n",
        "  characters.append(item[0])\n",
        "  count += 1\n",
        "  if count >= 10:\n",
        "      break"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aNOCde_kn3XB"
      },
      "source": [
        "def create_dataset(img_folder,characters):\n",
        "  img_data_array=[]\n",
        "  class_name=[]\n",
        "  for person in os.listdir(img_folder):\n",
        "    if person in characters:\n",
        "      for image in os.listdir(os.path.join(img_folder, person)):   \n",
        "        image_path= os.path.join(img_folder, person,  image)\n",
        "        image= cv2.imread( image_path, cv2.COLOR_BGR2RGB)\n",
        "        image=cv2.resize(image, IMG_SIZE,interpolation = cv2.INTER_AREA)\n",
        "        image=np.array(image)\n",
        "        image = image.astype('float32')\n",
        "        image /= 255 \n",
        "        img_data_array.append(image)\n",
        "        class_name.append(person)\n",
        "  return img_data_array, class_name\n",
        "img_data,class_name = create_dataset(\"/content/drive/MyDrive/simpsons_characters_dataset/simpsons_dataset\",characters=characters)"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lSaduAR4n8LV"
      },
      "source": [
        "target_dict = {k: v for v, k in enumerate(np.unique(class_name))}\n",
        "target_val=  [target_dict[class_name[i]] for i in range(len(class_name))]"
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8G6IVi6jn9ti"
      },
      "source": [
        "#On met en place une fonction chargée de créer le modèle\n",
        "def build_model(hp):\n",
        "    model = keras.Sequential()\n",
        "    model.add(layers.Conv2D(hp.Int(\"filters_1\",32,128,step=32,default=96), \n",
        "                            kernel_size=(3, 3), \n",
        "                            activation='relu', \n",
        "                            input_shape=(80, 80, 3))) \n",
        "    model.add(layers.MaxPooling2D((2, 2))) \n",
        "    model.add(layers.Conv2D(hp.Int(\"filters_2\",64,256,step=64,default=192), \n",
        "                            kernel_size = (3, 3), \n",
        "                            activation='relu'))\n",
        "    model.add(layers.MaxPooling2D((2, 2)))\n",
        "    model.add(layers.Conv2D(hp.Int(\"filters_3\",64,256,step=64,default=256), \n",
        "                            kernel_size = (3, 3), \n",
        "                            activation='relu'))\n",
        "    model.add(layers.Flatten())\n",
        "    model.add(layers.Dense(units=hp.Int(\"units\",64,128,step=32,default=128),\n",
        "                            activation='relu'))\n",
        "    model.add(layers.Dense(10,activation=\"softmax\"))\n",
        "    model.compile(\n",
        "    optimizer = \"rmsprop\",\n",
        "    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),\n",
        "    metrics = [\"accuracy\"],\n",
        "    )\n",
        "    return model\n",
        "\n",
        "tuner = RandomSearch(\n",
        "        build_model,\n",
        "        objective = \"val_accuracy\",\n",
        "        max_trials = 5,\n",
        "        executions_per_trial = 1,\n",
        "        overwrite = True,\n",
        "        directory = \"my_dir\",\n",
        "        project_name = \"hello_world\",\n",
        ")"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_F3VGvVT2suy",
        "outputId": "642bb2f4-f516-40f2-f352-625a7cee9844"
      },
      "source": [
        "tuner.search_space_summary()"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Search space summary\n",
            "Default search space size: 4\n",
            "filters_1 (Int)\n",
            "{'default': 96, 'conditions': [], 'min_value': 32, 'max_value': 128, 'step': 32, 'sampling': None}\n",
            "filters_2 (Int)\n",
            "{'default': 192, 'conditions': [], 'min_value': 64, 'max_value': 256, 'step': 64, 'sampling': None}\n",
            "filters_3 (Int)\n",
            "{'default': 256, 'conditions': [], 'min_value': 64, 'max_value': 256, 'step': 64, 'sampling': None}\n",
            "units (Int)\n",
            "{'default': 128, 'conditions': [], 'min_value': 64, 'max_value': 128, 'step': 32, 'sampling': None}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "r3RAcb8soCu3"
      },
      "source": [
        "x = np.array(img_data,dtype=\"float32\")\n",
        "y = np.array(list(map(int,target_val)),np.float32)\n",
        "train_data,train_labels = shuffle(x,y,random_state=0)\n",
        "x_train = train_data[:11049]\n",
        "y_train = train_labels[:11049]\n",
        "x_val =  train_data[11049:]\n",
        "y_val = train_labels[11049:]\n",
        "# y_train = to_categorical(y_train)\n",
        "# y_val = to_categorical(y_val)\n",
        "train_datagen = ImageDataGenerator(\n",
        "            rotation_range = 10,\n",
        "            width_shift_range = .1,\n",
        "            height_shift_range = .1,\n",
        "            shear_range = 0.3,\n",
        "            zoom_range = 0.3,\n",
        "            horizontal_flip = True,\n",
        "            fill_mode = 'nearest',\n",
        ")\n",
        "val_datagen = ImageDataGenerator()\n",
        "train_set = train_datagen.flow(x_train,y_train,batch_size=32)\n",
        "val_set = val_datagen.flow(x_val,y_val,batch_size=32)"
      ],
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bt9QXts-oIaZ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9fc283dd-fbaf-478c-8cbc-ac2fd5527bef"
      },
      "source": [
        "tuner.search(\n",
        "    train_set,\n",
        "    validation_data=val_set,\n",
        "    epochs=5,\n",
        "    callbacks=[keras.callbacks.TensorBoard(\"/tmp/logs_dir\")]\n",
        ")"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Trial 5 Complete [00h 02m 28s]\n",
            "val_accuracy: 0.8457639217376709\n",
            "\n",
            "Best val_accuracy So Far: 0.8772628307342529\n",
            "Total elapsed time: 00h 12m 43s\n",
            "INFO:tensorflow:Oracle triggered exit\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2021-09-30 15:54:34.749 INFO    tensorflow: Oracle triggered exit\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5rlWO6uXpNkf",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c992c288-eefd-4fa8-98fc-fdbd99d8a257"
      },
      "source": [
        "models = tuner.get_best_models(num_models=1)\n",
        "model = models[0]\n",
        "history = model.fit_generator(train_set,\n",
        "                              validation_data = val_set,\n",
        "                              verbose=2,\n",
        "                              epochs=5)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/keras/engine/training.py:1972: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.\n",
            "  warnings.warn('`Model.fit_generator` is deprecated and '\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/5\n",
            "346/346 - 25s - loss: 0.5186 - accuracy: 0.8420 - val_loss: 0.4407 - val_accuracy: 0.8794\n",
            "Epoch 2/5\n",
            "346/346 - 24s - loss: 0.4703 - accuracy: 0.8582 - val_loss: 0.3952 - val_accuracy: 0.8820\n",
            "Epoch 3/5\n",
            "346/346 - 24s - loss: 0.4313 - accuracy: 0.8701 - val_loss: 0.3873 - val_accuracy: 0.8845\n",
            "Epoch 4/5\n",
            "346/346 - 24s - loss: 0.4336 - accuracy: 0.8775 - val_loss: 0.3278 - val_accuracy: 0.8954\n",
            "Epoch 5/5\n",
            "346/346 - 24s - loss: 0.4097 - accuracy: 0.8757 - val_loss: 0.6111 - val_accuracy: 0.8707\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4HJMA5__O7yP"
      },
      "source": [
        "x_test,y_test = create_dataset(\"/content/drive/MyDrive/simpsons_characters_dataset/kaggle_simpson_testset/kaggle_simpson_testset\",\n",
        "                               characters=characters)\n",
        "target_dict = {k: v for v, k in enumerate(np.unique(y_test))}\n",
        "target_val = [target_dict[y_test[i]] for i in range(len(y_test))]\n",
        "x_test = np.array(x_test,np.float32)\n",
        "y_test = np.array(list(map(int,target_val)),np.float32)"
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qgKvcpZAMU2o",
        "outputId": "0e3cfd58-d31f-4467-cf31-778795f86208"
      },
      "source": [
        "np.unique(y_test)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.], dtype=float32)"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p0-QCWiqO777",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e425b4c4-3a98-43c5-f4ef-b85f528fedb2"
      },
      "source": [
        "test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)\n",
        "print(test_acc)"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "16/16 - 1s - loss: 0.3052 - accuracy: 0.9113\n",
            "0.9112903475761414\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V-U7zalvasH3"
      },
      "source": [
        "def print_confusion_matrix(confusion_matrix,class_names,figsize=(10,7),fontsize=14):\n",
        "    df_cm = pd.DataFrame(confusion_matrix,index=class_names,columns=class_names,)\n",
        "    fig = plt.figure(figsize=figsize)\n",
        "    try:\n",
        "        heatmap = sns.heatmap(df_cm,annot=True,fmt='d')\n",
        "    except ValueError:\n",
        "        raise ValueError(\"Confusion matrix must be integers.\")\n",
        "    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(),rotation=0,ha=\"right\",fontsize=fontsize)\n",
        "    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(),rotation=45,ha=\"right\",fontsize=fontsize)\n",
        "    plt.ylabel(\"Truth\")\n",
        "    plt.xlabel(\"Prediction\")"
      ],
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8_4iEn3vasS1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 584
        },
        "outputId": "4e5f039a-0c07-415c-e5e6-253d0f7fe246"
      },
      "source": [
        "predictions = model.predict(x_test)\n",
        "prediction_labels = np.argmax(predictions,1)\n",
        "cm = confusion_matrix(y_test,prediction_labels)\n",
        "print_confusion_matrix(cm,class_names=['bart_simpson','charles_montgomery_burns', 'homer_simpson','krusty_the_clown',\n",
        "                                     'lisa_simpson','marge_simpson','milhouse_van_houten','moe_szyslak','ned_flanders',\n",
        "                                       'principal_skinner'])"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x504 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Cr-WF6JfasZZ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "420dc748-efd4-44a2-ef8b-cff3f87817d2"
      },
      "source": [
        "print(classification_report(y_test,prediction_labels))"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "         0.0       0.88      0.92      0.90        50\n",
            "         1.0       0.68      1.00      0.81        48\n",
            "         2.0       0.94      0.94      0.94        50\n",
            "         3.0       0.96      1.00      0.98        50\n",
            "         4.0       1.00      0.78      0.88        50\n",
            "         5.0       0.98      1.00      0.99        50\n",
            "         6.0       1.00      0.88      0.93        49\n",
            "         7.0       0.82      0.82      0.82        50\n",
            "         8.0       1.00      0.98      0.99        49\n",
            "         9.0       1.00      0.80      0.89        50\n",
            "\n",
            "    accuracy                           0.91       496\n",
            "   macro avg       0.93      0.91      0.91       496\n",
            "weighted avg       0.93      0.91      0.91       496\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SMti_rv_oLk4"
      },
      "source": [
        "model.save(\"model.hdf5\")"
      ],
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pIPRLiftdMMA",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1512c0b6-1e1f-40fe-e7ec-1854cc04a022"
      },
      "source": [
        "%%writefile app.py\n",
        "import tensorflow as tf\n",
        "import streamlit as st\n",
        "import numpy as np\n",
        "from PIL import Image\n",
        "import os\n",
        "import cv2\n",
        "import caer\n",
        "from  matplotlib import pyplot as plt\n",
        "import dlib\n",
        "from imutils import face_utils\n",
        "@st.cache(allow_output_mutation=True)\n",
        "def load_model():\n",
        "  model = tf.keras.models.load_model('model.hdf5')\n",
        "  return model\n",
        "model=load_model()\n",
        "def detect_dlib(our_image):\n",
        "  img = np.array(our_image.convert(\"RGB\"))\n",
        "  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
        "  face_detector = dlib.get_frontal_face_detector()\n",
        "  rects = face_detector(gray,2)\n",
        "  for (i,rect) in enumerate(rects):\n",
        "    (x,y,w,h) = face_utils.rect_to_bb(rect)\n",
        "    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)\n",
        "    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)\n",
        "  return img\n",
        "face_detector = st.container()\n",
        "face_recognizer = st.container()\n",
        "with face_detector:\n",
        "  st.title(\"Face Detection And Recognition WebApp\")\n",
        "  st.text(\"This face detector was built using the dlib library\")\n",
        "  html_body = \"\"\"<body style=\"background-color:red;\"></body>\"\"\"\n",
        "  st.markdown(html_body,unsafe_allow_html=True)\n",
        "  html_temp = \"\"\"\n",
        "      <body style=\"background-color:red;\">\n",
        "      <div style=\"background-color:red;padding:10px;\">\n",
        "      <h2 style=\"color:white;text-align:center;\">Face Detection</h2>\n",
        "      </div>\n",
        "      </body>\n",
        "      \"\"\"\n",
        "  st.markdown(html_temp,unsafe_allow_html=True)\n",
        "  image_file = st.file_uploader(\"Upload Image\",type=['jpg','png','jpeg'],key=0)\n",
        "  if image_file is not None:\n",
        "    our_image = Image.open(image_file)\n",
        "    st.text(\"Original Image\")\n",
        "    st.image(our_image)\n",
        "  if st.button(\"Detect\"):\n",
        "    result_image = detect_dlib(our_image)\n",
        "    st.text(\"Results\")\n",
        "    st.image(result_image)\n",
        "with face_recognizer:\n",
        "  st.title(\"Face Recognition\")\n",
        "  st.text(\"This face recognizer is used to distinguish between simpsons characters\")\n",
        "  html_body = \"\"\"<body style=\"background-color:red;\"></body>\"\"\"\n",
        "  st.markdown(html_body,unsafe_allow_html=True)\n",
        "  html_temp = \"\"\"\n",
        "      <body style=\"background-color:red;\">\n",
        "      <div style=\"background-color:red;padding:10px;\">\n",
        "      <h2 style=\"color:white;text-align:center;\">Simpsons Face Recognition</h2>\n",
        "      </div>\n",
        "      </body>\n",
        "      \"\"\"\n",
        "  st.markdown(html_temp,unsafe_allow_html=True)\n",
        "  image_file_2 = st.file_uploader(\"Upload Image\",type=['jpg','png','jpeg'],key=1)\n",
        "  if image_file_2 is not None:\n",
        "    our_image_1 = Image.open(image_file_2)\n",
        "    st.text(\"Original Image\")\n",
        "    st.image(our_image_1)\n",
        "    our_image_1 = np.array(our_image_1,dtype=\"float32\")\n",
        "  if st.button(\"Recognise\"):\n",
        "    result = class_name[np.argmax(model.predict(our_image_1))]\n",
        "    st.text(\"Results\")\n",
        "    st.text(result)"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rj_ErxBwRlBM",
        "outputId": "6c90ff17-1e11-4778-97d9-b0437522aaa1"
      },
      "source": [
        "from pyngrok import ngrok\n",
        "public_url = ngrok.connect(port='80')\n",
        "print (public_url)\n",
        "!streamlit run app.py>/dev/null"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2021-09-30 16:01:52.076 INFO    pyngrok.ngrok: Opening tunnel named: http-80-a88667e4-7cd3-40b6-ba67-927a01d18e86\n",
            "2021-09-30 16:01:52.203 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=\"no configuration paths supplied\"\n",
            "2021-09-30 16:01:52.205 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=\"using configuration at default config path\" path=/root/.ngrok2/ngrok.yml\n",
            "2021-09-30 16:01:52.209 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=\"open config file\" path=/root/.ngrok2/ngrok.yml err=nil\n",
            "2021-09-30 16:01:52.219 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=\"starting web service\" obj=web addr=127.0.0.1:4040\n",
            "2021-09-30 16:01:52.416 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=\"tunnel session started\" obj=tunnels.session\n",
            "2021-09-30 16:01:52.418 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=\"client session established\" obj=csess id=0d37eb3d3120\n",
            "2021-09-30 16:01:52.431 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=start pg=/api/tunnels id=759f4f55d0c762cb\n",
            "2021-09-30 16:01:52.442 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=end pg=/api/tunnels id=759f4f55d0c762cb status=200 dur=594.545µs\n",
            "2021-09-30 16:01:52.444 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=start pg=/api/tunnels id=8e601f359b27cdc8\n",
            "2021-09-30 16:01:52.452 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=end pg=/api/tunnels id=8e601f359b27cdc8 status=200 dur=3.681488ms\n",
            "2021-09-30 16:01:52.454 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=start pg=/api/tunnels id=4a4e9d6318445bef\n",
            "2021-09-30 16:01:52.521 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=\"started tunnel\" obj=tunnels name=\"http-80-a88667e4-7cd3-40b6-ba67-927a01d18e86 (http)\" addr=http://localhost:80 url=http://7770-34-72-53-78.ngrok.io\n",
            "2021-09-30 16:01:52.523 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=\"started tunnel\" obj=tunnels name=http-80-a88667e4-7cd3-40b6-ba67-927a01d18e86 addr=http://localhost:80 url=https://7770-34-72-53-78.ngrok.io\n",
            "2021-09-30 16:01:52.574 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=end pg=/api/tunnels id=4a4e9d6318445bef status=201 dur=76.639351ms\n",
            "2021-09-30 16:01:52.580 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=start pg=\"/api/tunnels/http-80-a88667e4-7cd3-40b6-ba67-927a01d18e86 (http)\" id=3d1a864af08d4eb4\n",
            "2021-09-30 16:01:52.582 INFO    pyngrok.process.ngrok: t=2021-09-30T16:01:52+0000 lvl=info msg=end pg=\"/api/tunnels/http-80-a88667e4-7cd3-40b6-ba67-927a01d18e86 (http)\" id=3d1a864af08d4eb4 status=200 dur=343.572µs\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NgrokTunnel: \"http://7770-34-72-53-78.ngrok.io\" -> \"http://localhost:80\"\n",
            "2021-09-30 16:01:56.682811: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:01:56.697720: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:01:56.698445: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:01:56.699883: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:01:56.700612: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:01:56.701273: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:01:57.255782: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:01:57.256471: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:01:57.257150: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:01:57.257748: W tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc:39] Overriding allow_growth setting because the TF_FORCE_GPU_ALLOW_GROWTH environment variable is set. Original config value was 0.\n",
            "2021-09-30 16:01:57.257818: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6403 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7\n",
            "2021-09-30 16:01:57.421 Error in loading the saved optimizer state. As a result, your model is starting with a freshly initialized optimizer.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2021-09-30 16:02:08.479 WARNING pyngrok.process.ngrok: t=2021-09-30T16:02:08+0000 lvl=warn msg=\"failed to open private leg\" id=8bb2f7ef3526 privaddr=localhost:80 err=\"dial tcp 127.0.0.1:80: connect: connection refused\"\n",
            "2021-09-30 16:02:08.947 WARNING pyngrok.process.ngrok: t=2021-09-30T16:02:08+0000 lvl=warn msg=\"failed to open private leg\" id=40f9f4ddad95 privaddr=localhost:80 err=\"dial tcp 127.0.0.1:80: connect: connection refused\"\n",
            "2021-09-30 16:02:09.587 WARNING pyngrok.process.ngrok: t=2021-09-30T16:02:09+0000 lvl=warn msg=\"failed to open private leg\" id=2f4369b77b88 privaddr=localhost:80 err=\"dial tcp 127.0.0.1:80: connect: connection refused\"\n",
            "2021-09-30 16:02:15.612 INFO    pyngrok.process.ngrok: t=2021-09-30T16:02:15+0000 lvl=info msg=\"received stop request\" obj=app stopReq=\"{err:<nil> restart:false}\"\n",
            "2021-09-30 16:02:15.614 INFO    pyngrok.process.ngrok: t=2021-09-30T16:02:15+0000 lvl=info msg=\"session closing\" obj=tunnels.session err=nil\n"
          ]
        }
      ]
    }
  ]
}