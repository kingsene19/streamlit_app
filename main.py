{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "name": "main.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6_xbATYNUs-v",
        "outputId": "d5a585dd-3ef0-4a3b-f058-2e83a074a304"
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
            "Requirement already satisfied: ipykernel>=5.1.2 in /usr/local/lib/python3.7/dist-packages (from pydeck) (6.4.1)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck) (5.1.0)\n",
            "Requirement already satisfied: jinja2>=2.10.1 in /usr/local/lib/python3.7/dist-packages (from pydeck) (2.11.3)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck) (7.6.5)\n",
            "Requirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (5.3.5)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (1.0.0)\n",
            "Requirement already satisfied: tornado<7.0,>=4.2 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (5.1.1)\n",
            "Requirement already satisfied: importlib-metadata<5 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (4.8.1)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (0.1.3)\n",
            "Requirement already satisfied: ipython<8.0,>=7.23.1 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (7.28.0)\n",
            "Requirement already satisfied: argcomplete>=1.12.3 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (1.12.3)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (0.2.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck) (3.5.0)\n",
            "Requirement already satisfied: typing-extensions>=3.6.4 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck) (3.7.4.3)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.7.5)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (2.6.1)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (3.0.20)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (4.8.0)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.18.0)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.2.0)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (57.4.0)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (4.4.2)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (1.0.2)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (3.5.1)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (5.1.3)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.7/dist-packages (from jedi>=0.16->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.8.2)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2>=2.10.1->pydeck) (2.0.1)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (4.8.1)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (22.3.0)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (2.8.2)\n",
            "Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /usr/local/lib/python3.7/dist-packages (from nbformat>=4.2.0->ipywidgets>=7.0.0->pydeck) (2.6.0)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect>4.3->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.2.5)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.1->jupyter-client<8.0->ipykernel>=5.1.2->pydeck) (1.15.0)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (5.3.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (1.8.0)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (5.6.1)\n",
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.12.1)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.5.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.7.1)\n",
            "Requirement already satisfied: entrypoints>=0.2.2 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.3)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (1.5.0)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (4.1.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.8.4)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.5.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (21.0)\n",
            "Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (2.4.7)\n",
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.7/dist-packages (0.89.0)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.1.0)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (5.1.1)\n",
            "Requirement already satisfied: tzlocal in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.5.1)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: astor in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.8.1)\n",
            "Requirement already satisfied: attrs in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.2.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.23.0)\n",
            "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.17.3)\n",
            "Requirement already satisfied: click<8.0,>=7.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.1.5)\n",
            "Requirement already satisfied: blinker in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: gitpython!=3.1.19 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.1.24)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: pydeck>=0.1.dev5 in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.7.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.19.5)\n",
            "Requirement already satisfied: pyarrow in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.0.0)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: watchdog in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.1.5)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.0)\n",
            "Requirement already satisfied: base58 in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.1.0)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: validators in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.18.2)\n",
            "Requirement already satisfied: jsonschema in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.6.0)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.11.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit) (4.0.7)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit) (3.7.4.3)\n",
            "Requirement already satisfied: smmap<5,>=3.0.1 in /usr/local/lib/python3.7/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (4.0.0)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.21.0->streamlit) (2018.9)\n",
            "Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.7/dist-packages (from protobuf!=3.11,>=3.6.0->streamlit) (1.15.0)\n",
            "Requirement already satisfied: ipykernel>=5.1.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (6.4.1)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (7.6.5)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (5.1.0)\n",
            "Requirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (5.3.5)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.3)\n",
            "Requirement already satisfied: argcomplete>=1.12.3 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.12.3)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.0.0)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: ipython<8.0,>=7.23.1 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (7.28.0)\n",
            "Requirement already satisfied: importlib-metadata<5 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.1)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.5.0)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.4.2)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.0.20)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.0)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.6.1)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (57.4.0)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.18.0)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.0.2)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.1.3)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.7/dist-packages (from jedi>=0.16->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.8.2)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (22.3.0)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.1)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect>4.3->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.5)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.3.1)\n",
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.12.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.8.0)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.6.1)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.0)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.1.0)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.1)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
            "Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->streamlit) (2.4.7)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (2.10)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (2021.5.30)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (1.24.3)\n"
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
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BciVMSajdKTD",
        "outputId": "4a31bcdd-e744-4044-ced7-48d3a6cccfd0"
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
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Found GPU at: /device:GPU:0\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "2021-09-30 16:39:31.387150: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:31.839412: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:31.840266: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.103568: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.104417: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.105236: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.106162: W tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc:39] Overriding allow_growth setting because the TF_FORCE_GPU_ALLOW_GROWTH environment variable is set. Original config value was 0.\n",
            "2021-09-30 16:39:37.106216: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /device:GPU:0 with 10819 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7\n",
            "2021-09-30 16:39:37.114786: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.115593: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.116335: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.117450: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.118275: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.119031: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.119811: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.120558: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-30 16:39:37.121241: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 10819 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7\n",
            "2021-09-30 16:39:39.739826: I tensorflow/stream_executor/cuda/cuda_dnn.cc:369] Loaded cuDNN version 8005\n"
          ]
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Time (s) to convolve 32x7x7x3 filter over random 100x100x100x3 images (batch x height x width x channel). Sum of ten runs.\n",
            "CPU (s):\n",
            "3.801010630999997\n",
            "GPU (s):\n",
            "0.04864265899999509\n",
            "GPU speedup over CPU: 78x\n"
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
        "id": "fWAE083VVJBi",
        "outputId": "7ecfa9be-a82b-4e33-bb21-830127063cdc"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive',force_remount=True)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
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
      "execution_count": null,
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
      "execution_count": null,
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
      "execution_count": null,
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
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_F3VGvVT2suy",
        "outputId": "26351630-b24a-4599-874b-3e3001ac1696"
      },
      "source": [
        "tuner.search_space_summary()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
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
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bt9QXts-oIaZ",
        "outputId": "85535c33-a3b6-43ca-830f-7be4730abfd5"
      },
      "source": [
        "tuner.search(\n",
        "    train_set,\n",
        "    validation_data=val_set,\n",
        "    epochs=5,\n",
        "    callbacks=[keras.callbacks.TensorBoard(\"/tmp/logs_dir\")]\n",
        ")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Trial 5 Complete [00h 02m 41s]\n",
            "val_accuracy: 0.8656770586967468\n",
            "\n",
            "Best val_accuracy So Far: 0.8703837990760803\n",
            "Total elapsed time: 00h 12m 40s\n",
            "INFO:tensorflow:Oracle triggered exit\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "2021-09-30 17:59:55.034 INFO    tensorflow: Oracle triggered exit\n"
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
        "id": "5rlWO6uXpNkf",
        "outputId": "db256d16-4543-4baf-a305-59dc2e2b6056"
      },
      "source": [
        "models = tuner.get_best_models(num_models=1)\n",
        "model = models[0]\n",
        "history = model.fit_generator(train_set,\n",
        "                              validation_data = val_set,\n",
        "                              verbose=2,\n",
        "                              epochs=5)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/keras/engine/training.py:1972: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.\n",
            "  warnings.warn('`Model.fit_generator` is deprecated and '\n"
          ]
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Epoch 1/5\n",
            "346/346 - 23s - loss: 0.5214 - accuracy: 0.8353 - val_loss: 0.5279 - val_accuracy: 0.8295\n",
            "Epoch 2/5\n",
            "346/346 - 23s - loss: 0.4647 - accuracy: 0.8552 - val_loss: 0.3911 - val_accuracy: 0.8668\n",
            "Epoch 3/5\n",
            "346/346 - 22s - loss: 0.4427 - accuracy: 0.8644 - val_loss: 0.3766 - val_accuracy: 0.8903\n",
            "Epoch 4/5\n",
            "346/346 - 23s - loss: 0.4101 - accuracy: 0.8761 - val_loss: 0.3804 - val_accuracy: 0.8943\n",
            "Epoch 5/5\n",
            "346/346 - 22s - loss: 0.4109 - accuracy: 0.8794 - val_loss: 0.3085 - val_accuracy: 0.9164\n"
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
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qgKvcpZAMU2o",
        "outputId": "5cd21f39-9fae-4adb-f4e8-566c26cbf49a"
      },
      "source": [
        "np.unique(y_test)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "data": {
            "text/plain": [
              "array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.], dtype=float32)"
            ]
          },
          "execution_count": 15,
          "metadata": {},
          "output_type": "execute_result"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p0-QCWiqO777",
        "outputId": "6f63ed3b-496a-434f-93a9-0e218ae1ac9e"
      },
      "source": [
        "test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)\n",
        "print(test_acc)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "16/16 - 0s - loss: 0.1423 - accuracy: 0.9496\n",
            "0.9495967626571655\n"
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
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 584
        },
        "id": "8_4iEn3vasS1",
        "outputId": "275648f7-7414-41af-a098-4e30c8e4eb16"
      },
      "source": [
        "predictions = model.predict(x_test)\n",
        "prediction_labels = np.argmax(predictions,1)\n",
        "cm = confusion_matrix(y_test,prediction_labels)\n",
        "print_confusion_matrix(cm,class_names=['bart_simpson','charles_montgomery_burns', 'homer_simpson','krusty_the_clown',\n",
        "                                     'lisa_simpson','marge_simpson','milhouse_van_houten','moe_szyslak','ned_flanders',\n",
        "                                       'principal_skinner'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x504 with 2 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Cr-WF6JfasZZ",
        "outputId": "ab275520-cb0d-4f8c-e14a-b324f064201f"
      },
      "source": [
        "print(classification_report(y_test,prediction_labels))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "         0.0       0.87      0.94      0.90        50\n",
            "         1.0       0.98      0.85      0.91        48\n",
            "         2.0       0.92      0.96      0.94        50\n",
            "         3.0       0.96      1.00      0.98        50\n",
            "         4.0       0.96      0.88      0.92        50\n",
            "         5.0       1.00      1.00      1.00        50\n",
            "         6.0       0.98      0.96      0.97        49\n",
            "         7.0       0.92      0.92      0.92        50\n",
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SMti_rv_oLk4",
        "outputId": "80a997c6-e245-468a-be06-a99fce578dd5"
      },
      "source": [
        "model.save(\"model.hdf5\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Model: \"sequential\"\n",
            "_________________________________________________________________\n",
            "Layer (type)                 Output Shape              Param #   \n",
            "=================================================================\n",
            "conv2d (Conv2D)              (None, 78, 78, 96)        2688      \n",
            "_________________________________________________________________\n",
            "max_pooling2d (MaxPooling2D) (None, 39, 39, 96)        0         \n",
            "_________________________________________________________________\n",
            "conv2d_1 (Conv2D)            (None, 37, 37, 64)        55360     \n",
            "_________________________________________________________________\n",
            "max_pooling2d_1 (MaxPooling2 (None, 18, 18, 64)        0         \n",
            "_________________________________________________________________\n",
            "conv2d_2 (Conv2D)            (None, 16, 16, 192)       110784    \n",
            "_________________________________________________________________\n",
            "flatten (Flatten)            (None, 49152)             0         \n",
            "_________________________________________________________________\n",
            "dense (Dense)                (None, 96)                4718688   \n",
            "_________________________________________________________________\n",
            "dense_1 (Dense)              (None, 10)                970       \n",
            "=================================================================\n",
            "Total params: 4,888,490\n",
            "Trainable params: 4,888,490\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
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
        "id": "pIPRLiftdMMA",
        "outputId": "df5f75ff-4154-4457-f34d-6c2457c8e5ae"
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
        "  model = tf.keras.models.load_model('/content/model.hdf5')\n",
        "  return model\n",
        "model=load_model()\n",
        "class_names=['bart_simpson','charles_montgomery_burns', 'homer_simpson','krusty_the_clown',\n",
        "                                     'lisa_simpson','marge_simpson','milhouse_van_houten','moe_szyslak','ned_flanders',\n",
        "                                       'principal_skinner']\n",
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
        "  if st.button(\"Recognise\"): \n",
        "    our_image_1= our_image_1.resize((80,80))\n",
        "    our_image_1 = np.expand_dims(our_image_1,axis=0)\n",
        "    our_image_1 = np.array(our_image_1)\n",
        "    our_image_1 = our_image_1.astype(\"float32\")\n",
        "    our_image_1/= 255\n",
        "    our_image_1 = np.array(our_image_1,dtype='float32')\n",
        "    result = class_names[np.argmax(model.predict(our_image_1,1))]\n",
        "    st.text(\"Results\")\n",
        "    st.text(result)"
      ],
      "execution_count": 2,
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
        "outputId": "b0360d01-0587-4864-856a-e757bd44cc55"
      },
      "source": [
        "from pyngrok import ngrok\n",
        "public_url = ngrok.connect(port='80')\n",
        "print (public_url)\n",
        "!streamlit run --server.port 80 app.py >/dev/null"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NgrokTunnel: \"http://acc4-35-204-14-67.ngrok.io\" -> \"http://localhost:80\"\n",
            "2021-10-01 09:11:39.316 Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/streamlit/legacy_caching/caching.py\", line 515, in get_or_create_cached_value\n",
            "    hash_funcs=hash_funcs,\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/streamlit/legacy_caching/caching.py\", line 308, in _read_from_cache\n",
            "    raise e\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/streamlit/legacy_caching/caching.py\", line 294, in _read_from_cache\n",
            "    mem_cache, key, allow_output_mutation, func_or_code, hash_funcs\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/streamlit/legacy_caching/caching.py\", line 212, in _read_from_mem_cache\n",
            "    raise CacheKeyNotFoundError(\"Key not found in mem cache\")\n",
            "streamlit.legacy_caching.caching.CacheKeyNotFoundError: Key not found in mem cache\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/streamlit/script_runner.py\", line 354, in _run_script\n",
            "    exec(code, module.__dict__)\n",
            "  File \"/content/app.py\", line 15, in <module>\n",
            "    model=load_model()\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/streamlit/legacy_caching/caching.py\", line 543, in wrapped_func\n",
            "    return get_or_create_cached_value()\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/streamlit/legacy_caching/caching.py\", line 527, in get_or_create_cached_value\n",
            "    return_value = func(*args, **kwargs)\n",
            "  File \"/content/app.py\", line 13, in load_model\n",
            "    model = tf.keras.models.load_model('model.hdf5')\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/keras/saving/save.py\", line 205, in load_model\n",
            "    return saved_model_load.load(filepath, compile, options)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/keras/saving/saved_model/load.py\", line 108, in load\n",
            "    meta_graph_def = tf.__internal__.saved_model.parse_saved_model(path).meta_graphs[0]\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/tensorflow/python/saved_model/loader_impl.py\", line 121, in parse_saved_model\n",
            "    constants.SAVED_MODEL_FILENAME_PB))\n",
            "OSError: SavedModel file does not exist at: model.hdf5/{saved_model.pbtxt|saved_model.pb}\n",
            "\n"
          ]
        }
      ]
    }
  ]
}