int myAtoi(char* s) {
    while (*s == ' ') {
        s++;
    }

    int sign = 1;
    if (*s == '+' || *s == '-') {
        if (*s == '-') sign = -1;
        s++;
    }

    int result = 0;
    while (isdigit((unsigned char)*s)) {
        int digit = *s - '0';

        if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > 7)) {
            return (sign == 1) ? INT_MAX : INT_MIN;
        }

        result = result * 10 + digit;
        s++;
    }

    return (int)(result * sign);
}