<div align="center">
  <img src="assets/logo.svg" width="300" height="300"></img>
</div>

# Curtis - The engine

![Python package](https://github.com/gantoreno/curtis-engine/workflows/Python%20package/badge.svg) ![Upload Python Package](https://github.com/gantoreno/curtis-engine/workflows/Upload%20Python%20Package/badge.svg) ![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue) ![PyPi](https://shields.io/pypi/v/curtis-engine.svg) ![License](https://img.shields.io/github/license/gantoreno/curtis-engine)

The cardiovascular unified real-time intelligent system is an AI-based engine whose purpose is to analyze the cardiovascular health of a given person, this is done through ECG analysis (an existent ECG measuring system is needed to obtain the required values).

## How does it work?

Curtis acts as an expert system, a rule-based program that emulates a real-life expert way of thinking about a certain topic, those rules were obtained for Curtis using the "decision tree approach", in which some existent data was given to a decision tree classifier, and it categorized the data into branches of rules and decisions.

## Usage

First, install the `curtis-engine` package:

```sh
$ pip install curtis-engine
```

To start using Curtis, the `CurtisEngine` class must be imported, as well as `CurtisFacts` for the facts declaration:

```python
>>> from curtis import CurtisEngine, CurtisFacts
>>> curtis = CurtisEngine()
```

After that, use `curtis.declare_facts` method to declare a new `CurtisFacts` object, which should contain all the ECG values needed for a diagnosis to be performed:

```python
>>> curtis.declare_facts(
...    CurtisFacts(
...         sex=1,
...         age=89,
...         height=140,
...         weight=30,
...         HR=56,
...         Pd=122,
...         PQ=164,
...         QRS=118,
...         QT=460,
...         QTcFra=451
...     )
... )
```

Finally, to get a diagnosis over the declared fact, use the `curtis.diagnose` method:

```python
>>> diagnosis = curtis.diagnose()
>>> print(diagnosis)
60
```

The `curtis.diagnose` method returns a number (as seen). This number is a _diagnosis index_, which means it's a unique index for a given diagnosis. To see which diagnosis belongs to that index, import the `diagnosis_indexes` dictionary from the `curtis.utils.encoding` package, and use the diagnosis as the index:

```python
>>> from curtis.utils.encoding import diagnosis_indexes
>>> print(diagnosis_indexes[diagnosis])
Unifocal premature ventricular complexes
```

And voilà! you've made your first Curtis diagnosis. 🎉

## Docs

To see the docs, you can clone the repo and open the `docs` folder to serve it as a website.

Using [`serve`](https://www.npmjs.com/package/serve):

```sh
$ git clone github.com/gantoreno/curtis-engine.git
$ cd curtis-engine
$ serve docs/curtis
```

The documentation should now be available at [http://localhost:5000](http://localhost:5000).

## License

This project is licensed under the [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) license.
