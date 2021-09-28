{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "main.ipynb",
      "provenance": []
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6_xbATYNUs-v",
        "outputId": "cfff4f79-9561-4fe6-d86e-3a166ef149f9"
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
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck) (7.6.5)\n",
            "Requirement already satisfied: numpy>=1.16.4 in /usr/local/lib/python3.7/dist-packages (from pydeck) (1.19.5)\n",
            "Requirement already satisfied: ipykernel>=5.1.2 in /usr/local/lib/python3.7/dist-packages (from pydeck) (6.4.1)\n",
            "Requirement already satisfied: jinja2>=2.10.1 in /usr/local/lib/python3.7/dist-packages (from pydeck) (2.11.3)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck) (5.1.0)\n",
            "Requirement already satisfied: ipython<8.0,>=7.23.1 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (7.28.0)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (0.1.3)\n",
            "Requirement already satisfied: argcomplete>=1.12.3 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (1.12.3)\n",
            "Requirement already satisfied: tornado<7.0,>=4.2 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (5.1.1)\n",
            "Requirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (5.3.5)\n",
            "Requirement already satisfied: importlib-metadata<5 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (4.8.1)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (1.0.0)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck) (0.2.0)\n",
            "Requirement already satisfied: typing-extensions>=3.6.4 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck) (3.7.4.3)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck) (3.5.0)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (3.0.20)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (57.4.0)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (2.6.1)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (4.4.2)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.18.0)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (4.8.0)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.2.0)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck) (0.7.5)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (5.1.3)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck) (3.5.1)\n",
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
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.12.1)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (5.6.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (1.8.0)\n",
            "Requirement already satisfied: entrypoints>=0.2.2 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.3)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (1.5.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.7.1)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (4.1.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.8.4)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.5.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (0.5.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (21.0)\n",
            "Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck) (2.4.7)\n",
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.7/dist-packages (0.89.0)\n",
            "Requirement already satisfied: validators in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.18.2)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.1.24)\n",
            "Requirement already satisfied: tzlocal in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.5.1)\n",
            "Requirement already satisfied: pyarrow in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.0.0)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.23.0)\n",
            "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.17.3)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (5.1.1)\n",
            "Requirement already satisfied: attrs in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.2.0)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: astor in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.8.1)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.1.5)\n",
            "Requirement already satisfied: pydeck>=0.1.dev5 in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.7.0)\n",
            "Requirement already satisfied: click<8.0,>=7.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: blinker in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.1.0)\n",
            "Requirement already satisfied: base58 in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.1.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.19.5)\n",
            "Requirement already satisfied: watchdog in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.1.5)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.3)\n",
            "Requirement already satisfied: jsonschema in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.6.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.11.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit) (4.0.7)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit) (3.7.4.3)\n",
            "Requirement already satisfied: smmap<5,>=3.0.1 in /usr/local/lib/python3.7/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (4.0.0)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.21.0->streamlit) (2018.9)\n",
            "Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.7/dist-packages (from protobuf!=3.11,>=3.6.0->streamlit) (1.15.0)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (7.6.5)\n",
            "Requirement already satisfied: ipykernel>=5.1.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (6.4.1)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (5.1.0)\n",
            "Requirement already satisfied: ipython<8.0,>=7.23.1 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (7.28.0)\n",
            "Requirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (5.3.5)\n",
            "Requirement already satisfied: importlib-metadata<5 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.1)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.0.0)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: argcomplete>=1.12.3 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.12.3)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.3)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata<5->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.5.0)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.6.1)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.0)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (57.4.0)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.0.20)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.18.0)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.4.2)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.1.3)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\n",
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
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.1.0)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.1)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
            "Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->streamlit) (2.4.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (2021.5.30)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (1.24.3)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (3.0.4)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (2.10)\n"
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
        "from keras_tuner import HyperParameters"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BciVMSajdKTD",
        "outputId": "d69dc410-d1b3-4d9e-83b3-cdcfd23e83f6"
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
            "2021-09-28 18:19:15.992391: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.004933: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.005693: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.519222: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.520148: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.520944: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.521753: W tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc:39] Overriding allow_growth setting because the TF_FORCE_GPU_ALLOW_GROWTH environment variable is set. Original config value was 0.\n",
            "2021-09-28 18:19:16.521817: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /device:GPU:0 with 10819 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7\n",
            "2021-09-28 18:19:16.524548: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.525531: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.526361: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.527505: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.528279: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.529014: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.529813: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.530703: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero\n",
            "2021-09-28 18:19:16.531411: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 10819 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7\n",
            "2021-09-28 18:19:17.241968: I tensorflow/stream_executor/cuda/cuda_dnn.cc:369] Loaded cuDNN version 8005\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Time (s) to convolve 32x7x7x3 filter over random 100x100x100x3 images (batch x height x width x channel). Sum of ten runs.\n",
            "CPU (s):\n",
            "3.78202464900005\n",
            "GPU (s):\n",
            "0.04381178100084071\n",
            "GPU speedup over CPU: 86x\n"
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fWAE083VVJBi",
        "outputId": "d9337b19-91e8-4a82-8ad4-a3499016df42"
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
        "hypermodel = HyperResNet(input_shape=(80,80,3),classes=10)\n",
        "hp = HyperParameters()\n",
        "hp.Int(\"filters\",64,256,step=32,default=192)\n",
        "hp.Int(\"units\",32,194,step=32,default=64)\n",
        "hp.Fixed(\"learning_rate\",1e-2)\n",
        "hp.Fixed(\"kernel_size\",3)\n",
        "\n",
        "tuner = RandomSearch(\n",
        "        hypermodel,\n",
        "        hyperparameters=hp,\n",
        "        objective = \"val_accuracy\",\n",
        "        max_trials = 3,\n",
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
        "id": "r3RAcb8soCu3"
      },
      "source": [
        "x = np.array(img_data,dtype=\"float32\")/255.0\n",
        "y = np.array(list(map(int,target_val)),np.float32)\n",
        "train_data,train_labels = shuffle(x,y,random_state=0)\n",
        "x_train = train_data[:11049]\n",
        "y_train = train_labels[:11049]\n",
        "x_val =  train_data[11049:]\n",
        "y_val = train_labels[11049:]\n",
        "y_train = to_categorical(y_train)\n",
        "y_val = to_categorical(y_val)\n",
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
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bt9QXts-oIaZ",
        "outputId": "80e9df65-2b11-4310-c5a9-3b8ffa9211d5"
      },
      "source": [
        "tuner.search(\n",
        "    train_set,\n",
        "    validation_data=val_set,\n",
        "    epochs=10,\n",
        "    callbacks=[keras.callbacks.TensorBoard(\"/tmp/logs_dir\"),\n",
        "               ModelCheckpoint(filepath=r\"C:\\Users\\Massamba Sene\\Desktop\\checkpoints\",monitor=\"val_accuracy\",verbose=0)],\n",
        ")"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Trial 5 Complete [00h 33m 27s]\n",
            "val_accuracy: 0.765749454498291\n",
            "\n",
            "Best val_accuracy So Far: 0.8041274547576904\n",
            "Total elapsed time: 02h 00m 11s\n",
            "INFO:tensorflow:Oracle triggered exit\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2021-09-28 20:59:51.511 INFO    tensorflow: Oracle triggered exit\n"
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
        "outputId": "eea56982-675e-407c-e19d-5391647bdee7"
      },
      "source": [
        "models = tuner.get_best_models(num_models=1)\n",
        "model = models[0]\n",
        "history = model.fit_generator(train_set,\n",
        "                              validation_data = val_set,\n",
        "                              verbose=2,\n",
        "                              epochs=10)"
      ],
      "execution_count": 12,
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
            "Epoch 1/10\n",
            "346/346 - 133s - loss: 0.5438 - accuracy: 0.8196 - val_loss: 4.4340 - val_accuracy: 0.5279\n",
            "Epoch 2/10\n",
            "346/346 - 110s - loss: 0.5082 - accuracy: 0.8401 - val_loss: 0.9413 - val_accuracy: 0.7777\n",
            "Epoch 3/10\n",
            "346/346 - 110s - loss: 0.4682 - accuracy: 0.8541 - val_loss: 1.0780 - val_accuracy: 0.7799\n",
            "Epoch 4/10\n",
            "346/346 - 110s - loss: 0.4436 - accuracy: 0.8639 - val_loss: 1.3073 - val_accuracy: 0.7314\n",
            "Epoch 5/10\n",
            "346/346 - 110s - loss: 0.4112 - accuracy: 0.8705 - val_loss: 3.2226 - val_accuracy: 0.6463\n",
            "Epoch 6/10\n",
            "346/346 - 110s - loss: 0.4015 - accuracy: 0.8792 - val_loss: 1.4293 - val_accuracy: 0.6966\n",
            "Epoch 7/10\n",
            "346/346 - 110s - loss: 0.3818 - accuracy: 0.8792 - val_loss: 19.9611 - val_accuracy: 0.8411\n",
            "Epoch 8/10\n",
            "346/346 - 110s - loss: 0.3601 - accuracy: 0.8879 - val_loss: 2.0870 - val_accuracy: 0.6665\n",
            "Epoch 9/10\n",
            "346/346 - 110s - loss: 0.3445 - accuracy: 0.8920 - val_loss: 2.1023 - val_accuracy: 0.7799\n",
            "Epoch 10/10\n",
            "346/346 - 110s - loss: 0.3350 - accuracy: 0.8985 - val_loss: 418.1658 - val_accuracy: 0.6441\n"
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
        "x_test = np.array(x_test,np.float32)/255.0\n",
        "y_test = np.array(list(map(int,target_val)),np.float32)"
      ],
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SLCSR_2XTaBJ"
      },
      "source": [
        "y_test = to_categorical(y_test)"
      ],
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p0-QCWiqO777",
        "outputId": "53c918da-37a6-42f2-94a8-668918774157"
      },
      "source": [
        "test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)\n",
        "print(test_acc)"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "16/16 - 4s - loss: 270.1249 - accuracy: 0.7036\n",
            "0.7036290168762207\n"
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
      "execution_count": 13,
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
        "      result = class_name[np.argmax(model.predict(our_image_1))]\n",
        "      st.text(\"Results\")\n",
        "      st.text(result)\n",
        "  if __name__ == 'main':\n",
        "    main()"
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fJlMunmjUh11",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "067c629b-1e65-40c9-b189-e31c5cea9ae7"
      },
      "source": [
        "!jupyter nbconvert --to script main.ipynb"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[NbConvertApp] WARNING | pattern u'main.ipynb' matched no files\n",
            "This application is used to convert notebook files (*.ipynb) to various other\n",
            "formats.\n",
            "\n",
            "WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.\n",
            "\n",
            "Options\n",
            "-------\n",
            "\n",
            "Arguments that take values are actually convenience aliases to full\n",
            "Configurables, whose aliases are listed on the help line. For more information\n",
            "on full configurables, see '--help-all'.\n",
            "\n",
            "--execute\n",
            "    Execute the notebook prior to export.\n",
            "--allow-errors\n",
            "    Continue notebook execution even if one of the cells throws an error and include the error message in the cell output (the default behaviour is to abort conversion). This flag is only relevant if '--execute' was specified, too.\n",
            "--no-input\n",
            "    Exclude input cells and output prompts from converted document. \n",
            "    This mode is ideal for generating code-free reports.\n",
            "--stdout\n",
            "    Write notebook output to stdout instead of files.\n",
            "--stdin\n",
            "    read a single notebook file from stdin. Write the resulting notebook with default basename 'notebook.*'\n",
            "--inplace\n",
            "    Run nbconvert in place, overwriting the existing notebook (only \n",
            "    relevant when converting to notebook format)\n",
            "-y\n",
            "    Answer yes to any questions instead of prompting.\n",
            "--clear-output\n",
            "    Clear output of current file and save in place, \n",
            "    overwriting the existing notebook.\n",
            "--debug\n",
            "    set log level to logging.DEBUG (maximize logging output)\n",
            "--no-prompt\n",
            "    Exclude input and output prompts from converted document.\n",
            "--generate-config\n",
            "    generate default config file\n",
            "--nbformat=<Enum> (NotebookExporter.nbformat_version)\n",
            "    Default: 4\n",
            "    Choices: [1, 2, 3, 4]\n",
            "    The nbformat version to write. Use this to downgrade notebooks.\n",
            "--output-dir=<Unicode> (FilesWriter.build_directory)\n",
            "    Default: ''\n",
            "    Directory to write output(s) to. Defaults to output to the directory of each\n",
            "    notebook. To recover previous default behaviour (outputting to the current\n",
            "    working directory) use . as the flag value.\n",
            "--writer=<DottedObjectName> (NbConvertApp.writer_class)\n",
            "    Default: 'FilesWriter'\n",
            "    Writer class used to write the  results of the conversion\n",
            "--log-level=<Enum> (Application.log_level)\n",
            "    Default: 30\n",
            "    Choices: (0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL')\n",
            "    Set the log level by value or name.\n",
            "--reveal-prefix=<Unicode> (SlidesExporter.reveal_url_prefix)\n",
            "    Default: u''\n",
            "    The URL prefix for reveal.js (version 3.x). This defaults to the reveal CDN,\n",
            "    but can be any url pointing to a copy  of reveal.js.\n",
            "    For speaker notes to work, this must be a relative path to a local  copy of\n",
            "    reveal.js: e.g., \"reveal.js\".\n",
            "    If a relative path is given, it must be a subdirectory of the current\n",
            "    directory (from which the server is run).\n",
            "    See the usage documentation\n",
            "    (https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-\n",
            "    slideshow) for more details.\n",
            "--to=<Unicode> (NbConvertApp.export_format)\n",
            "    Default: 'html'\n",
            "    The export format to be used, either one of the built-in formats\n",
            "    ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf',\n",
            "    'python', 'rst', 'script', 'slides'] or a dotted object name that represents\n",
            "    the import path for an `Exporter` class\n",
            "--template=<Unicode> (TemplateExporter.template_file)\n",
            "    Default: u''\n",
            "    Name of the template file to use\n",
            "--output=<Unicode> (NbConvertApp.output_base)\n",
            "    Default: ''\n",
            "    overwrite base name use for output files. can only be used when converting\n",
            "    one notebook at a time.\n",
            "--post=<DottedOrNone> (NbConvertApp.postprocessor_class)\n",
            "    Default: u''\n",
            "    PostProcessor class used to write the results of the conversion\n",
            "--config=<Unicode> (JupyterApp.config_file)\n",
            "    Default: u''\n",
            "    Full path of a config file.\n",
            "\n",
            "To see all available configurables, use `--help-all`\n",
            "\n",
            "Examples\n",
            "--------\n",
            "\n",
            "    The simplest way to use nbconvert is\n",
            "    \n",
            "    > jupyter nbconvert mynotebook.ipynb\n",
            "    \n",
            "    which will convert mynotebook.ipynb to the default format (probably HTML).\n",
            "    \n",
            "    You can specify the export format with `--to`.\n",
            "    Options include ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'rst', 'script', 'slides'].\n",
            "    \n",
            "    > jupyter nbconvert --to latex mynotebook.ipynb\n",
            "    \n",
            "    Both HTML and LaTeX support multiple output templates. LaTeX includes\n",
            "    'base', 'article' and 'report'.  HTML includes 'basic' and 'full'. You\n",
            "    can specify the flavor of the format used.\n",
            "    \n",
            "    > jupyter nbconvert --to html --template basic mynotebook.ipynb\n",
            "    \n",
            "    You can also pipe the output to stdout, rather than a file\n",
            "    \n",
            "    > jupyter nbconvert mynotebook.ipynb --stdout\n",
            "    \n",
            "    PDF is generated via latex\n",
            "    \n",
            "    > jupyter nbconvert mynotebook.ipynb --to pdf\n",
            "    \n",
            "    You can get (and serve) a Reveal.js-powered slideshow\n",
            "    \n",
            "    > jupyter nbconvert myslides.ipynb --to slides --post serve\n",
            "    \n",
            "    Multiple notebooks can be given at the command line in a couple of \n",
            "    different ways:\n",
            "    \n",
            "    > jupyter nbconvert notebook*.ipynb\n",
            "    > jupyter nbconvert notebook1.ipynb notebook2.ipynb\n",
            "    \n",
            "    or you can specify the notebooks list in a config file, containing::\n",
            "    \n",
            "        c.NbConvertApp.notebooks = [\"my_notebook.ipynb\"]\n",
            "    \n",
            "    > jupyter nbconvert --config mycfg.py\n",
            "\n"
          ]
        }
      ]
    }
  ]
}