- Recursion is the concept of calling the [[Methods]] inside of the same method until a base condition hits.

```java
public static int sum(int k) {
    if (k > 0) {
      return k + sum(k - 1);
    } else {
      return 0;
    }
  }
```

