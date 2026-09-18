# For

```r
for (i in 1:10){
	print(i)
}

for (i in vect){
	print(i)
}
```

# While

```r
i <- 1
while (i <= 10){
	print(i)
	i <- i + 1
}
```

# break & next

```r
for (i in 1:10){
	if (i %% 2 == 0){
		next
	}
	if (i %% 7 == 0){
		break
	}
}
```