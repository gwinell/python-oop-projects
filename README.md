# Python OOP Practice

**A test-driven collection of Python object-oriented programming exercises.**

The repository is designed for learning by doing: read an exercise, implement the class in `solutions/`, and use the supplied `unittest` suites to check your work. It covers progressively more involved class design, state management, validation, inheritance and domain modelling.

[Browse all exercise briefs (Russian)](docs/EXERCISES.md)

## How to use

1. Choose an exercise from the [task list](docs/EXERCISES.md).
2. Create the corresponding Python module under `solutions/` (for example, `solutions/counter.py`).
3. Run the matching test suite:

```bash
python3 -m unittest test_counter.py
```

To run the entire collection once you've implemented the modules:

```bash
python3 -m unittest discover -p 'test_*.py'
```

**Note:** this is an exercise repository, not a packaged library. The `solutions/` implementations are intentionally not supplied in the public repository; tests will fail until you add your own solutions.

## What you'll practise

- Classes, constructors, instance attributes and methods.
- Input validation, error handling and encapsulation.
- Inheritance, polymorphism and Python's special methods.
- Writing implementations against clearly specified test cases.

The detailed exercise descriptions are in Russian and were prepared with AI assistance for educational use. The tests provide runnable acceptance criteria.
