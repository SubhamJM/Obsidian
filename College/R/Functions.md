```r
add_members <- function(a, b){
	result <- a + b
	return (result)
}

add_numbers <- function(a, b){
	a + b
}
```

# Default Arguments

```r
check_result <- function(marks, passing_mark = 35){
	if (marks >= pass_mark){
		return("pass")
	} else{
		return ("fail")
	}
}
```

# Returning multiple things:

```r
student_info <- function(marks){
	return (
		list(
			highest = max(marks),
			lowest = 
		)	
	)
}
```