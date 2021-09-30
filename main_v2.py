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
        "outputId": "5989004b-bc4e-4d81-9a5f-64897767fe0d"
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
            "Requirement already satisfied: numpy>=1.16.4 in /usr/local/lib/python3.7/dist-packages (from pydeck) (1.19.5)\n",
            "Requirement already satisfied: jinja2>=2.10.1 in /usr/local/lib/python3.7/dist-packages (from pydeck) (2.11.3)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck) (7.6.5)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck) (5.1.0)\n",
            "Requirement already satisfied: ipykernel>=5.1.2 in /usr/local/lib/python3.7/dist-packages (from pydeck) (6.4.1)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (0.1.3)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (1.0.0)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (0.2.0)\n",
            "Requirement already satisfied: importlib-metadata<5 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (4.8.1)\n",
            "Requirement already satisfied: argcomplete>=1.12.3 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (1.12.3)\n",
            "Requirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (5.3.5)\n",
            "Requirement already satisfied: ipython<8.0,>=7.23.1 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (7.28.0)\n",
            "Requirement already satisfied: tornado<7.0,>=4.2 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (5.1.1)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck) (3.5.0)\n",
            "Requirement already satisfied: typing-extensions>=3.6.4 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck) (3.7.4.3)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.7.5)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (57.4.0)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (3.0.20)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (2.6.1)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.2.0)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (4.4.2)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (4.8.0)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.18.0)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (3.5.1)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (5.1.3)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (1.0.2)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.7/dist-packages (from jedi>=0.16->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.8.2)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2>=2.10.1->pydeck) (2.0.1)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (22.3.0)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (2.8.2)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (4.8.1)\n",
            "Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /usr/local/lib/python3.7/dist-packages (from nbformat>=4.2.0->ipywidgets>=7.0.0->pydeck) (2.6.0)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect>4.3->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.2.5)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.1->jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (1.15.0)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (5.3.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (1.8.0)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (5.6.1)\n",
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.12.1)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.8.4)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (1.5.0)\n",
            "Requirement already satisfied: entrypoints>=0.2.2 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.3)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (4.1.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.7.1)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.5.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.5.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (21.0)\n",
            "Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (2.4.7)\n",
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.7/dist-packages (0.89.0)\n",
            "Requirement already satisfied: astor in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.8.1)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: watchdog in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.1.5)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.23.0)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.1.5)\n",
            "Requirement already satisfied: validators in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.18.2)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.1.0)\n",
            "Requirement already satisfied: base58 in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.1.0)\n",
            "Requirement already satisfied: pydeck>=0.1.dev5 in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.7.0)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (5.1.1)\n",
            "Requirement already satisfied: gitpython!=3.1.19 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.1.24)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.19.5)\n",
            "Requirement already satisfied: pyarrow in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.0.0)\n",
            "Requirement already satisfied: attrs in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.2.0)\n",
            "Requirement already satisfied: tzlocal in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.5.1)\n",
            "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.17.3)\n",
            "Requirement already satisfied: click<8.0,>=7.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: blinker in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.11.1)\n",
            "Requirement already satisfied: jsonschema in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.6.0)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit) (4.0.7)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit) (3.7.4.3)\n",
            "Requirement already satisfied: smmap<5,>=3.0.1 in /usr/local/lib/python3.7/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (4.0.0)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.21.0->streamlit) (2018.9)\n",
            "Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.7/dist-packages (from protobuf!=3.11,>=3.6.0->streamlit) (1.15.0)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (7.6.5)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (5.1.0)\n",
            "Requirement already satisfied: ipykernel>=5.1.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (6.4.1)\n",
            "Requirement already satisfied: importlib-metadata<5 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.1)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (5.3.5)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.3)\n",
            "Requirement already satisfied: argcomplete>=1.12.3 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.12.3)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.0.0)\n",
            "Requirement already satisfied: ipython<8.0,>=7.23.1 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (7.28.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.5.0)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.0)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.6.1)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.18.0)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.4.2)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (57.4.0)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.0.20)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.0.2)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.1.3)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.7/dist-packages (from jedi>=0.16->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.8.2)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (22.3.0)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.1)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect>4.3->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.5)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.3.1)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.6.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.8.0)\n",
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.12.1)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.1)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.0)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.1.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
            "Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->streamlit) (2.4.7)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (3.0.4)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (1.24.3)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (2.10)\n",
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
        "outputId": "525b6778-1c55-4124-ba68-539f4426b65a"
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
            "2021-09-30 13:20:20.706961: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:21.148855: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:21.149741: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.428866: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.429909: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.430683: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.431853: W tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc:39] Overriding allow_growth setting because the TF_FORCE_GPU_ALLOW_GROWTH environment variable is set. Original config value was 0.\n",
            "2021-09-30 13:20:26.431914: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /device:GPU:0 with 10819 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7\n",
            "2021-09-30 13:20:26.454655: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.455561: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.456342: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.457481: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.458300: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.459084: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.460021: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.460945: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 13:20:26.461718: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 10819 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7\n",
            "2021-09-30 13:20:29.046272: I tensorflow/stream_executor/cuda/cuda_dnn.cc:369] Loaded cuDNN version 8005\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Time (s) to convolve 32x7x7x3 filter over random 100x100x100x3 images (batch x height x width x channel). Sum of ten runs.\n",
            "CPU (s):\n",
            "3.724701197999991\n",
            "GPU (s):\n",
            "0.04444383699996024\n",
            "GPU speedup over CPU: 83x\n"
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
        "outputId": "b096d60b-dcc4-4d8b-b8ae-49213140a985"
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
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_F3VGvVT2suy",
        "outputId": "2c837ea9-1554-4f43-a435-a4801208a2bb"
      },
      "source": [
        "tuner.search_space_summary()"
      ],
      "execution_count": 45,
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
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bt9QXts-oIaZ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6c5c2700-7ec4-4206-c029-3efe9e4a8de2"
      },
      "source": [
        "tuner.search(\n",
        "    train_set,\n",
        "    validation_data=val_set,\n",
        "    epochs=5,\n",
        "    callbacks=[keras.callbacks.TensorBoard(\"/tmp/logs_dir\")]\n",
        ")"
      ],
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Trial 5 Complete [00h 02m 27s]\n",
            "val_accuracy: 0.8620564937591553\n",
            "\n",
            "Best val_accuracy So Far: 0.8808833956718445\n",
            "Total elapsed time: 00h 12m 44s\n",
            "INFO:tensorflow:Oracle triggered exit\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2021-09-30 14:47:46.463 INFO    tensorflow: Oracle triggered exit\n"
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
        "outputId": "8c569f92-cc38-41ed-f3d4-7238bb7b7d2a"
      },
      "source": [
        "models = tuner.get_best_models(num_models=1)\n",
        "model = models[0]\n",
        "history = model.fit_generator(train_set,\n",
        "                              validation_data = val_set,\n",
        "                              verbose=2,\n",
        "                              epochs=5)"
      ],
      "execution_count": 48,
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
            "346/346 - 25s - loss: 0.5277 - accuracy: 0.8394 - val_loss: 0.3895 - val_accuracy: 0.8791\n",
            "Epoch 2/5\n",
            "346/346 - 24s - loss: 0.5156 - accuracy: 0.8456 - val_loss: 0.3703 - val_accuracy: 0.8892\n",
            "Epoch 3/5\n",
            "346/346 - 24s - loss: 0.4681 - accuracy: 0.8603 - val_loss: 0.3298 - val_accuracy: 0.9004\n",
            "Epoch 4/5\n",
            "346/346 - 24s - loss: 0.4617 - accuracy: 0.8692 - val_loss: 0.3553 - val_accuracy: 0.8892\n",
            "Epoch 5/5\n",
            "346/346 - 24s - loss: 0.4617 - accuracy: 0.8723 - val_loss: 0.2922 - val_accuracy: 0.9138\n"
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
      "execution_count": 63,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qgKvcpZAMU2o",
        "outputId": "2adf0055-52b7-4b0d-fed9-c2836ca75810"
      },
      "source": [
        "np.unique(y_test)"
      ],
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.], dtype=float32)"
            ]
          },
          "metadata": {},
          "execution_count": 64
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
        "outputId": "6c0e4fa4-6bc9-4d02-a2a7-b30afd0f9bd6"
      },
      "source": [
        "test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)\n",
        "print(test_acc)"
      ],
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/keras/backend.py:4907: UserWarning: \"`sparse_categorical_crossentropy` received `from_logits=True`, but the `output` argument was produced by a sigmoid or softmax activation and thus does not represent logits. Was this intended?\"\n",
            "  '\"`sparse_categorical_crossentropy` received `from_logits=True`, but '\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "16/16 - 1s - loss: 0.1786 - accuracy: 0.9456\n",
            "0.9455645084381104\n"
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
      "execution_count": 66,
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
        "outputId": "a83e6269-25a0-4d2c-a772-98345da6aa37"
      },
      "source": [
        "predictions = model.predict(x_test)\n",
        "prediction_labels = np.argmax(predictions,1)\n",
        "cm = confusion_matrix(y_test,prediction_labels)\n",
        "print_confusion_matrix(cm,class_names=['bart_simpson','charles_montgomery_burns', 'homer_simpson','krusty_the_clown',\n",
        "                                     'lisa_simpson','marge_simpson','milhouse_van_houten','moe_szyslak','ned_flanders',\n",
        "                                       'principal_skinner'])"
      ],
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAuYAAAI3CAYAAADX+57ZAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdd5gV9dnG8e+9gA00aohKU4hoxIYFa9RANJZEY4mCMSZY8mIsCcYajTUWrLE3Eg1IMLYUEMUa0aCoYAEBEUFBAcGChSZSnvePmYPHddk9C2d3dpb7c13ncs/Ue2YH9zm/fWZWEYGZmZmZmWWrIusAZmZmZmbmwtzMzMzMrEFwYW5mZmZm1gC4MDczMzMzawBcmJuZmZmZNQAuzM3MzMzMGoCmWQcwMzMzM8s7SVOAOcASYHFEdJG0PnAf0B6YAnSPiE+Wtw2PmJuZmZmZlUe3iNguIrqk7/8APBURmwFPpe+Xy4W5mZmZmVndOBjon37dHzikuoVdmJuZmZmZrbwAHpf0sqRe6bQNI+L99OuZwIbVbcA95mYZWTD0xsg6Q22sffCVWUeotbVXWzPrCLUy58sFWUeotbydY8jfeW7WxD+q69qiJYuzjlBrebwuFiyYqvrc36KP3i7bz9nVvrPpCUCvokl9I6JvpcX2iIjpkjYAnpA0oXhmRISkajPl77tqZmZmZlaP0iK8ciFeeZnp6X8/kPRvYGdglqRWEfG+pFbAB9Vtw60sZmZmZtb4LF1SvlcNJDWXtHbha2BfYCwwGOiZLtYTGFTddjxibmZmZmaNTyytz71tCPxbEiT19T0R8aikkcD9ko4HpgLdq9uIC3MzMzMzs5UQEW8DnauY/jGwd6nbcWFuZmZmZo3P0nodMS8LF+ZmZmZm1uhE/baylIVv/jQzMzMzawA8Ym5mZmZmjY9bWczMzMzMGgC3spiZmZmZ2YrwiLmZmZmZNT4l/GGghsYj5qsQScMk3Zx1jppIukjS2KxzmJmZWY7F0vK96okLc1tpdVBIXwP8oIzbMzMzM2vwXJjbSpHUrNzbjIi56V/KshIsWbqUHlffx2/7DgHgon/8l+5X3csRV97LGX97lPkLv8w44fLtt29Xxo19lgnjh3PWmSdnHadGbdq0YvAjf2fEqEd5fuRQTjipZ9aRSpKn8+xzXD9uv/1qpk59mVGjHs86SsnymNnXRcaWLi3fq564MF/1NJV0g6RP0tfVkioAJB0taaSkOZI+kPSApDaFFSV1lRSSfizpJUlfAicAFwJbpfNC0jE1hZB0gqSJkr6Q9JGkxyQ1Ted9bQReUj9JQySdLWmmpM8kXSGpIl32g3T62ZX2EZJOkfSwpPmSpko6utIyF6TTF6bbuLto3uqSrpc0K835gqQ9qjgfe0t6Md3HKEk71PabsjLueWYMHTZcb9n7Mw7dg/vPOpIHzj6SjdZtwb3/e70+45SsoqKCG2+4jAMPOpptOnejR49D6NRps6xjVWvx4sWcd04fduuyP/t2O5xf/9/RfG+LjlnHqlbezrPPcf0YMOABDj44Hx96CvKW2ddF9iKWlu1VX1yYr3p+QfJ9342kqO4FnJrOW42kyO4MHAi0BP5RxTauBM4DtgAGAdcCbwKt0td91QWQ1AW4BbgY+B6wN/BoDbn3AjoAXYHfAGcBjwCrA3sAFwFXSNqx0noXA4OB7YC+wN3p/pH0M+AM4CRgs/SYXypa9yqgB3AcsD3wOvCopFaV9tEH+AOwA/AxMFCSajiespj16Vz+N34Kh+265bJpLdZYDYCIYOGixYh6iVJrO++0PZMnT+Gdd95l0aJF3H//IH560H5Zx6rWrFkfMmb0OADmzp3HxDcn06rVhhmnql7ezrPPcf147rmXmD3706xj1EreMvu6sBXhp7Kset4HfhcRAUyQtDlwGvDniLiraLm3JZ0IvCGpbURMK5p3UUQs+z2XpLnA4oiYWWKGjYF5wOCImANMBUbXsM5nwMkRsSTNfTrQKiL2T+dPlPQHoBvwctF6/4qIO9KvL5PUjeSDyNHAJun5eDwiFgHvAqPSY2oOnAj8OiIeTqf9BvghcDLJB5OC8yPi6XSZPwHDgTZA8TmrE1f/ezin/nR35n2x6GvTL7jnKYaPn8p3N1qf0w75fl3HWCGt22zEe9NmLHs/bfr77LzT9hkmqp12G7dh285b8vKomi7dbOX5PPscW575umgAcvgHhjxivup5IS3KC0YAbSStI2kHSYPS1o45pEUqSSFdbBQr5wmSYvwdSQMl9ZS0dg3rjE+L8oJZQOUbTmcBG1SaNqKK94Xh5QeANdIcd0o6QtLq6bxNgWbAc4UV0/0Xr18wpujrwv+FK+cou2fHTWG9FmuyZbtv7upPR+3NE386hg4brsdjr06q6yirnObN1+LugbdwztmXMmfO3KzjNEo+x2a20vxUFssxAY8B84FfAjsBhdHo1SotO29ldpSOku8AdCcZpT6HZBS8dTWrLar0PpYzreRrOiLeI2mlOQH4nKQl5+V0tLzaVavJVphXZQ5JvdI+9FF3Dn2+1KhVeu3t93lm7DsccPHd/OHuxxj51nTOHfDEsvlNKirYf4fNeGr05JXaT12ZMX0m7dp+9S1v26YVM2aU+kuX7DRt2pT+A2/hgfsGM2Rww79BKo/n2efYGgNfFw3A0iXle9UTF+arnl0q9T/vSjLK25Gkp/zciHg2IiZQ+qjvl0CT2oSIiMUR8d+IOAfYFmhO0uNdbrtW8f6NohxfRMTDEfF7kg8jWwHfByaTHNeyPhBJTUh688evaJiI6BsRXSKiy/EH7L6imwHgdwftxuMXH8PQC3/FFb/aj502a8NlR+/Dux9+WtgXz4x952s3hjYkI0e9RseOHWjfvh3NmjWje/eDeWhIwy/Cbrq1DxPfnMStN99V88INQB7Ps8+xNQa+LmxFuMd81dMauF7SrcA2wJnApSQj1wuBUyTdAnQCLilxm1OATdKnkbwLzImIhctbWNKBJK0izwKzSfrC16aoYC6jwySNBIYBh5PcaLpLmuMYkn8DLwJzSW70XAS8FRHzJN0GXCnpI+Ad4PfAhsCtdZCzLCLg/HueYt4XXxIBm7f5Nn88omvWsaq0ZMkSep96Ho88fA9NKiro1/8+xo+fmHWsau26244cedShjBs7gWefHwzAJRddyxOPP5NxsuXL23n2Oa4f/fvfyJ577kbLlusxadILXHLJdfTvX+19+5nLW2ZfFw1APbaglIu+3m5sjZmkYcAEYDHJzY8B3AWcFRFLJPUALie5cXEMcD7J01K6RcQwSV2Bp4HvRMRHRdtdHRhIUvSuCxwbEf2qybEHSdG/LbAWyej0tRHxt3T+RcDhEbF1+r4f0DIiDizaxhDgo4g4pmjaC8DwiDgjfR/Ab0lG4n8AfEhyo2b/dP4hwNkkH0KakYyEXxwRQ4qO60rg5+lxvQqcERHD0/nfOB+S2pMU8TtFRLW9+AuG3pirf3xrH3xl1hFqbe3V1sw6Qq3M+XJB1hFqLW/nGPJ3nps18RhaXVu0ZHHWEWotj9fFggVT6/UxYQvHPVW2n7Orb7V3vWR3YW6NVlqYHxERD2adpSouzOte3orGvBWMkL9zDPk7z3kswPLGhXn9cGFes/x9V83MzMzMapLDVhYX5lZ2kn4B3LGc2VMjYqv6zGNmZmaroBw+x9yFudWFwSQ3VFal8iMO60xENMw/eWlmZmZWBRfmVnbpc8rnZJ3DzMzMVl1f/7uE+eDC3MzMzMwanxz2mPsPDJmZmZmZNQAeMTczMzOzxsc3f5qZmZmZNQBuZTEzMzMzsxXhEXMzMzMza3yW+qksZmZmZmbZcyuLmZmZmZmtCI+Ym5mZmVnj46eymFmp1j/s2qwj1Mqcvx2XdYRaW/vYu7KOUCvNmuTvf8lfLFmUdQRrgNZo0izrCLWyaMnirCNYXXAri5mZmZmZrYj8Dc+YmZmZmdXErSxmZmZmZg1ADgtzt7KYmZmZmTUAHjE3MzMzs0Ynwn9gyMzMzMwse25lMTMzMzOzFeERczMzMzNrfHL4HHMX5mZmZmbW+LiVxczMzMzMVoRHzM3MzMys8XEri5mZmZlZA+BWltJIai8pJHWpo+0Pk3RzXWzbGh5/v83MzKwxcI95jkmaIumMrHOYmZmZNTixtHyvetKoCnNJq2WdwWqnIX/PGnK2qtx++9VMnfoyo0Y9nnWUGi1ZupQefR/nt//4HwD3vvQWB930CNv96X4+mb8w43TV22/frowb+ywTxg/nrDNPzjpOjfJ0XRTkMbOvi7rVpk0rBj/yd0aMepTnRw7lhJN6Zh2pJL4uMrZ0afle9aROC3MlTpf0lqSFkqZJ6lO0yCaSnpA0X9J4ST8qWreJpDslvSNpQbqNsyRVFC3TT9IQSWdLmgZMW06O1SRdme5/vqSRkvYrmt9M0o2SZqQ535N0RYnHOEXSBWmWOem6PSStK+leSXPT7PtWWm8vSS9K+kLSLEnXFReCaXvGrZIul/SRpA8kXVM4fknDgE2Aq9O2oCha9zhJ76bH+pCkk4rnp8ucIGmSpC/T//5fpfkh6URJg9LtTJTUTVJbSY9JmifpNUk7VFpvd0nPpOtMl3SbpHUqHddt6bF8CDwn6S5JQyptpyI9htNK+T4ATSXdIOmT9HV1pWvlG79dqNwCky5zUZrnU2CgpGPS7+Heksamx/20pA5F67VLz9Ps9LgnSDqyxNxlM2DAAxx8cD5+WN3z4lt0aLnssmC7di25/Zc/oNW31sowVc0qKiq48YbLOPCgo9mmczd69DiETp02yzpWtfJ0XRTkLbOvi7q3ePFizjunD7t12Z99ux3Or//vaL63RcesY1XL14WtiLoeMb8cOB/oA2wFHAG8VzT/MuBGoDMwErhXUouibNOB7kAn4I/AucCxlfbxA2BbYH9g7+Xk+Fu63FHA1kB/4CFJndP5vwMOBY4ENgN6AG/W4jhPBV4CdgDuT7d/D/AIsB3wLPB3SWsASGoDDAVeBbYHjgd+TnKeiv0CWAzsDpyS7qdHOu8wkg8ifwJapS8k7Qb8Fbgl3fdg4OLijUo6FLgZuD49HzcAt0o6qNL+zwPuJfn+jEq/vhO4Nc09A+hXtN1tgMfTfXZOM24H3FVpu0cDAvYEfgX8BdhfUquiZX4EbAQMoDS/ILlmdgNOAHqRnK/aOg2YAHQhud4AVgfOAY5Lt78ucHvROrcCawHdSK7zU4FPV2DfK+W5515i9ux6322tzfp8Pv97630O237ZZxu2aLUebdZtnmGq0uy80/ZMnjyFd955l0WLFnH//YP46UH71bxihvJyXRTLW2ZfF3Vv1qwPGTN6HABz585j4puTadVqw4xTVc/XRQOQwxHzOnsqS1pg/x44NSIKhdkkYISk9un76yLioXT5c0mKtO2A4RGxCLigaJNT0tHZn5MUhwVfAMdFRJW//5a0abpO+4h4N518s6R9SAq4k0hGnicC/4uIAN4Fnq/F4T4WEbem+7uQpLibFBF3p9MuISnqtiYpcE8iKWpPioilwBuS/gDcIen8iJifbnd8RBTOwcR0VHtv4B8RMVvSEmBORMwsyvI74PGIuLJovZ2A4hHxM4ABEXFz0TI7AmcDDxUtd3dE/CM9hsvT8/hYRAxKp10FPC2pZUR8BJwJ3BcR1xY2IOlE4FVJG0TEB+nkdyLi9OITKGkC0BMo/KbiOGBwRHxY9Sn/hveB36XfvwmSNif5Pvy5xPULnomIq4pyfZ/k38nJEfFmOu0a4C5JSve3CfDPiBhdOL5a7nOVcvVjr3HqPtsy78vFWUeptdZtNuK9aTOWvZ82/X123mn7DBNZQ+Dron6127gN23bekpdHja554Qz5umgAcvi4xLocMd+SZKTxqWqWGVP0deHq3aAwQdJvJI2S9KGkuSSF/saVtjF2eUV5ageS0dnxaUvC3HRbPwE2TZfpR/KBYKKkWyT9pLgNogTLjiMi5gLzgdeL5s+qdGydgBfSorxgOLAaUPy7ueLzA8k52oDqbUEyel/sxUrvOwHPVZo2nOR7Vqx4/4VjqO64dgSOrnSeC/vZtGi9l6vI/RfS34ZIWh84mK9/AKvJC2mRXDACaFPcRlOiUVVMW1goylMzSL5X66XvbwDOkzRC0qXphxyrwrMTZ7Be89XZsvX6WUcxsxxq3nwt7h54C+ecfSlz5szNOo5Z2WX9HPNFhS8iIiRB+mFBUg+SVoszSEavPwdOJmk5KTavhn1UAAHsVLy/1IJ036+ko/j7kYxI9wdGS/pRpeK5xuMoHE6laYWCsZRiv7i4rGq7dflhKiq9r+oYqjuuCpI2muuq2Pb0oq+r+p4NAK6UtAdJm8yHwGMlZC7VUpIPaMWaVbFcVdkqD+1+7bgj4k5JjwE/BvYBnpfUJyIuqrwhSb1I2mxo2nR9mjZtUXmRRu219z7imTdnMPyt9/ly8VLmLVzEuf9+gcsP3TXraCWZMX0m7dq2Xva+bZtWzJgxs5o1bFXg66J+NG3alP4Db+GB+wYzZHDDvznR10UDkMPnmNdlYf4GsJCk0H1rBdbfA3ixqN2i0JZSW6+SFGQbRcTTy1soIuYADwIPSuoHvEAyej1xBfZZkzeA7pIqigr/PYAvgcm12M6XQJNK0yaQfAgptnMV+/8+Xx+R3gMYX4t9V+UVYKuImFTbFdPWnH+RtLBsD/Qv8UNRwS5FrSUAuwIzIuLz9P2HpH34AGm//xYk18dKi4hpQF+gr6Szgd7ARVUs1zddjjXX3KTyB6FG73d7b8vv9t4WgJFTPuDuEW/mpigHGDnqNTp27ED79u2YPn0m3bsfzC9/1fCftGB1y9dF/bjp1j5MfHMSt95c+balhsnXRQPgVpavpIXuDUAfScdK2lTSzmnPcSkmAjtIOkDSZpLOJ7mBs7Y5JgIDgX6SDpf0XUldJJ0h6TAASadJ+rmkTpI6ktwk+jnLecpLGdwKtCa54bKTpJ+Q9FbfXNRfXoopwJ6S2khqmU67EdhX0pnpeTueb/6W4Wrgl5JOTpf5LcnNk1excq4EdpZ0u6TtJXWUdKCkO0pc/y9pjs5884bRmrQGrpf0PUmHk/S7F4/c/xf4haSukrZKt1+WD6ZKngazf3ptbUdyI/LKfsiptf79b2TYsH+z+ebfZdKkF+jZs0fNKzUQ97w4kX2ve4gPPl9A99sf4+KHRmYdqUpLliyh96nn8cjD9zB2zDAefPAhxo+vi8/u5ZPH6yJvmX1d1L1dd9uRI486lL1+sBvPPj+YZ58fzI/2rXVJUK98XdiKqOtWlnOAT0iezNKWpCf57hLXvYOk7/sekhHvfwLXkoyo1taxJE91uSrNMZukD7swgj6HpJDbjKRN4VXggFoWySWLiOmSDiApkF8jeYLHPXz1FJBSXUByniaT9PMrIkakN4leTPLElidJCuZLi/b/n7QYP4OkXWgqyY2oD7ESImKMpL3SfT1DMpr/NvDvEjcxjOTD0NSIeLuWux+Y7u9Fku/hnXy9MO8DtAcGAXNJngjUmvKoAG4C2pFcS08Bp1e7Rh3o2fN39b3LlbJT+w3YqX1ye8JRu2zOUbtsnnGi0gx99L8MffS/WccoWd6uC8hnZl8XdeuFES+zXouG/XjEqvi6yFgOW1n09fvlrDGSdB2wT0Rsk3WW6khak6QX/bcRMTDrPHUtb60ss//6q6wj1Nrax+bjV94FzZpkfdvPqmHRknw9ESiP18UaTaq6hafhmvPlgqwj1Foer4sFC6ZWvterbvf3r8vL9nN2zcPOrZfs+fuuWo0knQk8QTIyvA/wG2o/Gl9v0ifgtCTpy15A8ix4MzMzs1WKC/NqSNqT5A8BVSkiGuojNbqQtKl8i+SZ2ueQ9Ps3VBuT5JwGHJs+wx4ASRtTfb/2lkXPpzczMzNL5LCVxYV59UaR9LnnSkTk6m6NiJjCNx9lWDCD6r8HM6qZZ2ZmZqsqF+aNS0QsIPlrpZaRiFiMvwdmZma2CnBhbmZmZmaNTw4fcOLC3MzMzMwanxy2stTln3c3MzMzM7MSecTczMzMzBqfHI6YuzA3MzMzs8Yn8leYu5XFzMzMzKwBcGFuZmZmZo3P0qXle5VIUhNJr0oakr7vIOlFSZMk3SdpterWd2FuZmZmZo1PRPlepesNvFH0/krguojoCHwCHF/dyi7MzczMzKzxqecRc0ltgZ8Af03fC/gh8GC6SH/gkOq24Zs/zTKyRpNmWUeolbWPvSvrCLU279W7s45QK823/1XWEawBWrRkcdYRrAHyddEgXQ+cBaydvv828Gn6V8wBpgFtqtuAR8zNzMzMrPEp44i5pF6SRhW9ehXvStKBwAcR8fLKRPaIuZmZmZk1PmV8XGJE9AX6VrPI94GfSvoxsAawDnADsK6kpumoeVtgenX78Yi5mZmZmdlKiIhzIqJtRLQHjgT+GxG/AJ4GDk8X6wkMqm47LszNzMzMrNGJpVG210o4GzhN0iSSnvM7q1vYrSxmZmZm1vjU4vnj5RQRw4Bh6ddvAzuXuq5HzM3MzMzMGgCPmJuZmZlZ41PGmz/riwtzMzMzM2t8Vq43PBNuZTEzMzMzawA8Ym5mZmZmjU9GN3+uDBfmZmZmZtb45LAwdyuLmZmZmVkD4MI8JyQNk3Rz1jnqg6Qpks7IOoeZmZnlWET5XvXErSzWEO0EzMs6hJmZmeWYW1nMQFKzlVk/Ij6MiPnlyrOqaNOmFYMf+TsjRj3K8yOHcsJJPbOOVKP99u3KuLHPMmH8cM468+Ss41RryZKldD/9ck657FYAev7xWo447XKOOO1y9j7+HHpfcXvGCZcvT+cZ8pcX8pc5b3kBbr/9aqZOfZlRox7POkrJ8nae85a3MXJhni8Vki6X9JGkDyRdI6kCQNJ6kvpL+kTSAklPStqqsKKkYyTNlXSApAmS5ksaLOlbkg6X9JakzyQNkLRm0XqSdJakyel2X5d0dNH89pJC0s8l/VfSAuCE6g4i3eeA9Bi+kPS2pFOL5n+tlSXd/omSBqW5J0rqJqmtpMckzZP0mqQdqjjeg9Llv5D0tKTvFi3TLt3m7HS7EyQdWTR/m/Q8LkiX6SfpW0Xz+0kaIqm3pOnpuf+bpLVq+X0ti8WLF3PeOX3Yrcv+7NvtcH79f0fzvS06ZhGlJBUVFdx4w2UceNDRbNO5Gz16HEKnTptlHWu5Bj78NB3abrTsff/LTueBP5/LA38+l22/14G9d9kuw3TLl7fznLe8kL/MectbMGDAAxx8cMMfcCjI23nOW96SLI3yveqJC/N8+QWwGNgdOAU4FeiRzusH7AIcDOwMzAceLS6ygdWB09Pt7A10Af4J9AR+BhwCHAicVLTOpcDxwMnAlkAf4A5JP6mUrQ9wa7rMf2o4jkuBbdJ9fQ84DphewzrnAfcCnYFR6dd3pvvcHpiRnoNiqwMXAscCuwFNgH9JUjr/VmAtoBuwFcn5/BRAUnPgMWAuyfk8lOS831VpH3sCWwP7kHwvDgV613AsdWLWrA8ZM3ocAHPnzmPim5Np1WrDLKKUZOedtmfy5Cm88867LFq0iPvvH8RPD9ov61hVmvnRJzz78lgO2+f735g3d/4CXnr9TX64S+cMktUsT+cZ8pcX8pc5b3kLnnvuJWbP/jTrGCXL23nOW96SxNLyveqJC/N8GR8RF0TExIi4H3ga2FvSZsBPgV4R8WxEvA78EliHpAgvaAqcHBEvR8QI4B6SovTYiBgTEU8Dg9JpheL0NODXEfFoRLwTEfcAfyEp1IvdFBEPpstMq+E4NgFeiYiXImJqRAyLiAdqWOfuiPhHRLwFXA5sADwWEYMiYiJwFbCNpJaVjrd3RDwXEa+m52Qbkg8lhRzDI2J0mvvRiHg0nXcU0Bz4ZUS8HhHPAL2AwyQVD0N/DvwmIt6IiMeBB4q2n5l2G7dh285b8vKo0VlHWa7WbTbivWkzlr2fNv19WrfeqJo1snPVXQ9y2q8OpWLZZ7qv/PfF0eyyzRa0WGvNKtbMXp7OM+QvL+Qvc97y5lXeznPe8jZWLszzZUyl9zNICtROwFJgRGFGRHwGvE4ygl2wMCLeLHo/C5gZER9VmrZB+vWWwBokI+9zCy/gRGDTSllG1eI4bgN6SBqdtuP8oIR1io99Vvrf16uYtkHRtKXAS4U3ETGV5JwVzskNwHmSRki6VNKORet2AsZExJyiac+n2yw+p+MjYknR+8L3JDPNm6/F3QNv4ZyzL2XOnLlZRmkUnhn1Out/qwVbbrpxlfOHDh/FAXt2qedUZmZWoxy2svipLPmyqNL7oOYPV8VX0+Iq5lW3zcJ/DwLerSFLyU9RiYihkjYBDiAZXX5Y0gMRcWw1qxXvL6qZVvl8LPdfU0TcKekx4MckrSjPS+oTERfVdAjLyVWYt9zviaReJCPvrLnad1i92To17Kp2mjZtSv+Bt/DAfYMZMrhh3yA1Y/pM2rVtvex92zatmDFjZoaJqvbahMkMG/k6w18Zx8JFi5k3fwHnXP83+px6LJ98Ppexb03l+rOrva0iU3k5zwV5ywv5y5y3vHmVt/Oct7ylCD+VxTLyBsn3crfCBEnrkLRtjF+J7Y4HFgKbRMSkSq+pKxM4Ij6KiAERcQxJD3tPSauvzDarUEHSHw6ApI2B1iTnq5BjWkT0jYjuwAWkRXO6zDaS1i7a3u7pNt9gBaX76hIRXcpdlAPcdGsfJr45iVtvrtwK3/CMHPUaHTt2oH37djRr1ozu3Q/moSEN78NE76MP4cm/Xs6jd1zKVacdx87bfI8+pyafIZ8Y8Qp7ddma1VdbqQcR1am8nOeCvOWF/GXOW968ytt5zlvexsoj5o1ARLwlaRDJTZm9SG5gvIyk//meldjuHEnXANekN0w+C7QAdgWWRkTfFdmupD8BrwDjSK7Bw4C3I2LhimZdjsXA9ZJ6AwuA69J9PpnmuAEYCkwk6cffn68+yAwELgbulnQBsB5wB/CviJhU5pxlsetuO3LkUYcybuwEnn1+MACXXHQtTzz+TMbJqrZkyRJ6n3oejzx8D00qKujX/z7Gj5+YdaxaeXT4yxx36L5Zx6hW3s5z3vJC/jLnLW9B//43sueeu9Gy5XpMmvQCl8T8AFQAACAASURBVFxyHf3735d1rOXK23nOW96S1GMLSrko6vGvGdmKkzQMGBsRpxRN6we0jIgDJa0HXE9yE+gawHMkNz6OS5c9Brg5IloUrX8GcEpEtC+adgWwT0R0Sd+L5Akwhb7yz4HXgKsi4glJ7YF3gJ0ioqQ+c0l/JLm5sgPwBfACcHpEvJHOn5JmvSZ9H8AREfFg+r4l8CHQLSKGpdO2IB3ljoixheMlufn1GmDjdD/HFwprSTeRFOPtgDnAU2mO6en8bdJzunuac1B6Tj+rfP6Lju0i4PCI2Lqm87Bei465+sc358sFWUeotXmv3p11hFppvv2vso5gVhbNmuRr3G/RksqdnlYXFn85/Zt30NeheZceXbafs83P+3u9ZHdhbo1SVR9EGhoX5nXPhblZNlyYW1VcmNcsX/9yzMzMzMxKkcNWFt/8aWUnaWjx4xUrvc7NOp+ZmZmtApYuLd+rnnjE3OrCr4Hl/bWV2fURICL68c2/BGpmZmbWYLkwt7Ir3DxpZmZmlpkctrK4MDczMzOzxif8B4bMzMzMzGwFeMTczMzMzBoft7KYmZmZmWUv6vFpKuXiVhYzMzMzswbAI+ZmZmZm1vi4lcXMzMzMrAHIYWHuVhYzMzMzswbAI+ZmZmZm1vjk8DnmLszNMjLnywVZR2j0mm//q6wj1MqCGf/LOkKtrdl6z6wjWAO0aMnirCOYuZXFzMzMzMxWjEfMzczMzKzRiRyOmLswNzMzM7PGJ4eFuVtZzMzMzMwaAI+Ym5mZmVnjs9RPZTEzMzMzy55bWczMzMzMbEV4xNzMzMzMGp8cjpi7MDczMzOzRicif4W5W1nMzMzMzBoAj5ibmZmZWePjVhYzMzMzswYgh4W5W1kyJmmYpJuzzlEXJHWVFJJaZpghJB2e1f7NzMzMSuXCfBUk6SJJY8u8zUb7AcPMzMzyJ5ZG2V71xYV5jkhaLesM1rDtt29Xxo19lgnjh3PWmSdnHadGecsL+cm87896cugvT+RnPU+m+3G/A+Czz+fw697n8uMex/Pr3ufy2edzMk5Ztbyc42J5y5y3vODM9SFveWu0NMr3qicuzBsYSXtL+lTSbyT1kzRE0tmSpgHT0mWmSDqj0npfG7GWdJikMZIWSJot6RlJG0o6BrgQ2Cpt8whJx0i6S9KQStuskPSupNNqyNwP+AFwctE22xct0lnSi5LmSxolaYdK6++e5psvabqk2yStU+L5kqTTJb0laaGkaZL6VLP8NpKeLDov/SR9K523RZp9o/T9Wuk2Hy1a/9eSJqVft0+X/5mkJ9L84yX9qJTs5VZRUcGNN1zGgQcdzTadu9GjxyF06rRZFlFKkre8kL/Md910Bf/sfwv333UjAH8dcD+7dtmOR+67k127bMedf78/44TflLdzDPnLnLe84Mz1IW95S7K0jK964sK8AUl7of8N9IqI29PJPwC2BfYH9i5xOxsB9wL9gU7AXsCAdPZ9wLXAm0Cr9HUf8Bdgf0mtijb1I2CjonWXpzcwAvhb0TbfK5rfB/gDsAPwMTBQktKs2wCPA4OBzsBhwHbAXaUcK3A5cH66j62AIyrtexlJzYHHgLnAzsChwO6FfUXEBGAm0DVdZXfgc+D7kgo3SncFhlXa9GXAjWn+kcC9klqUmL9sdt5peyZPnsI777zLokWLuP/+Qfz0oP3qO0bJ8pYX8pm52NP/G8HBB+wDwMEH7MN/nx2RcaJvyuM5zlvmvOUFZ64PecvbWLkwbyAk9QLuBA6PiOJhrC+A4yJibES8XuLmWgPNgAcjYkq67l8jYlZELCApTBdHxMz0tSAiRgATgJ5F2zkOGBwRH1a3s4j4DPgSmF+0zSVFi5wfEU+nhe+fgC2ANum8M4H7IuLaiHgrIl4ETgR+JmmD6vabFr+/B/4QEXdFxKSIGBERty5nlaOA5sAvI+L1iHgG6AUcJqljuswzQLf0667AgyQfJnZKp/2Abxbm10XEQxHxFnAusD7Jh4t61brNRrw3bcay99Omv0/r1hvVd4yS5S0v5CuzJHr9/o90P+63PDDoEQA+/uRTvtNyfQBafns9Pv7k0ywjVilP57ggb5nzlhecuT7kLW8p8thj7sclNgyHACcAe6UFcrGxEbGwltsbDTwJjJX0ePr1gzUV2CSj5icBV0haHziYZFR5ZY0p+rrwr34DktacHYGOknoULaP0v5sCH1Sz3S2B1YGnSszRCRgTEcWNtc+T/JJqS2ASSdH9+3ReV5KR8DWBrpI+BNryzcJ8ecdnlpm7b7uGDb/Tko8/+ZT/O/VcOmzS7mvzJZH+4srMrHHy4xJtBY0G3geO1zd/Us6rYvmlfFW8FjQrfJGOVu+bvsYAxwNvSepcQ44BwCaS9gB+AXxI0vqxshYVfV34V1JR9N+/kowwF16dgc2A18qw71IVcg0DNk9H0Luk74eRjKJ3BSZHxLRK6y47vvjq7/9W+W9LUq+0z37U0qVVfWtX3IzpM2nXtvWy923btGLGjJll3Uc55S0v5Cvzht9JnlL67fXWZe+9duf18W/y7fXW5cOPZgPw4UezWX/db2UZsUp5OscFecuct7zgzPUhb3kbKxfmDcM7JEXfvkDfKorzyj4k6eMGQNIaJO0hy0RiRERcTNKGMQMojEp/CTSpvNGImA38i6SF5Tigf0SUestDldsswSvAVmkbSuXXghrWfQNYSIm99+ny20hau2ja7iT/Dt6Ar/WZ/5GkCP+ApDD/PknP/bAS91WliOgbEV0ioktFRfOV2dQ3jBz1Gh07dqB9+3Y0a9aM7t0P5qEhj5d1H+WUt7yQn8zzF3zBvHnzl339/EuvsNl329N1j10ZNPRJAAYNfZJue+6WZcwq5eUcF8tb5rzlBWeuD3nLW5Ic3vzpVpYGIiLeltSNpPC7Q9IJ1Sz+X+A4SYNJivQ/UvS9lLQrsA/JaPcsYHugHTA+XWQKycj4DsC7wJyidpm/AI+SjMD/rBaHMAXYOX0ay1xgdonrXQm8IOl24A5gDsmHjIMiorpzQETMkXQD0EfSQuBZ4NvAjhFxWxWrDAQuBu6WdAGwXrrPf0XEpKLlngGOTucREVPSNpbDgGNLPK56t2TJEnqfeh6PPHwPTSoq6Nf/PsaPn5h1rOXKW17IT+aPZ39C73MvAWDJ4iX8eN+u7LFrF7butDmnn385/xryGK032oBrLzk346TflJdzXCxvmfOWF5y5PuQtbynqsze8XPTVb94tC5KGkfSRn5K+35SkOB9K0j/97Yg4sNI665AUjT8mKYIvA7oXtiOpE/BnkqegrEvylJK+EXFVuv7qJEXq3un8YyOiXzpPJL3WUyPih7U4js1JngLTmaQnuwPQHnga+E5EfJQu157kNwQ7RcSodFoX4FKS0esmwNvAvyPighL2WwGcRXITZ1uSDyJ3R8Qf0/kBHBERD6bvtwGuT/f1BTAI6J3ewFrY5m+A2yqt14/kxth2hVaWqo6lqn0uT9PV2vgfn33Nghn/yzpCra3Zes+sI5hZTiz+cnq93tjyyRFdy/Zzdr0HhtVLdhfm9jWS1gSmA7+NiIFZ52nMXJhbZS7Mzawxq/fC/GdlLMz/WT+FuVtZDFg28tyS5JnkC4CG95dHzMzMzEqUx1YWF+ZWsDFJW8Y0ktaWZU8akbQxX/WnV2XLiHi33IGy2q+ZmZlZFlyYG5Dc4Mg3H8FYMIPq/2DOjGrmrYys9mtmZmZ5V49PUykXF+ZWo4hYTHJD6CqxXzMzM8u/kh/43ID4OeZmZmZmZg2AR8zNzMzMrPHJ4Yi5C3MzMzMza3TcymJmZmZmZivEI+ZmZmZm1vjkcMTchbmZmZmZNTpuZTEzMzMzW8VIWkPSS5JGSxon6eJ0egdJL0qaJOk+SatVtx0X5mZmZmbW6MTS8r1KsBD4YUR0JvnjiPtL2hW4ErguIjoCnwDHV7cRF+ZmZmZm1ujUZ2Eeibnp22bpK4AfAg+m0/sDh1S3HfeYm2Vk7dXWzDpCrcz5ckHWERq9NVvvmXWEWpv7wm1ZR6i1FruemHUEs5WWt58hqwJJTYCXgY7ALcBk4NP0L5kDTAPaVLcNj5ibmZmZWeMTKttLUi9Jo4pevb6xu4glEbEd0BbYGdiitpE9Ym5mZmZmjU45n8oSEX2BviUu+6mkp4HdgHUlNU1HzdsC06tb1yPmZmZmZmYrQdJ3JK2bfr0m8CPgDeBp4PB0sZ7AoOq24xFzMzMzM2t0Yqnqc3etgP5pn3kFcH9EDJE0HrhX0qXAq8Cd1W3EhbmZmZmZNTr1+QeGImIMsH0V098m6TcviVtZzMzMzMwaAI+Ym5mZmVmjE1GvrSxl4cLczMzMzBqd+mxlKRe3spiZmZmZNQAeMTczMzOzRqeen8pSFi7MzczMzKzRicg6Qe25lcXMzMzMrAHwiLmZmZmZNTp5bGXxiPkqTlI/SUMqf51xpq6SQlLLrLOYmZlZPsVSle1VX1yYW7HewNFZhwCeJ/nTth9nHSRP2rRpxeBH/s6IUY/y/MihnHBSz6wj1Wi/fbsybuyzTBg/nLPOPDnrOCVx5rqzZOlSuv/hOk656i4AIoKb7hvKQb+/kkNOv5qBjw7POOHy5eUcF+QtLzhzXcvjz5DGyK0stkxEfJZ1BoCI+BKYmXWOvFm8eDHnndOHMaPH0aJFc57+338Y9t/neHPCpKyjVamiooIbb7iM/X/8c6ZNe58XRjzCQ0Me54033so62nI5c90aOPR/fLfNBsxdsBCAQc+MYubHnzLo2jOpqKjg48/mZpywank6x5C/vODM9SFvP0NK4Zs/Ldcqt7JI2kvSC5LmSvpM0kuStk7nfVvSPyRNk7RA0jhJx9ZiX9Vt+2utLJKOSZc7QNIESfMlDZb0LUmHS3or3cYASWsW7WOYpNsl3SDpk/R1taSKomUOkzQmPYbZkp6RtGHR/BMkTZL0Zfrf/6t0HCGpl6QHJM2T9LakTH7rMGvWh4wZPQ6AuXPnMfHNybRqtWENa2Vn5522Z/LkKbzzzrssWrSI++8fxE8P2i/rWNVy5roz6+NP+d+rEzi02y7Lpt3/5AhOOOxHVFQk/2S//a0WWcWrVl7OcUHe8oIz14e8/QwphVtZrNGQ1BQYBAwHOgO7ANcDS9JF1gBeAQ4EtgJuAO6QtHcZtl2V1YHTgV8AewNdgH8CPYGfAYekWU6qtN4vSK7z3YATgF7AqWmOjYB7gf5AJ2AvYEBRzkOBm9NsW6fHeKukgyrt44L0eDoD9wF3Sdq4pvNQl9pt3IZtO2/Jy6NGZxmjWq3bbMR702Ysez9t+vu0br1Rholq5sx156q7B/P7o35CRcVXPwCnzfqYx0aM5ufn3sBJV/yVqe9/mGHC5cvLOS7IW15w5vqWh58hjZVbWWx51gHWBR6KiMnptAmFmRExHbi6aPm+kn4I/Bx4amW2vRxNgZMj4k0ASfcAvwc2jIiP0mmDgG7AtUXrvQ/8LiICmCBpc+A04M9Aa6AZ8GBETE2XH1u07hnAgIi4OX0/UdKOwNnAQ0XLDYiIv6cZzifp1d8L+HsNx1Qnmjdfi7sH3sI5Z1/KnDkN81f/ZsWeeWU866/Tgi2/25aR4ycvm/7losWs1qwp/7i8N0++9DoX3vEA/S6q/NnbzMqpMf0MicjfU1lcmFuVImK2pH7AY5KeIim2H4yIdwEkNQH+APQA2pCMaK8GDFvZbS/HwkJRnpoFzCwU5UXTtqy03gtpUV4wArhE0jrAaOBJYKykx9OvH4yIwrBcJ+CuStsbDvy00rQxRce2WNKHwAZVHYSkXiSj9qy52ndYvdk6VR7simratCn9B97CA/cNZsjgx8u67XKbMX0m7dq2Xva+bZtWzJjRsG8tcOa68dqbUxj2yniGvzaBhYsWMW/BQs65+R42/Pa32HvnbQDYe6etufD2+zNOWrU8nONiecsLzlxf8vQzpBSxNOsEtedWFluuiDiWpM3kWZJi9E1JhQa5M0haS64maS3ZDvgPSXG+stuuyuLKmwAWVTGt5Gs6IpYA+6avMcDxwFuSOte0aqX3JeeIiL4R0SUiupS7KAe46dY+THxzErfeXPnzRMMzctRrdOzYgfbt29GsWTO6dz+Yh4Y07B8Ezlw3ev/8xzxxy3kMvelcrvzd0ey0VUf6nHIU3bpszchxyY1no954m01aNcwnqObhHBfLW15w5vqSp58hjZVHzK1aETGaZGT5SklDSXq6HwP2IGlFGQAgScDmwKdl2HY57SJJRaPmuwIzIuLzNEOQjKKPkPQnYBzJbwFGA28A3wfuLNreHsD4Mmcsi11325EjjzqUcWMn8OzzgwG45KJreeLxZzJOVrUlS5bQ+9TzeOThe2hSUUG//vcxfvzErGNVy5nr13E/7ca5N9/D34f+j7XWWI0Lex2RdaQq5e0c5y0vOHN9yNvPkFIszWEriyKPz5KxsklbSlpGxIGVvu5AcrPkYGA68F2SnunbIuJSSdeSFLBHAh8BvyV5BvqrEdG1hn3WtO2uwNPAdyLiI0nHADdHRIuibZwBnBIR7YumXQHsExFd0vfDgB1J2lFuBbYB/gpcGhHXSNoV2Ifkw8AsYPs0x4kR8XdJhwAPkNws+jiwP0lv+mER8VC6jwCOiIgHi3JMSfNeU915WK9Fx1z945vz5YKsI1gDNPeF27KOUGstdj0x6whmK23t1daseaEG5pO5k+q1Un5ziwPK9nP2exOG1kt2j5jb8swnGQF/AGhJUrgOBK5M518KdACGAguAfun8yj3eK7LtchoINAFeJGkxuRO4Lp33GcmI+G9JbkZ9D7ikcCNnRPxH0m9J2nauB6YCJxWKcjMzM7Ny8oi5NVrpiPnYiDgl6yxV8Yi5NQYeMTfLhkfMazZh8x+X7efsFhMf8Yi5mZmZmdmKyOPYswtzK7v0j+tUd4PkljU8GtHMzMxslVNSYS5pd6B98fIRcXcdZbL8m0Hy+MTq5te5mm5CNTMzs8YrlubvqSw1FuaSBgCbAq/x1Z9MD8CFuVUpIhYDk7LOYWZmZquuPD4usZQR8y4krQc57NQxMzMzM8uHUgrzscBGwPt1nMXMzMzMrCyiMY2YS3qIpGVlbWC8pJeAhYX5EfHTuo9nZmZmZlZ7eez1qG7EvNq/WmhmZmZm1lA1qh7ziHgGQNKVEXF28TxJVwLP1HE2MzMzM7NVRkUJy/yoimkHlDuImZmZmVm5RKhsr/pSXY/5icBJwKaSxhTNWht4vq6DmZmZmZmtqMbWY34PMBToA/yhaPqciJhdp6nMzMzMzFYx1fWYfwZ8JunsSrNaSGrhP6lutnLmfLkg6whmK63FridmHaHW5r3xz6wj1Mq6W/fIOkKjt2jJ4qwj1Jp/htSsUd38WeRhkscmClgD6AC8CWxVh7nMzMzMzFZYo3qOeUFEbFP8XtIOJL3nZmZmZmZWJqWMmH9NRLwiaZe6CGNmZmZmVg6NspVF0mlFbyuAHYAZdZbIzMzMzGwl5fChLCWNmK9d9PVikp7zfN05Y2ZmZmbWwFVbmEtqAqwdEWfUUx4zMzMzs5XWqFpZJDWNiMWSvl+fgczMzMzMVlZjeyrLSyT95K9JGgw8AMwrzIyIf9VxNjMzMzOzVUYpPeZrAB8DP+Sr55kH4MLczMzMzBqkpVkHWAHVFeYbpE9kGctXBXlBHm90NTMzM7NVRNC4WlmaAC2gyqNyYW5mZmZmVkbVFebvR8Sf6i2JmZmZmVmZLM3hMHJ1hXn+xv/NzMzMzIClOSxlK6qZt3e9pTArIikkHZ51DjMzM7P6tNzCPCJm12cQsyKtgIeyDpFH++3blXFjn2XC+OGcdebJWcepUd7ygjPXhzzlXbJkKd1POZ9TLvwzAC+8No7uv72AI045n55nXMq7M2ZlnLBqt99+NVOnvsyoUY9nHaVkecycp2sZ8pe3JoHK9qov1Y2Y2ypGUlNJmf/eJyJmRsTCrHPkTUVFBTfecBkHHnQ023TuRo8eh9Cp02ZZx1quvOUFZ64Pecs7cNDjdGjXetn7y27uzxVn/oYHbr6EA7ruRt97B2eYbvkGDHiAgw/umXWMWslb5rxdy3nLW4qlZXzVFxfmOSFpmKTbJF0rabakDyX1lrS6pFskfSrpXUm/LFrnCklvSlogaYqkqyStUTT/IkljJR0jaTKwEGguaXNJz0j6Il3/x5LmSjqmaN02ku6V9En6elhSSf+CJbWTNCg9jvmSJkg6smj+slYWSe3T90emmRZIelXStpK2lvS8pHmShkvqUMWx/To9Lwsk/UdSy6JltpH0lKTP0+MbLalb0fy9JL2YnodZkq6TtFql78mtki6X9JGkDyRdIymTf1c777Q9kydP4Z133mXRokXcf/8gfnrQfllEKUne8oIz14c85Z350WyeHTmaw/b7wVcTJebOXwDA3Hnz+c7662aUrnrPPfcSs2d/mnWMWslb5jxdy5C/vI2VC/N8+QUwB9gFuAK4HvgPMBHoAvQH/iqpVbr8POA4oBNwEnAk8MdK2+wAHAUcAXQGvgT+DSwGdgWOAS4EVi+sIGkt4GngC+AHwG7A+8CT6bya3AqsBXQDtgJOBWr6v+3FwJXA9umy/wBuSo9nZ5I/hHVjpXXaA0cDBwP7AJsBdxXNvyfNvTOwHXBRekxIagMMBV5N93k88HOgT6V9/ILkXO0OnJIeS48ajqVOtG6zEe9Nm7Hs/bTp79O69UZZRClJ3vKCM9eHPOW96o6BnHZcdyoqvvpF40W9j+PkC69ln1+eypD/Ps/x3Q/MMKFlKU/XMuQvbyncymJ1bVxEXBQRbwF/Bj4CFkXEDRExCfgTydN0vg8QEZdExHMRMSUiHgEuJykui60G/DIiXomIsSTF8veAX0XEaxExAvg9X3+Cz5Hpfo6NiDERMQE4geS596X8FNoEGB4RoyPinYh4NCIerWGdP0fEI+m+rgW2BG6KiKcjYhxwc5q92JrpcbwaEc+lGQ8qGtnfBHgiIiZExKSI+Hd6vJB8kJkBnBQRb0TEEOAPwCmVPnyMj4gLImJiRNxP8oHFN06bNXLPvPga66+7Dltu1uFr0//+n8e45eLTeXLA9Rz8oz25uu89GSU0szy2slT3uERreMYUvoiIkPQB8HrRtEWSPgE2AEjbQU4FOpIUzU3SV7FpEVF8d9IWwIyImF40bSRfvy53JBlpn1OpJX0tYNMSjuMG4HZJ+wNPAf+OiJdrWGdM0deFvK9XmtZc0loRMT+dNj0i3i1a5sX0ODoBhQ83f5XUM83xz7TwJ13mhYgoPu7hJB9kOhblKc4FSTG/wfIOQlIvoBeAmnyLiormy1u01mZMn0m7tl/1urZt04oZM2aWbfvllre84Mz1IS95Xxs/kWEvvMrwkWNYuGgR8+Yv4OQL/8w7781g2y2S/w3uv9cunHj+NRkntazk5VouyFvexsoj5vmyqNL7WM60Ckm7AvcCjwEHkbRjnAc0q7T8vBXIUQG8RtL+UfzaHLijppUj4k6Swv5v6TrPS7qohtWKjzOqmVbyNR0RF5GMvP+HpBVljKTjSll1ObkK86p72lHfiOgSEV3KWZQDjBz1Gh07dqB9+3Y0a9aM7t0P5qEhDffpBXnLC85cH/KSt/ex3XlywPU82u9arjr7RHbethM3XNCbufMXMGVaUsyMeHXs124MtVVLXq7lgrzlLYVHzK0h+T7JiPElhQmSNilhvQlAa0mtI6LQbNaFrxebr5C0xHwUESt0J05ETAP6An0lnQ30JunxLqc2ktpFxHvp+51JjuONohxvkYye3yjpNuDXJH3obwDdJVUUjZrvQdKDP7nMOctiyZIl9D71PB55+B6aVFTQr/99jB8/MetYy5W3vODM9SFveYs1bdKEC393LKdddhMVFWKdFs3506nHZx2rSv3738iee+5Gy5brMWnSC1xyyXX0739f1rGqlbfMebuW85a3FPXZG14uisjh3ytdBUkaBoyNiFOKpo0FHkxHfgvTZgKXAlNJbuLsCYwA9iPpQW8ZEUqXvQg4PCK2Llq/gqRFZAZwBkmf9nUkxfmvI6J/2mP9KjATuAB4F2hHcpPl7WmxW92x3EByY+VEYJ10+0siYp90fgBHRMSDktoD7wA7RcSodH4XkvaaDhExJZ22f7rNtSNibnpsZ/D/7N13vBTl9cfxz7kXNIoFERtoBJVEjCX2rhh7gmKFqKBRE2woxq4RwYKxYEeD/KIBURMxFhRN7NhiQ0VEIIgKCohKsNBUyvn98TwLw3gr7t3ZuXzfvObF3ZnZ2bPPnbt75pkzz8DrwFnxfQwEJrt7RzNbCegH3A9MAtYB/gq85u6/jxd/TgCGEEpvNgLuAO5x97Nr+J0Mim1ca619kxVa649PJANzxj2QdQj10nzzTK4nX67MX7gg6xCWCwu+n1rSTPmxdY4q2vfsbz77e0liVylLI+XujwLXEkZuGQ3sS0iia3veIuBQwigsrxNGeulLKNH4Nq4zF9gD+JCQ2I6P660BfFmH8CoII6qMBZ4i1Ic3xOC0kwjlPI8CzxLiPT4uW0iIdxDwX8JBzCuEJJ5YY38goQRoFKEX/e/ARQ0Qp4iIiBTZIiveVCrqMZdamdlWhOR0uzpcpFkWqjobUG7UYy6SDfWYS5p6zEuj1D3mw9Y9umjfs52m31uS2FVjLj9gZocSLgp9nzAW+PXAO4TachERERFpACplkaqsShgXfCxwD+FCyP29jqdXzOy9eCfNqqZjGjBuERERESDU4BZrKhX1mMsPuPtdwF0/YhO/5ofDMhZ8Vs38oooXxPYpxWuJiIhI+SnlMIfFosRcis7dJ2cdg4iIiEjeKDEXERERkUZnkeVvHHMl5iIiIiLS6ORx6DNd/CkiIiIiUgbUYy4iIiIijY4u/hQRERERKQOlvGNnsaiURURERESkDCgxFxEREZFGZxFWtKk2ZraBmT1nZmPjjRZ706PIEgAAIABJREFUxvktzOwpM3s//r9GTdtRYi4iIiIijU6J7/y5ADjb3TcDdgJOM7PNgAuAZ9y9HfBMfFwt1ZiLiMgya1qZv6+RZu0PzzqEepkz7oGsQ6i3vLWxyI/l7p8Cn8afZ5nZOKA10AnoEFcbDIwAzq9uO/n7RBURERERqUUxL/40s+5A98Ssge4+sJp12wBbA68B68SkHWA6sE5Nr6PEXEREREQanWIOlxiT8CoT8SQzWwV4ADjT3b+xxN1H3d3NrMbKGNWYi4iIiIj8SGbWlJCU3+PuD8bZn5nZenH5esDnNW1DibmIiIiINDqlvPjTQtf4HcA4d78+segR4Lj483HAsJq2o1IWEREREWl0SnyDoV2BbsC7ZjYqzrsIuAoYamYnApOBzjVtRIm5iIiIiMiP4O4vQbUDnu9d1+0oMRcRERGRRqeYF3+WihJzEREREWl0lJiLiIiIiJQBL22NeVFoVBYRERERkTKgHnMRERERaXRUyiIiIiIiUgbymJirlEVEREREpAwoMV8GZuZmdkRVj82sTXy8XXYRNg7pdhYRERGpq1Le+bNYVMqybNYDvsw6CCkOMxsEtHT3jlnHIiIiIsVR4jt/FoV6zJeBu0939++yjkMkbf/9OvDemBcYP/Ylzjv3tKzDqVXe4gXFXAoDBlzL5MlvMnLkk1mHUmd5aeOFCxfRuUcvevS+HoBXR71H59Mv4cgevTjunCv4eNpnGUdYvby0cVLeYs5bvI3Rcp+Ym9kIM/uLmV1nZjPN7Asz62lmK5rZrWb2lZl9bGbdEs+pS4nFhmb2lJnNNbOxZrZv6nX3MLPXzOxbM/vMzG4wsxVScfVPPWeQmQ1PbeNVM5ttZl+b2etmtnli+S5m9nyMYWp8n6vVoU26x5gqU/PvNbNH4s8bm9kwM5tuZnPM7C0z65haf5KZXWxmt5vZN2Y2xczOre31U1qY2f3xNT40s66p19jCzJ42s3nx9zfIzFavrs3ivD5mNqbwM3Ac8Jv4e3Uz6xCXtTazf5jZl3F6zMzapbdjZr81sw/MbJaZPWxmLev5HouioqKCm2/qS8eDurLFVnvRpcshtG/frvYnZiRv8YJiLpUhQ+6nU6fjsg6jzvLUxvcMe5K2G7Ra/Lhv/8Fcde7J3N//cg7ssDMD//FIhtFVL09tXJC3mPMWb10sKuJUKst9Yh4dA8wCdgSuAm4EHgYmANsBg4G/mtl69dhmX+BmYCvgDeAfZrYKhIQP+BfwNrA1cCJwFPDnum7czJoAw4CX4mvsGONeGJdvATwJPBKXHwb8ErizDpu/H1gdWHwwEWPvBNwdZ60S38O+cfsPAA+a2aapbf0ReBfYBrgauMbMdq7r+wQuie9zK+A+4E4z+2mMqRnwBDAb2AE4FNilju+xoB8wFHiaUKK0HvAfM1sZeA74FtgT2Bn4FHg6LitoA3SJr70f4ffZtx6vXzQ7bL81H3wwiY8++pj58+czdOgwDj5o/yxCqZO8xQuKuVRefvl1Zs78Kusw6iwvbTx9xkxeeOMdDtt/zyUzzZg9dx4As+fMZa0WzTOKrmZ5aeOkvMWct3jrQol5fr3n7n3c/X3gemAGMN/db3L3icBlgAG71mObN7j7o3GbFwEtCIkxwKnANOBUdx/n7sOBC4AeqaSvJqsBzYFH3f0Ddx/v7ve6+7i4/FzgPne/zt3fd/fXgFOAw81s7Zo27O5fAo8TDlgKDgEWEBJ93P0ddx/g7u+6+0R37wu8BaTPJDzp7v3jOrcAE4G96/geAYa4+93x99ArxrBHXHY00AzoFuN4HugOHGZmm9Rl4+4+G5gHfBdLlKa7+/fAbwm/8+PdfbS7jwdOIhyQJM8MNAF+F9d5BRhYz/dXNK1ar8snU6Ytfjxl6qe0arVuFqHUSd7iBcUsVctLG19z+z2cdUJnKiqWFN726XkCp/W+jn26ncnwZ//DiZ3L81KbvLRxUt5izlu8jZUS82B04Qd3d+BzQi9vYd58wsWeNSa01W2TkISTeH574FV3Tx6EvQSsANQ1oZwJDAKeiCUWZxV6kqNtga6xzGW2mc0GXo7LNq7DS9wNHJI4UDgGeMDdv4XQW21m18QynS/j9rcDfprazujU42ksYzu6+wLgC5Zux9HuPiux/n8IB7eb1eM1qrIt0BaYlWi/r4E1WLr9Jrv714nHNb6/WCY00sxGLlo050eGKCJSN8+/NooWzVdjs3Ztl5p/98NPcOulZ/P0kBvptO/uXDvw3owiFCk+jcqSX/NTj72aefU5kFn8fHd3M6OOzy/8/hcRemyTmi61ovvxZnYjcABwMNDXzA5x9yfia/0VuKGK15hahzgeI/ROdzKzZ4B9gOQ5rX7xdc8B3gfmAncRDi6SitaO9Xx+nduxGhXAKELPedrMZY3P3QcSetVpskLrov6tT5s6nQ3WX1I7un7r9Zg2bXoxX6Ko8hYvKGapWh7aeNTYCYx49W1eemM0382fz5y58zit9/V89Mk0ttw09DUcsMeOnNKrX8aRVi0PbZyWt5jzFm9daFQWqatxwE5mlmz/3YDvgQ/i4y8I9c5JW6U3FEtKrnb3DsAIwoWMEMpKfhFLSNLTvNoCjKPO3E/oKe8CTI/bT8Z7l7s/4O6jgSnUrSe+mMYBW5jZqol5uxD260JJT1Xt+MvU4++BytS8twhnL2ZU0X4zKUNvjBzFJpu0pU2bDWjatCmdO3fi0eHlO6pF3uIFxSxVy0Mb9zy+M08PuZF/D7qOa84/hR22bM9Nl/Rk9tx5TJoSkq9X3h6z1IWh5SQPbZyWt5jzFm9jpR7zbNwGnAncZmY3ARsRLjrt7+5z4zrPAjea2cHAfwn1zRsAkwDMrG2c9wihB3wjYEvgL/H5VwOvmtkA4HbCxa2bAge5+0l1jPNu4BlCScffU6U3E4BDzWwYode4N/CTerRBMdwDXArcZWaXEMpMbgcejDXpENrxPDM7AXiBcBHsroQDiYJJwIFm9nPgf4SSlXsIZwOGxW1/TGj/TsCAeO1AWVm4cCE9z7yYxx+7l8qKCgYNvo+xYydkHVa18hYvKOZSGTz4ZnbffWdatlyDiRNf5fLLb2Dw4PuyDqtaeWxjgCaVlfQ+43jO6nsLFRXGaqs047IzT8w6rCrlsY3zFnPe4q2LUl60WSwWSqqXX2Y2Ahjj7j0S88YA/3T3Pol504Er3L2/mTlwpLv/My5b/NjM2gAfAdu7+8jE89PP2QO4ltB7+xVwL3BBYXx0M2tKGGWlS9zErcCGxBvhmNk6hCR8R6Al8BnwD+BPsSYeC3cfvYLQi1wJfAg85O6X1LFtLL6XDYGtYs94YdmGwB2E0Uq+jLF2IPQw/y6uM4lwsNEv8bwftHcNr79Um1W1zTj6zI3xPX5LGMGlZ7LuOw6JeBKwMiHh/go42N03j8vXivN3JlzcuZe7j4htfBXwG8IoNdMII7Wc5+4z4naPKGwnbut3Mb5Vant/xS5lEclC08r89e/MX7gg6xDqZc64B7IOod6atT886xCkDC34fmpJi0v+vGHXon3PXjj57pLEvtwn5iJZUWIujYES84anxFwaCyXmtcvfJ6qIiIiISC0WlXQ8leJQYr4cisMqjq1hlc3c/eMGjuEYQj14VSa7+y8a8vVFRESkcctjjbkS8+XTNH44Mkl6eUN7BHitmmXpIQhFREREGj0l5suheKOeibWu2LAxzCKMFCMiIiJSdPkrZFFiLiIiIiKNUB5LWXSDIRERERGRMqAecxERERFpdBaVdHDG4lBiLiIiIiKNTh6HS1Qpi4iIiIhIGVCPuYiIiIg0OvnrL1diLiIiIiKNkEZlERERERGRZaIecxERERFpdPJ48acScxGpk6aV+fu4mL9wQdYhiPxozdofnnUI9TZn3ANZh1AveWxjqV3+0nKVsoiIiIiIlIX8dYGJiIiIiNQijxd/KjEXERERkUYnjzXmKmURERERESkD6jEXERERkUYnf/3lSsxFREREpBHKY425SllERERERMqAesxFREREpNHxHBazKDEXERERkUZHpSwiIiIiIrJM1GMuIiIiIo1OHscxV2IuIiIiIo1O/tJylbKILGZmfcxsTD2f42Z2REPFJCIiIssP9ZiLiIiISKOTx1IW9ZiLNCL779eB98a8wPixL3HeuadlHU6tBgy4lsmT32TkyCezDqXO8tbGkL+YtV80vDzFu3DhIjr36EWP3tcD8Oqo9+h8+iUc2aMXx51zBR9P+yzjCKuXp3aG/MVbm0VFnEpFiflyzsxGmNlfzOw6M5tpZl+YWU8zW9HMbjWzr8zsYzPrlnjOFmb2tJnNi88ZZGarp7Z7vJmNNbNvzWyCmf3RzOq0v5nZSfE535rZDDN7wsyamFmbWDqSniZZMNHMzkltq11cZ5uatl1NHNub2ZNxvW/M7CUz27mW2M+P6+9Ul/daTBUVFdx8U186HtSVLbbaiy5dDqF9+3alDqNehgy5n06djss6jDrLYxvnMWbtFw0rb/HeM+xJ2m7QavHjvv0Hc9W5J3N//8s5sMPODPzHIxlGV728tXPe4m2slJgLwDHALGBH4CrgRuBhYAKwHTAY+KuZrWdmzYAngNnADsChwC7AnYWNmdkfgCuBS4D2wNnA+cCptQViZtsBtwKXAj8H9gb+HRd/AqyXmH4GTAZGuLsDdwDHpzZ5AjDK3d+qZdtVWRUYAuwe3+so4HEzW7OKuM3M+gGnA3u6+6u1vddi22H7rfngg0l89NHHzJ8/n6FDh3HwQfuXOox6efnl15k586usw6izPLZxHmPWftGw8hTv9BkzeeGNdzhs/z2XzDRj9tx5AMyeM5e1WjTPKLqa5amdIX/x1oUX8V+pKDEXgPfcvY+7vw9cD8wA5rv7Te4+EbgMMGBX4GigGdDN3d919+eB7sBhZrZJ3F4v4Dx3/6e7f+TujxIS/loTc+CnwBzgEXef7O7vuPsN7r7A3Re6+3R3nw58DtwAfAqcHJ/7N+Bnhd5qM6sEjiUk7DVuu6pA3P1Zdx/i7uPcfTwh6f4WODC1aiXhwORgYFd3f68O77PoWrVel0+mTFv8eMrUT2nVat0sQmm08tjGeYw5b/LWxnmK95rb7+GsEzpTUWGL5/XpeQKn9b6OfbqdyfBn/8OJnTtmGGH18tTOkL9460KlLJJXows/xJ7nz4F3E/PmA18CaxN6wEe7+6zE8/9D2G83M7O1gA2A281sdmEiJOYb1yGWpwi94B+Z2T1mdpyZrVrFelcDWwKHuPu3Mc7pwHBCLznAAUAL4J56bhsAM1vbzG6PpS9fE84qrE1I8JP6AR2A3dx9ck1vzsy6m9lIMxu5aNGcmlYVEVmuPf/aKFo0X43N2rVdav7dDz/BrZeezdNDbqTTvrtz7cB7M4pQpPg0KosAzE899mrm1XYgl1znZELCXi/uPivWg+8B7AtcCFxpZtu7+zQAMzsubn83d09f9fNX4F4zO5OQoD/k7l/Wddspg4F1gD8Ck4DvgGeAFVLrPQUcBfwaGFTL+xsIDARoskLrop4bmzZ1Ohusv6QOc/3W6zFt2vRivsRyL49tnMeY8yZvbZyXeEeNncCIV9/mpTdG8938+cyZO4/Tel/PR59MY8tNQz/PAXvsyCm9+mUcadXy0s4FeYu3LkpZglIs6jGX+hoHbJHqad6FsC+Ni4nyNGBjd5+YnuryArFs5Vl3v5DQK94M6AhgZrsAfwG6uvs7VTz938A3hMT9IBK177Vtuwq7Abe4+2OxPGUWobY97XHgSOAv8aAhE2+MHMUmm7SlTZsNaNq0KZ07d+LR4fkZ1SIP8tjGeYw5b/LWxnmJt+fxnXl6yI38e9B1XHP+KeywZXtuuqQns+fOY9KUkDC+8vaYpS4MLSd5aeeCvMVbF3ksZVGPudTXPYSLJ+8ys0uANYDbgQcTiXdv4BYz+4qQtDYFtgFau/ufa9q4mXUklLy8AMwE9iJchDnOzNYFHgJuA16LjwEWuvsXAO6+0MzuBP4MTCX0cNe67WrCmQB0NbPXCAn8NcD3Va3o7sPN7EjgfjNzd7+rpvfZEBYuXEjPMy/m8cfupbKigkGD72Ps2AmlDqNeBg++md1335mWLddg4sRXufzyGxg8+L6sw6pWHts4jzFrv2hYeYs3qUllJb3POJ6z+t5CRYWx2irNuOzME7MOq0p5a+e8xdtYWSgpluWVmY0Axrh7j8S8McA/3b1PYt504Ap3729mWxBGbtmFcDHkMKCnu3+dWP8o4FxgM2Ae8B7Q393/UUs8uwGXE3qzVwY+AK5z97+ZWQfguSqeNtnd2yS2sSGh9KS3u19Wl23H5X2AI9x98/h4K0LZyZaEswB9CKPLLG4bM3PgSHf/Z3x8EDAUOKm25LzYpSwNrWll/o7j5y+s8rpeKSLtF1KVOeMeyDqEemnW/vCsQ1guLPh+qtW+VvF02/Cwon3PDpn8YEliV2IujY6Z7Qi8DGzk7h9nHU91lJg3PCVgDU/7hVRFiblUpdSJedciJuZ3lygxz98nqkg1zGxFYC1Cr/hD5ZyUi4iISMNapIs/RWpmZsckh1FMTT92/O+jCMMhtgTO+vHRioiIiJSOesyl1B4BXqtmWXqIxnpx90HUMlyhiIiILB/yOFyiEnMpqXhjolm1rigiIiLyI5RymMNiUSmLiIiIiEgZUI+5iIiIiDQ6ebz4U4m5iIiIiDQ6eawxVymLiIiIiEgZUI+5iIiIiDQ6ebz4U4m5iIiIiDQ6eby7vUpZRERERER+BDO708w+N7MxiXktzOwpM3s//r9GbdtRYi4iIiIijc4ivGhTHQwCDkjNuwB4xt3bAc/ExzVSYi4iIiIijc6iIk61cfcXgJmp2Z2AwfHnwcAhtW1HNeYiUifzFy7IOgQpQ3ncL5pW5uurL49t3Kz94VmHUC9zxj2QdQj1lrc2zjsz6w50T8wa6O4Da3naOu7+afx5OrBOba+Tr08nEREREZE6KOY45jEJry0Rr+n5bma1BqTEXEREREQanTK48+dnZraeu39qZusBn9f2BNWYi4iIiIgU3yPAcfHn44BhtT1BPeYiIiIi0uiUchxzM/s70AFoaWZTgN7AVcBQMzsRmAx0rm07SsxFREREpNEp5Z0/3f2oahbtXZ/tqJRFRERERKQMqMdcRERERBqdYo7KUipKzEVERESk0SmDUVnqTaUsIiIiIiJlQD3mIiIiItLolHJUlmJRYi4iIiIijY5KWUREREREZJkoMZeiMrPtzMzNrE0d1+9kZu+b2QIzG2RmHeLzWzZspGBmY8ysT0O/joiIiJSeF/FfqaiURbJ2B/BX4BZgNrB1tuGIiIhIY7AohzXm6jGXzJhZc2BN4Al3n+ruX2cdU32YWYWZVWYdR9L++3XgvTEvMH7sS5x37mlZh1OrvMULirkU8hbvgAHXMnnym4wc+WTWodRZ3toY8hPzwoWL6NyjFz16Xw/Aq6Peo/Ppl3Bkj14cd84VfDzts4wjrF5e2rgxU2K+HDOzEWZ2m5ldaWYzzOxzM+tnZhVx+QpmdrWZTTGzuWb2hpntn9rGAWY23sy+NbMXgZ/V8bU7AF/Gh8/G8pUOVay3ppn9PcYwz8zeM7Pj6/M+4jprm9mwuI3JZnZCFa+1upkNjM+fZWbPm9l2ieW/M7PZZvZrMxsDfA+0N7MtzOwZM/smLn/HzPaqSzsUU0VFBTff1JeOB3Vli632okuXQ2jfvl2pw6izvMULirkU8hYvwJAh99Op03FZh1FneWzjPMV8z7AnabtBq8WP+/YfzFXnnsz9/S/nwA47M/Afj2QYXfXy1MZ15UWcSkWJuRwDLAB2AXoAZwJd4rK/AXsCRwObA4OBR81sKwAz2wB4GHgK+CWhHOWaOr7uf4BfxJ8PB9aL89J+ArwFdIzr3wTcbmZ71+N9AAwCNgH2AQ4BjgXaFBaamQGPAa3ja20NvEA4aFgvFU8v4CRgM2AycC/wKbADoR36AN/W3gTFtcP2W/PBB5P46KOPmT9/PkOHDuPgg/av/YkZyVu8oJhLIW/xArz88uvMnPlV1mHUWR7bOC8xT58xkxfeeIfD9t9zyUwzZs+dB8DsOXNZq0XzjKKrWV7auD4W4UWbSkWJuYx190vcfYK7DwWeA/Y2s42Bo4DO7v6Cu3/o7v2BxwlJKcApwMfAGe4+Pj5/QF1e1N2/Bz6PD2e6+/Q4L73eVHe/1t1HxRgGAg/G2Gp9HwBm9jPgQKC7u7/s7m8DxwErJZ6/FyGpPsLdX3f3ie7eC/gQ6JZYrxLoEbczwd1nARsCT8U2mOjuD7n7K3Vph2Jq1XpdPpkybfHjKVM/pVWrdUsdRp3lLV5QzKWQt3jzKI9tnJeYr7n9Hs46oTMVFbZ4Xp+eJ3Ba7+vYp9uZDH/2P5zYuWOGEVYvL23c2Ckxl9Gpx9OAtYFtAAPGxvKM2WY2G/gNsHFctz3wqi89gn9RE1IzqzSzP5nZaDP7X4zhMOCndXwfhTgXAa8XFrr75LhOwbbAysAXqfe7OUveL4Re+VGp17oe+KuZPRtj3bSG99PdzEaa2chFi+bU9NZFRCRHnn9tFC2ar8Zm7douNf/uh5/g1kvP5ukhN9Jp3925duC9GUW4/Mljj7lGZZH5qcdOOGCriD9vX8U680oQV8E5wNlAT+BdwsgtV7Ik6S6o7n2k51WnAvgM2L2KZd8kfv7O3RcutVH3PmZ2D6FXfn+gt5md7O53pjcUe/wHAjRZoXVR/9KnTZ3OBusvqWtcv/V6TJs2vZgvUVR5ixcUcynkLd48ymMb5yHmUWMnMOLVt3npjdF8N38+c+bO47Te1/PRJ9PYctPQv3PAHjtySq9+GUdatTy0cX3l8c6f6jGX6rxN6DFfN5ZnJKepcZ1xwI6xPrtgpyLHsRvwqLsPcfdRwAfU8QLThPGEfX2Hwgwz+ynQKrHOW8A6wKIq3u/n1MLd33f3m939N4QhIH9fzxh/tDdGjmKTTdrSps0GNG3alM6dO/Ho8PIdJSJv8YJiLoW8xZtHeWzjPMTc8/jOPD3kRv496DquOf8UdtiyPTdd0pPZc+cxaUpIcF95e8xSF4aWkzy08fJAPeZSJXefEHuBB5nZ2YTEtQXQAfjQ3R8k1JOfDdxoZrcBWwAnFzmUCUAXM9sNmAGcDrQlHDjUibv/18z+TbhotDuhx/96lu75fxp4GRhmZucRkvl1gQOAp939xaq2bWYrAf2A+4FJhOR+N+C1erzHoli4cCE9z7yYxx+7l8qKCgYNvo+xYyeUOow6y1u8oJhLIW/xAgwefDO7774zLVuuwcSJr3L55TcwePB9WYdVrTy2cR5jBmhSWUnvM47nrL63UFFhrLZKMy4788Ssw6pSXtu4JqUsQSkWy2M3vxSHmY0Axrh7j8S8QUBLd+9oZk2BPxFGMFkfmEmo077U3d+M6/+GkORuCLwJ3AbcDbR190m1vH5L4AtgL3cfEed1IFy4uZa7zzCzNQg90PsSEulBwCrAZu7eoS7vIz5eB/i/uJ0ZwKWEkVv+6e594jqrAlcQRolZm1Da8jLwJ3f/wMx+B/R391USr7NCjGkXwsgy/wOGA+e4e7IE5geKXcoiInXTtDJffVLzFy7IOoRGb864B7IOod6atT886xDqbcH3U632tYpn+1Z7FO179o1pL5QkdiXmIhlRYi6SDSXmkqbEvDSUmNcuX59OIiIiIiJ1kMfOZ138KQ3GzP6VHHowNV2UdXwiIiLSeGm4RJGl/Z6lb+KTNLOUgYiIiIiUOyXm0mASwyqKiIiIlFQeS1mUmIuIiIhIo5PH4RJVYy4iIiIiUgbUYy4iIiIijY7nsMdcibmIiIiINDqLclhjrlIWEREREZEyoB5zEREREWl0VMoiIiIiIlIGVMoiIiIiIiLLRD3mIiIiItLoqJRFRESkzM1fuCDrEKTMNGt/eNYh1Nu8aS9mHULZUymLiIiIiIgsE/WYi4iIiEijo1IWEREREZEykMdSFiXmIiIiItLo5LHHXDXmIiIiIiJlQD3mIiIiItLouC/KOoR6U2IuIiIiIo3OIpWyiIiIiIjIslCPuYiIiIg0Oq5RWUREREREsqdSFhERERERWSbqMRcRERGRRiePpSzqMc85M3MzO6KI2+tjZmOKtb3EdosSp5mNMLP+NSxvkPhFREQkXxa5F20qFSXm+bce8GgRt9cP2LOI2yu1vMcvIiIiyykl5jllZisAuPt0d/+uWNt199nu/r9iba/Uyil+M2ta6tfcf78OvDfmBcaPfYnzzj2t1C9fb3mLFxRzKeQtXshfzHmLFxRzQ9nv8OM4tNspHH7caXQ+4QwAvv5mFr/veRG/7nIiv+95EV9/MyvjKJeNF/FfqSgxLxOxRGOAmd1kZl/G6Vozq4jLJ8UyjTvN7Cvgnjh/cYmImbWJjw83s6fMbK6ZjTWzfVOvtamZPWJmX5vZbDN7xcy2iMuWKgUxs0FmNtzMLjazz+L6fzOzlRLrHGBmL8aYZ5rZE2bW/ke0xSVmNtnMvjOz6WZ2Vw3r7m1mX5nZybXE39PMpsYY/2ZmK6fa/jYzu9LMZpjZ52bWr9D2cZ0VzOxqM5sS2/UNM9s/sbxDbPtfm9nrZvY9sHh5KVRUVHDzTX3peFBXtthqL7p0OYT27duVMoR6yVu8oJhLIW/xQv5izlu8oJgb2p23XMUDg29l6J03A/DXIUPZabtf8vh9d7DTdr/kjruHZhzhsnH3ok2losS8vBxD+J3sDJwEdAfOTCw/CxgPbAdcVMN2+gI3A1sBbwD/MLNVAMysFfAS4MC+wDbArUBlDdvbM25rb+BwYD/g6sTyZsCNwA5AB+Br4NFCr359mNnhwDnAqUA7oCPwejXrHgE8BHR39wE1bHZ3YHNgH6ALcCjQM7XOMcACYBegB6HduySW/43QDkfHbQ0mvMetUtu5GrgY2BR4rYaYim6H7beZezonAAAgAElEQVTmgw8m8dFHHzN//nyGDh3GwQeV9NigXvIWLyjmUshbvJC/mPMWLyjmUnvuxVfodOA+AHQ6cB+efeGVjCNafigxLy+fAme4+3h3HwpcS0jGC55392vcfaK7v1/Ddm5w90fjOhcBLYBfxmWnAXOAI939dXef4O53u/uoGra3EDje3ce4+xPA+cBJZtYMwN0fiNP77j4aOB5oS0jU62tDQjs86e4fu/tId//BxZ5m1h24AzgitlVNvgFOdvdx7v4kcD/hICNprLtfEttjKPBcYR0z2xg4Cujs7i+4+4cxpscJB1BJfdz9ybjOF/V76z9Oq9br8smUaYsfT5n6Ka1arVvKEOolb/GCYi6FvMUL+Ys5b/GCYm5IZkb3P/6Jzieczv3DHgfgf19+xVotWwDQcs01+N+XX2UZ4jJbhBdtKhUNl1heXvWlz5e8AlxuZqvFxyPruJ3RiZ8Lnwprx/+3Bl5y9+/rEddod5+dimsFYGNgdExcLwd2BNYiHPBVAD+tx2sU3E/ozf7IzJ4A/g08kqqjP4SQEO/h7nU5jB/r7gsTj6fFWJNGpx5PY0mbbQMYMNbMkuusCDybel6Nv6N4QNEdwCpXp6KiWa3Bi4iINJS7/tKPddZqyf++/Io/nHkRbTfcYKnlZkbquy83NFyiNLQ5dVxvfuGHRKLfkL/r4YSE/CRCwrs1oSyk3qUs7v4J8PO4rW+A64A3C73z0TuEXvUTrW6fFvNTj50ftkdN61TEx9sTzjwUpvbACann1fg7cveB7r6du29X7KR82tTpbLB+q8WP12+9HtOmTS/qaxRT3uIFxVwKeYsX8hdz3uIFxdyQ1lmrJQBrrtGcvffYhXfH/pc112jOFzNmAvDFjJm0aL56liEuV5SYl5cdU4nmTsA0d/+miK/xNrBbPeu/t0glxjsB3wMfmNmahHrqK939aXcfB6zKjzgb4+7fuvtj7v5HQjL8C2DXxCofEWrZ9wMG1jE5/zHeJvSYrxvLiJLT1AZ+7Tp7Y+QoNtmkLW3abEDTpk3p3LkTjw5/MuuwqpW3eEExl0Le4oX8xZy3eEExN5S5875lzpy5i3/+z+tv0W6jNnTYbSeG/etpAIb962n22n3nLMNcZnkcx1ylLOWlFXCjmd0GbAGcC1xR5Ne4DTgZGGpmfYEvCcnvuBrqzJsAd5rZZTHGq4D/c/c5ZjYPmAH8wcw+AVoTauMXLEtwZva7+HqvAbMJF2DOB5aqqXf3D81sL2AEcLuZneQNdM7K3SeY2T3AIDM7G3iLULffAfjQ3R9siNetr4ULF9LzzIt5/LF7qayoYNDg+xg7dkLWYVUrb/GCYi6FvMUL+Ys5b/GCYm4o/5v5JT0vuhyAhQsW8uv9OrDbTtuxefufcXavK3lw+BO0Wndtrru8pvEmylceS1ksj0E3RmY2gjDiygKgK6F04k7gPHdfaGaTgP7u3i/1PCdcyPlPM2tD6E3e3t1HVrVOfPwLQvK8R3yddwkjm4wxsz6ECyo3j+sOAloSRkbpAawMPACc4u5z4zq/IowCswkwETg7rtPD3QdVFUMN7XAI4eLS9kBTYCxwqbsPT7TTGHfvER9vTEjO/0Uof+ldVfzu3jHxGun3uNQ2q3qehTHJ/wQcC6wPzIxtcqm7v2lmHQgXjK7l7jNqeo8FTVZorT8+ERFZJvOmvZh1CPXWtOVGJS1WX2OVTYr2Pfvl7IkliV2JeZmoKjksB1UltlIcSsxFRGRZKTGv3eqrbFy079mvZ39QkthVyiIiIiIijU4eO5918aeUlJldFO8eWtX0r6zjExEREcmKeszLhLt3yDqGqrj774q8yQFAdTcEmlfk1xIREZHlVClHUykWJeZSUu4+k3DhpIiIiEiD8RLesbNYVMoiIiIiIlIG1GMuIiIiIo2OSllERERERMqARmUREREREZFloh5zEREREWl08njxpxJzEREREWl0VMoiIiIiIrIcMrMDzOy/ZjbRzC5Ylm2ox1xEREREGp1S9pibWSVwK7AvMAV4w8wecfex9dmOesxFREREpNHxIk51sAMw0d0/dPfvgX8Aneobs3rMRTKy4Pup1hDbNbPu7j6wIbbdUPIWc97iBcVcCnmLFxRzKeQtXshnzFUp5vesmXUHuidmDUy1UWvgk8TjKcCO9X0d9ZiLND7da1+l7OQt5rzFC4q5FPIWLyjmUshbvJDPmBuUuw909+0SU4McuCgxFxERERH5caYCGyQerx/n1YsScxERERGRH+cNoJ2ZtTWzFYDfAo/UdyOqMRdpfPJYF5i3mPMWLyjmUshbvKCYSyFv8UI+Y86Uuy8wsx7AE0AlcKe7v1ff7VgeB18XEREREWlsVMoiIiIiIlIGlJiLiIiIiJQBJeYiIiIiImVAibmIiIiISBlQYi4iRWdm+mwRESkj+lzOB/2SRMqcmRXtlsKlYGYV7r4o/ry9mW2YdUz1kbf2Fsm7PCaMefucMDNLfC7vaGarZh2TVC13fwwiy5OY5Hr8eUUzWyn+XJZfCqmkvC9wK7Cjma2SbWTVSycFnoMxZKv6/ZfrPlGQt+Qrb/FC9TGX876RShh3NrMVs46pNqnP5TXLfV9JxXsdMARYo5z3i+WZbjAkUsYSX1gXAXsCq5pZP3d/MNvIqpaI93Lg90A34BV3n51cL34ZZ54Ap5KCE4AtgEnAU+4+tlziTEod/KwLVLr71HKLMykV82FAG+A94CV3n5NlbFVJ7Re/BX4GvAu84e5TMg2uGqk2PghYAZjt7k+4u5fbvmxmzdx9TiJhPAK4CvhFtpHVLNXOFwKtgL8C72QaWA0S8bYA1gb+4O4fZxuVVKesj/JEllfJHpj44d8TGA1MAf5pZueZWWVW8dXEzDYHugDHuPuTQBMz29zMzjCzg6E8eqWTiYqZXQlcA2wDnAzcYWa7FxKaLONMS3zJXgE8BbxtZjeZWetsI6teIuY/A4MJB2z/Aq41s7JKxFL7xdVAf+AI4Gagn5ltlWV8VUkdSFwH/A24CRhgZrdC+Jsrl33ZzB4ELjGz5onZqwOT3P27comzKol2vgY4E3gdmJ5cpxzjN7NTgPFAO0BJeRlTYi5ShhIf/m2ARcBv3f1cd+8MnAH8GTinTJPz+cBcoKmZ7UKI9e+EhPcuMzsmy+AKEsnX5oRerwPcfU/gNGAq8JdySs5TB2vdgd8BtwBXAscRkrCfZRNd7cxsS2BnYB933xo4BDgYOCv+DspCYr/YFmgP/NrdtwQuJPQ29jWzX2YY4lJSBxIbE9r4V8A+hL+9I8xsEJRVcv4mcA5wqpmtFeetAnwJS/0OyiHWHzCzzoSDy33dfYi7f2Zmq5tZezNbqYzaOeltwtnAzYFCSaRywDKkUhaRMmVmBwCPA58CRxfmu3v/+Jl/I7DIzG5w9wUZxbj4tG7CV8ACoA+wLfAXQlLzBjAUWLeUMdYklin8kXAgMQHA3Z81s+/j/NvM7FR3fzHDMIlxLa7DJXyxnuXuQ+O8J4BXgOvN7I/u/n52kf6QmV0AbAp8BIwEcPdHYmJwC+BmdqO7j8kwzMXMrBtwKDAPeAvA3e+O+8XJwOVmdrG7Z16+kEhi/wB0BMYC77n7QjObAnxL6On/m7sfn2VZS+F13b2vmc0ifIZVxjNWzdPrl8OZNajyc6458Ka7jzazzYCDgJMI+8t4Mzs2yxKtaj6XXyPsu38HBplZB3efW24lTqLEXKScvQn0A84i1OQ+X/jAjcn5IsJp9k+Bu0sdXKrWcntCT/lX7j7JzA4Ftga+TCa1Fi7s+q7UsdagBdCUUNe6FvANgLu/FA9+zgAeMLN9s0rCCu0ck9j2wMtx0UmJ5eNiwv4f4Dozu8Ddx2YRbzUcOBYYB6wDTANw94fNzAllFy3M7Bx3/zC7MBfbDNiVsD+0JJYquPvQGG93whmKY8vhIMjMViP0hG4PjHf3hQDuPtvMHiC0/zVmNszdO2WViMWDgsJn2M2xV/kGYAYh2V0l7sdrAbMJB8ztgSfcfVoWMce4k+VjLxA+M/Y1s9uBfQl/dzcTPgPPIlyT8HYWsaY+l/cGWgMzgbHu/lbsjLgfeNrM9nb3edUk8pIVd9ekSVPGE1BRzfzVCD3O3wO/ifMssfxwoEnGsV8FfEGof58C/CoZJ7AysD7wb0LvYybx1tDGRwGjgEeAn6eW/QroS7jAMut9pEX8/zBCwjgIaBbnVcb/NyWUPl2bYZzVtXP3GFsfYI3Usi7AQ9U9N6N4zwY+ICRc66eWHRfnlzze6mIGNor76hzgT6llzQi9pcMzjDn5uVWR+PnsuF/8D/ickOR+DnxIvOC2HNqZcDZiPrBdfHw+cBdwAvDTxO9gFLB1FvGmYr8amEw4kHiHUAt/UFy2LfBf4EVg5axj1ZT63WUdgCZNy/uU+vDvApwLXEy4ELEyTgOpJjmPj0uW7Ka+YHcg1C3uBhxIGJ3g+8QXQCVwXvxyeB5oWpifYRvvCnQA9kvMOyZ+ST0I/KyabWSWnBOS8fHAuvHxkbGd+wE/ScYHbFjK/aGGdm4PbFdIWuK8c2ISdjGp5LyqbZQ43q2BrYBtE/MuionW9UDrrOOtIuZNCCMJNY+PWxDqyt8HLkw97ydlEnNzYL3U8pPifnEt4YzKysCKhJ7pwgG+lSreKuLvSjiwOTk1f4VCbDHmx4BnSt2+VcR7IuGs1M7x8bmEMptDEutsDcwCBmQZq6Yqfn9ZB6BJk6YwxSRrBvAEocfo3fgl2zROAwindg/PMMZkUn4GodfogsS8NQhjl38PdIzzWgHHJxLHzHr4CSOvTAY+Ab4m9OK3i8u6EQ4e/glslvG+UJF6vC8wgnDBZ0WcdyShBy+ZnCcToJK2c2rf+DOhbGUO4ZT+0MSyQnJ+EbBmhm2cjPeqmMx+TihbuQtYMS67OL6Ha0kcZJRBzJcRhpz8MO7PFxMS81aEC4InAOfXtI0SxZzcJy8GXiKcYRtMPLsWl/0RWEi4HmXN6raRQZtvTBjFZBHxYIeYkMefVwL+FD+332JJ50MWZ38KBzH9gevjz4fFz7qT4uNmxDNAwM8pg7OBmlK/x6wD0KRJkwN0IowEsm183CR+ub4SExgjJL33AiMyijH5BbsVofRgEXBdcnmMsz+hh6ZLahtZ9jqfSjjw2T5+IW1NuBjxNWDtuM7xhIvnrsx6n4jxbJD4eQCh93alxLwjYzv/XzJZyDjmcwhlCfsDOxJGuRkLvJBYp2fcd44rg3jPivvFHsAuMZH5HBieWOfi+Pd5etbxxnguAD4jnvUBHoiPtynsN4SylllA14xiTJ/Vu5xwPczvCSPHfAQ8DRyRWOfMrPeLKuJekXBx51uEkpBCB0NlYp1TCBcxN4mPMz1jBdxHKLHZPe4DhaS8Mn7GnZiMMcvPZU1V/B6zDkCTJk0OcHpMulZmSa/H6sDthBrLQi/MqmR/mrQvcA+wd0wIvgI2jcsKXwzN4zrPZ922ibgHAP8Xfy608RoxWRiUWO/AcviiAnrFBPEP8XElYSz7u1PrHUvo6c/sVH8ilpWBh0n01BJudLM/oQf9ysT8I7NKYBIxVAL/AK5Izd8qJjTXpNo50/2CJSUTTwDHx3kd49/gyfFx4bOiDaFEpOQxs6TkqvB5sA+hd3/3+HhnwmgxHxJG6UmWWHTJOrEt/Ayslmj3fQkHEy8mPj+aVrVPZRFvan4fwshY3wJHJeavTjgYujSL9tVUt0ljWIqUWDVjxy4i9MwUxsBt4u5fE8oUtiX05OHus3zJCB2litcSP+9NGHu6n7s/A1wKvAo8a2abFmJz968IScFepYqzupjj40rCjTXWhsWjQ/zE3b8ELgF2MbNWcdm/PAw1l/UY8SsSRgS5Kd4kpiMhWV87jqwAgLvf5e57xvdU0s/0KsZq/pYwHObi8dTd/XvgScJFfVuZWZM4/353X1B4nFG8TQi18Osl1mniYQSeG4EdCzfBie2c9X5hhP2iHfCMme1JGP7uAncfYGY/AXqY2WbuPsndby91zGbWB3jJzDaOnweVhFKK/u7+opntR7gI9Q+Ea1TaAmeY2XEA7n5fqfeLGHdyNJPzCL3O75rZpcBu7v4Uoc68JaGsDHefn47T44g4JY53dzPbK45jD+Fs68OEksJRZraWmW0Y39PqhLMXUqaUmIuUUOrDtKOZtY2LHiNctNcLwJeMS74SoQxgZnI7XsKhrdxDV4uZHU0ouXnG3d+Oy0YTTquPIiQKP49fxubus0t9EBHjrEjEvKmZrRG/LO8kJFpdYuzfxqcsINRCz0pup1RfsDW4jTCM4M2E2tsuhLKm74FdzWyF9BNKuV+k2nmdQgiEBHwjS9whM643jjDK0FJxe4nG4E/Fu4GZrezu3xGGGt0hHnQm45kVY52Xirdk+4Ul7ooaxynfJB5MjiOUtT0GnOHuA+JqaxDGX98huZ0S78tjCD3Ld5nZJvG1xwMPmdnKhFKnmwhnfmYQauG3JZSWJWMu6b0ZEp/LVxJGinmG8Pd2ItDbzFoCzxJq4dcys7FZxFlFvP0I+8LjwGAz6xkPhnsTSiHfJIzI8iDhjOsu8cAn644HqYYSc5ESiclq8tbk1xPuyrequ08iXHx4kpndaWb7mNk2hIvoZhFOA5c83sL/MbnuEactkj2P7j6K8AX2NjDOzH5aSIDi8lIni4U2vozQ67lb/BJ6nXCx5x/NrGtcZx3C7dYnE8ZNzpSZXWRm15lZGw/jNn9EGGrySsLFfhOBXxPqtjtkGGeynXsREoJfxN/7/xF6zHuZ2S5x/1k1xv2hu8/NON7ehLGzt4mLXyRc8Hla7M3FzFoQhsr8gHAgVHLx7//vZnaumV1PKGsruJ/Qy/+6u/8trr8acAfh4GhIqeMtcPd/Ev7u5gFDzKxdPNM3ndDbvxYwPZ7hWZFwkHEwodY/E4nPul8SDmwOiwc7Ewln2Ya4+wx3n08oI7oQeCeL5DZ1BnMvQolNF8LnwX+BbmZ2vru/5+77E0acOj9OexR6+cug40GqU+raGU2alveJUP4xg1BnuUpq2b6EusuphJ6kEWR4lX983XXi/00Jp0I/JVxY9JPUetsTSm/KoT77SsLFcAeRGOGBMLTc/xF6yD8mJAVvZ93GifiOju07HOgR570IDEyscxIhAcu0PjvGcjVhWLZuLH2h6i/j/vsuIVl4Lf5caOdM6uEJo69MJyQy6yTm7w38K/5djiXU8r+TZbyEBLZfjPdrYPPEslUI5QhjY7s+ROgdHUUZDEkaHx9MqGd+hdDTD2EoxLGEewb8kZDkvsmSWvRS1mf3BY5NzdsOeDv+3JnQKVKo3W9GKCdbmaUv/Mzk8y627+1An8S8dQln2N4kNZZ91vFqqsfvNusANGlanibCBVmvAwfEx+sR6scHAN3ivBaEutctEl9YWV0MdQJh+MDCaA9NCadMRwG/pZqRQLL88CeMRDAJ2DE+Xolw448jgA3jvF8S6kUPJaNhHNOJTGofuZJQEvAo4SZS7wKHVrFulkNP7ku4odRO8bEBaxJOlUOoxT2McCDanexHrNgvxlsY+aiSMLTg7oS621UIFyn2IgxLmUm8hDPZhYsLf0+4mdRYUkMfxkRxj5iIXUcY6SazmBM/b5r4uSNLkvOfxXnbEQ56XiUcDJX8oJhwcfpowv0VDk/M35MwlOPJhAtqT00texjYMov9NxX/WoTvkXn88GLwdQmlQq8CV2cdq6b6T4U/fhEpATNbkzAKQX/CSBo9CbeDn0foQT/F3W9PPSez2yWb2SmEocBeB25197djbfMwwhfAVcDDHmp1y4KZ7UoYuqwroUa4G6E2vpKQpHd095Gp51R6aWuHk6UVXQl37FwZGObuz8c23ohQZ74JIWl8mtB7N7OazZaUmXUDerr7drHsohPhLqrrAk8RhhaclnpOSds59dqdCDe7OpBwweGRhHibEM5SHOvuE1LPyTLe1QkHwhsSDoL3Ah5x98tqeV6W+3JvwsFYT3cfEed1JAyDuArwO3cfH0uFFgCz3Bdf7F6qaw0svuY6hJGjmhDurjw0zr+fcDB8mbv3ic/5CaF8aAEhkS/p53Eh5tS8TQkHZBsTRln5e2LZOoR7NiwAfp9+rpQ31ZiLNJBqLnqcRxierQfhRhufE0457goMJXUBFJSuRruqeN39L4TT6dsQRk7YxsOFRQcTeh9vJPQ4ZqKaNp5POOtwK6EMZBXCONSdCONr/zz9hFInX770hVv9CON97wg8Z2aXAM3cfby7/4rQe/4RoQzgy1LGWZCsa00YA2xjZo8RLkL8KaEO/ijgAELCsJRStXNhv0jFPZtw8DuEcGFfK0Jv/qmEHsgN09vJMCk/mnAwvLa7v0n4O3sZONjM/pRY71Iza5d8bob78tWEg/jehGs2CsuHE66nmQPcYWHEmJnu/k1MhCtKlZRHFTGuzwh3xFyNUB52aFx+E/AccKKZ/d7MziWU3rQFOnvpR8VKX7S8arxweTzhQPPjGGvnwnPiezuTMNSqV/P3K+Uq6y57TZoa48TSp3Y7EGpat2TJuLibAVsn1yecVr2oDGLfmR/eMvt3hBtsDAa2iPNWIMOa8lQbbxynwmnxHQgJV0dCkguht/xN4Mis2zjGcyDxpjAsKV04hXBg0TO17oYsKWvK8s6NrQkHOqvHx/sT6t1/y5KbNDUjJJW/KmWcNcTbkiUlHr8mHOgcSbz2gDBSxdvA/lnvE4m4OxEOHl4BfhHntSIk6G8RrvV4jFB/nnnNMLAb4ULZwi3gVyScOTkUaBnnHUgogbs963hjPP0IPeajCXdUHgscHJdtQajfnhx/D7eTfSlWH5Zc/9CfJXfv3JIwHOlSN2tKPC/T62Y0LcPvOusANGlqzBPhNt4zCb3Ln8YPzz0Ty5sReskfi19aWd9wZU9Cz9afColWYtkfCD3+dxLrtxPLsqwpv5JwS/JphN6jE4DmieWFkSAeJ1yEmMUNVy4E2qfmdYsJ4UosfTHZeYSLzjaqYjsl/ZJl6VvAXx6TgvcJpSp7J3/3hLKL1Qh1w69knTDGeCfE6U2gQ2p5Id7HCb3RmR9gpuYfEBOu11mSnK9LGG7wIcL45ZlctJx+PcJF1p/En7cklLj9lzCizX+AVnHZbuWQKBKuefiScFC8PqE3fCThZm4HJdZrmXpeyT6fU397RxPOrh5DKNN7gTAwwE/j8i3i3907ZHRArKmIv/usA9CkqTFNqQ/TvYl3uyP0MnYi1CmOZskFckfFL9lnyGA0BarofSWMtPFhTCaTI1dUEEYx+Qy4sLrnlyDmZI/oYYSRNA4jXAjXnzCizcWECxErCTcQejYmi1m08fqEG0gNI45OEecfGxOXwqg3K8T/2xEOMvbKaj+uop1PiO3clTDG8xBC/eoRcflKhHKAFwmJZBYX9CXj7UY4ID42/vwAoZTl2LhPrEjogRyRijfLA8yDiHfMTMw7kDByyWvAz5P7SWKdLC8A7kroXGhF6F1+j5BADiScJWwV9/GjU8/L+qDtBuDfyf0mxjqOUKJ1RPqzLYvPuvi6+xFGkDkmMe9wwjVKz7MkOd8mvq/MD3w0/cjfedYBaNLUGCdCGcVVwM2p+bsQejYGxsdtCOMll3xkEBK3k67iS+hqQi/0hSwpUWhNuEjquKy/WGM8XQm1+qen5veKSeS+8fGuhF7GLNq48KW/GaGH7lGWjE7RktCb+BCxRzGxT7xP4sxKxu28G/BX4MTEvNXjPvIdYZhMI5SJ9Cb7U/6dCEn3ian5/QkjnGwaH+8PXJF1vPG1tyfchOdufnim6gjCwfALJIZMjMsySRbjazcnlF1dFB9vRajZP5glJXs/IZyN+E1WcaZiLnwG3Aq8lJj/k8S+M49w9rLkPc+EsyC7Jh7vTjjY+QI4JLXuYYQDy+eAtlW9T035nDIPQJOmxjgRSlYWEXoQm6WWXUgoa1k9Nb8kPR2khvsCTo9fCLeRqG0m3NzoA0LpSnfCAcW/WFIPnWXv4saEspVFxHF8gRUTy4cDT1XxvFKP7WyJZOAXMTF8FNg4zusW95ERhDKivQllTZmU3FQR/15xH5hBHM4z8b7WJpyJuCLOa5JYnlVZyLaEg5pvCaNRpPeLV4A7y2G/qGLeOYQLwgeTSM4JJTevEurJ78h6n0jF/Oe4P6+amr8C4WLl4YTykHIrE9otfnackZp/OOHsyi2l+jxOvHb72J7JDpMVCWWFHxMuQF0t9ZxDCYn7rdXtV5ryN2lUFpEfqZrRTPYhfMHuAhxiZs0Si98knGZfPfWcBh99Jd5u+jYz+1V83ItQoz2XcIFhLzMbFuO5kNDL2IZQvgDh4iiPw3eVcki29KgCUwh3v3wLONzMmrr7d2bWNC4fT+pW6lDy26lXeLAw3t31PcL+sAdws5mt7+5DCKef5xLKmW4k9DLuFp9X0jsLptvZ3Z8D7iIk4l3NrFWc7+7+OeF6hDZx3oLE80o1+kp6v3ifMK73dMJBD4X9Iq47iSpGI8tiv0g8bhJj6EcoddsUuMbM1oirNCfsz6cQrvMouRpGIXmScDC5fVzP4lCfnQnvpTCufSb7si8ZMeZQMzvDzPY2s5bu/hKhxO16M7vAzNqa2QbA8YQbDJ3uYfSVksXs7uMIZx/mm9kpZnaYh2ForyF0mrQCrop30S085yHC2dkz4mOvYtOSMxrHXORHSI3h246QDH5a+KI3swcJvY69CBfMfUsoC1iRUKpQ0j9AM9s/xjITuJfQQ3Sbuz8Xb4+9e5z/nLt3ic9ZgzDW74yYlJdszOH4+sk2XoHQ+zYvji28F+FL63PCzWEWEGpanwcmuXvXUsVZQ8ynARsA/d19ipltRui5fRk4yd0/iev9gnCHx2kxKciynZcaNzmOT92ZUO/c193/F/eXEcAr7l7y26mnx/ePB2fzY+LSlXCL91HufmRinVcIideppY43vn6yjU8ljIDUDHjZ3a+L8xXEVYIAACAASURBVHsQLvJzwt/iYcBCwqgxi9Lvu8Tx7wl84+5vJ+bdRbi4+rfu/nX8u9yVUL71F3df8P/tnXWYXdXVh98VgyABUoIXh+IQ3C24FAlSHIIED8G1eIDgRRqK01KgLVpo8VIKxS1QCnxFimuxoCFZ3x+/fTJ7Tu7EyJxzJ1nv8+xn5u6zz511z+x7ztprL6lhLo+av2Z2Joot+Dodvg843t3fMbMByJ3pC2RB/xhYPs2j0XKHt6O8o66PmfUCrkJpXQ9097+k+97hyE3oSVRs6svSe9SWcz+YuIRiHgQTATM7DW0rzoZSa93k7o+kY39CD9eP0ENhBmAzd/++jodserieipTA2VHBnbfTsU7Iz/ICYBd3v6/0kKtTKTgGPfCnQBXt7k7WxnWQct4NBa2+hnKCL1H1A7aBzIOR5faX6H//elrcFMr5P4CDffTCNnVe5wFogfZ/aIF2d+o/FWWH+Aa5VvRA2+9LufvwOmRNch2KXFi+Boa4+xNJOd8JuQF8gTKEfJ3GLVqlktiIlPN7NxQQ3A0Fgd+JCoy9Y2Z9kfzzof/DtmkuVzovcmXPzBZEc/YjZGS4HAWyr4N2erZy9xfT2PyeUXXBo/xvL4+y8xybZN0LpfZ8CzjM3d8ys/mABdPpdyfrfiULiQYL4CXd/TkzWxHtCC6b5Lw9KeeHoRSwryNXra8bvnHQsfEm8KeJFq0jN2Bz4D/ImnEw2nb+A1nwEPLTHonyJ3dPfV3rkDf97bWQcjWSLNo/HZsXuQJsU/e1zWQaiPzyz0K+liORtRlkzd8QKQ0fkPKsF8dqlHkL5HKzcqm/CDZcBO1cPEzKSVx3A45EitfVyE3oCVoHfR6bZL6/uP51XmcUr/FBkvcfSPneKB2bFpVW/xfKtrF23fKmv718mherZX2LI2vt9VmfoQDhwoBWqcy0znJzIFokzI6yx/wb+cP/Ocn+X5okP3km8/aomNuVxTVM/Xul79z1pFiP0nmV+MOTYh9oCRDvj6zhxf97ObRj8m9kPAEt4s4ALiWyr0yyLXzMg2A8aeBv+Q0KKLvN3c9BD7F5gX0LX25374cCoYYA65hZd6/RyujyHT4IKV79zGyj7PDHwGfIMl0LDa5xZ2QhOhQpvMcDF5nZPi7L1r3IMvYJyrhQUOeW4CJokfZo0ZEsZD+YWTeXdbEP8tN+t433aFcaXOdZUQGmXVBRqWeAQ8xsDwB3PwXtTkwBzGMqGw9ytahD3mkzeX+B0jjeamYbu7b6r0WZhIYhC3VBnfNiWrSwfAVGueA8jxb2W5jZxjDKj79wH6u0OmbJ5eYUZBE/293fcfc/ox2pU2lxt+kGbGZmC1cl4ziwFsq80xvFbQDg7r9BriKzAkPMbJb8JK/Aup/ca443s6m99Q7Iv9ylgbv7E+i6P4NiDjZyVV0+FtjLK65AGlRH/FODYDwoBRT1N7NfIQW3CDrEtfV/FAqK629mG6T+nyN3hlvRQ6NW3P1R5LfYHQUVHWdmuyLlpnjgVk5JKVg/betvhCyIuPsIdz8ZpcT7lZn1T4uce1CQak8zG1qMrUH+IiCxB1JgRwUoJiWrMwoIntPdn3H39ep4yJau86pmtjQwP1qU4e5DUSDlQ8BBZtYv9R+LLObrAKeYWa9CmahQ3tWSS9aqtMyLd1D8xOXATUmR+RIFr14JLGpmt6SxdQWngnYkZkduCgAj0v/+ZZR94yflE7xa95X8Op+HAk6vQfO5cE35wt3/mu5pA1GAYk9kTa+cRtfZ3fdEi/TpgGOsJZgWd78UpSn9D4pPqYz0v54DWBc4wFqCOWdG8TGjFqDu/jhSzp8CfmdmK7v78HQfsSrnRVAhdZvso0XrKI3W26EnIEvnbchi/jIpb3Y2Zh30oD2F1imwriEVC2mGhvyJH0M5ie9Byk3hblFnSsTTUbDsUGRhHARMVRpzdDq2RXrdBfnIPw7MVfN13SbJtkmpvwdanO1Snlc1yXkWyrH+EVIM9i4dXxTt9HxMKlme+s9BubVnqljeM9J378U0Z/coHe+FrPojaSnkNTVatD1EljO+neXM00fmKRu7oXzlj5AVkUKW9H9RKsZT47y4CO1ALYxcxYaWjncuvd4fFeeZpSoZ09/NXW56oiw2+fU+Fym2J5BVBE7HrPwe7SzrKLekdH2fTPewrmhxc3Ub5y0HnFTn/Thada12AaJF6wiN1iXTl0Xb46um12ujLCC3kcqUZ2OXIytZXqG846XsASuirfVjsodH1bmd8wfsMqj4zorIins0cpfYn1QMJBu7S0kJ6kIpd3yN8+ZS4EuUFWKJpOTemRSFyh+yyLqcLzAXSAruCmhX4grks71L6byl0O5KWRnrVfG8WB54HgUBr5m+h9+SLRjSuFlQoFw+L6YCZqhA3gVLf/cgpIj/Huid+lYAbkEL+kPTHL4LlVSvK+d3Pi9WQ4ufpdLrNZC7Vc/yfYwWH+nVkGI+a4Uy53PjGOTS9g5SxtfJjhVW518CPdv63FVc4+x6dUUL3qfTHLkQLXZXQdl6Vkg/tyTFJaXzQjmfxFvtAkSL1swNOKT0eqv08Hya1uXq10Op4/5Mg4pxNT5sfzIeY5ehZRFRZSn1pUuvj0DuCL8p9efK+RQN3qe2gL4xfLaeSUkYhqyPQ1GQYuUl4Mv/06S4XoZ8h4u+BZD7yjuUlPNsTOcq5gcwe+n1ocCZwFlZ39RJofkW2LSN9+lSlfKVFMCPgBXS6yNRVpiLUKGmV0mFmtBCbTDaiXgEKeqVz4vy3Mhk6JX1LZfm7yxZ35XAktnrgUiZn7k9ZW1D/lPTddwJxUY8jHbNNs3GnIOysfSrWr4G13j24lqjLF5PJvlHprnwPnKxeQ1V9oxAz8mo1S5AtGjN2lAKs5tpbS3/OXL3GEapzDTyGbwv3ViXaQL59wcGpd/bfNCTWXHGNrYdZPwtynWc952SHlDPUtoWR7773yWFp7asNhPwOZdFcQUr0mIxq2whkZS+Idnr6ZC1+TvgltLYBYHzkRvWPjVdr3uB80p9l6d5cRetLYhTo/SeX1FzJiHkpjIUWY5XRdli8hLrf0ABwbsA3VJfz/QZmiH7yuHAbxjdZWwmtKM2W3r9l6Q0Fi5vUyPFfMkK5LXSz03SNV0+vV4DLdSeRFbyDbNzB1R5f2vjGh+JEgEUuxFd0GL4abTI7IHi/2ZGintxv4iqnpNJq12AaNGatSGfz+KmuFHWvyaqePcQsF7pnE2poZxzG/KfhHyHe45lXL6FvUjFMs6VKSjzZP0DkhJ2JDBd6ZxByOrc9A+qtmSsWjlArijdSn3zIX/tkSQrbnZsARQLcUsd1zn9/SKd3AxZ/yDkV75dafxUyF3kbzX+rwsltStyD/oPynq0UGncDSgF3q6MXmK9tjmNrPdvJwV7ntKxHigl4rq0uOC0su5XMafTvfVZWhtLlkEFgwA2Rpbn3dHC6MOk8G5bep+6djDPRNbw7chSNdLareWwBve82p8n0SqcJ3ULEC1aM7aSsrpiuplemvWth6weD1AK+szGVOkOYuW/i9KBPQwcVB7Txnn7o0DWeSuSObci9UcBqOtlfcckpfHQBg+qVlazCq9zw//p2P7XdSpcJTkGJGWxuH5zIveLr4EdS2PnoAZrXWleHJG+YwtkfRemebp16bwp61ZgaK2cP5zm7+ZluZC/+SeUdt1qlHuHdI9bNuvrSvIpRxbcF9J1f4EWpbzKXZ9tUHrR/6I4jWJB0IWWXYd7gWOycx5Ei4gh6XWdC5+fo12o/BpPQ4ulv3Oa229SWihHm7xapEsMghIpXZhnXa8i/8QVzWwIjEqJeAEK7DvSzEZLE+YVpbIaQ2XOD5DVbqskj4/hvP7Aiciv+LWKZM6vz0PIKneQma2b5D0VZYg5A9i9lO7Mc/mroJRGbjMz29vMjjCzmcb0vy5d5wXbGtceNEjB+BxSxv+a5HoT+cBfgnI6b18MdPe3vaUEfCXXucG8uBctjM8ws/mTXPsjt5arUyrNQt5vvebczt5Sfn442lkbCpwGLJ+n9HP37ZHf+Z21CDo6CwH3u/uTZra4qfrr0NQOSv+Tv6Kc2r1dVUgrqY4JYGYPAX3RfWI7VCPgziK/u7v/Dym585FqApjZjChW4jhgHxj9HlgxcwAfpGu8qKmS8dPAw2Z2rSuF50Dk1lJLqtqgSah7ZRAtWjM1WlvrtiJZj4EZULq1F2ntq7se8im/oAnk3Rq4EZgHmDb1zYEU9P6l83JLeX/gc6BvDTL3JgWZIfeFochNaN1szFHI8tgsaeQGI//ae1FMwTdoi39sOxIHoEDAOWu4znPSYmFcGQXB3UOL5Xwu4Ox0nderQr6xyLsAKbUdsFi6brfR2nJ+fpJ3rSrlHMfPklvOn0dpEFdsY47UnmUj3QNGIleLF5Av/IFoUTEs3Ud6ZPOlSkv5tshK3jO97okyl7yV7hXFvP5p+k7+AVX3vBNlyyp2fereTVknyXxnun9cleTsk6796s02L6LVNFfqFiBatGZpJSVqEPK3PIoUCIWU80ORf+ivs7HL13HTL8k7AFk970al63+LFhZToBR4F6HtaCu9R39UYr0OpfxklHHgF6RgvqSQPc/oyvnOVSoDY5B/Z7Tlv3R6vWl6qG5e/r8w+uLnE0q+rhVd5+NRwOQKpHSJSbF5m9bK+XxJGav8OpfkPREp4Rtm82JxtDt1GzB/NnZgM8yLNj5TrpwPRbsVq5e/g83QUKDh0cjNaT/SAgilKn2M1v7QVbuP9UOK+UzID/vMdF/LlfNC+d4JKecvpTlfuNzU7qOdnh/boliIHWkJpJ0dGXeWqlvGaM3RahcgWrRma0mR+RilCJumdKwHcDCyKl1XOlaXT/lBwBu0pGjbAbnZfJseZA8gH+JlSu9RWGoqUcpLf3sQSiu3Pi2WsEJBXCgpMn+llAKvbiUszY3T0+9bI0tu/2xuFAGLeXBapTsSJXlPR1v7v2D0DDeFcn5nee7WdZ2RhfZDVCRqxtRXKF1Lpet9M7BwM8g7Dp8nV84/AH5Xt0xjkXfK7Pcp0nfw7vL8qFgmQzsOr6d7WrEo7kSLcn5vNr5XarVkuRmXz5N+dkbZkW5Hwey1Lx6iNUcLH/MgyDCzWVDBoN3d/QlgOjNb3cyuSX7YXVHRmD8CrfxZvcLyyO5e+Cwvh4rWDHD3x9Kxa939ALR1/hWq5jglsLeZdc98XR8DVnT3G6uSO8m8Egrk2tTd7wKGm9kCwB5mtqS7v5SOL43+F6Pwinxax8C8wE/MbAPk53yEu1+Sju0GnJBKlo+AUb77p6PcyVVf57XQIm1Ld78e+NjMZjGzNc1sXnd/GF3ndVAMxSjquM5mtjawPcqAdCvwpZnNAWxsZvO7+7OoiM1mKKNJrfKOC97a53x2lCaxaXH3b9M9YnuklM+CAlRr8d1P3yVHFuW5UCDn+1m8xz/RonNBM7sr9X+Umhc+6BXIOe24jk1ydUdy34Ku8dp1XeOg+ehStwBB0GR8j7ZvFzez99BW+Xwo3/PWyHf7LDM7F/gyu/lXppQXpMC3E1E2gt+kvi5JGejk7s+a2YtoMXESsAWy6H6TguyGoSIcVfMNus6Y2RIotdmGyII0l5mt4O5PmdkyyC2ncsbwP70PxRrsABzm7r9O46dFCu5LmVK+AcoVvpW731SN5K2YDu38PGVmy6L//9ap/3kzO8jd/2lmvVHsRN0Y2kX52MwWR9v9W6f+zma2gbs/l4JA36xFwAn4rqfvY9eknBfvM2rx1oTMitxGXgIOzBYXlS9+3H2EmU2Ncqivh7KW3IxcVl5J999COf87ipMYmJ3f7vdlM7sJeMfMTnD3T8bxtO7IWPIgcHKd1zhoPmJ1FgQZruj+c1Cg3gNoq/9Yd18NuB5YMim1X6SHQjmLRJU8jLZ4ZwH6Jll+KCkPw939K3c/BHDkrznK4l4Tw5Frx7nI4tUNOBZZQ/+NylDjygoywsw6VylcekAW2VfWNrONkqIIKqzyXmpfmdkMaXFxA7KIHpW91ePAqjUp5SDr4pLAHcjfdhbkirMj2mWZHcDdn6/jOjfgO+TrfAlSWHoieX+BFnOLALj7a4UiU6Vw+XfdzLY1sxPMbHMzmy0f08Z5w9Pvq4EUzqpkHt9zXFmZrnD3fbNFRW0Ko7t/BZzr7vci97sZgGuKDEfpXvYo2mE7tAYR/4b88gea2U/G5YT0nLnW3Y9vhmscNBdhMQ+C0bkIuAkFff4LZOFCmS0ezpXaqhTcsqUuWdzeN7P9UZn69ZCf+RBvSXE3Mi0eCuvcO2lsrbj7v1I6tvmRhfRBd//OzKZEytmnpfFVKTE3oLiBW9Lrwcg//DNg1mRhvtjMdkGl7I9AFvHnkQ//Cukh29ndR6SH7z+rkL3BZ+nk7v82s5VRmrkhqPjOp2Y2BZoL3fJz6rbguvtDZrYnysJyMfCAu39uZj2QS9Z3pfGVKTJJuS7cx05D6fdeQcVg/mhmQ9z90Wyx7g3O6w+cbWarufszFcicp/fsga6fJXeVNi32heGheJ1b+uvClZ6xk7u/Y2ZrIOv41Wa2i7u/kj7n81D9boS7X2BmX6Ig+05mdo67fzymc9Jn+Tb7vfZrHDQPRRBCEASJ0sN0apQR4likmC9dtWWj9IDdEVkOZwBudfc7k5XmYpQu7BrgkgYKwtooW8Fi7l6b20IuU9Y3BTAjcsfpBaxUtZKY/s9XoCIgm6P8739GvszDUNnv01HxktPMbBpgNqRE/gd4IS2ImmY7urjW2c9uaAv9ejR/VqlbGS9opMyaWVcUUPtbJO+qdctrZksDpyD3g0fMbHNUCOs1ZNV9NI0zaBUL0h+l2awk1qB0zzgc7UbNinakBrv7822cl/8f+iF3vT+2t7zjSjY3ZgXuR4vLNd39rTrlSb/vhuJOTgfaVM5L5+yKMuAcU5HIQQcgLObBZMW4+IhmN81OqEjIHugBsExuEW13YVvkKR6wg1G6rQdRdoq/mNlAdz/fzPZD/pc7IJ/zs0sK8EPA3K6CMu1KWfnOXzdQyruiiqPrIiVsFU9uFRVf46/MbG+U0vBW4FTgz+5e+OC/aGbfAueZ2Uik3LyCrKbFZ6kk0Gxcya95us77ohSaXUlKbtXXuS0azItuwJEoveC0NIG8ZrYPKvP+OfAkgLvfYmaOFu4Hmdl5heU8O69SpTzJVdwzBgF7Ir9rBw4H7jKzhd398/ycRtZ9FIzbrpjZ75Fbxx1jG5stNN8zs3WSjO+2t4xlimuV5Cl2yK5MC7LL0pjRlPMG1/gsKrjGQQfDmyA1TLRoVTdKqePGNA5lNylSttWVRm5TlBZsufR6HZTqcMdszEzIKn4JNeVKpnU+6rnH8ZwVkcvIqBLbNc6LHsiVaSRwS+orFwn6HgXTdpj0ZiiwdlWkQBYp/JoqjVwDmfug3Nq1z4v0949O//v/I8ulno5thjKH3IN2pYr+/aiwTkBJpoVQZcnV0+uNkVvWPun1qHz7pTlepPfcsgIZp0SZSb4A+ozHebWl9yzd46YhpXvN+nZP949BpJSfDc4rXOQqnxfRmr/VLkC0aFU0YCNgj/T7eahq4BQT8D61KGPA3sDv0+9boWIrRf7s6YEF0+8zZIuI2gqZoCIgVwMzj+d5VqXcyBWlqJJ6OPJ7nxFZ4r4n5VEvKS5HobzDdS1+fvTfrUuRGVPf+L5HHdc4KVQfpfk9V+nYtshaWnz/VkhK+TY1zZPl0WK+C3LR+hLYOx2bClnSy0rlXlRbBdiScnsliiNY+8f8fyqQN1euj0AJAl5FbnA/y/73hXJ+CjBTndc4WsdrtQsQLVp7N2QFvQSlWLsjPQAWH4fzWpWOr/kzHIwKwWyLrEt7Z8e2R9XkGlpnKpIvV1yXRNliVhjPazxrxTL3TnIehdyARgI/S8d6ooDJ74ANG3zG0ap7ViRzfr2mJlU2HJssJdkrK/Vdknc+lA1munE4Ly/QNH2N17gXMGfp+CEoePa08rHSuHnIrOftLHP+/y2Uw95oATkwKYL9szHLoExCy2d9+yPlvd0t5envdcl+XxBlDnofWGM8PuvGwPpVzo/0d09BLjQDgLWQ9fsmVPCouDf0S/eU/Lrvke4plVzjaB2z1S5AtGjt2bKH1LyoWudI4Jfl4w3OK2/t/q9Q2qqQt0H/uijrwDfAIVn/VChIsTb3lZKchycl95JxGFu+xr8DflKxvINRRcZhyI85nzMzIOX8G2CDBjLXqZQfhlwAnkUuFgu1JVNJ5gHIr7XdZS/93ZPQIug1VF79aOCn4zgvBlOqwFvRNT4eZdUZBlwFbJ0dOxSlUj0VmLct+auWucH1+3u65x2X9XVHaT//nM31WYEbgW2rlD397UFoAXFPutafA+uMw9zYB2VDWq1ieTdEQbTF/WLldI/4DKVtXDm7rpvQ4jr2E+Qmt3nV1zhax2q1CxAtWhUN+WRfgKxEL5PcWtKxzqWx5XLqlfgClh46v0BbzdtkfWcji9IpwLLAGsiK/lx2869VOUc54EeiHN5tWjpLn3Wv9GCrbGuXFr/l7ZBi/hKynJe39mdAGW9GoiqpzTCXT0OFg/ZNyuMTqErjEg2ubfk6DwO2q1jeo9I1Xi+9vinN49F2oRrI+12V8yL72yclmbdLitaTqFLuntmYg1H60f5Vy5fJkC8k9kEZbG4kLd6Rxf8pVEDqBLRwvh8t8lvttlDxojj93d3SnFwxKa5LoqxBwyj5nDO6j/anqHhXlfIaepbsl16vjwLGt0dZmj5HC+Y+NNilYhx2i6JFq12AaNHao5Vu4oOSIjMX8gO8CKW426N0zlyl10UQVKWKQZL3SxS49QNwWXbsLGSVGYmCzf5SPGCp0EWhfI1L/cck+fZh7BbcygLN2pB1bmAOlOLs6aS8zFAaM11SaGoPlkSVMF8Blk2v+yDl9XlUlXTR4ho3UGQqvc5JhqmQi8KuqW8TtNAtfJ270CAmos55ka7pv0iWWOSe8G2aH88Au2Rjt6v6e9eGzGcAHyIf92tQEa9bURGpadFu1EPIKn0hTRIAjBZAt5f6egG3pXt28T9oNJerMJY0io+YBqWmnRbtSByb+qdFRpKRwEV1z4loHbfVLkC0aO3ZUFaVwcC6Wd9C6eH0cqYg3AGcmo3Zl4qyKeSKCbIa3Y2q2M2Itk2/QIVvivE9geXQ9nPhz1jpA7b0oFwA+azOkfWdkZSDXcbwHnvTRJkJkLX/aeA4kmUL7bLMk42pW5HZEOXQBgX0fYIsy79IysrdJKU9O2fPChUZK73uhYLj5kSpR/MAxCmRa81CpXMqzVjRQOafAQek39dLCuKu6V7yDrJAH1w6pzblHAV5vk3m0gEskeTO7xtT0dpK3gwLzRNRFd3ColzcC7dHCu5IUiaqbG5U4gfP6PERvWgdx1Pkhd8ivZ4a7a4tUed8iNbxW+0CRIvWXg0FSo5Efq3LlY79LCliw5CC/m9aLM9rI9eKrSuQMb/5z4y2coeQuYEgC94XyOo15Zjeo6Lrmls2T02KyqdJKfwtLYuFU5E1d+cG77Fz+ky1K+Wl/8HZ6fPchlJPflyXAlOSa8r0s3NSEKYHHgaOyPqfQ/7bv8rOOwBZe7eoWPbpst/vRD7Ew4Ddsv7ZUE7+nbO+vakpYwVyq+iTfu8JTAHcjtyFCsXx7nQ/OY8miOlIMq2DAttnTq+L+9gq6fu3cYNzavWDz/qXRrE/p5TmzBrpPngoLdb9n6GdoTp2MF8FXkc7KZun/hmQS9b1wI5pnj+e3f9COY82Qa0TQTDp8hjwe+TCMjOAmXUBcPeXkfvChsg9ZDFX2efOKB3aql5BxTtvXQjkfuQfugHagi7G3IeqUW6Eyn9P0eg9qsLd9WQ3OxJZaw9G1/hNZLldOY07Bim6V5nZhqW36Yl8nSspuDImXBU7O6ffDwGuRW4B76JMMT8Ux6uiVLnxEOBQM5vdVcjkI1K2EKSMg+bLv1EKt4Oyt+qOdi1ubm95s98PRYWYfpa6rkPuQo+5+5VpTA/kduHoehfMRYWFeArMbA6UvWQVAHf/H3KzmR34xlXcqBvyOx+ILOZeVPisUM5Gz+yPk5zLptcj0riX0XeyZ/mE4jtcBaW53NfMDjGzw8xsWXd/Gt3z+gCDzGweM1sQKeRTuPtZ6fvXKd2zN2nPuWGJ7PU2aMfpMLSTdh9wo5kNcPdPkWvZ6knerqhAWlEEqfbCXUEHpe6VQbRoE6PRtkVmLuRr+TEpRSJtWDKor0jFLsAbqBjJ4chieB2j57/dEFnsai1sg1xupkP+7dulvvXRFvPu6XX3bPzeVV7bMVznMVoJxzCHqpwXZbeKwWirfx+ynPAovdyTyKq4MXLF+gs1WOtK13hhtJ0/HFmVZ0KLg5OQojgUBX8+gjLKFNbdrlXJO4bPcQxyDZopve6FFLHbkNX8brSbUrhb1LlTtTlKb7gKSgd7Gcogs1Y2ZloU9Ll93dc2yTMYLXavTbK+jBb2XdL1fRztcP4nnxt1XOv0NzdG8UgHlvoPS3KumV5Phww/tbgVRpv0WjGRgqDDUrLIrIi29X9w98dS3+zAb5Bf9lru/q/8nDoxs3VRRoK33P2q1LcqyrJxGzDQ3T9scF6t8ptZdxRMthdySfg9cJi7D0mWxV2B19z93uycLl5TyXoz2x14293vGtu1K5XNHvV71ZhZP5SBZV13H5r6pkRuLZ+lEvF7IYvo62nc8Lrmhpmdjfze70RxB+uhwiuHo9oBK6AdlW9Q4ZsLXdbQSudF+fqYWdd03WZEi/h7kR//D+l+chLyH/4EuVHUdo2TvKcCB6LF/KJIqX0HpVTtjZT0j5Cf9szAMl6z9dbMtkVFmfq6+xNmtgu6J+/q7tclK3U3FIcwDHjUtUtRydwwsz8A17j77en18km+uVF63V+lXTNP7TZa4juGZ/eLpniuBB2culcG0aL9mEZrK9IpyP/zZaQInEBLObf48gAAIABJREFUEN9syKr4HrBUM8iNtp+LAKejS8dXRT7Y1wCz1Cxro8wEPZDF9i8oSHaf7NjcaGGxQ5Nc585pXlw5nvNp6grlvAzYrNR3InBp+n0htKPyEsrKc3TqnxVVKy2suHXtTKyH4gzygjXbonSClwGzt3FenUGTO6T7wigLOKoI/CRZVWBkee5OTRbR7O9akvc+UupOVGHyA+BkpIifiJTyx1DavloyNjX4DMfQUrl4a7QrWAQBT0uDQkxVyYwKQR1LadcGxWcU1vufFnMk/bwauLHOaxpt0m3hYx50aNy9sFQci6qq7YKUmAuAXwInmtl07v4u8hV8EynwlZP7Lrp4B/mFfg70MbP5s+MPIdeVHZFVphZKuxHzmVkPM5vG3b9APperIt/hX5tZZzObHm3/ToWCouqm8PU8FFg5WUAbD2xtKR8I3JIs1O0roCy1H6HFTM40wA5mdjS6lmshF6enU/+s7v6eu//H5SffySuyPDfwdZ4SWRDfMLNOSZYbUEDlbsDBZjZf+X28JkuumS0EHIn88k8zs3XTPD8eubAclQ0f5u7fuI/yHa7aul/s2PRCC4RnkLKIu1+OijXthQLHf4VS+a2FAn6HJ6tzZde5DT/4mYC3zWxltItyhGt3zYDNgI3NbNr8hKpkdvfX3f2UdK32SztRuPsFKP7oB+AcM5s5fc+6ooJ1/6tCvmAypO6VQbRoP7YhRfzPKDAI5H/5P1QN83vgXFLhGJSCsA5/xVYZNpD1q7BmrYQyZ1xPlpovHVuCJvBZRIuZV5EicyEwX+rfF1n8/wY8gPL6PkN9udUb+pEjn+xngIPK/4/yebQUL2l331xk4cytzLuTipek11cgl6EBwMKpbzmknM/dBPPifGBTFAA3ArlNAHRLP+dAgbRfI1eGzm39j+qYJ8hP+0bkPnEpWgwfC/wJBf7WKmcm7yCkjA8D/o/Srh9a/HyAKpTOnvXXWZ12YVIKVZQ5ptgdzCuoTo3y3J9f03XN5Z0RueS9Qetc9QcgX/130XPmepRJprjH1T6fo01arXYBokUb39ZAqeqVlKlpkAX3LWD/dOyi9DC4gsw1ofweVcmLMpj8ESmxpwMLpv6iiMl1jRQualTOgS3Sw2ozFMB1f2rzpuPLJ6XrTLJAz6plprVyvTUlxTopXB8As43hvMoK2yA3lKdQUOEaaLH2Z6R0756Ny9PIdUPuQ7fXoRCUrtV6KOC3T5L9j2jhtkg2ZmaUlnQvpLg3LLVe12dIr3ui4OV/ooXlsHTPWLtGGfN7xjbIh3zPdM/4BBkdyvnf9yMLAK75Gp+GCmF9BlyJ/N8PQ4aSnZDFeUkUj/AMNVQuLl3jGdLPn6Hg5f8jFcVK/f3T3H4S2DHrr91oEm3SaxH8GXQozKyzpy3OtB39NfCZy7UCMzsfPWj3cvdvzOwUVPymO3rQ1hkweTpSUM5BVv65Ucq7jdz9hbTNezdSEHZx9/dqkrMcHLcdMKe7n5Fe90VKQCdUjvzlcpBW/n+qmuSucgRKO3kHypV9IVKEfwdc6+6XNfice6Kt68rS9ZnZAsjq3A1Zxf+HijMtBPzG3S9L43ogH+LN0udYzusN9NweBR5+7O7npr5VkFvFEsgV5DvkXtYVKe8vADe5+3FVy9uIwnUp+9kLWXkPQn7Hy3lNwcqZjGuhReYT3pJqsh9yw7kHuMDdX8rGF5+l0nlRcnnbEs3p/uh6bpCG3YIs5Cei+Jl30XzfIM3lyu4ZJXmPQQWEznf358xsUWQl74OKzl2Vxg1Awc3voZ23jyPYM2gX6l4ZRIs2Lg1tOS+dvR6MAnM+QhbGQ1P/fbQEGXVFWRY2ys6rJdUgsBgKSl0n61smyfciLcFFqyFrdF1y5hbRPZGf/vXAIaVxW6LsFfeTXCxqnBsb0VJ972yUBWR6YBEUPPskst7tjgqE3NzgPXZHVtJKC/Gkv70A2s6/D1gcVZi8FqWP2y2N6YEUmiuouZw6WjQ8jnZ4jiodWwpZHD9J8/p+Wrb8n0QLudrmyhg+U9mKXnvquzQPXkW7EgNLx/qlOX0BpcDJ8mepWOa1kFK+Z9bXBynl96OdodnSz6WpP2j5dFQkaBeynTS06BySrvEuWf/+qFjWbdQclB9t0m21CxAt2tgasl69nZSSBZDV4l2UZ3YbFLD1Q7pprp8UrDtQ8ZWh1LBN2uAzrIS2yHtnfZYeUEORn25ZOag6T3K+tXs6smY9TkuxnblK4zdHfq8X1nhdeyYl9nXkK/wdsER2fIqk1J6L/Ec/TfOj7OayPqWsKBV/jraU88cKxQDtUDRFVUFkxX0MuTjN2eD4bECP7PVpaew8Vck4gZ+rU6Pfa5RniaQc/i2f1+nYbkhpP6QO2RrIWiwkPkcFmPJjaydl9gFgw7auecXyro4q5a6a9eWGiUWAXyPr/sZZ/6HpuzpbVbJGm7xa7QJEizYuDVninkI+478mWcjTsW7IgvQDyp+9JbKUnkmLUl5lwZXRFgAopd1QZIXukvV3SUrlUVXJNw7yz4KyOyyNFg8bIN/bpxhdOV+9bgUGBXa+nBTuAamvU/l/jtJTboh8Ra9o639V4+dopJxfkxTaXDGoxQ+3wbHNkdvVg7QE+bVaBKNA1QvR4q53e8o6NpnHNk+baS6U5FoS+WFfQSqSlh3buMp72zjIOqaFxJppvlzYDNcb6Ivcq6alxXLfauGLdjoPb3AvmaHuax1t0m3hYx50GMxsaVT0YV7gPHc/KTs2NcqX/K2772Zm3dz9+3SssgImJd/Fo1CqtQtScYqbkF/5QHe/P43pgRSxiz35kNaJme2ErvHzKHvCf1P/eshvuAdy93izdF6lPuWl6zwnWkgUacyOcfebyuOyc9dBwZPLuPu/qpJ5XEg+5xei7CUHIQv/HsApVV7fJEt+jXdCC7VvUfGXW1P/VminChQU93aD/83awEPu/p+KZV4fmAEpXleO6R5QSpU5h7u/3d6yjg9m1hu4HO1QnePuL5SO1xbTUcbMlkTZYZ4BznX357NjvYHnyt/JOjCzHdG9bh53/6CYOymF4zoofuKZbHxnlOm2dtmDSZvIYx50GNz9abR9+wXQNynqxbGvkOvFT9Pr77NjdSjlSyIr//lmtlN6aG6NFJtfmdmvzWx/4GaUPvG3Vcg4DryNrOMLk90f3P1ulLLtU+BhM5s5P6lGpXx15CLUF20xP47yUm+R5CrGzVaci2ISXkR+6E2Fu/8fUnSHI1eWKdz9RFcVxM4Vy1Jcu8HIFWV2lP7walMlVdz9T2ghMRK4y8x65YpLWsBdU4VSXpL5DLS7NgCl9HzVzJZtdE5JKT8QeMTMZqpC3nElKYj90E7KyWY2b+l4UyjlAO7+HJJ1KWCgmS2WHXsmKb+V6R5j+FtPop22E8xs9mzeToGMEBvkg919RCjlQRWEYh50KJL15efp5cGFcp6KUyyOUiXWJVuhFJyG3G06oS38q81s37RYWA25KyyAKg++h4Jaf6ha8WrjgfV3VDH1JeDeXEFx93tQYNctwMdVyFgmKVHFdT4FLWg2QFvQ/07yPQoMStZczOxWYGcY9T/aCSkNb47+F+onKecHo2C5N7L+ypWvlKlmG1RKfRuU3q4HcKmZHZTk+hNKifc3GhRdqVqZMbO90AJ+a3dfCS0qforSqhZjrPiZKeX9UbzK4e7+YZUyjwvu/izKhvQZ2bxoRsZhIVHJnCjdL3Yys6NNRYQ6ubLZ3IDif35lZmub2Wbo/jYDcoUMgsoJV5agQ2JmS6FgvhmRlfRrlPJqRVfqrVEP3Irl2g5tj66PfLLnRrm9BwD7eku1uy7AlO7+ZTqvMneb9Pdyq/PawHQocPLv7v5VWvBcjB5QqzVSVOrcPk9KeaE0vuDun2THFkWK7XYoGG1KlFt7eDq+MnIxGlq54BNAXdfZzLqjwlJvuvv5ZrYJsuKfiKznA4E93P2KZpA3+/uDgc/d/VQz2xq5uB3u7peYqtYOK8uZlPLBVJgqc0KpKyXihGBmywP7oLz8VS/Q8kXXIOBAdE9eDaWl7e/u/zWz/VBc0lrI/eZ9YHOvOIVjEBSEYh50WNIW6c1IoTwD5aceWbFPeefkZtAJcJRecC13XzMbMxtScHYFdnL3a1N/qzzKVchbxszORBbkT1EQ5f3ARe5+S9r6Px8p5328przqZcxsLuSv/0t3v8NU0n52YFtUJfN+5Fe8Agq6vTDtSFS6+OlotOGPPyfa2h+Jitf82t3PM7M+KI82yLf899VKO0q+0b47ZlYUrbkX3R+OcPdfpwXxkcAIdx+cjd8LKeW7N7tSXlDnPWN8qWMhUVLK50A7Ooej2Jk5URDqf4Cd3f21NG4RVIDsf0neuF8EtRCuLEGHJQVAbQ88DPyu8F2sUCnvnllTpk8PgneA+fOtW3d/F5X4BvitqUAIxYOjRqW8H3Lx2BRYEW07O3CAma3j7k+ian2dUVGkWmjgcjM1cgX62sxWQK4KVyDXoItQcOpH7n67u59XuAnFQ7ZtSlv+m5vZ/ma2sru/mVxrFkW+/FenU4rftwP+UJPMnTLla24zmzId+jOqNHkbspT/OvX3AFZGi7biPbZE+aqb3lKe01GUcpCs+fxqT8xshfRdL+bFEWiefgG86u4/JEV8WbRovzLtsOHuL7r7J9kiIu4XQS2EYh50aNz9CWDvGiwym6CgMsxsCAqI7IosMh8BeyRrY8EHKFPBqcBRlgVE1ciSwMPpGn7p7i+iinfTIx9dgEdQYOWO9YjYynd/yfT6RaR83Yoy2gwDjnP3udA29JIN3iO2o8dApsicivz2+wMPmdmpacfna7RwW8PMegLHoh3XG4rdiCrlLblinYAylvROh+9GC8zXgXfNrKuZLQhch6qmnpi91VOo6NdNVck+OVLFQsLMzgUGlb7rL6GUncsjd73CbfBtVOBtPuAGM5unJG9TuwgFkzahmAcdniotMhkbAoeY2f1Icd3K3Ye7+2OoUuaWwBFm1sfMfgacTIs7wE+AuSqUdTSrc9rWnxZZn4u+ru7+Mlo8bGFmc7t4wWvIClKSty9wbXI7wN13QP7la7n7QHf/Sxr6DTUFpnZE0jzAxGxo52Rdd18cVUPtj7LdfIN8tf8IPIHm757FuVVbFzOl/PQk4yVIES+CZ3dDgajnosXatchivpJngdbu/l9PqUuDjo27DyRlUjGz+Uwpc29F9+KeKPvK1NkO2jvAKmjeNGUgeDB5UqmVIwjai6q3dt19P1OA5JqoDPwr2bEzzOxbYBNkvXsVKTabAlOhTCzDq5K1FOS2MLKOv21m1wL3mNlWrswaxcJmBEoj9mX+PjVbnR8HXgN2MLMf3P0Kd78TRuWwnwvFGcwInFefmB2H0g5TL6A78s1+FsDdr0yK+xkozee1yC1gduDWtFirzQ/XzFZDrmx93f2fZtYtLS4WR4uH9VH1xsXR9/OxumUO2oekhH/vCtjsixaQG5vZve5+rykI+EZghJkNdAW4d3bVadg0vUcEegZNQSjmQTCOZEFMU6DvzitIWdwSeM/MrnL3/wG4slhcg3yhv0dFNTxtuxcuL+0t7/7AP13534s0jn2BmczsZqRoHY8s0dOiYL7hyAL5IQ1S31VBI5ckd3/LzPZGPuT90v/i8nR4Q+SCMwIVDfohHrJjJ7M6DwI2Qj637wG/o0U5vyIZ1U9FlUgPSrtChSJTZSahcsDj9Ch14DNmthz6HhbW0ReTrE8hd5XiPSLWYBIjzYuimNza7n6jmd2DsmPtaWb3u/tfMoV9hJkd5ik7T0HcL4JmIbKyBME4UPJpbaU4mtlFSLG5ABilnJvZzO7+Qfq9Dwq03AhYz7OKcu0k7zzAP5DF/nS0QBiClO6FSbm/UcrJHmnMJ8hf+0u05T+8Sr/9Mmb2C+DD3NXAzGZHBW3mBs5299+Z2U9QLuK/hkV07JTm8jbI3eME5G+7JwpUPteV57k4Zz9U/n2Tuv1vzWx6d//MVCX1ZZR7fylkEb0HLS6uB/Z09zvqkzRob/LFmpkdD+yC0ru+Y2Z3AUsgt6b73f17M9sQuAM40rPMPEHQTIRiHgRjoXTz748yO/wHeNDd/576L0TK7mWoQMWFKE/5qun4/MhX93xXIZwq5F4KBcU9glJKvuTul6ZjfZCVeTpkNX8DBU06NSm4JYWxO9qNeA442d0fzsbNiKygH6FS6xdlx8JSPo6Y2VqoGu0T7n5l6uuHUgreA1xQUs5rz59tZjuh9J4HuvtLZrYMsBXwGPBAUti7onR4p7r7LXXIGVSLmS0OnAScV9yTU3+hnO+KlPPhZrYSmvOxeA+aklDMg2AMlJTyE1ChoHtQlP9rwNXufnU6fg7yV+yMlMbVkpWmk1ecXz2Tf2m0pTsvUlTOzo6tDRxEspgXPtvpWJ3Fgy5Alv7/oK3nN5J8D2VjbkYpz25CLgtxIxsPzGwWlGZ0JpQP/tzsWKGc3wVc4kpLWhyrNX+2me2LFPM3USaeV6yllkA3FMNxHXJnWTkWaZM+aU5sj5JZbOHuHxQ+5+n4ncBiqGrqHcU9OHbWgmYlsrIEwRjIlPLeyH1iU1dp8s2RH/beZrZrGnswKkO9B1IKvk83/5HpeOUPgeRfvhsqILSJmS2RHbsf5SfvhgJVR2XpqFKhKf5m+n0D5Af/XdpZ2B75Ph9hZqunMV2Q282ewMBkxbXR3zloC3d/H9gCuX38vDQvrkC54XdFAZT5eZUp5TZ6/nrc/WK00JwNGGRm8yelfAqUvvQOVBBrVa85k1DQPjSYFy8BP0XpD5cHSPfebun3DVC62t3ze3Ao5UGzEhbzIBgLZrYzUrg7oVLNhQ/5UsARKCPIJYXlPDuvadwqTDnAr0JZN8519+ezY71RcGrdvsObIXegN1yZbbqkQM4lgGtQLu13UOaVnkBvbykqFXmHJ4CxzIuNgTvrnsNpQfaiu3+c9fVDC4cPgENdpdVXBtYAzvSo9DpJUnJ3WwhlC/ovquZ5H4o5OCkLUM4t53GfCDoEYTEPgrEzDOUeXwxZZQBw92dR0OTrwHFmVrYuNoVSDuDuz6HFxVLAQMsKHLn7M4WCW6VMJUv5KsgHfzugqOBYuP8MRb7QDyM3odeAZUMp//GMZV7cUbfVOfnBXwMcbCpsVMh2BXJzWgc43cwWdPd/uvtpHpVeJ0mSG1WhlJ8B3A48iRaVKyM3woWAw01ZegrLeZf0e+X3uCCYEMJiHgQZbSl6ZrYe2t5/Czir5O+8LHoonNRMyngjkpX/UuBt4BBXeepaMbNfotSM7wJHI1eEbdz9qaS8dyoUxPz6hkV04tGM86IgxW6sBtyJrPrFjlVXlNZxOhTrcUx9UgbtSYNMQuchV7apgUWB45AP+b3AX4GnUaD9w43fMQial1DMgyBRuvn3QUGRoGIqI81sI5TB5C0U/f9Qg/doGveVtjCz5YF9kM9lpdZmU271h939mSzLx31I4brdlGv4QJSy8Rh3fy63rGc+/7UGIU6K1Dkv0t9vc/fDzM5E1vHb0cL4czP7KXAi8Dfg2tg5mfRJAevbAS+7+1mprxuwI1pYrocC7/+J7inH1SVrEEwooZgHQYmkBGybXnZCVTu3SkriJsCxyK/xEu+g5bzrSH1nLbnV70IPzRfSQ3UocIK7X5/GbQPsDXyFlPOhVcgX1JcSsbQo3h1l3BkBPOOpkJSZnY6U89eAW1FdgG9R3EetaRyD9ifLJNQLxRGcnB2bCrgCBY3vknaAnm92I0kQNCL8rYIgw8z2QFlM+iK/xXWQEn67mc3l7rejKojLAWvXJuiPpMhkUqUi4+6vo+wvSyKf4cVSYNYIVMGxGPcH4NfANMAlZrZgVTJO7tQxL9LfLZTywcAg5M40D3CpmV2dZDoSVSXthSzlI9CCuRaZg2rJMgl9CGxlSgVbHPsa+BiYIy3Qnq07PiIIJpSwmAdBhpmdBczo7rtmfVMB9yNrzBqpbyXg8bDIjD8pC8zlyFJ+IXAMcKK7P2tm3d39mzTul0B3ZDUPpWsSJ2VfuQHY2t0fSi5M66BKpNe6+75p3DTIr/zdpJRHrMFkRMrS9FvgeeAcd3/azKZFqTJfdffdahUwCH4koZgHQYaZ/Q5Y2N2XSa+7uqrF7YRcWPq4+9vZ+Kb3KW9GknL+GxTwuSkKOvwSGImysjjyJz40sq9MHqT4gtOApdz968ytpi9wNbCRuz9YOifmxWRIclX5Pdo9eRy5G84DrJQysUQMStBhCVeWYLJkDGmzrgemMVWTw92Hp/7P0NZ5q5t9KOUThrs/A+yFKpI+ghSvfYCBKDPLccDhoZRPVryH8lEvA62KGT0HfEFLMPYoYl5MnrhS1W6DFvPTAfe6+zJJKe8WSnnQkQnFPJjsKAWabWBm25jZwunwo8BjwDZmdriZTWlmcyGl8XVk4Q0mAkk53wlVHp0N+MDd73X3P7r7DVk+6lC+JiFyv9884w76fj0ADCjyUCc+Q5Vr43kVjMLdXwC2BLoCyxexKCluJQg6LOHKEky2mNlpKDXfe8DcwMHu/iszmw1ZbDcAZgLeQNkfVkxuLWHBnYgkt5Yih/bBzZRDO5h4mNlP3P2T7PV+qCBMFxRj8L6Z/Rw4DO1OXYu+mweiAl/Lxw5VUCbdPy5BQfq/dPd/1yxSEPwowgIRTDYU1jkT8wNrAn2AVYAjgfPM7Fh3fxc4JPXvBRyAlILhKdAslPKJSLKc74usom/UK03QHpjZxcAjKfc4ZnYiyr4yE7AZ8LCZreHutwEnA68C5wMnoLiDFSPLRtCIdP/YD/mbfzaW4UHQ9ITFPJgsKLmvTAvMjvIgH5v1DwDORUGeF7r7F6X3iEDPdqSuHNpB+2NmC6CsGR+hdKQnAme7+5Pp+APAAsCO7v631Dcr8APwcWRfCcaGmU3p7t/WLUcQ/FhCMQ8mK5Klbi20hf5flJrtjez4AOAsYDAwyN2/qkPOyZXIpjBpYWYbAI+4KnXOA9yHCkd9Cuxc+u49AMwH7Ar8I/cVjsVaEASTC+HKEkzS5NlXUvGg/sCdwM0o+0M/M5upGOPuxfb5GsDXlQobEEr5pIOZ7QD8BdjRzHqkAlNro9R2KwIzpnGdAdx9TeBl9P1cMn+vUMqDIJhcCIt5MFlgZsuiDCB/d/ebUt/ByJ/1DGCIu3+YjS/cKsKCGwQTiJmdDBwBHAxc4+5fmNncSPn+DNjG3d/M3cTM7ALgoHAbC4JgcqRL3QIEQXuTqnT+DRgOPFP0u/s5KR70JGCkmV3u7u+lY6GUB8EEkNzFLnf3N939uLRrdV46do27v5FcXO4BrjezX+TKubsfkMZGTEcQBJMd4coSTPK4+yPIYjcSWDtZ7Ipj56CS8Ceh9Ij5eaGUB8F4YGaLAhuR5ft392NQzMZ5wM7JreUNYF3kznKtmc1TVsJDKQ+CYHIkXFmCSZpSNpYBaFv9CuA37v5mNm5b4MbI+hAEE0Y5QNPMtgD+5e6vpNeDgMOBg2jt1jIU+L2771291EEQBM1FuLIEkzR5SXd3P9/MuiDrOWZ2ibu/lcbdkPoiJVsQTBgOo4I5ZwFuBG40syPd/VV3Pzq5jp0HeObWsiBKoxgEQTDZE4p5MMlTUs7PNjMHBgDTmdnJedBnKOVBMP6UrOUj3f0dM1sNBXmONLOjM+XcgXOAaczsAnd/P71H+JQHQTDZE64swWRDya3leKA3sEX4kgfBhJMHSZvZ5sAcwLPu/pCZLQ08DNwGHO3ur6ZxFwJLAGvE9y8IgqCFUMyDDk2jwiNjyqZSUs6j0mQQTCTM7FTgQOANYFHgTOBoYHHgEeBW4JhMOY+UpEEQBCUiK0vQYSkp2TubWT8YczaV5NbSpTTO2l3YIJjEsOQwbmI2VDRoXXdfHNgd2AM4F3gBWAnYGBhiZrPn7xFKeRAEQQuhmAcdkvRAL5TywahQ0NSlh/5o8zud90P6vZ+ZLRZ+rUEwfqRFcaFQ9wK6oxoBzwK4+5XAocAOyJ/8BVT1szMwqlZAKOVBEAStieDPoEOS+bQOBHYBNnX3x0tj2nRxMbM9gUuALZDSEATBOJItigehvOXzI4X7d2TKeQr0PAOYHtjN3ddO54X7WBAEQQPCYh50SNL2+ZTAmsB57v64mc1vZtua2X1m9lczmz8bmyvl/YGzgL7ufmttHyIIOhj5LpSZbYMWxRcBFwI9gX3MbKFijLtfhYp3zUhKp5j6QykPgiBoQAR/Bh0aM/stMBtwPbANMAL4L8q40sndly2N74+qEPZz9xsrFjcIJgnMbC1ga+CJ5LZCivE4ErgHuMDdX8rGR6B1EATBOBCuLEGHYAwP9FuAndF2+TnAXe7+hJntDmxpZlO4+3fpPQYAJ6At9ZsqEj0IJinMbBbgMmAm4P+Kfne/IsWDHolyl1/i7i+kY0X2lVDKgyAIxkAo5kHTU8q+sgvyZ50R+BNwi7vfaGazufu72WnbAu9nSvmsyKK+byjlQTDhuPv7ZrYF+v793Mzuc/eh6dgVya/8Vyht4gvZebE9GwRBMBbClSXoMKTsKzsDvwcWABZBFvPDUhrEaYBlgGOAmYFl3X14OrczMIO7f1yL8EEwiWFmSwJXoWws57r789mxjYE7I+NREATB+BHBn0HTUuRJTr9vinxaN3b3g4HLgZ8CT2bb40sDuwKfA8u4+/AsZ/mIUMqDYOLh7s8B/YClgIFmtlh27A53H5EWxEEQBME4Eop50HSY2a5mNlfhl5q6ZwNecvenUjaIq4ED3f06M5vazJZ29weBQcA27v6DmXUpcpYHQTDxcfdnkHK+OHCymc1bOh4W8yAIgvEgFPOgqTCzvki5PtDM5sj8UmcGPjWz1ZC1/Eh3H5KObQRsY2bTu/v/ZdkfQikPgnbG3Z8F9gM+Q37lQRAEwQQSPuZB02FmRwN9gb8D57j722bWG3gMBSz/wt3/kMZ2B24C3gb2igCzIKiHSIkYBEFkOe6ZAAAHg0lEQVTw4wmLedA0mFk3AHcfBFwDrAccbGZzpi3zI4BvgSXMbEkzWx24Gbm57FNyfQmCoEIiJWIQBMGPJ9IlBk2Du38PYGZ7omqC3YAdUt8ZwMVIMT8Z2B14H3gHZV/5wcw6h09rENRH7FgFQRD8OMKVJaidYgs8/b4fcAHQ292fS24t2wL3AWe6+3upwMmsKPvK68lSF4GeQRAEQRB0aMJiHtROppSvBswLbJZSseHug5J3yraAm9mv3P2/yFpOOi8CPYMgCIIg6PCEYh40BWa2IXA2MB1QBHZ2c/fvM+W8LzC9mR3p7h8V54ZPaxAEQRAEkwIR/Bk0C68ADwPTA1uBfM5LAaF3A52BKBQUBEEQBMEkR/iYB5XTVjo1M5sTOBpYBbjS3c9J/d2ywNBIyRYEQRAEwSRJKOZBpeQKtZmtgYI4PwSGuvvHqXLgEUBv4Dp3PzeNHRXcmQeLBkEQBEEQTCqEYh5URin7yunIZaUT8C4wDNgjFROaFzgcWAr4i7ufVJfMQRAEQRAEVRE+5kFlZEr54cDOwM7uPi9wPyomdLOZze3urwGDgf8Cc0bRoCAIgiAIJgfCYh5USvIjvwq42N3/lLKx/AG4ElgN+A7YKlnOZwPed/eR4b4SBEEQBMGkTijmQeWY2cbA88AswE3AKe4+xMwGA4cCbwErufu7aXwEegZBEARBMMkTecyDdsPMOrv7iHK/u9+RjvcDHkTWcoDXgduAF4APsvGhlAdBEARBMMkTinkw0TGzTsilfER6vRWyjr/r7jdlQ2cCFge6IheWdYFH3f30dF5DxT4IgiAIgmBSJII/g4mKmf0JOIM0t8zsNORT3g/4k5ldZmZzp+H3IIX8aTN7ClgIOCudZ6GUB0EQBEEwOREW82Bi8w+kXH9pZjeggM7VgZeAZVH1zmnNbABwK+CpH+AEd/8hLOVBEARBEEyORPBnMNEogjTNbE9gCHA1spzv6e7D05gVgQeQUj7A3d8vvUco5UEQBEEQTJaExTyYKJQU6uuAz4HfA68APYBP0phHzWxN4F5gBjPbtci+AhBKeRAEQRAEkyvhYx78aJKlvAj0PAy4GHgR2An4GXCgmXV19xFp7KPARijo8/223jcIgiAIgmByIizmwY+mSGdoZmcAuwEHAF+7+3VmNjVwCTDCzAZlPuQPAmul8yJPeRAEQRAEkz2hmAcTBTNbC9ga6Ovu/yj63f2ylD7xYsDN7PTC3zwbE0p5EARBEASTPaGYBxOLOVHqw38VHSnlobv7b8zsS+Ba4B3gippkDIIgCIIgaFpCMQ9+FIXyDXRHMQtW9Gc/f4Gqea4P/K0mUYMgCIIgCJqaCP4MfhTekm/zAWBe4KCiP1PYtwc2cPd7ko95LAiDIAiCIAhKRB7zYKJhZnsBFwK/AW4HvgeOBGYBlnb3H2oULwiCIAiCoKkJxTyYaJhZZ6AvcA5KhfgB8in/ubsPj+JBQRAEQRAEbROKeTDRMbOZgJ7AcOA1d3cz6xIW8yAIgiAIgrYJxTxodyJPeRAEQRAEwdgJxTwIgiAIgiAImoDIyhIEQRAEQRAETUAo5kEQBEEQBEHQBIRiHgRBEARBEARNQCjmQRAEQRAEQdAEhGIeBEEQBEEQBE1AKOZBEARBU2FmI8zsWTN7wcz+aGZT/Yj3usrMtkq/X2Zmi4xh7JpmtnL2em8z23lC/3YQBMH4Eop5EARB0Gx84+5LuftiwPfA3vlBM+syIW/q7nu4+4tjGLImMEoxd/ch7n7NhPytIAiCCSEU8yAIgqCZ+Qcwf7Jm/8PMbgNeNLPOZnammT1hZkPNrD+AiQvN7GUzuxeYqXgjM3vAzJZNv29gZk+b2XNmdp+ZzY0WAAOTtX41MzvBzA5N45cys0fT37rZzGbI3vMMM3vczF4xs9UqvTpBEExSTJDVIQiCIAjam2QZ3xC4M3UtDSzm7q+b2V7A5+6+nJlNATxsZncDvYGfAYsAMwMvAleU3rcXcCmwenqvnu7+PzMbAgxz97PSuD7ZadcAB7j7383sJOB44KB0rIu7L29mG6X+dSb2tQiCYPIgFPMgCIKg2ehuZs+m3/8BXI5cTB5399dT/3rAEoX/ODAdsACwOnCdu48A3jWz+xu8/4rAg8V7ufv/xiSMmU0HTO/uf09dVwN/zIbclH4+Bcw9bh8xCIJgdEIxD4IgCJqNb9x9qbzDzAC+yruQBfuu0riN2l+80fgu/RxBPFeDIPgRhI95EARB0BG5C9jHzLoCmNmCZjY18CCwbfJBnxVYq8G5jwKrm9k86dyeqf9LYNryYHf/HPg08x/fCfh7eVwQBMGPJVb2QRAEQUfkMuQ28rTJnP4RsDlwM7A28i1/E3ikfKK7f5R81G8ys07Ah8C6wJ+BP5nZZsABpdN2AYak1I2vAbu1x4cKgmDyxty9bhmCIAiCIAiCYLInXFmCIAiCIAiCoAkIxTwIgiAIgiAImoBQzIMgCIIgCIKgCQjFPAiCIAiCIAiagFDMgyAIgiAIgqAJCMU8CIIgCIIgCJqAUMyDIAiCIAiCoAkIxTwIgiAIgiAImoD/B6TcsAsc5TtKAAAAAElFTkSuQmCC\n",
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
        "outputId": "f07f56d6-7c53-48a4-c16f-9c36bd971c1c"
      },
      "source": [
        "print(classification_report(y_test,prediction_labels))"
      ],
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "         0.0       0.90      0.86      0.88        50\n",
            "         1.0       0.98      0.85      0.91        48\n",
            "         2.0       0.96      0.94      0.95        50\n",
            "         3.0       0.98      1.00      0.99        50\n",
            "         4.0       0.90      0.92      0.91        50\n",
            "         5.0       0.98      0.96      0.97        50\n",
            "         6.0       0.94      0.98      0.96        49\n",
            "         7.0       0.91      0.96      0.93        50\n",
            "         8.0       1.00      0.98      0.99        49\n",
            "         9.0       0.93      1.00      0.96        50\n",
            "\n",
            "    accuracy                           0.95       496\n",
            "   macro avg       0.95      0.95      0.95       496\n",
            "weighted avg       0.95      0.95      0.95       496\n",
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
        "model.save(\"model.h5\")"
      ],
      "execution_count": 69,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pIPRLiftdMMA"
      },
      "source": [
        "def main():\n",
        "  face_detector = st.container()\n",
        "  face_recognizer = st.container()\n",
        "  with face_detector:\n",
        "    st.title(\"Face Detection And Recognition WebApp\")\n",
        "    st.text(\"This face detector was built using the dlib library\")\n",
        "    html_body = \"\"\"<body style=\"background-color:red;\"></body>\"\"\"\n",
        "    st.markdown(html_body,unsafe_allow_html=True)\n",
        "    html_temp = \"\"\"\n",
        "      <body style=\"background-color:red;\">\n",
        "      <div style=\"background-color:red;padding:10px;\">\n",
        "      <h2 style=\"color:white;text-align:center;\">Face Detection</h2>\n",
        "      </div>\n",
        "      </body>\n",
        "      \"\"\"\n",
        "    st.markdown(html_temp,unsafe_allow_html=True)\n",
        "    image_file = st.file_uploader(\"Upload Image\",type=['jpg','png','jpeg'],key=0)\n",
        "    if image_file is not None:\n",
        "      our_image = Image.open(image_file)\n",
        "      st.text(\"Original Image\")\n",
        "      st.image(our_image)\n",
        "    if st.button(\"Detect\"):\n",
        "      result_image = detect_dlib(our_image)\n",
        "      st.text(\"Results\")\n",
        "      st.image(result_image)\n",
        "  with face_recognizer:\n",
        "    st.title(\"Face Recognition\")\n",
        "    st.text(\"This face recognizer is used to distinguish between simpsons characters\")\n",
        "    html_body = \"\"\"<body style=\"background-color:red;\"></body>\"\"\"\n",
        "    st.markdown(html_body,unsafe_allow_html=True)\n",
        "    html_temp = \"\"\"\n",
        "      <body style=\"background-color:red;\">\n",
        "      <div style=\"background-color:red;padding:10px;\">\n",
        "      <h2 style=\"color:white;text-align:center;\">Simpsons Face Recognition</h2>\n",
        "      </div>\n",
        "      </body>\n",
        "      \"\"\"\n",
        "    st.markdown(html_temp,unsafe_allow_html=True)\n",
        "    image_file_2 = st.file_uploader(\"Upload Image\",type=['jpg','png','jpeg'],key=1)\n",
        "    if image_file_2 is not None:\n",
        "      our_image_1 = Image.open(image_file_2)\n",
        "      st.text(\"Original Image\")\n",
        "      st.image(our_image_1)\n",
        "      our_image_1 = np.array(our_image_1,dtype=\"float32\")\n",
        "    if st.button(\"Recognise\"):\n",
        "      model = st.load_model(\"model.h5\")\n",
        "      result = class_name[np.argmax(model.predict(our_image_1))]\n",
        "      st.text(\"Results\")\n",
        "      st.text(result)\n",
        "  if __name__ == 'main':\n",
        "    main()"
      ],
      "execution_count": 70,
      "outputs": []
    }
  ]
}