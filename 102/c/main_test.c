#include "unity/unity.h"

#define main solution_main
#include "main.c"
#undef main

void setUp(void) {}
void tearDown(void) {}

void test_solution_main_returns_zero(void) {
    TEST_ASSERT_EQUAL_INT(0, solution_main());
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_solution_main_returns_zero);
    return UNITY_END();
}
