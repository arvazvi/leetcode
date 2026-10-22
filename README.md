# LeetCode

Solutions to LeetCode problems implemented in Go and Python.

## Structure

Each problem is a directory named by its LeetCode number (e.g. `146/`). Inside, solutions are split by language:

```
<N>/
  go/    Go solution + tests
  py/    Python solution + tests
```

## Usage

Run tests for a specific problem:

```
make go-146    # Go tests for problem 146
make py-146    # Python tests for problem 146
```

Run all tests:

```
make test-all
```
