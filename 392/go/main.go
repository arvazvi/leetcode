package main

func isSubsequence(s string, t string) bool {
    RS, RT := len(s), len(t)
    var LS, LT int

    for LS < RS && LT < RT {
        if s[LS] == t[LT] {
            LS++
        }
        LT++
    }

    return LS == RS
}