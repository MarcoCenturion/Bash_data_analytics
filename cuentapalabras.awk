{
    for (k=1; k<=NF; k++) {
        cuenta[$k]++
    }
}

END {
    for (pal in cuenta) {
        print pal, cuenta[pal]
    }
}
