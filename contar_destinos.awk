{
    for (k=1; k<=$6; k++) {
        cuenta[$k]++
    }
}

END {
    for (pal in cuenta) {
        print pal, cuenta[pal]
    }
}
