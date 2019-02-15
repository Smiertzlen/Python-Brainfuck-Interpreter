# Python-Brainfuck-Interpreter
A simple Brainfuck interpreter written in Python3.
Now also ready for Python2.

Example:

```python
# import the brain_runner.py
import brain_runner

brain_runner.run('test.bf','abc')
```

test.bf:
```brainfuck
,.>,.>,.>
```

This will currently output the ASCII numbers of `a`, `b` and `c`, followed by the current memory tape and the pointer, which will be noted as a 1.
